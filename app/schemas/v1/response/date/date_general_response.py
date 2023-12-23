from pydantic import BaseModel
from datetime import datetime, date, time

class DateGeneralResponse(BaseModel):
    start_date: date
    end_date: date
    start_time: time
    end_time: time

    # start_time: datetime
    # end_time: datetime

    # start: datetime
    # end: datetime

    content: str

    class Config:
        from_attributes = True
