from pydantic import BaseModel
from datetime import datetime, date
from typing import List

from app.schemas.v1.response.plan.substitution_response import SubstitutionResponse


class PlanResponse(BaseModel):
    date: date
    updated: datetime
    substitutions: List[SubstitutionResponse]

    class Config:
        from_attributes = True
