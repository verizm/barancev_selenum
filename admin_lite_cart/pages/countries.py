from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from admin_lite_cart.base_page import BasePage


class Countries(BasePage):
    _country_td = (By.CSS_SELECTOR, ".row a:not([title])")
    _td_of_zones = (By.CSS_SELECTOR, ".row td:nth-of-type(6)")
    _edit_td = (By.CSS_SELECTOR, ".row td:nth-of-type(7)")

    def get_all_countries_text(self):
        countries = self.find_elements(self._country_td)
        countries_list = []
        for country in countries:
            countries_list.append(self.get_text(country))
        return countries_list

    def get_countries_names_with_geozones(self):
        zones = self.finds(self._td_of_zones)
        countries = self.finds(self._country_td)
        values_dict = dict(zip(zones, countries))
        countries_list = []
        for key, value in values_dict.items():
            if int(self.get_text(key)) > 0:
                countries_list.append(self.get_text(value))
        return countries_list

    def click_country_by_name(self, name):
            countries = self.find_elements_presence(self._country_td)
            element = self.get_element_by_text(countries, name)
            self.click(element)

    def go_back(self):
        self.navigate_back()

    # def click_country_by_names(self):
    #     countries = self.find_elements(self._country_td)
    #     element = self.get_element_by_text(countries, name)
    #     return self.click(element)


















