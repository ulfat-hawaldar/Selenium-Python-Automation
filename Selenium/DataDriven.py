import time

from selenium import webdriver
from openpyxl import load_workbook
from selenium.webdriver.common.by import By

from Selenium.Login import password

# Load the Excel Sheet

workbook = load_workbook('Testdata.xlsx')
sheet = workbook.active

driver = webdriver.Chrome()
driver.maximize_window()

for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row, values_only=True):
    Username = row[0]
    Password = row[1]

    driver.get("https://www.saucedemo.com/")
    time.sleep(5)
    driver.find_element(By.ID,"user-name").send_keys(Username)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.ID,"login-button").click()
    time.sleep(5)
