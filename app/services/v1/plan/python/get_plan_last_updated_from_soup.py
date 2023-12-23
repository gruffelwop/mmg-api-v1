from bs4 import BeautifulSoup
from datetime import datetime

def get_plan_last_updated_from_soup(soup: BeautifulSoup):
    dateString = soup.find("th", class_="TextAktuellesDatum").get_text().strip().replace("Stand:", "").strip()
    split = dateString.split(" ")
    date = split[1]
    time = split[2]
    dateString = f"{date} {time}"
    return datetime.strptime(dateString, "%d.%m.%Y %H:%M")
