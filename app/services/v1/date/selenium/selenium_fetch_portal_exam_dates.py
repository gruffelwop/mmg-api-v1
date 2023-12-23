from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from selenium import webdriver
from bs4 import BeautifulSoup

import app.constants.v1.exception as exception_v1
import app.constants.v1.url as url_v1
import app.constants.v1.regex as regex_v1

import re

def selenium_fetch_portal_exam_dates(email: str, password: str, name: str):
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
        
        if student_found == False:
            raise exception_v1.NameNotFoundException()

        try:
            driver.get(url_v1.EXAM_DATES_URL)
            soup = BeautifulSoup(driver.page_source, "html.parser")
            soup.find("div", class_="text-right settings").get_text().strip().startswith("letzter Login:")
            try:
                exams = []
                table = soup.find("table", class_="table2")
                for row in table.find_all('tr'):
                    cells = row.find_all('td')
                    if len(cells) >= 3:
                        date = datetime.strptime(cells[0].text.strip(), "%d.%m.%Y").date()
                        exam = cells[2].text.strip()

                        if re.match(regex_v1.UNTERSTUFE_EXAM_CLASS_TEACHER_REGEX, exam):
                            splitted_exam = exam.split(" ")
                            exams.append({
                                "date": date,
                                "type": exam.split(" in")[0],
                                "course": splitted_exam[-2].removeprefix("(").removesuffix(")"),
                                "subject": "",
                                "teacher": splitted_exam[-1].removeprefix("(").removesuffix(")"),
                            })
                            continue
                        if re.match(regex_v1.UNTERSTUFE_EXAM_TEACHER_REGEX, exam):
                            splitted_exam = exam.split(" ")
                            exams.append({
                                "date": date,
                                "type": exam.split(" in")[0],
                                "course": "9A",
                                "subject": "",
                                "teacher": splitted_exam[-1].removeprefix("(").removesuffix(")"),
                            })
                            continue
                        if re.match(regex_v1.OBERSTUFE_EXAM_REGEX, exam):
                            splitted_exam = exam.split(" ")
                            course_dash_teacher = exam.split("(")[1].removesuffix(")").split(" - ")
                            exams.append({
                                "date": date,
                                "type": exam.split(" in")[0],
                                "course": course_dash_teacher[0],
                                "subject": "",
                                "teacher": course_dash_teacher[1],
                            })
                            continue

                return exams
            except:
                return []
        except:
            raise exception_v1.InvalidPortalCredentialsException()
