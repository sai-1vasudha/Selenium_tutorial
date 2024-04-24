import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


opt = Options()
opt.add_argument("--disable-notifications")
s = Service(executable_path='C:\\Users\\Harshavardhan\\OneDrive\\Desktop\\Selenium_driver-files\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=opt)
driver.get('http://www.justdial.com')
driver.maximize_window()
time.sleep(5)