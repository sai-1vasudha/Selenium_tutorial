import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service

s = Service(executable_path='C:\\Users\\Harshavardhan\\OneDrive\\Desktop\\Selenium_driver-files\\edgedriver_win64\\msedgedriver.exe')
driver = webdriver.Edge(service=s)
driver.get("http://www.flipkart.com")
driver.maximize_window()
time.sleep(5)
driver.minimize_window()
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.close()