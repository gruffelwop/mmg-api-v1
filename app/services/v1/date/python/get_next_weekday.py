from datetime import datetime, timedelta

def get_next_weekday(today: datetime, weekday: int):
    if weekday == 4:
        return today + timedelta(days=3)
    if weekday == 5:
        return today + timedelta(days=2)
    else:
        return today + timedelta(days=1)
