from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# ── Exam ──
class ExamOut(BaseModel):
    id: int
    code: str
    name: str
    vendor: str
    total_questions: int
    passing_score: int
    class Config: from_attributes = True

class DomainOut(BaseModel):
    id: int
    name: str
    weight_pct: float
    sort_order: int
    class Config: from_attributes = True

class ObjectiveOut(BaseModel):
    id: int
    domain_id: int
    code: Optional[str] = None
    description: str
    class Config: from_attributes = True

class ExamDetail(ExamOut):
    domains: List[DomainOut] = []

# ── Content ──
class LessonSegmentOut(BaseModel):
    id: int
    sort_order: int
    content_md: str
    time_start: str
    class Config: from_attributes = True

class QuestionOptionOut(BaseModel):
    id: int
    label: str
    text: str
    class Config: from_attributes = True

class QuestionOut(BaseModel):
    id: int
    type: str
    stem: str
    explanation_md: str
    difficulty: str
    lesson_id: Optional[int] = None
    options: List[QuestionOptionOut] = []
    class Config: from_attributes = True

class LessonOut(BaseModel):
    id: int
    objective_id: Optional[int] = None
    title: str
    content_md: str
    source_type: str
    source_ref: str
    sort_order: int
    estimated_min: int
    segments: List[LessonSegmentOut] = []
    questions: List[QuestionOut] = []
    class Config: from_attributes = True

# ── Session ──
class SessionCreate(BaseModel):
    exam_id: int
    mode: str = "learn"
    user_id: int = 1

class SessionStepOut(BaseModel):
    id: int
    step_type: str
    lesson_id: Optional[int] = None
    question_id: Optional[int] = None
    sort_order: int
    tutor_message: str
    lesson: Optional[LessonOut] = None
    question: Optional[QuestionOut] = None
    class Config: from_attributes = True

class SessionOut(BaseModel):
    id: int
    mode: str
    status: str
    started_at: datetime
    steps: List[SessionStepOut] = []
    class Config: from_attributes = True

class StepResponse(BaseModel):
    step: SessionStepOut
    session_id: int
    step_number: int
    total_steps: int

class AnswerSubmit(BaseModel):
    session_id: int
    step_id: int
    response: str  # JSON-encoded: "A" for MCQ, ["A","B"] for multi, "text" for short

class AnswerResult(BaseModel):
    correct: bool
    explanation: str
    next_step: Optional[StepResponse] = None
    session_complete: bool = False

# ── Progress ──
class ObjectiveProgressOut(BaseModel):
    objective_id: int
    objective_code: Optional[str] = None
    objective_desc: str
    questions_answered: int
    correct_count: int
    accuracy: float
    streak: int
    class Config: from_attributes = True

# ── Ingest ──
class IngestResult(BaseModel):
    lessons_created: int
    segments_imported: int
    questions_created: int
    exam_id: int
