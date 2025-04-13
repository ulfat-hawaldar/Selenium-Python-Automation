import time

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
#driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
driver.get('https://practice.expandtesting.com/checkboxes')
driver.maximize_window()
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
A = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
time.sleep(3)
for checkbox in A:
    checkbox.click()
    time.sleep(5)

checked_count = 0
for checkbox in A:
    if checkbox.is_selected():
        checked_count +=1

        expected_checked_count = 1

        if checked_count == expected_checked_count:
            print('checkbox count verified')
        else:
            print('Checkbox count mismatch')

            time.sleep(5)
