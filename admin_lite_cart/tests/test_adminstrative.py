import pytest
from admin_lite_cart.pages.admin import IndexPage


class TestIndexAdminPage:
    @pytest.fixture(autouse=True)
    def init_page(self, create_admin):
        self.index_page = IndexPage(create_admin.get_driver())

    def test_login_to_admin(self):
        assert self.index_page.check_home_icon_is_visible()

    def test_go_to_all_page(self):
        self.index_page.go_to_page()
