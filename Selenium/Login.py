from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
username = 'error_user'
password = 'secret_sauce'
login_url = 'https://www.saucedemo.com/'
driver.get(login_url)

username_field = driver.find_element(By.ID,"user-name")
password_field = driver.find_element(By.ID,"password")

username_field.send_keys(username)
password_field.send_keys(password)

login_button = driver.find_element(By.ID,"login-button")
assert not login_button.get_attribute("disables")
login_button.click()

title_element = driver.find_element(By.CSS_SELECTOR,".title")
assert title_element.text == 'Products'

