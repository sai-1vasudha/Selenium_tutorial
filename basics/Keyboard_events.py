import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
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
driver.find_element(By.NAME,"firstname").send_keys("Saivasudha")
act = ActionChains(driver)
act.send_keys(Keys.TAB).send_keys("Vasudha").send_keys(Keys.TAB).send_keys("Saivasudha@gmail.com").send_keys(Keys.TAB).send_keys("saivasudha@gmail.com").send_keys(Keys.TAB).send_keys("vasudha").perform()
time.sleep(5)