from selenium import webdriver


def test_fb():
    driver = webdriver.Chrome()

    driver.get("Https://www.fb.com")

    driver.maximize_window()

    driver.implicitly_wait(30)

    actual_title = driver.title

    print('First assertion start')

    assert actual_title == "Facebook – log in or sign "

    print('First assertion completed')

    actual_url = driver.current_url

    print('Second assertion start')

    assert actual_url == "https://www.facebook.com/"

    print('Second assertion completed')

    driver.close()
