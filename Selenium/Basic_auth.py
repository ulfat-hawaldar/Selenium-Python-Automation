import time

from selenium import webdriver

driver = webdriver.Chrome()
Username = "admin"
Password = "admin"

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(5)
#https://username:password@domain/path