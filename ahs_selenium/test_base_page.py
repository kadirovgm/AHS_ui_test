import pytest
import time
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.pool_page import PoolPage
from pages.clients_projects import ClientsProjectsPage
from pages.positions_page import PositionsPage
from pages.reports_page import ReportsPage
from pages.help_center_page import HelpCenterPage

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
        page_reports = ReportsPage(browser, browser.current_url)
        page_reports.go_to_reports_page()
        page_reports.should_be_reports_page_text()

    def test_user_can_go_to_help_center(self, browser):
        page_help_center = HelpCenterPage(browser, browser.current_url)
        page_help_center.go_to_help_page()
        page_help_center.should_be_help_center_page_text()


