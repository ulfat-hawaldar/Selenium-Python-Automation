import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")

iframe = driver.find_element(By.ID,"mce_0_ifr")
driver.switch_to.frame(iframe)
Text_Editor = driver.find_element(By.ID,"tinymce")
Text_Editor.clear()
Text_Editor.send_keys("Hello Selenium")
time.sleep(10)

driver.switch_to.default_content()
selenium_link = driver.find_element(By.LINK_TEXT,"Elemental Selenium")
selenium_link.click()
