# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from ... import models, schemas
# from ...database import get_db
# from typing import List
# from datetime import datetime

# router = APIRouter(prefix="/tests", tags=["Test"])

# @router.get("/db", response_model=schemas.HolidayResponse)
# def test_db(db: Session = Depends(get_db)):
#     # holidays = db.query(models.Holiday).all()

#     now = datetime.now()
#     today = datetime(year=now.year, month=now.month, day=now.day)
#     today = datetime(year=2023, month=10, day=3)
#     result = db.query(models.Holiday).filter(models.Holiday.date == today).first()
#     return result