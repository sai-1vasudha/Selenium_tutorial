import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("all_browser")
class TestBase:
    pass


class Test_Chrome(TestBase):

    def test_verifyTitle(self):
        self.driver.get("http://www.fb.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        actual_title = self.driver.title
        assert actual_title == "Facebook – log in or sign up"


    def test_verifyUrl(self):
        actual_url = self.driver.current_url

        assert actual_url == "https://www.facebook.com/"

    def test_verifyHomepagetext(self):
        hm_text = self.driver.find_element(By.CLASS_NAME, "_8eso").text

        assert hm_text == "Facebook helps you connect and share with the people in your life."



    def test_verify_forgotten_password(self):
        forgot_text = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Forgott").text
        assert forgot_text == "Forgotten password?"

    def test_verify_create_new_account(self):
        cna_text = self.driver.find_element(By.LINK_TEXT, "Create new account").text
        assert cna_text == "Create new account"