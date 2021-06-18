import pytest
from admin_lite_cart.pages.store_litecart import StoreLitecart


class TestMainLitecart:
    @pytest.fixture(autouse=True)
    def init_page(self, create_store):
        self.main_page = StoreLitecart(create_store.get_driver())

    def test_sticker_count(self):
        assert self.main_page.check_all_stickers()
