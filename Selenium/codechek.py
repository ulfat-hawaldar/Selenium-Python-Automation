from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (for Chrome in this example)
driver = webdriver.Chrome()

# Navigate to a URL
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# Wait for the specific WebElement to be visible
element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@type='checkbox"))
)

# Scroll the page until the element is in view
driver.execute_script("arguments[0].scrollIntoView(true);", element)

# Optionally, interact with the element after scrolling
element.click()  # Example action

# Close the browser when done
driver.quit()