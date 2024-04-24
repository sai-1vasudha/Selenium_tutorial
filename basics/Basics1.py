from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.rediff.com")
driver.maximize_window()
actual_title = driver.title
print(actual_title)
driver.close()
