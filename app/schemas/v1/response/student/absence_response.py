from pydantic import BaseModel
from datetime import date

class AbsenceResponse(BaseModel):
    date: date
    reason: str