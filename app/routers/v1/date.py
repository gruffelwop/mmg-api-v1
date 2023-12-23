# fastapi
from fastapi import APIRouter, status, HTTPException

# python
from typing import List

from app.schemas.v1.response.date.date_exam_response import DateExamResponse
from app.schemas.v1.response.date.date_general_response import DateGeneralResponse
from app.schemas.v1.request.portal.portal_credentials_request import PortalCredentialsRequest
from app.schemas.v1.request.portal.portal_credentials_without_name_request import PortalCredentialsWithoutNameRequest

# constants
import app.constants.v1.exception as exception_v1
import app.constants.v1.error as error_v1

# functions
from app.services.v1.date.selenium.selenium_fetch_portal_exam_dates import selenium_fetch_portal_exam_dates as selenium_fetch_portal_exam_dates_v1
from app.services.v1.date.selenium.selenium_fetch_portal_general_dates import selenium_fetch_portal_general_dates as selenium_fetch_portal_general_dates_v1

router = APIRouter(
    prefix="/v1/dates",
    tags=["Dates"],
)

@router.get("/exams", response_model=List[DateExamResponse])
def get_date_exams(portal_credentials: PortalCredentialsRequest):
    try:
        return selenium_fetch_portal_exam_dates_v1(email=portal_credentials.email, password=portal_credentials.password, name=portal_credentials.name)
    except exception_v1.InvalidPortalCredentialsException:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=error_v1.INVALID_PORTAL_CREDENTIALS)
    except exception_v1.NameNotFoundException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error_v1.NAME_NOT_FOUND)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@router.get("/general", response_model=List[DateGeneralResponse])
def get_date_exams(portal_credentials_without_name: PortalCredentialsWithoutNameRequest):
    try:
        return selenium_fetch_portal_general_dates_v1(email=portal_credentials_without_name.email, password=portal_credentials_without_name.password)
    except exception_v1.InvalidPortalCredentialsException:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=error_v1.INVALID_PORTAL_CREDENTIALS)
    except exception_v1.NameNotFoundException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error_v1.NAME_NOT_FOUND)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
