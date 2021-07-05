import pytest
from admin_lite_cart.pages.admin import AdminPage
from admin_lite_cart.pages.countries import Countries
from admin_lite_cart.pages.zones import Zones


class TestIndexAdminPage:


    @pytest.fixture(autouse=True)
    def init_page(self, create_admin):
        self.index_page = AdminPage(create_admin.get_driver())
        self.countries = Countries(create_admin.get_driver())
        self.zones = Zones(create_admin.get_driver())

    def test_login_to_admin(self):
        assert self.index_page.check_home_icon_is_visible()

    def test_go_to_all_page(self):
        self.index_page.go_to_next_page()

    def test_countries_in_alfabet(self):
        self.countries.navigate_to("http://localhost/litecart/admin/?app=countries&doc=countries")
        list_of_countries = self.countries.get_all_countries_text()
        assert list_of_countries == sorted(list_of_countries)

    def test_geozones_with_countries_in_alfabet(self):
        self.countries.navigate_to("http://localhost/litecart/admin/?app=countries&doc=countries")
        countries = self.countries.get_countries_names_with_geozones()
        for country in countries:
            self.countries.click_country_by_name(country)
            list_zones = self.zones.get_all_zones_name()
            assert list_zones == sorted(list_zones)
            self.countries.go_back()

    def test_geozones_in_alfabet(self):
        self.countries.navigate_to("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
        countries = self.zones.get_countries_name()
        for country in countries:
            self.countries.click_country_by_name(country)
            list_zones = self.zones.get_zones_in_select()
            assert list_zones == sorted(list_zones)
            self.countries.go_back()









