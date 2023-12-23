from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import app.constants.v1.url as url_v1
import app.constants.v1.exception as exception_v1
from app.utils.v1.split_list_into_chunks import split_list_into_chunks as split_list_into_chunks_v1

import pandas as pd

from icecream import ic

def selenium_fetch_portal_absences(email: str, password: str, name: str):
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

        student_found = False
        student = driver.find_element(by=By.CSS_SELECTOR, value="select[class='form-control']")
        for option in student.find_elements(by=By.TAG_NAME, value="option"):
            if option.text.strip().startswith(name):
                student_found = True
                option.click()
                break

        # time.sleep(5)
        
        if student_found == False:
            raise exception_v1.NameNotFoundException()

        try:
            driver.get(url_v1.ABSENCES_URL)
            soup = BeautifulSoup(driver.page_source, "html.parser")
            soup.find("div", class_="text-right settings").get_text().strip().startswith("letzter Login:")
            try:
                rawDates = driver.find_elements(by=By.CSS_SELECTOR, value="td[class='four wide']")
                date_ranges = []
                dates_and_reasons = []
                for item in rawDates:
                    for day in item.get_attribute(name="innerHTML").strip().split("<br>")[0:2]:
                        date_ranges.append(f"{datetime.strptime(day.strip(), '%d.%m.%Y').date()}")
                    # date_ranges.append([f"{datetime.strptime(day.strip(), '%d.%m.%Y').date()}" for day in item.get_attribute(name="innerHTML").strip().split("<br>")[0:2]])
                
                raw_reasons = driver.find_elements(by=By.CSS_SELECTOR, value="td[class='eleven wide']")
                reasons = []
                for item in raw_reasons:
                    reasons.append(item.get_attribute(name="innerHTML").strip().replace("Krankheit:", "").strip())
                
                date_ranges = list(split_list_into_chunks_v1(date_ranges, 2))

                for date_range_index in range(0, len(date_ranges)):
                    date_list = pd.date_range(date_ranges[date_range_index][0], date_ranges[date_range_index][1])
                    for date in date_list:
                        dates_and_reasons.append({"date": date.date(), "reason": reasons[date_range_index]})
                return dates_and_reasons
            except:
                return []
        except:
            raise exception_v1.InvalidPortalCredentialsException()
