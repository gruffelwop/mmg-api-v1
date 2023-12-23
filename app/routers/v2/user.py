# from fastapi import status, HTTPException, Depends, APIRouter
# from sqlalchemy.orm import Session
# from ... import models, schemas, utils, oauth2
# from ...database import get_db

# router = APIRouter(
#     prefix="/users",
#     tags=["Users"],
# )

# @router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
# def create_user(user: schemas.User, db: Session = Depends(get_db)):
#     email = db.query(models.User).filter(models.User.email == user.email).first()
#     username = db.query(models.User).filter(models.User.username == user.username).first()
#     if email:
#         raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Email already in use")
#     if username:
#         raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Username already in use")
#     hashed_password = utils.hash(user.password)
#     user.password = hashed_password
#     new_user = models.User(**user.dict())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @router.get("/{id}", response_model=schemas.UserResponse)
# def get_user(id: int, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found")
#     return user