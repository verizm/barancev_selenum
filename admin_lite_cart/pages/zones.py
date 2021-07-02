from selenium.webdriver.common.by import By
from admin_lite_cart.base_page import BasePage


class Zones(BasePage):
    _zones_names = (By.CSS_SELECTOR, "input[name$='[name]']")

    def get_all_zones_name(self):
        list_of_names = []
        elements = self.find_elements_presence(self._zones_names)
        for element in elements:
            if element.get_attribute("value") != "":
                list_of_names.append(element.get_attribute("value"))
        return list_of_names





