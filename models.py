from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, Boolean, Text, ForeignKey, DateTime, Enum as SAEnum
from sqlalchemy.orm import relationship
from database import Base
import enum

class QuestionType(str, enum.Enum):
    MCQ = "mcq"
    MULTI_SELECT = "multi_select"
    SHORT_ANSWER = "short_answer"

class Difficulty(str, enum.Enum):
    FOUNDATION = "foundation"
    INTERMEDIATE = "intermediate"
    EXAM = "exam"

class SessionMode(str, enum.Enum):
    LEARN = "learn"
    DRILL = "drill"
    MOCK_EXAM = "mock_exam"

class SessionStatus(str, enum.Enum):
    ACTIVE = "active"
    COMPLETED = "completed"
    ABANDONED = "abandoned"

class StepType(str, enum.Enum):
    TEACH = "teach"
    PREDICTION = "prediction"
    QUESTION = "question"
    FEEDBACK = "feedback"
    COMPLETE = "complete"

# ── Exam Structure ────────────────────────────────────────────────────────────

class Exam(Base):
    __tablename__ = "exams"
    id = Column(Integer, primary_key=True)
    code = Column(String(50), unique=True, nullable=False)
    name = Column(String(200), nullable=False)
    vendor = Column(String(100), default="Microsoft")
    total_questions = Column(Integer, default=0)
    passing_score = Column(Integer, default=700)
    domains = relationship("Domain", back_populates="exam", cascade="all, delete-orphan")

class Domain(Base):
    __tablename__ = "domains"
    id = Column(Integer, primary_key=True)
    exam_id = Column(Integer, ForeignKey("exams.id"), nullable=False)
    name = Column(String(200), nullable=False)
    weight_pct = Column(Float, default=0)
    sort_order = Column(Integer, default=0)
    exam = relationship("Exam", back_populates="domains")
    objectives = relationship("Objective", back_populates="domain", cascade="all, delete-orphan")

class Objective(Base):
    __tablename__ = "objectives"
    id = Column(Integer, primary_key=True)
    domain_id = Column(Integer, ForeignKey("domains.id"), nullable=False)
    code = Column(String(20), nullable=True)
    description = Column(Text, nullable=False)
    domain = relationship("Domain", back_populates="objectives")
    lessons = relationship("Lesson", back_populates="objective", cascade="all, delete-orphan")
    questions = relationship("Question", back_populates="objective", cascade="all, delete-orphan")

# ── Content ───────────────────────────────────────────────────────────────────

class Lesson(Base):
    __tablename__ = "lessons"
    id = Column(Integer, primary_key=True)
    objective_id = Column(Integer, ForeignKey("objectives.id"), nullable=True)
    title = Column(String(300), nullable=False)
    content_md = Column(Text, default="")
    source_type = Column(String(20), default="video")
    source_ref = Column(String(500), default="")
    sort_order = Column(Integer, default=0)
    estimated_min = Column(Integer, default=5)
    objective = relationship("Objective", back_populates="lessons")
    segments = relationship("LessonSegment", back_populates="lesson", cascade="all, delete-orphan")
    questions = relationship("Question", backref="lesson", cascade="all, delete-orphan",
                             foreign_keys="Question.lesson_id")

class LessonSegment(Base):
    __tablename__ = "lesson_segments"
    id = Column(Integer, primary_key=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"), nullable=False)
    sort_order = Column(Integer, default=0)
    content_md = Column(Text, default="")
    time_start = Column(String(20), default="")
    lesson = relationship("Lesson", back_populates="segments")

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    objective_id = Column(Integer, ForeignKey("objectives.id"), nullable=False)
    lesson_id = Column(Integer, ForeignKey("lessons.id"), nullable=True)
    type = Column(SAEnum(QuestionType), default=QuestionType.MCQ)
    stem = Column(Text, nullable=False)
    explanation_md = Column(Text, default="")
    difficulty = Column(SAEnum(Difficulty), default=Difficulty.FOUNDATION)
    objective = relationship("Objective", back_populates="questions")
    options = relationship("AnswerOption", back_populates="question", cascade="all, delete-orphan")

class AnswerOption(Base):
    __tablename__ = "answer_options"
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    label = Column(String(10), nullable=False)
    text = Column(Text, nullable=False)
    is_correct = Column(Boolean, default=False)
    question = relationship("Question", back_populates="options")

# ── Learner ───────────────────────────────────────────────────────────────────

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), default="Learner")
    created_at = Column(DateTime, default=datetime.utcnow)
    sessions = relationship("Session", back_populates="user")
    progress = relationship("UserObjectiveProgress", back_populates="user", cascade="all, delete-orphan")
    cards = relationship("SpacedRepetitionCard", back_populates="user", cascade="all, delete-orphan")

class UserObjectiveProgress(Base):
    __tablename__ = "user_objective_progress"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    objective_id = Column(Integer, ForeignKey("objectives.id"), nullable=False)
    questions_answered = Column(Integer, default=0)
    correct_count = Column(Integer, default=0)
    accuracy = Column(Float, default=0.0)
    streak = Column(Integer, default=0)
    user = relationship("User", back_populates="progress")
    objective = relationship("Objective")

# ── Session ───────────────────────────────────────────────────────────────────

class Session(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    mode = Column(SAEnum(SessionMode), default=SessionMode.LEARN)
    exam_id = Column(Integer, ForeignKey("exams.id"), nullable=True)
    status = Column(SAEnum(SessionStatus), default=SessionStatus.ACTIVE)
    started_at = Column(DateTime, default=datetime.utcnow)
    ended_at = Column(DateTime, nullable=True)
    user = relationship("User", back_populates="sessions")
    steps = relationship("SessionStep", back_populates="session", cascade="all, delete-orphan",
                          order_by="SessionStep.sort_order")

class SessionStep(Base):
    __tablename__ = "session_steps"
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey("sessions.id"), nullable=False)
    step_type = Column(SAEnum(StepType), nullable=False)
    lesson_id = Column(Integer, ForeignKey("lessons.id"), nullable=True)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=True)
    sort_order = Column(Integer, default=0)
    tutor_message = Column(Text, default="")
    user_response = Column(Text, nullable=True)
    session = relationship("Session", back_populates="steps")

# ── Spaced Repetition ────────────────────────────────────────────────────────

class SpacedRepetitionCard(Base):
    __tablename__ = "spaced_repetition_cards"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    next_review_at = Column(DateTime, nullable=True)
    interval_days = Column(Integer, default=1)
    repetition_count = Column(Integer, default=0)
    easiness_factor = Column(Float, default=2.5)
    user = relationship("User", back_populates="cards")
    question = relationship("Question")
