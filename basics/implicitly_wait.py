import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service(executable_path='C:\\Users\\Harshavardhan\\OneDrive\\Desktop\\Selenium_driver-files\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('http://www.fb.com')
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.LINK_TEXT,"Create new account").click()
driver.find_element(By.NAME,"firstname").send_keys('Sai')
driver.find_element(By.NAME,"lastname").send_keys('Vasudha')
driver.find_element(By.NAME,"reg_email__").send_keys("saivasudha@gmail.com")
driver.find_element(By.NAME,"reg_email_confirmation__").send_keys("saivasudha@gmail.com")
driver.find_element(By.NAME,"reg_passwd__").send_keys('sai@123')
time.sleep(5)