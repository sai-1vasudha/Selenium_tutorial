import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from DataDriven_framework import XLReader

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(30)
path = "C:\\Users\\Harshavardhan\\OneDrive\\Desktop\\DDF1.xlsx"

rows = XLReader.total_rows(path, "Sheet3")  # 11
cols = XLReader.total_columns(path, "Sheet3")

for r in range(2, rows + 1):
    user = XLReader.read_data(path, "Sheet3", r, 1)
    pwd = XLReader.read_data(path, "Sheet3", r, 2)

    driver.find_element(By.NAME, 'username').send_keys(user)
    time.sleep(3)
    driver.find_element(By.NAME, "password").send_keys(pwd)
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    homepage_title = driver.title

    if homepage_title == "OrangeHRM":
        XLReader.write_data(path, "Sheet3", r, 3, "Pass")
        time.sleep(3)
        driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()

    else:
        XLReader.write_data(path, "Sheet3", r, 3, "Fail")

driver.close()
