from bs4 import BeautifulSoup
from datetime import date

from app.services.v1.plan.python.get_plan_last_updated_from_soup import get_plan_last_updated_from_soup as get_plan_last_updated_from_soup_v1
from app.services.v1.plan.python.get_substitutions_from_soup import get_substitutions_from_soup as get_substitutions_from_soup_v1

def get_plan_from_soup(soup: BeautifulSoup, timestamp: date):
    return {
        "date": timestamp,
        "updated": get_plan_last_updated_from_soup_v1(soup=soup),
        "substitutions": get_substitutions_from_soup_v1(soup=soup),
    }