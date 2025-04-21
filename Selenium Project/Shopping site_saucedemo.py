import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Selenium.Login import title_element

#Open URL through FireFox
driver = webdriver.Firefox()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()

# Login to the Demo site
driver.find_element(By.ID,'user-name').send_keys('standard_user')
driver.find_element(By.ID,'password').send_keys('secret_sauce')
driver.find_element(By.ID,'login-button').click()

# Verify and print the title
title_element = driver.title
assert title_element.title()
print('Login is successfully to:',title_element)

# Scroll Below
driver.execute_script('window.scrollTo(0,700)')

# Adding First Product to the cart
Product = driver.find_element(By.XPATH,"//div[normalize-space()='Test.allTheThings() T-Shirt (Red)']")
assert Product.is_displayed(), "Test.allTheThings() T-Shirt (Red)"
print("Adding product to cart:", Product.text )
driver.find_element(By.ID,'add-to-cart-test.allthethings()-t-shirt-(red)').click()
time.sleep(2)

# verify the cart
driver.execute_script("window.scrollTo(0, 0);")
driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()

Cart_Product = driver.find_element(By.XPATH,"//div[@class='inventory_item_name']")
assert  Cart_Product.is_displayed(), "Test.allTheThings() T-Shirt (Red)"
print(f"Product is added to the cart: ", Cart_Product.text)
driver.find_element(By.ID,"react-burger-menu-btn").click()
time.sleep(3)

# Navigate to the home page by clicking Main Menu
driver.find_element(By.XPATH,"//a[@id='inventory_sidebar_link']").click()
time.sleep(3)

# Apply Filter - High to low
Filter = driver.find_element(By.CLASS_NAME, "product_sort_container")
Filter.click()
select = Select(Filter)
select.select_by_visible_text("Price (high to low)")
time.sleep(2)

# Adding Second item to the cart and print the name of the product
Second_Product = driver.find_element(By.XPATH,"//div[normalize-space()='Sauce Labs Fleece Jacket']")
assert Second_Product.is_displayed(), "Sauce Labs Fleece Jacket"
print("Adding second product in cart", Second_Product.text)
driver.find_element(By.NAME,"add-to-cart-sauce-labs-fleece-jacket").click()

cart_items = driver.find_element(By.CLASS_NAME,"shopping_cart_link")
cart_items.click()
driver.find_element(By.XPATH,"//button[@id='remove-test.allthethings()-t-shirt-(red)']").click()

#CheckOut
driver.find_element(By.XPATH,"//button[@id='checkout']").click()
driver.find_element(By.ID,'first-name').send_keys('Shinchan')
driver.find_element(By.ID,'last-name').send_keys('Nohara')
driver.find_element(By.ID,"postal-code").send_keys("Kasukabe 592323")

driver.execute_script("window.scrollTo(0, 700);")
driver.find_element(By.ID,"continue").click()
driver.execute_script("window.scrollTo(0, 700);")
driver.find_element(By.ID,'finish').click()

message = driver.find_element(By.CSS_SELECTOR, ".complete-header")
# Verify it's visible
assert message.is_displayed(), "Message is not visible"

# Optional: Verify the text content of the message
expected_text = "Thank you for your order!"
actual_text = message.text
assert expected_text in actual_text, f"Expected message: '{expected_text}', but got: '{actual_text}'"

print(" Message is visible and correct.")