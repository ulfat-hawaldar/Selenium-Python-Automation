from datetime import datetime, timedelta
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Datepicker.html")
driver.find_element(By.ID,'datepicker2').click()
time.sleep(5)
current_date = datetime.now()
print(current_date)

next_day = current_date + timedelta(days=1)
print(next_day)
Next_day = (str(next_day.day))
print(Next_day)

Current_month = datetime.now().month
Current_year = current_date.year

next_month = (Current_month % 12) + 1
next_month_year = f"{next_month}/{Current_year}"
Month_Dropdown = driver.find_element(By.CSS_SELECTOR,"select[title='Change the month']")
select = Select(Month_Dropdown)
select.select_by_value(str(next_month_year))
year_dropdown = driver.find_element(By.CSS_SELECTOR,"select[title='Change the year']")
select = Select(year_dropdown)
select.select_by_visible_text("2024")
driver.find_element(By.LINK_TEXT, Next_day).click()
time.sleep(5)