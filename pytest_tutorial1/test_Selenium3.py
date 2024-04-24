from selenium import webdriver
from selenium.webdriver.common.by import By


def setup(module):
    global driver

    driver = webdriver.Chrome()
    driver.get("http://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)


def tearDown(module):
    driver.close()


def test_verifyTitle():
    actual_title = driver.title

    assert actual_title == "Facebook – log in or sign up"


def test_verifyUrl():
    actual_url = driver.current_url

    assert actual_url == "https://www.facebook.com/"


def test_verifyHomepagetext():
    hm_text = driver.find_element(By.CLASS_NAME,"_8eso").text

    assert hm_text == "Facebook helps you connect and share with the people in your life."

def test_verify_forgotten_Password():

    forgot_text = driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot").text

    assert forgot_text == "Forgotten password?"


def test_verify_create_new_account():

    cna_text = driver.find_element(By.LINK_TEXT,"Create new account").text

    assert cna_text == "Create new account"


