from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session as DBSession
from typing import List

from database import get_db
from models import Exam, Domain, Objective, Lesson, Question, AnswerOption
from schemas import ExamOut, ExamDetail, DomainOut, ObjectiveOut, LessonOut, QuestionOut, QuestionOptionOut

router = APIRouter(prefix="/api/exams", tags=["content"])

@router.get("", response_model=List[ExamOut])
def list_exams(db: DBSession = Depends(get_db)):
    return db.query(Exam).all()

@router.get("/{exam_id}", response_model=ExamDetail)
def get_exam(exam_id: int, db: DBSession = Depends(get_db)):
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, "Exam not found")
    return exam

@router.get("/{exam_id}/objectives", response_model=List[ObjectiveOut])
def list_objectives(exam_id: int, db: DBSession = Depends(get_db)):
    return db.query(Objective).join(Domain).filter(Domain.exam_id == exam_id).all()

@router.get("/{exam_id}/lessons", response_model=List[LessonOut])
def list_lessons(exam_id: int, db: DBSession = Depends(get_db)):
    lessons = db.query(Lesson).join(Objective).join(Domain).filter(
        Domain.exam_id == exam_id
    ).order_by(Lesson.sort_order).all()
    return lessons

@router.get("/{exam_id}/questions", response_model=List[QuestionOut])
def list_questions(exam_id: int, db: DBSession = Depends(get_db)):
    questions = db.query(Question).join(Objective).join(Domain).filter(
        Domain.exam_id == exam_id
    ).all()
    return questions

@router.get("/lessons/{lesson_id}", response_model=LessonOut)
def get_lesson(lesson_id: int, db: DBSession = Depends(get_db)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(404, "Lesson not found")
    return lesson
