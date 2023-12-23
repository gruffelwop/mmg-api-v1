# fastapi
from fastapi import APIRouter

# schemas
from app.schemas.v1.response.settings.settings_response import SettingsResponse

router = APIRouter(
    prefix="/v1/settings",
    tags=["Settings"],
)

@router.get("/default", response_model=SettingsResponse)
def get_settings_default():
    return {
        "corner_radius": 8,
        "ecetera": "ecetera",
    }
