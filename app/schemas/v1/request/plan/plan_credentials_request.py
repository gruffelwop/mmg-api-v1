from pydantic import BaseModel

class PlanCredentialsRequest(BaseModel):
    username: str
    password: str
