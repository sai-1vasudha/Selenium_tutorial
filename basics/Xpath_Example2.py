from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(
    executable_path="C:\\Users\\Harshavardhan\\OneDrive\\Desktop\\Selenium_driver-files\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://www.fb.com")
driver.maximize_window()
#text()
fp1 = driver.find_element(By.XPATH,"//a[text()='Forgotten password?']").text

print("text function  =", fp1)

#contains text()

fp2 = driver.find_element(By.XPATH,"//a[contains(text(),'wo')]").text

print("contains text function = ", fp2)

#starts-with text()
fp3 = driver.find_element(By.XPATH,"//a[starts-with(text(),'Fo')]").text

print("stars with text function = ", fp3)

# contains --> attribute

cna1 = driver.find_element(By.XPATH,"//a[contains(@id,'_0_0_')]").text

print("Contains attribute = ", cna1)

#starts-with --> attribute

cna2 = driver.find_element(By.XPATH,"//a[starts-with(@id,'u')]").text

print("Starts-with attribute = ", cna2)