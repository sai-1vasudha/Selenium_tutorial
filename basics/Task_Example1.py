import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(
    executable_path="C:\\Users\\Harshavardhan\\OneDrive\\Desktop\\Selenium_driver-files\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://www.fb.com")
driver.maximize_window()
'''
#Link text
driver.find_element(By.LINK_TEXT,"Create new account").click()

#partial link text

driver.find_element(By.PARTIAL_LINK_TEXT, "new acc").click()

#single attribute

driver.find_element(By.XPATH,"//a[@data-testid='open-registration-form-button']).click()

#text()
driver.find_element(By.XPATH,"//a[text()='Create new account']").click()

contains text()
driver.find_element(By.XPATH,"//a[contains(text(),'new')]").click()

'''

driver.find_element(By.XPATH,"//a[starts-with(text(),'Create n')]").click()

time.sleep(5)