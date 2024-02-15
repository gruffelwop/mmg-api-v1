# fastapi
from fastapi import APIRouter, status, HTTPException

# python
from typing import List

from app.schemas.v1.request.portal.portal_credentials_request import PortalCredentialsRequest
from app.schemas.v1.response.student.absence_response import AbsenceResponse

# functions
from app.services.v1.student.selenium.selenium_fetch_portal_absences import selenium_fetch_portal_absences as selenium_fetch_portal_absences_v1

# constants
import app.constants.v1.exception as exception_v1
import app.constants.v1.error as error_v1

router = APIRouter(
    prefix="/v1/students",
    tags=["Students"],
)

@router.get("/absences", response_model=List[AbsenceResponse])
def get_student_absences(portal_credentials: PortalCredentialsRequest):
    try:
        return selenium_fetch_portal_absences_v1(email=portal_credentials.email, password=portal_credentials.password, name=portal_credentials.name)
    except exception_v1.InvalidPortalCredentialsException:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=error_v1.INVALID_PORTAL_CREDENTIALS)
    except exception_v1.NameNotFoundException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error_v1.NAME_NOT_FOUND)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
