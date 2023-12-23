from bs4 import BeautifulSoup
from datetime import datetime

def get_plan_date_from_soup(soup: BeautifulSoup):
    dateString = soup.find("h2", class_="TextUeberschrift").get_text().strip().split(",")[1].strip()
    return datetime.strptime(dateString, "%d.%m.%Y").date()
