from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from admin_lite_cart.conftest import BasePage


class IndexPage(BasePage):

    def check_home_icon_is_visible(self):
        element = self.driver.find_element(By.CSS_SELECTOR, ".fa-home")
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of(element)
        )

    def go_to_page(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".name")
        for element in elements:
            element.click()
