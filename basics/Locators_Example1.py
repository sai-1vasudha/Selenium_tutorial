import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executable_path="C:\\Users\\Harshavardhan\\OneDrive\\Desktop\\Selenium_driver-files\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://www.fb.com")
driver.maximize_window()

time.sleep(5)
#using id locator
driver.find_element(By.ID,"email").send_keys("saivasudha@gmail.com")
#driver.find_element(By.NAME,"email").send_keys("Saivasudha@gmail.com")

time.sleep(5)
#using name locator
driver.find_element(By.NAME, "pass").send_keys("saivasu@123")
#driver.find_element(By.ID,"pass").send_keys('vasudha123')


time.sleep(5)
# using classname
actual_text = driver.find_element(By.CLASS_NAME,"_8eso").text
print(actual_text)

#link text
time.sleep(5)

actual_help_text = driver.find_element(By.LINK_TEXT,"Help").text
print(actual_help_text)
actual_forgot_password = driver.find_element(By.LINK_TEXT,"Forgotten password?").text
print("Link text = ", actual_forgot_password)

#partial_link text
actuaL_fp_text = driver.find_element(By.PARTIAL_LINK_TEXT,"word").text
print("Partial link text  = ", actuaL_fp_text)