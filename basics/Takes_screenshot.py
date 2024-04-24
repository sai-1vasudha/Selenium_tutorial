import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(executable_path="C:\\Users\\Harshavardhan\\OneDrive\\Desktop\\Selenium_driver-files\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.saucedemo.com/v1/index.html")
driver.maximize_window()
driver.implicitly_wait(30)
driver.save_screenshot("C:\\Users\\Harshavardhan\\OneDrive\\Desktop\\Screenshot\\screenshot1.png")
time.sleep(5)
driver.close()