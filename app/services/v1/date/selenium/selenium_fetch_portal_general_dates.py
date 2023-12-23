from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime, time
from selenium import webdriver
from bs4 import BeautifulSoup

import app.constants.v1.exception as exception_v1
import app.constants.v1.url as url_v1

from icecream import ic

def selenium_fetch_portal_general_dates(email: str, password: str):
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    with webdriver.Chrome(options=chrome_options) as driver:
        driver.get(url_v1.PORTAL_URL)

        inputEmail = driver.find_element(by=By.ID, value="inputEmail")
        inputPassword = driver.find_element(by=By.ID, value="inputPassword")

        inputEmail.send_keys(email)
        inputPassword.send_keys(password)
        
        submitButton = driver.find_element(by=By.CLASS_NAME, value="btn.btn-lg.btn-primary.btn-block")
        submitButton.click()

        driver.get(url_v1.PORTAL_URL + "start/")
        soup = BeautifulSoup(driver.page_source, "html.parser")

        div = soup.find("div", class_="text-right settings")
        if div:
            if not div.get_text().strip().startswith("letzter Login:"):
                raise exception_v1.InvalidPortalCredentialsException()
        if not div:
            raise exception_v1.InvalidPortalCredentialsException()

        try:
            driver.get(url_v1.GENERAL_DATES_URL)
            soup = BeautifulSoup(driver.page_source, "html.parser")
            soup.find("div", class_="text-right settings").get_text().strip().startswith("letzter Login:")
            try:
                general_dates = []
                table = soup.find("table", class_="table2")
                for row in table.find_all('tr'):
                    cells = row.find_all('td')
                    if len(cells) >= 3:
                        raw_date_range = cells[0].text.strip().split(" - ")
                        raw_time_range = cells[1].text.strip().split(" - ") if cells[1] != "" else ["",""]
                        raw_content = cells[2].contents

                        content = ""

                        for index in range(0, len(raw_content)):
                            if str(raw_content[index]) == "<br/>" and (index + 1) == len(raw_content):
                                continue

                            if str(raw_content[index]) == "<br/>" and (index + 1) != len(raw_content):
                                content = content + ", "
                                continue
                            
                            content += raw_content[index].strip().replace("\n", " ")

                        start_time = ""
                        end_time = ""

                        if raw_time_range == [""]:
                            # start_time = datetime.fromtimestamp(0).time()
                            # end_time = datetime.fromtimestamp(0).time()

                            start_time = datetime(1970, 1, 1, 0, 0, 0).time()
                            end_time = datetime(1970, 1, 1, 0, 0, 0).time()
                        else:
                            start_time = datetime.strptime(raw_time_range[0], "%H:%M").time()
                            end_time = datetime.strptime(raw_time_range[1], "%H:%M").time()

                        general_dates.append({
                            "start_date": datetime.strptime(raw_date_range[0], "%d.%m.%Y").date(),
                            "end_date": datetime.strptime(raw_date_range[1], "%d.%m.%Y").date(),
                            "start_time": start_time,
                            "end_time": end_time,
                            "content": content,
                        })

                return general_dates
            except:
                return []
        except:
            raise exception_v1.InvalidPortalCredentialsException()
