# from fastapi import APIRouter, Depends, status, HTTPException, BackgroundTasks

# from app.enums import PlanType
# from ...services import plan

# from ... import schemas, oauth2, exceptions

# router = APIRouter(
#     prefix="/plans",
#     tags=["Plans"],
# )

#     # html = HTML.HTML(URL.todayOrLastSchoolDayURL(username=plan_credentials.username, password=plan_credentials.password))
#     # return plan.getPlan(
#     #     soup=html,
#     #     timestamp=plan.getPlanDate(html)
#     # )

# @router.get("/today", response_model=schemas.Plan)
# def today(plan_credentials: schemas.PlanCredentials, current_user = Depends(oauth2.get_current_user)):
#     try:
#         return plan.fetch_correct_plan_2(plan_type=PlanType.today, username=plan_credentials.username, password=plan_credentials.password)
#     except exceptions.InvalidPlanCredentialsException:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Plan Credentials")
#     except:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

# # @router.get("/today", response_model=schemas.PlanExp)
# # def today():
#     # return {
#     #     "Plan": functions.fetch_correct_plan(plan_type=PlanType.today),
#     #     "Day": {
#     #         "is_holiday": True,
#     #         "is_public": False,
#     #         "name": "Sommerferien"
#     #     },
#     # }

# @router.get("/tomorrow", response_model=schemas.Plan)
# def tomorrow(plan_credentials: schemas.PlanCredentials, current_user = Depends(oauth2.get_current_user)):
#     try:
#         return plan.fetch_correct_plan(plan_type=PlanType.tomorrow, username=plan_credentials.username, password=plan_credentials.password)
#     except exceptions.InvalidPlanCredentialsException:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Plan Credentials")
#     except:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

# # {
# #     "Plan": {
# #         "timestamp": datetime(),
# #         "updated": datetime(),
# #         "substitutions": []
# #     },
# #     "Day": {
# #         "is_holiday": True,
# #         "is_public_holiday": False,
# #         "holiday_name": "",
# #     }
# # }