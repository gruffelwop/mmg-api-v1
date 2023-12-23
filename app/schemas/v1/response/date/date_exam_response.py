from pydantic import BaseModel
from datetime import date

class DateExamResponse(BaseModel):
    date: date
    type: str
    course: str
    subject: str
    teacher: str

    class Config:
        from_attributes = True
