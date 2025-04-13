from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.selenium.dev/')
driver.switch_to.new_window()
driver.get('https://playwright.dev/')
number_of_tabs = len(driver.window_handles)
print(f" Tab counts = {number_of_tabs}")
tabs_value = driver.window_handles
print(f" Tab Values = {tabs_value}")
Current_Tab = driver.current_window_handle
print(f" Current Tab = {Current_Tab}")
driver.find_element(By.CSS_SELECTOR,'.getStarted_Sjon').click()
First_tab = driver.window_handles[0]
if Current_Tab!= First_tab:
    driver.switch_to.window(First_tab)
driver.find_element(By.XPATH,"//span[normalize-space()='Downloads']").click()



