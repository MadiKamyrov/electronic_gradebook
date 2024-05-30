from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)


@app.get("/students/{student_id}", response_model=schemas.Student)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id=student_id)
    return student


@app.patch("/students/{student_id}", response_model=schemas.Student)
def update_student(student_id: int, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.update_student(db=db, student_id=student_id, student=student)


@app.delete("/students/{student_id}", response_model=schemas.Student)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    return crud.delete_student(db=db, student_id=student_id)


@app.post("/scores/", response_model=schemas.Score)
def create_score(score: schemas.ScoreCreate, db: Session = Depends(get_db)):
    return crud.create_score(db=db, score=score)


@app.get("/scores/{score_id}", response_model=schemas.Score)
def read_score(score_id: int, db: Session = Depends(get_db)):
    score = crud.get_score(db, score_id=score_id)
    return score


@app.patch("/scores/{score_id}", response_model=schemas.Score)
def update_score(score_id: int, score: schemas.ScoreCreate, db: Session = Depends(get_db)):
    return crud.update_score(db=db, score_id=score_id, score=score)


@app.delete("/scores/{score_id}", response_model=schemas.Score)
def delete_score(score_id: int, db: Session = Depends(get_db)):
    return crud.delete_score(db=db, score_id=score_id)
