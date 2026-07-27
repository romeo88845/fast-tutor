import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DB_DIR = "/opt/fast-tutor"
DB_PATH = os.path.join(DB_DIR, "fast-tutor.db")
os.makedirs(DB_DIR, exist_ok=True)

engine = create_engine(f"sqlite:///{DB_PATH}", echo=False)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

def init_db():
    from models import Exam, Domain, Objective, Lesson, LessonSegment, Question, AnswerOption, User, Session, SessionStep, SpacedRepetitionCard, UserObjectiveProgress
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
