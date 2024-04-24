from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service(executable_path='C:\\Users\\Harshavardhan\\OneDrive\\Desktop\\Selenium_driver-files\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=ser)
driver.get("http://www.fb.com")
driver.maximize_window()
actual_title = driver.title
print(actual_title)
actual_url = driver.current_url
print(actual_url)

ut = driver.find_element(By.ID, "email")
val = ut.get_attribute('data-testid')
print(val)
t=ut.get_attribute('placeholder')
print(t)
t1 = ut.value_of_css_property('height')
print(t1)

t2 = ut.value_of_css_property('width')
print(t2)
