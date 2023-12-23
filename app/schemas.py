# from pydantic import BaseModel, EmailStr
# from datetime import datetime, date
# from typing import List, Optional

# # class Error(BaseModel):
# #     encountered_error: bool
# #     error_type: str

# class Holiday(BaseModel):
#     is_holiday: bool
#     is_public_holiday: bool
#     holiday_name: str

# class HolidayResponse(BaseModel):
#     # is_holiday: bool
#     date: datetime
#     is_public: bool
#     name: str

# class HolidayResponse2(BaseModel):
#     # date: datetime
#     is_holiday: bool
#     is_public: bool
#     name: str

# class Teacher(BaseModel):
#     abbreviation: str
#     name: str

# # class Substitution(BaseModel):
# #     course: str
# #     hour: str
# #     substitute_teacher: str
# #     subject: str
# #     room: str
# #     replaced_teacher: str

# class SubstitutionNew(BaseModel):
#     course: str
#     hour: str
#     substitute_teacher: Teacher
#     subject: str
#     room: str
#     replaced_teacher: Teacher

# # class TeacherAbsence(BaseModel):
# #     teacher: str
# #     info: str

# # class Notification(BaseModel):
# #     recipient: str
# #     notice: str

# # class Plan(BaseModel):
# #     date: date
# #     updated: datetime
# #     substitutions: List[Substitution]
# #     # day: Holiday

# #     # day and error will be added later.
# #     # error: Error

# #     # absences: List[TeacherAbsence]
# #     # notifications: List[Notification]

# #     class Config:
# #         from_attributes = True

# # class StudentAbsence(BaseModel):
# #     start: date
# #     end: date
# #     # user_id: int

# #     class Config:
# #         from_attributes = True

# class Token(BaseModel):
#     access_token: str
#     token_type: str

# class PlanExp(BaseModel):
#     Plan: Plan
#     Day: HolidayResponse2

# class UserResponse(BaseModel):
#     id: int
#     email: EmailStr
#     username: str
#     created_at: datetime
    
#     class Config:
#         from_attributes = True

# class User(BaseModel):
#     email: EmailStr
#     password: str
#     username: str

# class TokenData(BaseModel):
#     id: Optional[str] = None

# # class DateExamResponse(BaseModel):
# #     date: date
# #     type: str
# #     course: str
# #     subject: str
# #     teacher: str

# # class DateGeneralResponse(BaseModel):
# #     date: date

# #     type: str
# #     # course: str
# #     # teacher: str

# # class PortalCredentials(BaseModel):
# #     email: EmailStr
# #     password: str
# #     name: str

# # class PortalCredentialsWithoutName(BaseModel):
# #     email: EmailStr
# #     password: str

# # class PlanCredentials(BaseModel):
# #     username: str
# #     password: str