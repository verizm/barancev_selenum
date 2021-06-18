import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    @classmethod
    def sleep(cls, second):
        return time.sleep(second)

    @classmethod
    def click(cls, web_element):
        web_element.click()

    @classmethod
    def send(cls, web_element, text):
        web_element.clear()
        web_element.send_keys(text)

    @classmethod
    def get_text(cls, element):
        return element.text

    def find_element(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator), ' : '.join(locator))
    #
    # def find_elements(self, locator, timeout=5):
    #     return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((locator)))
