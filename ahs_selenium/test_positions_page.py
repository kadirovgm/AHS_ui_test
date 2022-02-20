import pytest
from page_objects.positions_page import PositionsPage
from settings import Urls, Setup


"""Test Positions page fields correct"""
@pytest.mark.regression
@pytest.mark.e2e_9
class TestPositionPageFieldsCorrectness:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        Setup.setup_help(browser, browser)

    """Active tab fields"""
    def test_active_tab_fields(self, browser):
        active = PositionsPage(browser, Urls.POSITIONS_ACTIVE)
        active.open()
        active.should_be_correct_fields_active()

    """Mine tab fields"""
    def test_mine_tab_fields(self, browser):
        mine = PositionsPage(browser, Urls.POSITIONS_MINE)
        mine.open()
        mine.should_be_correct_fields_mine()

    """History tab fields"""
    def test_history_tab_fields(self, browser):
        history = PositionsPage(browser, Urls.POSITIONS_HISTORY)
        history.open()
        history.should_be_correct_fields_history()


"""Test Positions page filters correct"""
@pytest.mark.regression
@pytest.mark.e2e_10
class TestPositionPageFiltersCorrectness:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        Setup.setup_help(browser, browser)

    """Active tab filters"""
    def test_active_tab_filters(self, browser):
        active = PositionsPage(browser, Urls.POSITIONS_ACTIVE)
        active.open()
        active.should_be_correct_filters_active()

    """Mine tab filters"""
    def test_mine_tab_filters(self, browser):
        mine = PositionsPage(browser, Urls.POSITIONS_MINE)
        mine.open()
        mine.should_be_correct_filters_mine()

    """History tab filters"""
    def test_history_tab_filters(self, browser):
        history = PositionsPage(browser, Urls.POSITIONS_HISTORY)
        history.open()
        history.should_be_correct_filters_history()


@pytest.mark.regression
@pytest.mark.e2e_11
class TestPositionsActiveFiltering:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        Setup.setup_help(browser, browser)




