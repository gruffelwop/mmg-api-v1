from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from .routers.v1 import date as date_v1, plan as plan_v1, settings as settings_v1, student as student_v1
from .routers.v2 import auth as auth_v2, date as date_v2, plan as plan_v2, student as student_v2, test as test_v2, user as user_v2

app = FastAPI()

handler = Mangum(app)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# v1
app.include_router(date_v1.router)
app.include_router(plan_v1.router)
app.include_router(settings_v1.router)
app.include_router(student_v1.router)

# v2
# app.include_router(auth_v2.router)
# app.include_router(date_v2.router)
# app.include_router(plan_v2.router)
# app.include_router(student_v2.router)
# # app.include_router(teacher.router)
# app.include_router(test_v2.router)
# app.include_router(user_v2.router)

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/v1/plans/test")
def test():
    return {
            "date": "2023-12-18",
            "updated": "2023-12-16 19:50:00",
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