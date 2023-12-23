from pydantic import BaseModel

class SubstitutionResponse(BaseModel):
    course: str
    hour: str
    substitute_teacher: str
    subject: str
    room: str
    replaced_teacher: str

    class Config:
        from_attributes = True
