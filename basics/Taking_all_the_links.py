import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(
    executable_path="C:\\Users\\Harshavardhan\\OneDrive\\Desktop\\Selenium_driver-files\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://www.rediff.com")
driver.maximize_window()
driver.implicitly_wait(30)

links_li =driver.find_elements(By.TAG_NAME,"a")
print(len(links_li))
for i in links_li:
    print(i.text , " --->" ,i.get_attribute('href'))

time.sleep(5)