from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session as DBSession
from typing import List

from database import get_db
from models import Session, SessionStep, User, Exam
from schemas import SessionCreate, SessionOut, StepResponse, AnswerSubmit, AnswerResult
from services.session_service import start_session, get_current_step, submit_answer

router = APIRouter(prefix="/api/sessions", tags=["sessions"])

@router.post("")
def create_session(data: SessionCreate, db: DBSession = Depends(get_db)):
    """Start a new learning session."""
    # Ensure user exists
    user = db.query(User).filter(User.id == data.user_id).first()
    if not user:
        user = User(id=data.user_id, name="Learner")
        db.add(user)
        db.flush()

    session = start_session(db, data.exam_id, data.mode, data.user_id)
    step = get_current_step(db, session.id)
    return {
        "session_id": session.id,
        "status": "created",
        "current_step": step
    }

@router.get("/{session_id}/step")
def current_step(session_id: int, db: DBSession = Depends(get_db)):
    """Get the current step."""
    step = get_current_step(db, session_id)
    if not step:
        raise HTTPException(404, "Session or step not found")
    return step

@router.post("/{session_id}/step")
def answer_step(session_id: int, data: AnswerSubmit, db: DBSession = Depends(get_db)):
    """Submit answer and get next step."""
    result = submit_answer(db, session_id, data.step_id, data.response)
    return result

@router.get("/{session_id}/history")
def session_history(session_id: int, db: DBSession = Depends(get_db)):
    """Get full session history."""
    session = db.query(Session).filter(Session.id == session_id).first()
    if not session:
        raise HTTPException(404, "Session not found")
    return SessionOut(
        id=session.id,
        mode=session.mode.value,
        status=session.status.value,
        started_at=session.started_at,
        steps=[]
    )
