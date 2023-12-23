# from fastapi import APIRouter, Depends, status, HTTPException, BackgroundTasks
# from sqlalchemy.orm import Session
# from typing import List
# from datetime import date

# from ... import oauth2, schemas, exceptions
# from ...services import student
# from ...database import get_db

# router = APIRouter(
#     prefix="/students",
#     tags=["Students"],
# )

# @router.get("/absences", response_model=List[date])
# def get_student_absences(background_tasks: BackgroundTasks, portal_credentials: schemas.PortalCredentials, current_user = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
#     try:
#         absences = student.selenium_fetch_portal_absences(email=portal_credentials.email, password=portal_credentials.password, name=portal_credentials.name)
#         background_tasks.add_task(student.add_portal_absences_to_db, absences=absences, user_id=current_user.id, portal_email=portal_credentials.email, portal_name=portal_credentials.name, db=db)
#         return absences
#     except exceptions.InvalidPortalCredentialsException:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Plan Credentials")
#     except exceptions.NameNotFoundException:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Name was not found")
#     except:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

# # @router.get("/algorithm", )
# # def get_student_algorithm():
# #     pass