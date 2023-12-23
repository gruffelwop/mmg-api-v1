# python
from datetime import datetime, date
import asyncio
from icecream import ic

# constants
import app.constants.v1.enum as enum_v1

# functions
from app.services.v1.plan.httpx.fetch_all_plans import fetch_all_plans as fetch_all_plans_v1
from app.services.v1.plan.python.get_plan_date_from_soup import get_plan_date_from_soup as get_plan_date_from_soup_v1
from app.services.v1.plan.python.get_plan_from_soup import get_plan_from_soup as get_plan_from_soup_v1
from app.services.v1.date.python.get_next_weekday import get_next_weekday as get_next_weekday_v1
from app.services.v1.date.python.get_weekday_after_next_weekday import get_weekday_after_next_weekday as get_weekday_after_next_weekday_v1

def fetch_correct_plan(plan_type: enum_v1.PlanType, username: str, password: str):
    unix_epoch = date.fromtimestamp(0)
    now = datetime.now()
    today = datetime(year=now.year, month=now.month, day=now.day).date()
    weekday = today.weekday()

    nextWeekDay = get_next_weekday_v1(today=today, weekday=weekday)
    weekDayAfterNextWeekDay = get_weekday_after_next_weekday_v1(today=today, weekday=weekday)

    HTMLs = asyncio.run(fetch_all_plans_v1(username=username, password=password))

    todayOrLastSchoolDayHTML = HTMLs[0]
    nextSchoolDayHTML = HTMLs[1]
    schoolDayAfterNextSchoolDayHTML = HTMLs[2]

    # ic(todayOrLastSchoolDayHTML)

    planDateTodayOrLastSchoolDay = get_plan_date_from_soup_v1(soup=todayOrLastSchoolDayHTML)
    planDateNextSchoolDay = get_plan_date_from_soup_v1(soup=nextSchoolDayHTML)
    planDateSchoolDayAfterNextSchoolDay = get_plan_date_from_soup_v1(soup=schoolDayAfterNextSchoolDayHTML)

    # ic(planDateTodayOrLastSchoolDay)

    # View 1:
    if plan_type == enum_v1.PlanType.today:
        if weekday == 5 or weekday == 6: # Saturday or Sunday
            if nextWeekDay == planDateNextSchoolDay:
                return get_plan_from_soup_v1(soup=nextSchoolDayHTML, timestamp=planDateNextSchoolDay)
        else:
            if today == planDateTodayOrLastSchoolDay:
                return get_plan_from_soup_v1(soup=todayOrLastSchoolDayHTML, timestamp=planDateTodayOrLastSchoolDay)
            if today == planDateNextSchoolDay:
                return get_plan_from_soup_v1(soup=nextSchoolDayHTML, timestamp=planDateNextSchoolDay)

    # View 2:
    if plan_type == enum_v1.PlanType.tomorrow:
        if weekday == 5 or weekday == 6: # Saturday or Sunday
            if weekDayAfterNextWeekDay == planDateSchoolDayAfterNextSchoolDay:
                return get_plan_from_soup_v1(soup=schoolDayAfterNextSchoolDayHTML, timestamp=planDateSchoolDayAfterNextSchoolDay)
        else:
            if nextWeekDay == planDateNextSchoolDay:
                return get_plan_from_soup_v1(soup=nextSchoolDayHTML, timestamp=planDateNextSchoolDay)
            if nextWeekDay == planDateSchoolDayAfterNextSchoolDay:
                return get_plan_from_soup_v1(soup=schoolDayAfterNextSchoolDayHTML, timestamp=planDateSchoolDayAfterNextSchoolDay)

    return {
        "date": unix_epoch,
        "updated": unix_epoch,
        "substitutions": [],
    }
