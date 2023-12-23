from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), primary_key=False, nullable=False, server_default=text("now()"))
    
    email = Column(String, primary_key=False, nullable=False, unique=True)
    password = Column(String, primary_key=False, nullable=False, unique=False)
    username = Column(String, primary_key=False, nullable=False, unique=True)

    isTeacher = Column(Boolean, primary_key=False, nullable=False, unique=False, server_default="False")
    abbreviation = Column(String, primary_key=False, nullable=True, unique=False)
    isOberstufe = Column(Boolean, primary_key=False, nullable=False, unique=False, server_default="False")
    courses = Column(String, primary_key=False, nullable=True, unique=False)

    # beta_key = Column(String, primary_key=False, nullable=True, unique=False)
    # invites = Column(Integer, primary_key=False, nullable=False, unique=False, server_default=3)
    # waitlist = Column(TIMESTAMP(timezone=True), primary_key=False, nullable=False, server_default=text("now()")) # now() + 10 days

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), primary_key=False, nullable=False, server_default=text("now()"))

    abbreviation = Column(String, primary_key=False, nullable=True, unique=True)
    name = Column(String, primary_key=False, nullable=False, unique=False)

class Exam(Base):
    __tablename__ = "exams"

    id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), primary_key=False, nullable=False, server_default=text("now()"))

    date = Column(TIMESTAMP(timezone=True), primary_key=False, nullable=False)
    type = Column(String, primary_key=False, nullable=False, unique=False)
    course = Column(String, primary_key=False, nullable=False, unique=False)
    teacher = Column(String, ForeignKey("teachers.abbreviation", onupdate="CASCADE"), primary_key=False, nullable=False, unique=False)

class Substitution(Base):
    __tablename__ = "substitutions"

    id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), primary_key=False, nullable=False, server_default=text("now()"))

    date = Column(TIMESTAMP(timezone=True), primary_key=False, nullable=False)
    updated = Column(TIMESTAMP(timezone=True), primary_key=False, nullable=False)

    course = Column(String, primary_key=False, nullable=True, unique=False)
    hour = Column(Integer, primary_key=False, nullable=True, unique=False)
    substitute_teacher = Column(String, ForeignKey("teachers.abbreviation", onupdate="CASCADE"), primary_key=False, nullable=True, unique=False)
    subject = Column(String, primary_key=False, nullable=True, unique=False)
    room = Column(String, primary_key=False, nullable=True, unique=False)
    replaced_teacher = Column(String, ForeignKey("teachers.abbreviation", onupdate="CASCADE"), primary_key=False, nullable=True, unique=False)

class StudentAbsence(Base):
    __tablename__ = "student_absences"

    id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), primary_key=False, nullable=False, server_default=text("now()"))

    date = Column(TIMESTAMP(timezone=True), primary_key=False, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id", onupdate="CASCADE"), primary_key=False, nullable=True, unique=False)
    portal_email = Column(String, primary_key=False, nullable=False, unique=False)
    portal_name = Column(String, primary_key=False, nullable=False, unique=False)

# class Holiday(Base):
#     __tablename__ = "holidays"

#     id = Column(Integer, primary_key=True, nullable=False)
#     created_at = Column(TIMESTAMP(timezone=True), primary_key=False, nullable=False, server_default=text("now()"))

#     date = Column(TIMESTAMP(timezone=True), primary_key=False, nullable=False)
#     is_public = Column(Boolean, primary_key=False, nullable=True, unique=False)
#     name = Column(String, primary_key=False, nullable=True, unique=False)
