import pytest
from admin_lite_cart.pages.store_litecart import StoreLitecart
from admin_lite_cart.pages.new_castomer import NewCastomer
from admin_lite_cart.pages.yaml_parser import LoaderDataCss


class TestMainLitecart:
    @pytest.fixture(autouse=True)
    def init_page(self, create_store):
        self.data = LoaderDataCss()
        self.main_page = StoreLitecart(create_store.get_driver())
        self.store_litecart = StoreLitecart(create_store.get_driver())
        self.new_castomer = NewCastomer(create_store.get_driver())

    def test_sticker_count(self):
        assert self.main_page.check_all_stickers()

    def test_campaings_items(self):
        expected_values = self.data.load_css()
        regular = self.store_litecart.get_regular_css()
        campaings = self.store_litecart.get_campaings_css()
        duck_name = self.store_litecart.get_duck_name()
        assert expected_values["Campaing"] == campaings
        assert expected_values["Regular"] == regular
        self.store_litecart.click_on_campaings_item()
        assert self.store_litecart.get_h1_text() == duck_name

    def test_create_new_castomer(self):
        self.new_castomer.click_new_castomer_link()
        self.new_castomer.sleep(2)
        self.new_castomer.set_first_name()
        self.new_castomer.set_last_name()
        self.new_castomer.set_address()
        self.new_castomer.set_post_code()
        self.new_castomer.choose_country()
        password = self.new_castomer.set_password()
        self.new_castomer.set_phone()
        self.new_castomer.set_city()
        email = self.new_castomer.set_email()
        self.new_castomer.click_create_account()
        self.new_castomer.logout_from_store()
        self.store_litecart.login_to_store(password, email)
