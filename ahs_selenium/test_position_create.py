import pytest
import time
from pages.create_position_modal_page import CreateClientPositionModal
from pages.positions_page import PositionsPage
from settings import Setup, Urls


@pytest.mark.e2e_11
class TestClientProjectPositionCorrectness:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        Setup.setup_help(browser, browser)
        position = PositionsPage(browser, Urls.POSITIONS_ACTIVE)
        position.add_client_project_position_button_click()

    """Position detail tab checking"""
    def test_correct_elements_pos_details(self, browser):
        modal = CreateClientPositionModal(browser, browser.current_url)
        modal.go_to_pos_details_tab()
        modal.should_be_correct_client_position_modal_elements_pos_details()

    """Assigns tab checking"""
    def test_correct_elements_assigns(self, browser):
        modal = CreateClientPositionModal(browser, browser.current_url)
        modal.go_to_assigns_tab()
        modal.should_be_correct_client_position_modal_elements_assigns()

    """Requests tab checking"""
    def test_correct_elements_requests(self, browser):
        modal = CreateClientPositionModal(browser, browser.current_url)
        modal.go_to_requests_tab()
        modal.should_be_correct_client_position_modal_elements_requests()


@pytest.mark.e2e_12
class TestClientProjectPositionCreate:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        Setup.setup_help(browser, browser)
        position = PositionsPage(browser, Urls.POSITIONS_ACTIVE)
        position.add_client_project_position_button_click()

    """Creation"""
    def test_create_client_project_position(self, browser):
        position_create_modal = CreateClientPositionModal(browser, browser.current_url)
        result = position_create_modal.add_new_client_project_position(loading_time=1)
        active_tab = PositionsPage(browser, browser.current_url)
        active_tab.go_to_active_tab()
        active_tab.search_for_position(result)
        active_tab.checking_status_of_position("Open")


@pytest.mark.skip
class TestInternalProjectPosition:
    ...


@pytest.mark.skip
class TestBenchPosition:
    ...


@pytest.mark.skip
class TestPreOfferPosition:
    ...


@pytest.mark.skip
class TestTraineePosition:
    ...
