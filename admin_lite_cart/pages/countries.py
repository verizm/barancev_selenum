from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from admin_lite_cart.conftest import BasePage


class Countries(BasePage):
    _country_td = (By.CSS_SELECTOR, ".row a:not([title])")

    def get_all_countries(self):
        countries = self.find_elements(self._country_td)
        countries_list = []
        for country in countries:
            countries_list.append(self.get_text(country))
        return countries_list



