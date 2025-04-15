from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID,"user-name").send_keys("error_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()

driver.find_element(By.ID,"react-burger-menu-btn").click()

driver.find_element(By.XPATH,"//a[@id='logout_sidebar_link']").click()

driver.quit()
