import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope='class')
def chrome_browser(request):
    ch_driver = webdriver.Chrome()
    request.cls.driver = ch_driver
    yield
    ch_driver.close()
@pytest.fixture(scope='class')
def firefox_browser(request):
     ffd=webdriver.Firefox
     request.cls.driver=ffd
     yield
     ffd.close()

@pytest.fixture(scope='class')
def edge_browser(request):

    ed_driver = webdriver.Edge()
    request.cls.driver = ed_driver
    yield
    ed_driver.close()

@pytest.mark.usefixtures("edge_browser")
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
