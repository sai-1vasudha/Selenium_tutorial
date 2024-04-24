from selenium import webdriver


def test_Google():

   driver =  webdriver.Chrome()

   driver.get("http://www.google.com")

   driver.implicitly_wait(30)

   driver.maximize_window()

   actual_title = driver.title

   assert actual_title  == "Google"


   actual_url = driver.current_url

   assert actual_url == "https://www.google.com/"

   driver.close()


def test_Fb():

    driver = webdriver.Chrome()

    driver.get("Https://www.fb.com")

    driver.maximize_window()

    driver.implicitly_wait(30)

    actual_title = driver.title

    assert actual_title == "Facebook – log in or sign up"

    driver.close()

def test_rediff():

    driver = webdriver.Chrome()

    driver.get("http://www.rediff.com")

    driver.maximize_window()

    driver.implicitly_wait(30)

    actual_title = driver.title

    assert actual_title == "Rediff.com: News | Rediffmail | Stock Quotes | Shopping"

    driver.close()