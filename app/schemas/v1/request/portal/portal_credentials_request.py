from pydantic import BaseModel, EmailStr

class PortalCredentialsRequest(BaseModel):
    email: EmailStr
    password: str
    name: str
