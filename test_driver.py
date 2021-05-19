import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    print(driver.capabilities)
    request.addfinalizer(driver.quit)
    return driver


def test_example(driver):
    driver.get("https://www.software-testing.ru/")
    element = driver.find_element_by_css_selector(".inputbox-search")
    element.send_keys("webdriver")
    element.send_keys(Keys.ENTER)

