import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    driver = webdriver.Chrome()
    yield driver
    request.addfinalizer(driver.quit)


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


@pytest.fixture(scope="session", autouse=True)
def login_to_administrative(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    username_field = driver.find_element(By.CSS_SELECTOR, "[name='username']")
    username_field.send_keys("admin")
    password = driver.find_element(By.CSS_SELECTOR, "[name='password']")
    password.send_keys("admin")
    driver.find_element(By.CSS_SELECTOR, "[name='login']").click()
    yield
    driver.find_element(By.CSS_SELECTOR, ".fa-sign-out").click()
