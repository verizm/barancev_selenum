import pytest
from admin_lite_cart.pages.admin import AdminPage
from admin_lite_cart.pages.countries import Countries


class TestIndexAdminPage:
    @pytest.fixture(autouse=True)
    def init_page(self, create_admin):
        self.index_page = AdminPage(create_admin.get_driver())
        self.countries = Countries(create_admin.get_driver())

    def test_login_to_admin(self):
        assert self.index_page.check_home_icon_is_visible()

    def test_go_to_all_page(self):
        self.index_page.go_to_next_page()

    def test_countries_in_alfabet(self):
        self.countries.navigate_to("http://localhost/litecart/admin/?app=countries&doc=countries")
        list_of_countries = self.countries.get_all_countries()
        assert list_of_countries == sorted(list_of_countries)