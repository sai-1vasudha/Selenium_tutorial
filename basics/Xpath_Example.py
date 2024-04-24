import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(
    executable_path="C:\\Users\\Harshavardhan\\OneDrive\\Desktop\\Selenium_driver-files\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)

# single attribute
driver.find_element(By.XPATH, "//input[@placeholder='Email address or phone number']").send_keys("Pythonselenium")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@name='pass']").send_keys("java")
time.sleep(5)

#text() function

login_text = driver.find_element(By.XPATH,"//button[text()='Log in']").text

print(login_text)


fp_text = driver.find_element(By.XPATH,"//a[text()='Forgotten password?']").text

print(fp_text)

driver.find_element(By.LINK_TEXT, "Create new account").click()
time.sleep(5)

# multiple attribute
driver.find_element(By.XPATH, "//input[@class='_8esa' and @value='2']").click()

time.sleep(5)
