from selenium.webdriver.common.by import By
from admin_lite_cart.conftest import BasePage


class StoreLitecart(BasePage):
    _campaigns_item_links = (By.CSS_SELECTOR, "[id='box-campaigns'] .link .name")
    _campagins_item_text = (By.CSS_SELECTOR, "#box-campaigns .name")
    _campaigns_price = (By.CSS_SELECTOR, "#box-campaigns .campaign-price")
    _regular_price = (By.CSS_SELECTOR, "#box-campaigns .regular-price")
    _item_campaign_price = (By.CSS_SELECTOR, ".campaign-price")
    _item_regular_price = (By.CSS_SELECTOR, ".regular-price")
    _name_of_user = (By.CSS_SELECTOR, "[name='email']")
    _password_of_user = (By.CSS_SELECTOR, "[name='password']")
    _login_button = (By.CSS_SELECTOR, "[name='login']")
    _h1 = (By.CSS_SELECTOR, "h1")

    def check_all_stickers(self):
        element_duck = self.driver.find_elements(By.CSS_SELECTOR, ".product")
        for element in element_duck:
            sticker = element.find_elements(By.CSS_SELECTOR, ".sticker")
            if len(sticker) != 1:
                return False
        return bool(element_duck)

    def get_duck_name(self):
        return self.get_text(self.find_element(self._campaigns_item_links))

    def _get_css_from_element(self, locator: object):
        list_of_css = ["color", "font-weight"]
        value_css = {}
        element = self.find_element(locator)
        for css in list_of_css:
            value_css[css] = element.value_of_css_property(css)
        value_css["text"] = self.get_text(element)
        value_css["size"] = element.size
        return value_css

    def get_campaings_css(self):
        return self._get_css_from_element(self._campaigns_price)

    def get_regular_css(self):
        return self._get_css_from_element(self._regular_price)

    # page of item

    def get_h1_text(self):
        return self.get_text(self.find_element(self._h1))

    def get_item_regular_price(self):
        element = self.find_element(self._item_regular_price)
        return self.get_text(element)

    def get_item_camping_price(self):
        element = self.find_element(self._item_campaign_price)
        return self.get_text(element)

    def get_color_regular_item(self):
        element = self.find_element(self._item_campaign_price)
        return element.value_of_css_property("color")

    def get_color_campaing_item(self):
        element = self.find_element(self._item_regular_price)
        return element.value_of_css_property("color")

    def get_font_regular_price_item(self):
        element = self.find_element(self._item_regular_price)
        return element.value_of_css_property("text-decoration-line")

    def get_font_camping_price_item(self):
        element = self.find_element(self._item_campaign_price)
        return element.value_of_css_property("font-weight")

    def click_on_campaings_item(self):
        return self.click(self.find(self._campaigns_item_links))

    def login_to_store(self, password: str, email: str):
        self.send(self.find_element(self._password_of_user), password)
        self.send(self.find_element(self._name_of_user), email)
        self.click(self.find_element(self._login_button))
