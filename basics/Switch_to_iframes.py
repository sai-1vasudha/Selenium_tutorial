import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executable_path="C:\\Users\\Harshavardhan\\OneDrive\\Desktop\\Selenium_driver-files\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('http://www.rediff.com')
driver.maximize_window()
driver.implicitly_wait(30)
win_text1 = driver.find_element(By.CLASS_NAME,"mailicon").text
print(win_text1)

#driver.switch_to.frame("moneyiframe") # id or name  //webpage to iframe

#driver.switch_to.frame(0)  # index

fr1 = driver.find_element(By.XPATH,"//iframe[@class='moneyiframe']") # webelement

driver.switch_to.frame(fr1)

f1 = driver.find_element(By.XPATH,"//span[text()='BSE']").text

print(f1)

driver.switch_to.default_content()  #

win_text2 = driver.find_element(By.PARTIAL_LINK_TEXT,"Money").text
print(win_text2)