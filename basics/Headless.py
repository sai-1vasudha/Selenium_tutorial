import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

opt = Options()
opt.add_argument("--headless")
s = Service(executable_path='C:\\Users\\Harshavardhan\\OneDrive\\Desktop\\Selenium_driver-files\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=opt)
driver.get('http://www.fb.com')
driver.maximize_window()
print(driver.title)
actual_url = driver.current_url
print(actual_url)
time.sleep(5)
driver.close()
