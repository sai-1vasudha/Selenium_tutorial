from selenium import webdriver
from selenium.webdriver.firefox.service import Service

s = Service(executable_path="C:\\Users\\Harshavardhan\\OneDrive\\Desktop\\Selenium_driver-files\\geckodriver-v0.34.0"
                            "-win-aarch64\\geckodriver.exe", service_args = ['--marionette-port', '2828', '--connect-existing'] )
driver = webdriver.Firefox(service=s)