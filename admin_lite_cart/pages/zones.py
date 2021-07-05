from selenium.webdriver.common.by import By
from admin_lite_cart.base_page import BasePage


class Zones(BasePage):
    _zones_names = (By.CSS_SELECTOR, "input[name$='[name]']")
    _zones_in_select = (By.CSS_SELECTOR, 'tbody [selected="selected"]:not([data-phone-code="1"])')
    _country_td = (By.CSS_SELECTOR, ".row a:not([title])")

    def get_all_zones_name(self):
        list_of_names = []
        elements = self.find_elements_presence(self._zones_names)
        for element in elements:
            if element.get_attribute("value") != "":
                list_of_names.append(element.get_attribute("value"))
        return list_of_names

    def get_zones_in_select(self):
        zones = self.find_elements_presence(self._zones_in_select)
        list_of_zones = []
        for zone in zones:
            list_of_zones.append(self.get_text(zone))
        return list_of_zones

    def get_countries_name(self):
        elements = self.finds(self._country_td)
        res = [self.get_text(element) for element in elements]
        return res






