import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_page import BasePage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--base_url", action="store", default="http://localhost/")


class LoginAdminPage(BasePage):
    username = (By.CSS_SELECTOR, "[name='username']")
    password = (By.CSS_SELECTOR, "[name='password']")
    login = (By.CSS_SELECTOR, "[name='login']")

    def __init__(self, driver, url):
        super().__init__(driver)
        self.url = url
        self.navigate_to(self.url + "litecart/admin/login.php")
        username_field = self.find_element(self.username)
        username_field.send_keys("admin")
        password = self.find_element(self.password)
        password.send_keys("admin")
        self.find_element(self.login).click()
        # self.driver.find_element(By.CSS_SELECTOR, ".fa-sign-out").click()

    def get_driver(self):
        return self.driver


class StorePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver)
        self.url = url

        self.navigate_to(self.url + "litecart/en/")

    def get_driver(self):
        return self.driver


@pytest.fixture(scope="session")
def create_factory(request, pytestconfig):
    url = pytestconfig.getoption("--base_url")

    class Factory:
        def __init__(self, driver):
            self.driver = driver

        def go_to_admin_page(self):
            return LoginAdminPage(driver, url)

        def go_to_store(self):
            return StorePage(driver, url)

    browser = pytestconfig.getoption("--browser")
    if browser == "safari":
        driver = webdriver.Safari()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError('Unsupported browser.  Please, select from [chrome, safari]')
    driver.maximize_window()
    request.addfinalizer(driver.quit)

    return Factory(driver)


@pytest.fixture(scope="session")
def create_admin(create_factory):
    admin = create_factory.go_to_admin_page()
    # todo add finalizert
    return admin


@pytest.fixture(scope="session")
def create_store(create_factory):
    store = create_factory.go_to_store()
    return store
