from pydantic import BaseModel, EmailStr

class PortalCredentialsWithoutNameRequest(BaseModel):
    email: EmailStr
    password: str
