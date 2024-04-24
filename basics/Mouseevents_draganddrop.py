import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executable_path="C:\\Users\\Harshavardhan\\OneDrive\\Desktop\\Selenium_driver-files\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
driver.implicitly_wait(30)

iframe_ele = driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
driver.switch_to.frame(iframe_ele)

first_ele = driver.find_element(By.ID,"draggable")

second_ele = driver.find_element(By.ID,"droppable")

act = ActionChains(driver)

act.drag_and_drop(first_ele,second_ele).perform()

time.sleep(5)