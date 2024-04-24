import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(
    executable_path="C:\\Users\\Harshavardhan\\OneDrive\\Desktop\\Selenium_driver-files\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.find_element(By.XPATH,"html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input").send_keys("Saivasudha")
driver.find_element(By.XPATH,"html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input").send_keys('sai@123')
fbt= driver.find_element(By.XPATH,"html/body/div[1]/div[1]/div[1]/div/div/div/div[1]/h2").text
print(fbt)
time.sleep(5)
