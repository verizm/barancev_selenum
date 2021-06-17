import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--start_url", action="store", default="http://localhost/litecart/admin/login.php")


@pytest.fixture(scope="session", autouse=True)
def create_driver(request, pytestconfig):
    browser = pytestconfig.getoption("--browser")
    if browser == "safari":
        driver = webdriver.Safari()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError('Unsupported browser.  Please, select from [chrome, safari]')
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


# @pytest.fixture(scope="session", autouse=True)
# def login_to_administrative(create_driver):
#     create_driver.get("http://localhost/litecart/admin/login.php")
#     username_field = create_driver.find_element(By.CSS_SELECTOR, "[name='username']")
#     username_field.send_keys("admin")
#     password = create_driver.find_element(By.CSS_SELECTOR, "[name='password']")
#     password.send_keys("admin")
#     create_driver.find_element(By.CSS_SELECTOR, "[name='login']").click()
#     yield
#     create_driver.find_element(By.CSS_SELECTOR, ".fa-sign-out").click()


@pytest.fixture(scope="session")
def open_main_page_litecart(create_driver):
    create_driver.get("http://localhost/litecart/en/")
