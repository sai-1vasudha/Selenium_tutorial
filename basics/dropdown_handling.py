import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service(executable_path='C:\\Users\\Harshavardhan\\OneDrive\\Desktop\\Selenium_driver-files\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('http://www.fb.com')
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.LINK_TEXT,"Create new account").click()
time.sleep(3)

month_dd = driver.find_element(By.ID,"month")

sel = Select(month_dd)

sel.select_by_visible_text("Jul") #

time.sleep(3)

sel.select_by_value("11")

time.sleep(3)

sel.select_by_index(0)

time.sleep(5)
