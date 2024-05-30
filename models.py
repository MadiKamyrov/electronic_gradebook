from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, DATE
from sqlalchemy.orm import relationship
from database import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(VARCHAR(255), nullable=False)
    last_name = Column(VARCHAR(255), nullable=False)
    birth_date = Column(DATE, nullable=False)
    gender = Column(VARCHAR(1), nullable=False)
    address = Column(VARCHAR(255))
    phone_number = Column(VARCHAR(11), unique=True)
    email = Column(VARCHAR(255), unique=True)
    faculty = Column(VARCHAR(255), nullable=False)
    course_number = Column(Integer)
    major = Column(VARCHAR(255), nullable=False)
    student_card_number = Column(VARCHAR(255), unique=True, nullable=False)
    form_of_education = Column(VARCHAR(255), nullable=False)

    scores = relationship("Score", back_populates="student")

class Score(Base):
    __tablename__ = 'scores'

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    subject = Column(VARCHAR(255), index=True)
    score = Column(Integer)

    student = relationship("Student", back_populates="scores")
