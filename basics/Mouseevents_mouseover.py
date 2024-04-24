import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Mouse Events:
# 1) Mouse over  2) Context click(Rightclick), 3) Doubleclick 4) drag and drop
# 2) Keyboard events


s = Service(executable_path="C:\\Users\\Harshavardhan\\OneDrive\\Desktop\\Selenium_driver-files\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://www.naukri.com")
driver.maximize_window()
driver.implicitly_wait(30)

jobs_menu = driver.find_element(By.XPATH,"//div[text()='Jobs']")
act = ActionChains(driver)
act.move_to_element(jobs_menu).perform()
time.sleep(5)

driver.find_element(By.XPATH,"//div[text()='IT jobs']").click()

#driver.back()

time.sleep(5)