from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from admin_lite_cart.conftest import BasePage


class MainLitecart(BasePage):

    def check_all_stickers(self):
        element_duck = self.driver.find_elements(By.CSS_SELECTOR, ".product")
        for element in element_duck:
            sticker = element.find_elements(By.CSS_SELECTOR, ".sticker")
            if len(sticker) != 1:
                return False
        return True

