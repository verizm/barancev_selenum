import pytest
from admin_lite_cart.pages.store_litecart import StoreLitecart
from admin_lite_cart.pages.yaml_parser import LoaderDataCss


class TestMainLitecart:
    @pytest.fixture(autouse=True)
    def init_page(self, create_store):
        self.data = LoaderDataCss()
        self.main_page = StoreLitecart(create_store.get_driver())
        self.store_litecart = StoreLitecart(create_store.get_driver())

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


