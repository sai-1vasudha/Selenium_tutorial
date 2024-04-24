import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ser = Service(executable_path='C:\\Users\\Harshavardhan\\OneDrive\\Desktop\\Selenium_driver-files\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=ser)
driver.get('http://www.google.com')
driver.maximize_window()
time.sleep(5)
driver.get('http://www.fb.com')
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()
time.sleep(5)
driver.close()