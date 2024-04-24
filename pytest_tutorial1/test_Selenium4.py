import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope='function')
def setup():
    global driver
    driver = webdriver.Chrome()
    driver.get("http://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield
    driver.close()


def test_verifyTitle(setup):
    actual_title = driver.title

    assert actual_title == "Facebook – log in or sign up"


def test_verifyUrl(setup):
    actual_url = driver.current_url

    assert actual_url == "https://www.facebook.com/"


def test_verifyHomepagetext(setup):
    hm_text = driver.find_element(By.CLASS_NAME, "_8eso").text

    assert hm_text == "Facebook helps you connect and share with the people in your life."


def test_verify_forgotten_Password(setup):
    forgot_text = driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot").text

    assert forgot_text == "Forgotten password?"


def test_verify_create_new_account(setup):
    cna_text = driver.find_element(By.LINK_TEXT, "Create new account").text

    assert cna_text == "Create new account"
