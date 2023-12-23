from pydantic import BaseModel

class SettingsResponse(BaseModel):
    corner_radius: int
    ecetera: str

    class Config:
        from_attributes = True
