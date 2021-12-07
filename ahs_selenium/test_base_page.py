import pytest
import time
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.pool_page import PoolPage


LINK_LOGIN_PAGE = "http://192.168.52.122/login"


class TestBasePageActions:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = LINK_LOGIN_PAGE
        self.page = LoginPage(browser, link)
        self.page.open()
        time.sleep(2)
        self.page.login_new_user()

    def test_user_can_go_to_pool(self, browser):
        page_base = BasePage(browser, browser.current_url)
        page_base.go_to_pool_page()
        page_pool = PoolPage(browser, browser.current_url)
        page_pool.should_be_pool_page_text()

