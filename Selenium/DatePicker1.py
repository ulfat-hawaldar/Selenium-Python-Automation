from datetime import datetime, timedelta
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://www.globalsqa.com/demo-site/datepicker"
driver.get(url)
driver.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//a[@class='close_img']").click()
frameLo = driver.find_element(By.XPATH,"//iframe[@class='demo-frame lazyloaded']")
driver.switch_to.frame(frameLo)
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"#datepicker").click()
current_date = datetime.now()
next_date = current_date + timedelta(days = 2)
formatted_date = next_date.strftime("%m/%d/%y")
driver.find_element(By.CSS_SELECTOR,"#datepicker").send_keys(formatted_date + Keys.TAB)
time.sleep(5)