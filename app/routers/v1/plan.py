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

# @router.get("/today", response_model=PlanResponse)
@router.post("/today", response_model=PlanResponse)
def today(plan_credentials: PlanCredentialsRequest):
    if plan_credentials.username.strip() == "" or plan_credentials.password.strip() == "":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=error_v1.INVALID_PLAN_CREDENTIALS)
    try:
        return fetch_correct_plan_v1(plan_type=enum_v1.PlanType.today, username=plan_credentials.username, password=plan_credentials.password)
        # return fetch_correct_plan_v1(plan_type=enum_v1.PlanType.today, username="mmg-sus", password="Pinigo47watu&")
    except exception_v1.InvalidPlanCredentialsException:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=error_v1.INVALID_PLAN_CREDENTIALS)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

# @router.get("/tomorrow", response_model=PlanResponse)
@router.post("/tomorrow", response_model=PlanResponse)
def tomorrow(plan_credentials: PlanCredentialsRequest):
    if plan_credentials.username.strip() == "" or plan_credentials.password.strip() == "":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=error_v1.INVALID_PLAN_CREDENTIALS)
    try:
        return fetch_correct_plan_v1(plan_type=enum_v1.PlanType.tomorrow, username=plan_credentials.username, password=plan_credentials.password)
    except exception_v1.InvalidPlanCredentialsException:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=error_v1.INVALID_PLAN_CREDENTIALS)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@router.post("/test")
def test():
    return {
            "date": "2023-12-18",
            "updated": "2023-12-16T19:50:00",
            "substitutions": [
                {
                    "course": "",
                    "hour": "8",
                    "substitute_teacher": "entfällt",
                    "subject": "VL",
                    "room": "Mensa",
                    "replaced_teacher": "HART"
                },
                {
                    "course": "2ph1",
                    "hour": "5",
                    "substitute_teacher": "entfällt",
                    "subject": "Ph",
                    "room": "E131",
                    "replaced_teacher": "LEHM"
                },
                {
                    "course": "5D",
                    "hour": "3",
                    "substitute_teacher": "KRAM",
                    "subject": "M",
                    "room": "B09",
                    "replaced_teacher": "LEHM"
                },
                {
                    "course": "5d2",
                    "hour": "5",
                    "substitute_teacher": "KRAM",
                    "subject": "D",
                    "room": "B09",
                    "replaced_teacher": "EISE"
                },
                {
                    "course": "6C",
                    "hour": "5",
                    "substitute_teacher": "KREN",
                    "subject": "E1",
                    "room": "E140",
                    "replaced_teacher": "GREI"
                },
                {
                    "course": "6absm",
                    "hour": "3",
                    "substitute_teacher": "DOME",
                    "subject": "Sm",
                    "room": "rThJ",
                    "replaced_teacher": "HART"
                },
                {
                    "course": "7D",
                    "hour": "5",
                    "substitute_teacher": "FRON",
                    "subject": "Mu",
                    "room": "E119",
                    "replaced_teacher": "SHWA"
                },
                {
                    "course": "8B",
                    "hour": "6",
                    "substitute_teacher": "entfällt",
                    "subject": "E1",
                    "room": "A11",
                    "replaced_teacher": "GREI"
                },
                {
                    "course": "9A",
                    "hour": "4",
                    "substitute_teacher": "BODA",
                    "subject": "B",
                    "room": "C06",
                    "replaced_teacher": "RAMI"
                },
                {
                    "course": "9C",
                    "hour": "6",
                    "substitute_teacher": "entfällt",
                    "subject": "Mu",
                    "room": "E119",
                    "replaced_teacher": "GORZ"
                },
                {
                    "course": "10A",
                    "hour": "5",
                    "substitute_teacher": "EU",
                    "subject": "PuG",
                    "room": "B19",
                    "replaced_teacher": "VOGH"
                },
                {
                    "course": "2b1",
                    "hour": "5",
                    "substitute_teacher": "entfällt",
                    "subject": "B",
                    "room": "E141",
                    "replaced_teacher": "RAMI"
                },
                {
                    "course": "5D",
                    "hour": "2",
                    "substitute_teacher": "MÄRK",
                    "subject": "D",
                    "room": "B09",
                    "replaced_teacher": "EISE"
                },
                {
                    "course": "5d1",
                    "hour": "6",
                    "substitute_teacher": "KRAM",
                    "subject": "D",
                    "room": "B09",
                    "replaced_teacher": "EISE"
                },
                {
                    "course": "5d2",
                    "hour": "6",
                    "substitute_teacher": "KRAM",
                    "subject": "E1",
                    "room": "B09",
                    "replaced_teacher": "KRAM"
                },
                {
                    "course": "6D",
                    "hour": "3",
                    "substitute_teacher": "GRAF",
                    "subject": "D",
                    "room": "A02",
                    "replaced_teacher": "GREI"
                },
                {
                    "course": "6absm",
                    "hour": "4",
                    "substitute_teacher": "DOME",
                    "subject": "Sm",
                    "room": "rThJ",
                    "replaced_teacher": "HART"
                },
                {
                    "course": "8A",
                    "hour": "4",
                    "substitute_teacher": "HASL",
                    "subject": "D",
                    "room": "A12",
                    "replaced_teacher": "EISE"
                },
                {
                    "course": "8D",
                    "hour": "1",
                    "substitute_teacher": "REIT",
                    "subject": "L2",
                    "room": "E140",
                    "replaced_teacher": "EISE"
                },
                {
                    "course": "9B",
                    "hour": "4",
                    "substitute_teacher": "HÖLZ",
                    "subject": "Mu",
                    "room": "C07",
                    "replaced_teacher": "GORZ"
                },
                {
                    "course": "10A",
                    "hour": "4",
                    "substitute_teacher": "EU",
                    "subject": "D",
                    "room": "B19",
                    "replaced_teacher": "VOGH"
                },
                {
                    "course": "10cdntg",
                    "hour": "6",
                    "substitute_teacher": "entfällt",
                    "subject": "Ph",
                    "room": "E133",
                    "replaced_teacher": "LEHM"
                }
            ]
        }