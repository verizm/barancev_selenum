import pytest
from admin_lite_cart.pages.main_litecart import MainLitecart


class TestMainLitecart:
    @pytest.fixture(autouse=True)
    def init_page(self, create_driver):
        self.main_page = MainLitecart(create_driver)

    def test_sticker_count(self):
        assert self.main_page.check_all_stickers()