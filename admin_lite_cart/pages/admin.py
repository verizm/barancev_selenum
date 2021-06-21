import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from admin_lite_cart.conftest import BasePage


class AdminPage(BasePage):
    icon = (By.CSS_SELECTOR, ".fa-home")
    h1 = (By.CSS_SELECTOR, "h1")
    name = (By.CSS_SELECTOR, ".name")

    def check_home_icon_is_visible(self):
        element = self.find(self.icon)
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of(element)
        )

    def go_to_next_page(self):
        elements = self.find_elements(self.name)
        


