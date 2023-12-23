# from fastapi import APIRouter, Depends, status, HTTPException
# from typing import List

# from ... import oauth2, schemas, exceptions
# from ...services.date_v1.selenium.selenium_fetch_portal_exam_dates import selenium_fetch_portal_exam_dates_v1

# router = APIRouter(
#     prefix="/dates",
#     tags=["Dates"],
# )

#     # exams = db.query(models.Exam).filter(models.Exam.user_id == )

# @router.get("/exams", response_model=List[schemas.DateExamResponse])
# def get_date_exams(portal_credentials: schemas.PortalCredentials, current_user = Depends(oauth2.get_current_user)):
#     try:
#         return selenium_fetch_portal_exam_dates_v1(email=portal_credentials.email, password=portal_credentials.password, exam=portal_credentials.name)
#     except exceptions.InvalidPortalCredentialsException:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Plan Credentials")
#     except exceptions.NameNotFoundException:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Name was not found")
#     except:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

# # @router.get("/general", response_model=List[schemas.DateGeneralResponse])
# # def get_date_general(db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
# #     pass