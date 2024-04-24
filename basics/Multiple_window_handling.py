import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executable_path="C:\\Users\\Harshavardhan\\OneDrive\\Desktop\\Selenium_driver-files\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Create new account").click()
print("====Parent window====")
print(driver.title)
parent_window = driver.current_window_handle
driver.find_element(By.ID,"cookie-use-link").click()

child_window = driver.window_handles

for i in child_window:

    if parent_window != i:
        driver.switch_to.window(i)
        child_text = driver.find_element(By.XPATH,"//span[contains(text(),'this policy cover?')]").text
        print("===Child window====")
        print(driver.title)
        print(child_text)
        driver.close()

driver.switch_to.window(parent_window)
print("====Parent window ====")
print(driver.title)
driver.find_element(By.NAME,"firstname").send_keys('Saivasudha')
time.sleep(10)