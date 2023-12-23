# fastapi
from fastapi import APIRouter, status, HTTPException

from app.schemas.v1.response.plan.plan_response import PlanResponse
from app.schemas.v1.request.plan.plan_credentials_request import PlanCredentialsRequest

# constants
import app.constants.v1.exception as exception_v1
import app.constants.v1.error as error_v1
import app.constants.v1.enum as enum_v1

# functions
from app.services.v1.plan.httpx.fetch_correct_plan import fetch_correct_plan as fetch_correct_plan_v1

router = APIRouter(
    prefix="/v1/plans",
    tags=["Plans"],
)

@router.get("/today", response_model=PlanResponse)
def today(plan_credentials: PlanCredentialsRequest):
    try:
        # return fetch_correct_plan_v1(plan_type=enum_v1.PlanType.today, username=plan_credentials.username, password=plan_credentials.password)
        return fetch_correct_plan_v1(plan_type=enum_v1.PlanType.today, username="mmg-sus", password="Pinigo47watu&")
    except exception_v1.InvalidPlanCredentialsException:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=error_v1.INVALID_PLAN_CREDENTIALS)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@router.get("/tomorrow", response_model=PlanResponse)
def tomorrow(plan_credentials: PlanCredentialsRequest):
    try:
        return fetch_correct_plan_v1(plan_type=enum_v1.PlanType.tomorrow, username=plan_credentials.username, password=plan_credentials.password)
    except exception_v1.InvalidPlanCredentialsException:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=error_v1.INVALID_PLAN_CREDENTIALS)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
