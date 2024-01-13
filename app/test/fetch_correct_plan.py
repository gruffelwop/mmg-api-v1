# python
from datetime import datetime, date, timedelta
from icecream import ic
from enum import Enum


class PlanType(Enum):
    today = "today"
    tomorrow = "tomorrow"

def get_next_weekday_v1(today: datetime, weekday: int):
    if weekday == 4:
        return today + timedelta(days=3)
    if weekday == 5:
        return today + timedelta(days=2)
    else:
        return today + timedelta(days=1)
    
def get_weekday_after_next_weekday_v1(today: datetime, weekday: int):
    if weekday == 4:
        return today + timedelta(days=4)
    if weekday == 5:
        return today + timedelta(days=3)
    else:
        return today + timedelta(days=2)

def fetch_correct_plan(plan_type: PlanType, planDateTodayOrLastSchoolDay: date, planDateNextSchoolDay: date, planDateSchoolDayAfterNextSchoolDay: date):
    unix_epoch = date.fromtimestamp(0)
    now = datetime.now()
    today = datetime(year=now.year, month=now.month, day=now.day).date()
    weekday = today.weekday()

    nextWeekDay = get_next_weekday_v1(today=today, weekday=weekday)
    weekDayAfterNextWeekDay = get_weekday_after_next_weekday_v1(today=today, weekday=weekday)

    # View 1:
    if plan_type == PlanType.today:
        if weekday == 5 or weekday == 6: # Saturday or Sunday
            if nextWeekDay == planDateTodayOrLastSchoolDay:
                return planDateTodayOrLastSchoolDay
            if nextWeekDay == planDateNextSchoolDay:
                return planDateNextSchoolDay
            if nextWeekDay == planDateSchoolDayAfterNextSchoolDay:
                return planDateSchoolDayAfterNextSchoolDay
        else:
            if today == planDateTodayOrLastSchoolDay:
                return planDateTodayOrLastSchoolDay
            if today == planDateNextSchoolDay:
                return planDateNextSchoolDay
            if today == planDateSchoolDayAfterNextSchoolDay:
                return planDateSchoolDayAfterNextSchoolDay

    # View 2:
    if plan_type == PlanType.tomorrow:
        if weekday == 5 or weekday == 6: # Saturday or Sunday
            if weekDayAfterNextWeekDay == planDateTodayOrLastSchoolDay:
                return planDateTodayOrLastSchoolDay
            if weekDayAfterNextWeekDay == planDateNextSchoolDay:
                return planDateNextSchoolDay
            if weekDayAfterNextWeekDay == planDateSchoolDayAfterNextSchoolDay:
                return planDateSchoolDayAfterNextSchoolDay
        else:
            if nextWeekDay == planDateSchoolDayAfterNextSchoolDay:
                return planDateSchoolDayAfterNextSchoolDay
            if nextWeekDay == planDateNextSchoolDay:
                return planDateNextSchoolDay
            if nextWeekDay == planDateSchoolDayAfterNextSchoolDay:
                return planDateSchoolDayAfterNextSchoolDay

    return unix_epoch

ic(fetch_correct_plan(
    plan_type=PlanType.tomorrow,
    planDateTodayOrLastSchoolDay=date(2023, 12, 22),
    planDateNextSchoolDay=date(2024, 1, 9),
    planDateSchoolDayAfterNextSchoolDay=date(2024, 1, 8),
))