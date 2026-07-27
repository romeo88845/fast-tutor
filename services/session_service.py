"""Core session loop — tutor behavior logic."""
from sqlalchemy.orm import Session as DBSession
from datetime import datetime
from typing import Optional
import json

from models import (
    Session, SessionStep, SessionMode, SessionStatus, StepType,
    Lesson, Question, QuestionType, Difficulty,
    UserObjectiveProgress, SpacedRepetitionCard, Objective
)
from services.spaced_repetition import calculate_next_review
from schemas import StepResponse, SessionStepOut, AnswerResult

def start_session(db: DBSession, exam_id: int, mode: str = "learn", user_id: int = 1) -> Session:
    """Create a new session and generate first step."""
    session = Session(
        user_id=user_id,
        mode=SessionMode(mode),
        exam_id=exam_id,
        status=SessionStatus.ACTIVE
    )
    db.add(session)
    db.flush()

    # For mock exam, pre-generate questions
    if mode == "mock_exam":
        import random
        all_qs = db.query(Question).order_by(Question.id).all()
        random.shuffle(all_qs)
        selected = all_qs[:10]  # 10 questions per mock exam
        # Create question steps
        for i, q in enumerate(selected):
            db.add(SessionStep(
                session_id=session.id, step_type=StepType.QUESTION,
                question_id=q.id, sort_order=i+1,
                tutor_message=f"Question {i+1} of {len(selected)}:"
            ))
        db.flush()
        # Add complete step at end
        db.add(SessionStep(
            session_id=session.id, step_type=StepType.COMPLETE,
            sort_order=len(selected)+1,
            tutor_message="Mock exam complete. Submit last answer for results."
        ))
        db.flush()
        db.commit()
        # Refresh and return session
        session = db.query(Session).filter(Session.id == session.id).first()
        return session

    # Generate first step
    step = _generate_next_step(db, session, user_id, None)
    if step:
        db.add(step)
        db.flush()

    db.commit()
    return session

def get_current_step(db: DBSession, session_id: int) -> Optional[StepResponse]:
    """Get the current (first unanswered) step."""
    session = db.query(Session).filter(Session.id == session_id).first()
    if not session:
        return None
    steps = session.steps
    if not steps:
        return None
    for step in steps:
        if step.user_response is None:
            return _to_step_response(step, len(steps))
    return _to_step_response(steps[-1], len(steps))

def submit_answer(db: DBSession, session_id: int, step_id: int, response: str, user_id: int = 1) -> AnswerResult:
    """Process answer and generate next step."""
    step = db.query(SessionStep).filter(
        SessionStep.id == step_id,
        SessionStep.session_id == session_id
    ).first()
    if not step:
        return AnswerResult(correct=False, explanation="Step not found", session_complete=True)

    step.user_response = response
    db.flush()

    session = db.query(Session).filter(Session.id == session_id).first()

    if step.step_type == StepType.QUESTION and step.question_id:
        question = db.query(Question).filter(Question.id == step.question_id).first()
        if question:
            correct, explanation = _check_answer(question, response)
            _update_progress(db, user_id, question.objective_id, correct)
            _update_spaced_repetition(db, user_id, question.id, correct)

            # Generate next step
            next_step = _generate_next_step(db, session, user_id, step)
            if next_step:
                db.add(next_step)
                db.flush()

            steps = session.steps
            next_sr = _to_step_response(next_step, len(steps)) if next_step else None
            is_complete = next_step is None or next_step.step_type == StepType.COMPLETE

            db.commit()
            return AnswerResult(
                correct=correct,
                explanation=explanation,
                next_step=next_sr,
                session_complete=is_complete
            )

    # Non-question step — just advance
    next_step = _generate_next_step(db, session, user_id, step)
    if next_step:
        db.add(next_step)
        db.flush()
    steps = session.steps
    next_sr = _to_step_response(next_step, len(steps)) if next_step else None
    db.commit()
    return AnswerResult(
        correct=True,
        explanation="",
        next_step=next_sr,
        session_complete=next_step is None
    )

def _generate_next_step(db: DBSession, session: Session, user_id: int, 
                        current_step: Optional[SessionStep]) -> Optional[SessionStep]:
    """Generate the next step in the learning loop."""
    order = (current_step.sort_order + 1) if current_step else 1

    # If we just completed a question, generate feedback step
    if current_step and current_step.step_type == StepType.QUESTION:
        question = db.query(Question).filter(Question.id == current_step.question_id).first()
        if question:
            correct, _ = _check_answer(question, current_step.user_response or "")
            msg = "✅ Correct!" if correct else "❌ Not quite."
            if correct:
                msg += f" {question.explanation_md[:200]}"
            else:
                msg += f" The right answer and more detail: {question.explanation_md[:200]}"
            return SessionStep(
                session_id=session.id,
                step_type=StepType.FEEDBACK,
                lesson_id=current_step.lesson_id,
                question_id=question.id,
                sort_order=order,
                tutor_message=msg
            )

    # After feedback, check if more questions or teach next lesson
    if current_step and current_step.step_type == StepType.FEEDBACK:
        return _pick_next_lesson_step(db, session, user_id, order)

    # Start — pick first lesson
    if not current_step or current_step.step_type == StepType.COMPLETE:
        return _pick_next_lesson_step(db, session, user_id, order)

    # After teach step — find questions for this lesson
    if current_step and current_step.step_type == StepType.TEACH and current_step.lesson_id:
        import random
        questions = db.query(Question).filter(
            Question.lesson_id == current_step.lesson_id
        ).all()
        existing_qids = [s.question_id for s in session.steps if s.step_type == StepType.QUESTION and s.question_id]
        remaining = [q for q in questions if q.id not in existing_qids]
        if remaining:
            q = random.choice(remaining)
            lesson = db.query(Lesson).filter(Lesson.id == current_step.lesson_id).first()
            msg = "Let's test your understanding of " + (lesson.title if lesson else "") + ":"
            return SessionStep(
                session_id=session.id, step_type=StepType.QUESTION,
                lesson_id=current_step.lesson_id, question_id=q.id,
                sort_order=order, tutor_message=msg
            )
        else:
            # No questions for this lesson - mark it as complete via next lesson
            return _pick_next_lesson_step(db, session, user_id, order)

    return None

def _pick_next_lesson_step(db: DBSession, session: Session, user_id: int, order: int) -> Optional[SessionStep]:
    """Select next lesson and create appropriate step for the current mode."""
    import random
    mode = session.mode

    # Refresh session from DB to get fresh steps
    session = db.query(Session).filter(Session.id == session.id).first()
    served_lesson_ids = set()
    for s in session.steps:
        if s.lesson_id:
            served_lesson_ids.add(s.lesson_id)

    # Get all lessons not yet served
    if served_lesson_ids:
        available = db.query(Lesson).filter(
            ~Lesson.id.in_(served_lesson_ids)
        ).order_by(Lesson.sort_order).all()
    else:
        available = db.query(Lesson).order_by(Lesson.sort_order).all()

    if not available:
        return SessionStep(
            session_id=session.id, step_type=StepType.COMPLETE,
            sort_order=order, tutor_message="Session complete! Great work."
        )

    lesson = available[0]

    # In drill mode, skip teach and go straight to a question
    if mode == SessionMode.DRILL:
        questions = db.query(Question).filter(
            Question.lesson_id == lesson.id
        ).all()
        if questions:
            q = random.choice(questions)
            return SessionStep(
                session_id=session.id, step_type=StepType.QUESTION,
                lesson_id=lesson.id, question_id=q.id,
                sort_order=order, tutor_message="Quick question:"
            )
        # No questions for this lesson - skip to next
        return _pick_next_lesson_step(db, session, user_id, order)

    # Learn mode - teach first, then question (handled by _generate_next_step)
    return SessionStep(
        session_id=session.id, step_type=StepType.TEACH,
        lesson_id=lesson.id, sort_order=order,
        tutor_message=f"Let's learn: {lesson.title}"
    )
def _check_answer(question: Question, response: str) -> tuple:
    """Check if response is correct. Returns (bool, explanation)."""
    import json
    try:
        data = json.loads(response) if isinstance(response, str) else response
    except:
        data = response

    if question.type == QuestionType.MCQ:
        correct_labels = [o.label for o in question.options if o.is_correct]
        user_label = data if isinstance(data, str) else ""
        is_correct = user_label.strip().upper() in correct_labels
        correct_str = ", ".join(correct_labels)
        explanation = f"Correct answer: {correct_str}" if not is_correct else ""
        return is_correct, explanation

    elif question.type == QuestionType.MULTI_SELECT:
        correct_labels = set(o.label for o in question.options if o.is_correct)
        user_labels = set(data) if isinstance(data, list) else set()
        is_correct = user_labels == correct_labels
        explanation = f"Correct answers: {', '.join(sorted(correct_labels))}" if not is_correct else ""
        return is_correct, explanation

    else:
        return False, "Short answer evaluation coming in v2"

def _update_progress(db: DBSession, user_id: int, objective_id: int, correct: bool):
    """Update user progress for an objective."""
    prog = db.query(UserObjectiveProgress).filter(
        UserObjectiveProgress.user_id == user_id,
        UserObjectiveProgress.objective_id == objective_id
    ).first()
    
    if not prog:
        prog = UserObjectiveProgress(
            user_id=user_id,
            objective_id=objective_id,
            questions_answered=0,
            correct_count=0,
            accuracy=0.0,
            streak=0
        )
        db.add(prog)
        db.flush()

    prog.questions_answered += 1
    if correct:
        prog.correct_count += 1
        prog.streak += 1
    else:
        prog.streak = 0
    prog.accuracy = round(prog.correct_count / prog.questions_answered, 3) if prog.questions_answered else 0.0

def _update_spaced_repetition(db: DBSession, user_id: int, question_id: int, correct: bool):
    """Update spaced repetition card."""
    card = db.query(SpacedRepetitionCard).filter(
        SpacedRepetitionCard.user_id == user_id,
        SpacedRepetitionCard.question_id == question_id
    ).first()
    
    if not card:
        card = SpacedRepetitionCard(
            user_id=user_id,
            question_id=question_id
        )
        db.add(card)
        db.flush()

    result = calculate_next_review(
        is_correct=correct,
        interval_days=card.interval_days,
        repetition_count=card.repetition_count,
        easiness_factor=card.easiness_factor
    )
    card.interval_days = result["interval_days"]
    card.repetition_count = result["repetition_count"]
    card.easiness_factor = result["easiness_factor"]
    card.next_review_at = result["next_review_at"]

def _to_step_response(step: SessionStep, total_steps: int) -> StepResponse:
    """Convert SessionStep to StepResponse with lesson/question data."""
    lesson = None
    question = None
    from schemas import LessonOut, QuestionOut, QuestionOptionOut
    
    # Fetch fresh from DB
    from database import SessionLocal
    db2 = SessionLocal()
    try:
        if step.lesson_id:
            l = db2.query(Lesson).filter(Lesson.id == step.lesson_id).first()
            if l:
                lesson = LessonOut(
                    id=l.id, objective_id=l.objective_id,
                    title=l.title, content_md=l.content_md,
                    source_type=l.source_type, source_ref=l.source_ref,
                    sort_order=l.sort_order, estimated_min=l.estimated_min,
                    segments=[], questions=[]
                )
        if step.question_id:
            q = db2.query(Question).filter(Question.id == step.question_id).first()
            if q:
                question = QuestionOut(
                    id=q.id, type=q.type.value,
                    stem=q.stem, explanation_md=q.explanation_md,
                    difficulty=q.difficulty.value, lesson_id=q.lesson_id,
                    options=[QuestionOptionOut(id=o.id, label=o.label, text=o.text) for o in q.options]
                )
    finally:
        db2.close()

    return StepResponse(
        step=SessionStepOut(
            id=step.id, step_type=step.step_type.value,
            lesson_id=step.lesson_id, question_id=step.question_id,
            sort_order=step.sort_order, tutor_message=step.tutor_message,
            lesson=lesson, question=question
        ),
        session_id=step.session_id,
        step_number=step.sort_order,
        total_steps=total_steps
    )
