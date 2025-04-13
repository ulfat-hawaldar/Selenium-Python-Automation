from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()
login_url = 'https://the-internet.herokuapp.com/dropdown'
driver.get(login_url)

dropdown_element = driver.find_element(By.ID, "dropdown")
select = Select(dropdown_element)
option_count = len(select.options)
expected_count = 3
if option_count == expected_count:
    print("Test case passed. Count is correct")
else:
    print('Test case failed. Count is incorrect')

#select.select_by_visible_text("Option 2")    # Select the value by visible text
#select.select_by_index(2)                      # Select the value by Index
#select.select_by_value('2')                      # Select option by using a value