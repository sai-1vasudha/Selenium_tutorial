import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#accept --> ok button
#dismiss --> cancel button
#text --> get the text in alert
#send_keys -->

s = Service(
 executable_path="C:\\Users\\Harshavardhan\\OneDrive\\Desktop\\Selenium_driver-files\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.NAME,"proceed").click()
time.sleep(5)
alt = driver.switch_to.alert
text1 = alt.text
print(text1)
alt.accept()   # ok button
#alt.dismiss() # cancel button
#alt.send_keys("Pythonselenium")
time.sleep(5)