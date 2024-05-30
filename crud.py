from sqlalchemy.orm import Session

import models
import schemas


def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def create_student(db: Session, student: schemas.StudentCreate):
    create_student = models.Student(**student.dict())
    if create_student is not None:
        db.add(create_student)
        db.commit()
        db.refresh(create_student)
    return create_student


def update_student(db: Session, student_id: int, student: schemas.StudentCreate):
    update_student = get_student(db, student_id)
    if update_student is not None:
        update_student.first_name = student.first_name
        update_student.last_name = student.last_name
        update_student.birth_date = student.birth_date
        update_student.gender = student.gender
        update_student.address = student.address
        update_student.phone_number = student.phone_number
        update_student.email = student.email
        update_student.faculty = student.faculty
        update_student.course_number = student.course_number
        update_student.major = student.major
        update_student.student_card_number = student.student_card_number
        update_student.form_of_education = student.form_of_education
        db.commit()
        db.refresh(update_student)
    return update_student


def delete_student(db: Session, student_id: int):
    delete_student = get_student(db, student_id)
    if delete_student is not None:
        db.delete(delete_student)
        db.commit()
    return delete_student


def get_score(db: Session, score_id: int):
    return db.query(models.Score).filter(models.Score.id == score_id).first()


def create_score(db: Session, score: schemas.ScoreCreate):
    create_score = models.Score(**score.dict())
    if create_score is not None:
        db.add(create_score)
        db.commit()
        db.refresh(create_score)
    return create_score


def update_score(db: Session, score_id: int, score: schemas.ScoreCreate):
    update_score = get_score(db, score_id)
    if update_score is not None:
        update_score.subject = score.subject
        update_score.score = score.score
        db.commit()
        db.refresh(update_score)
    return update_score

def delete_score(db: Session, score_id: int):
    delete_score = get_score(db, score_id)
    if delete_score is not None:
        db.delete(delete_score)
        db.commit()
    return delete_score
