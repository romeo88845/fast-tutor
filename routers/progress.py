from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session as DBSession
from typing import List

from database import get_db
from models import User, UserObjectiveProgress, Objective, Domain, Exam, SpacedRepetitionCard
from schemas import ObjectiveProgressOut
from services.spaced_repetition import calculate_next_review

router = APIRouter(prefix="/api/progress", tags=["progress"])

@router.get("/{user_id}/overview")
def progress_overview(user_id: int, db: DBSession = Depends(get_db)):
    """Get learner's progress overview."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(404, "User not found")
    
    progress = db.query(UserObjectiveProgress).filter(
        UserObjectiveProgress.user_id == user_id
    ).all()
    
    total_q = sum(p.questions_answered for p in progress)
    total_c = sum(p.correct_count for p in progress)
    accuracy = round(total_c / total_q, 3) if total_q else 0
    
    return {
        "user_id": user_id,
        "total_questions": total_q,
        "total_correct": total_c,
        "overall_accuracy": accuracy,
        "objectives_count": len(progress),
        "streak": max((p.streak for p in progress), default=0)
    }

@router.get("/{user_id}/objectives", response_model=List[ObjectiveProgressOut])
def objective_progress(user_id: int, db: DBSession = Depends(get_db)):
    """Get per-objective progress."""
    progress = db.query(UserObjectiveProgress).filter(
        UserObjectiveProgress.user_id == user_id
    ).all()
    
    result = []
    for p in progress:
        obj = db.query(Objective).filter(Objective.id == p.objective_id).first()
        if obj:
            result.append(ObjectiveProgressOut(
                objective_id=obj.id,
                objective_code=obj.code,
                objective_desc=obj.description,
                questions_answered=p.questions_answered,
                correct_count=p.correct_count,
                accuracy=p.accuracy,
                streak=p.streak
            ))
    return sorted(result, key=lambda x: x.accuracy)

@router.get("/{user_id}/weak")
def weak_objectives(user_id: int, db: DBSession = Depends(get_db)):
    """Get weakest objectives (lowest accuracy)."""
    progress = db.query(UserObjectiveProgress).filter(
        UserObjectiveProgress.user_id == user_id,
        UserObjectiveProgress.accuracy < 0.6
    ).order_by(UserObjectiveProgress.accuracy.asc()).all()
    
    result = []
    for p in progress:
        obj = db.query(Objective).filter(Objective.id == p.objective_id).first()
        if obj:
            result.append({
                "objective_id": obj.id,
                "description": obj.description,
                "accuracy": p.accuracy,
                "questions_answered": p.questions_answered
            })
    return result

from datetime import datetime, timezone

@router.get("/{user_id}/dashboard")
def progress_dashboard(user_id: int, db: DBSession = Depends(get_db)):
    """Comprehensive learning dashboard."""
    progress = db.query(UserObjectiveProgress).filter(
        UserObjectiveProgress.user_id == user_id
    ).all()
    
    total_q = sum(p.questions_answered for p in progress)
    total_c = sum(p.correct_count for p in progress)
    
    # Per-domain stats
    domains = []
    for p in progress:
        obj = db.query(Objective).filter(Objective.id == p.objective_id).first()
        if obj and obj.domain:
            domains.append({
                "domain": obj.domain.name,
                "accuracy": p.accuracy,
                "answered": p.questions_answered,
                "correct": p.correct_count,
                "streak": p.streak
            })
    
    # Group by domain
    from collections import defaultdict
    domain_stats = defaultdict(lambda: {"answered": 0, "correct": 0, "accuracies": [], "streaks": []})
    for d in domains:
        ds = domain_stats[d["domain"]]
        ds["answered"] += d["answered"]
        ds["correct"] += d["correct"]
        ds["accuracies"].append(d["accuracy"])
        ds["streaks"].append(d["streak"])
    
    domain_result = []
    for name, ds in sorted(domain_stats.items()):
        domain_result.append({
            "name": name,
            "accuracy": round(ds["correct"] / ds["answered"], 3) if ds["answered"] else 0,
            "answered": ds["answered"],
            "correct": ds["correct"],
            "best_streak": max(ds["streaks"]) if ds["streaks"] else 0
        })
    
    return {
        "overall": {
            "total_questions": total_q,
            "total_correct": total_c,
            "accuracy": round(total_c / total_q, 3) if total_q else 0,
            "objectives_attempted": len(progress),
            "overall_streak": max((p.streak for p in progress), default=0)
        },
        "domains": domain_result,
        "weak_objectives": [
            {"description": obj.description, "accuracy": p.accuracy}
            for p in progress
            for obj in [db.query(Objective).filter(Objective.id == p.objective_id).first()]
            if obj and p.accuracy < 0.6
        ]
    }

@router.get("/cards/due/{user_id}")
def cards_due(user_id: int, db: DBSession = Depends(get_db)):
    """Get spaced repetition cards due for review."""
    now = datetime.utcnow()
    cards = db.query(SpacedRepetitionCard).filter(
        SpacedRepetitionCard.user_id == user_id,
        SpacedRepetitionCard.next_review_at <= now
    ).order_by(SpacedRepetitionCard.next_review_at.asc()).all()
    
    result = []
    for c in cards:
        q = db.query(Question).filter(Question.id == c.question_id).first()
        if q:
            result.append({
                "card_id": c.id,
                "question_id": c.question_id,
                "question_stem": q.stem[:100],
                "due_at": str(c.next_review_at) if c.next_review_at else None,
                "interval_days": c.interval_days,
                "repetition_count": c.repetition_count,
                "easiness_factor": c.easiness_factor
            })
    return result

@router.post("/cards/review")
def card_review(card_id: int, is_correct: bool, user_id: int = 1, db: DBSession = Depends(get_db)):
    """Submit a spaced repetition card review."""
    from services.spaced_repetition import calculate_next_review
    card = db.query(SpacedRepetitionCard).filter(
        SpacedRepetitionCard.id == card_id,
        SpacedRepetitionCard.user_id == user_id
    ).first()
    if not card:
        raise HTTPException(404, "Card not found")
    
    result = calculate_next_review(
        is_correct=is_correct,
        interval_days=card.interval_days,
        repetition_count=card.repetition_count,
        easiness_factor=card.easiness_factor
    )
    card.interval_days = result["interval_days"]
    card.repetition_count = result["repetition_count"]
    card.easiness_factor = result["easiness_factor"]
    card.next_review_at = result["next_review_at"]
    db.commit()
    
    return result