import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service(executable_path='C:\\Users\\Harshavardhan\\OneDrive\\Desktop\\Selenium_driver-files\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://money.rediff.com/gainers/bse/daily/groupa?src=gain_lose')
driver.maximize_window()
driver.implicitly_wait(30)
#Single column
single_column = driver.find_element(By.XPATH,"//table[@class='dataTable']/tbody/tr[6]/td[1]/a").text
print(single_column)
#single row
Single_row = driver.find_element(By.XPATH,"//table[@class='dataTable']/tbody/tr[6]").text
print(Single_row)
#Entire table
tablelist = driver.find_elements(By.XPATH,"//table[@class='dataTable']/tbody/tr")
print(len(tablelist))

for i in tablelist:
    print(i.text)

time.sleep(5)