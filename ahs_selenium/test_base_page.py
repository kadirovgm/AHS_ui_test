import pytest
import time
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.pool_page import PoolPage
from pages.clients_projects import ClientsProjectsPage
from pages.positions_page import PositionsPage

LINK_LOGIN_PAGE = "http://192.168.52.122/login"


class TestBasePageActions:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = LINK_LOGIN_PAGE
        self.page = LoginPage(browser, link)
        self.page.open()
        time.sleep(0.5)
        self.page.login_new_user()

    def test_user_can_go_to_positions(self, browser):
        page_positions = PositionsPage(browser, browser.current_url)
        page_positions.go_to_positions_page()
        page_positions.should_be_positions_page_text()

    def test_user_can_go_to_pool(self, browser):
        page_pool = PoolPage(browser, browser.current_url)
        page_pool.go_to_pool_page()
        page_pool.should_be_pool_page_text()

    def test_user_can_go_to_clients_projects(self, browser):
        page_clients_projects = ClientsProjectsPage(browser, browser.current_url)
        page_clients_projects.go_to_clients_projects_page()
        page_clients_projects.should_be_clients_projects_page_text()

    def test_user_can_go_to_reports(self, browser):
        ...

    def test_user_can_go_to_help_center(self, browser):
        ...


