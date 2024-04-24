import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def chrome_browser(request):
    ch_driver = webdriver.Chrome()
    request.cls.driver = ch_driver
    yield
    ch_driver.close()


@pytest.fixture(scope='class')
def firefox_browser(request):
    ffd = webdriver.Firefox
    request.cls.driver = ffd
    yield
    ffd.close()


@pytest.fixture(scope='class')
def edge_browser(request):
    ed_driver = webdriver.Edge()
    request.cls.driver = ed_driver
    yield
    ed_driver.close()


@pytest.fixture(params=['chrome','edge'], scope='class')
def all_browser(request):

    if request.param == 'chrome':
       ldriver = webdriver.Chrome()

    if request.param == 'edge':
        ldriver =  webdriver.Edge()

    request.cls.driver=ldriver
    yield
    ldriver.close()