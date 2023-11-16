from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

driver.get('https://www.saucedemo.com')

user_name_field = driver.find_element('xpath', '//*[@id="user-name"]')
user_name_field.click()
# time.sleep(2)
user_name_field.send_keys('standard_user')
# time.sleep(2)
password = driver.find_element('xpath', '//*[@id="password"]')
user_name_field.click()
password.send_keys('secret_sauce')
enter_button = driver.find_element('xpath', '//*[@id="login-button"]')
enter_button.send_keys(Keys.ENTER)

time.sleep(2)

item1 = driver.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-backpack"]')
item1.click()
time.sleep(2)
item2 = driver.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-bike-light"]')
item2.click()
time.sleep(2)
item3 = driver.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
item3.click()

po = driver.find_element('xpath', '//*[@id="shopping_cart_container"]/a')
po.click()

check_out = driver.find_element('xpath', '//*[@id="checkout"]')
check_out.click()

check_out_user = driver.find_element('xpath', '//*[@id="first-name"]')
check_out_user.send_keys('Special')
check_out_last_name = driver.find_element('xpath', '//*[@id="last-name"]')
check_out_last_name.send_keys('Order')
postal_code = driver.find_element('xpath', '//*[@id="postal-code"]')
postal_code.send_keys('12911')
continue_btn = driver.find_element('xpath', '//*[@id="continue"]')
continue_btn.click()


screen = driver.find_element('css selector', '#checkout_summary_container > div > div.summary_info')
screen.screenshot('order.png')

finish_button = driver.find_element('xpath', '//*[@id="finish"]')
finish_button.click()


burger_menu = driver.find_element('xpath', '//*[@id="react-burger-menu-btn"]')
burger_menu.click()
time.sleep(2)

log_out = driver.find_element('xpath', '//*[@id="logout_sidebar_link"]')
log_out.click()


time.sleep(5)

