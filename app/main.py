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
