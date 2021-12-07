import pytest
import time
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.pool_page import PoolPage


LINK_LOGIN_PAGE = "http://192.168.52.122/login"


class TestPoolPageInternalFiltering:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = LINK_LOGIN_PAGE
        self.page = LoginPage(browser, link)
        self.page.open()
        time.sleep(0.5)
        self.page.login_new_user()

    def test_main_search(self, browser):
        ...


class TestPoolPageExternalFiltering:
    ...


class TestPoolPageBlacklistFiltering:
    ...


class TestAddPerson:
    ...
