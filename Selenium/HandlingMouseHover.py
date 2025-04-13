import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Datepicker.html")
driver.maximize_window()
action = ActionChains(driver)
Hove_element = driver.find_element(By.XPATH,"//a[normalize-space()='SwitchTo']")
action.move_to_element(Hove_element).perform()
time.sleep(5)
driver.find_element(By.XPATH,"//a[normalize-space()='Frames']").click()


