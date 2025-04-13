from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/nested_frames")

#swtiching to top Frame
driver.switch_to.frame("frame-top")

#switching to Middle Frame
driver.switch_to.frame("frame-middle")

content = driver.find_element(By.ID,"content").text
print("Content in middle frame", content)

#switch to Default content
driver.switch_to.default_content()

#switch to Bottom Frame
driver.switch_to.frame("frame-bottom")
content_Bottom = driver.find_element(By.TAG_NAME,"body").text
print("Content in Bottom frame", content_Bottom)


