import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service(executable_path='C:\\Users\\Harshavardhan\\OneDrive\\Desktop\\Selenium_driver-files\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://register.rediff.com/register/register.php?FormName=user_details")
driver.maximize_window()
driver.implicitly_wait(30)
country_dd = driver.find_element(By.ID,"country")

sel = Select(country_dd)

dd = sel.options

print(len(dd))

for country in dd:
    print(country.text)

time.sleep(5)