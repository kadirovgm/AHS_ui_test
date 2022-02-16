import pytest
import time
from pages.create_position_modal_page import CreateClientPositionModal
from pages.positions_page import PositionsPage
from settings import Setup, Urls


@pytest.mark.e2e_11
class TestClientProjectPosition:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        Setup.setup_help(browser, browser)

    def test_open_create_client_project_position(self, browser):
        position = PositionsPage(browser, Urls.POSITIONS_ACTIVE)
        position.add_client_project_position_button_click()

    def test_should_be_create_position_modal_elements(self, browser):
        ...
    
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
