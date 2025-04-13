import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://www.saucedemo.com/')
driver.find_element(By.ID,"user-name").send_keys('error_user')
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
title_element = driver.find_element(By.CSS_SELECTOR,".title").text == 'Products'

driver.find_element(By.CSS_SELECTOR,".shopping_cart_link").click()
time.sleep(3)
driver.back()  #webpage operations for refresh, forward,back
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()
time.sleep(3)
#driver.close()

#driver.set_window_size(786,1024)
#time.sleep(3)

resolutions = [(1014,786),(786,1024),(375,667),(414,896)]  # changing resolution

try:
    for width,height in resolutions:
        driver.set_window_size(width,height)
        time.sleep(4)

finally:
    driver.close()

