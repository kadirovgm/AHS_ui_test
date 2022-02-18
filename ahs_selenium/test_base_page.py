import pytest
from page_objects.pool_page import PoolPage
from page_objects.clients_projects_page import ClientsProjectsPage
from page_objects.positions_page import PositionsPage
from page_objects.reports_page import ReportsPage
from page_objects.help_center_page import HelpCenterPage
from settings import Setup
from settings import Urls


"""Test User can go to main pages"""
@pytest.mark.e2e_4
class TestBasePageActions:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        Setup.setup_help(browser, browser)

    """Correct Position"""
    def test_user_can_go_to_positions(self, browser):
        positions = PositionsPage(browser, browser.current_url)
        positions.go_to_positions_page()
        positions.should_be_positions_page_text()
        positions.is_correct_url(Urls.POSITIONS_ACTIVE)

    """Correct Pool"""
    def test_user_can_go_to_pool(self, browser):
        pool = PoolPage(browser, browser.current_url)
        pool.go_to_pool_page()
        pool.should_be_pool_page_text()
        pool.is_correct_url(Urls.POOL_INTERNAL)

    """Correct Clients&Projects"""
    def test_user_can_go_to_clients_projects(self, browser):
        clients_projects = ClientsProjectsPage(browser, browser.current_url)
        clients_projects.go_to_clients_projects_page()
        clients_projects.should_be_clients_projects_page_text()
        clients_projects.is_correct_url(Urls.PROJECTS_ACTIVE)

    """Correct Reports"""
    def test_user_can_go_to_reports(self, browser):
        reports = ReportsPage(browser, browser.current_url)
        reports.go_to_reports_page()
        reports.should_be_reports_page_text()
        reports.is_correct_url(Urls.REPORTS)

    """Correct Help center"""
    def test_user_can_go_to_help_center(self, browser):
        help_center = HelpCenterPage(browser, browser.current_url)
        help_center.go_to_help_page()
        help_center.should_be_help_center_page_text()
        help_center.is_correct_url(Urls.HELP_CENTER)



