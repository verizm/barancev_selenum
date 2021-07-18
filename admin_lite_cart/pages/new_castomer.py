from selenium.webdriver.common.by import By
from admin_lite_cart.conftest import BasePage
from selenium.webdriver.common.keys import Keys
from admin_lite_cart.data.data_faker import DataFaker



class NewCastomer(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.faker = DataFaker()

    _new_castomer_link = (By.CSS_SELECTOR, "[name='login_form'] a")
    _first_name = (By.CSS_SELECTOR, "[name='firstname']")
    _last_name = (By.CSS_SELECTOR, "[name='lastname']")
    _adress1_field = (By.CSS_SELECTOR, "[name='address1']")
    _post_code = (By.CSS_SELECTOR, "[name='postcode']")
    _city = (By.CSS_SELECTOR, "[name='city']")
    _email = (By.CSS_SELECTOR, "[name='email']")
    _phone = (By.CSS_SELECTOR, "[name='phone']")
    _desired_password = (By.CSS_SELECTOR, "[name='password']")
    _confirm_password = (By.CSS_SELECTOR, "[name='confirmed_password']")
    _create_account_button = (By.CSS_SELECTOR, "[name='create_account']")
    _country = (By.CSS_SELECTOR, ".select2-selection__arrow")
    _input_for_country = (By.CSS_SELECTOR, "[type='search']")
    _logout_link = (By.CSS_SELECTOR, ".content a[href$='logout']")

    def click_new_castomer_link(self):
        return self.click(self.find_element(self._new_castomer_link))

    def set_first_name(self):
        name = self.faker.get_first_name()
        self.send(self.find(self._first_name), name)
        return name

    def set_last_name(self):
        last_name = self.faker.get_last_name()
        self.send(self.find(self._last_name), last_name)
        return last_name

    def set_address(self):
        address = self.faker.get_address()
        self.send(self.find(self._adress1_field), address)
        return address

    def set_post_code(self):
        post_code = self.faker.get_post_code()
        self.send(self.find(self._post_code), post_code)
        return post_code

    def set_email(self):
        email = self.faker.get_email()
        self.send(self.find(self._email), email)
        return email

    def set_city(self):
        city = self.faker.get_city()
        self.send(self.find(self._city), city)

    def set_password(self):
        password = self.faker.get_password()
        self.send(self.find(self._confirm_password), password)
        self.send(self.find(self._desired_password), password)
        return password

    def set_phone(self):
        phone = self.faker.get_phone()
        self.send(self.find(self._phone), phone)
        return phone

    def choose_country(self):
        element = self.find_element(self._country)
        self.click(element)
        element = self.find_element(self._input_for_country)
        element.send_keys("United States" + Keys.ENTER)

    def logout_from_store(self):
        return self.click(self.find_element(self._logout_link))

    def click_create_account(self):
        return self.click(self.find(self._create_account_button))


