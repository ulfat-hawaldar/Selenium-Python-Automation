import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://the-internet.herokuapp.com/javascript_alerts"
driver.get(url)
driver.maximize_window()
AlertButton = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']")
AlertButton.click()
alert1 = driver.switch_to.alert
alert_Text = alert1.text
print(alert_Text)
alert1.accept()
time.sleep(5)
message_element1 = driver.find_element(By.XPATH,"//p[@id='result']")
assert message_element1.text == 'You successfully clicked an alert'

AlertButton2 = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']")
AlertButton2.click()
alert2 = driver.switch_to.alert 
alert_Text2 = alert2.text
print(alert_Text2)
alert2.dismiss()
time.sleep(5)
message_element2 = driver.find_element(By.XPATH,"//p[@id='result']")
assert message_element2.text == 'You clicked: Cancel'

AlertButton3 = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']")
AlertButton2.click()
alert3 = driver.switch_to.alert
alert_Text3 = alert3.text
alert3.send_keys("Hello")
print(alert_Text3)
#alert3.send_keys("Hello")
alert3.accept()
time.sleep(5)
message_element2 = driver.find_element(By.XPATH,"//p[@id='result']")
assert message_element2.text == 'You entered: Hello'

