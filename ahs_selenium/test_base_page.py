import pytest
import time

from pages.login_page import LoginPage
from pages.pool_page import PoolPage
from pages.clients_projects_page import ClientsProjectsPage
from pages.positions_page import PositionsPage
from pages.reports_page import ReportsPage
from pages.help_center_page import HelpCenterPage
from urls import Urls


@pytest.mark.e2e_3
class TestBasePageActions:
    @pytest.fixture(scope="class", autouse=True)  # scope=class because don't need to close browser everytime
    def setup(self, browser):
        link = Urls.LINK_LOGIN_PAGE
        page = LoginPage(browser, link)
        page.open()
        time.sleep(0.5)
        page.login_new_user(email="admin@admin.com", password="P@ssw0rd1")

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


