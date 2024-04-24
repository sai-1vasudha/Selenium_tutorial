from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.rediff.com")
driver.maximize_window()