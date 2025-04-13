from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.selenium.dev/')
driver.maximize_window()
#driver.find_element()
title = driver.title
assert "Selenium" in title

#driver.findElement(By.id("APjFqb"))