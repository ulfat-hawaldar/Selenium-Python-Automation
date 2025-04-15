import time

from selenium import webdriver
import csv

from selenium.webdriver.common.by import By

csv_file = 'TestData1.csv'

test_data = []
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        test_data.append(row)
print(test_data)

for data in test_data:
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    time.sleep(5)
    driver.find_element(By.ID, "user-name").send_keys(data['Username'])
    driver.find_element(By.ID, "password").send_keys(data['Password'])
    driver.find_element(By.ID, "login-button").click()
    time.sleep(5)
    driver.quit()


