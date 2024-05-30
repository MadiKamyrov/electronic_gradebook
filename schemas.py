from pydantic import BaseModel
from datetime import date

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: date
    gender: str
    address: str
    phone_number: str
    email: str
    faculty: str
    course_number: int
    major: str
    student_card_number: str
    form_of_education: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class config:
        org_mode = True

class ScoreBase(BaseModel):
    student_id: int
    subject: str
    score: int

class ScoreCreate(ScoreBase):
    pass

class Score(ScoreBase):
    id: int

    class Config:
        org_mode = True
