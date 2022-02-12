import pytest
import time
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.positions_page import PositionsPage
from settings import Urls, Setup


@pytest.mark.e2e_7
class TestPositionPageFieldsCorrectness:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        Setup.setup_help(browser, browser)

    def test_active_tab_fields(self, browser):
        active = PositionsPage(browser, Urls.POSITIONS_ACTIVE)
        active.open()
        active.should_be_correct_fields_active()

    def test_mine_tab_fields(self, browser):
        mine = PositionsPage(browser, Urls.POSITIONS_MINE)
        mine.open()
        mine.should_be_correct_fields_mine()

    def test_history_tab_fields(self, browser):
        history = PositionsPage(browser, Urls.POSITIONS_HISTORY)
        history.open()
        history.should_be_correct_fields_history()


@pytest.mark.e2e_8
class TestPositionPageFiltersCorrectness:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        Setup.setup_help(browser, browser)

    def test_active_tab_filters(self, browser):
        active = PositionsPage(browser, Urls.POSITIONS_ACTIVE)
        active.open()
        active.should_be_correct_filters_active()

    def test_mine_tab_filters(self, browser):
        mine = PositionsPage(browser, Urls.POSITIONS_MINE)
        mine.open()
        mine.should_be_correct_filters_mine()

    def test_history_tab_filters(self, browser):
        history = PositionsPage(browser, Urls.POSITIONS_HISTORY)
        history.open()
        history.should_be_correct_filters_history()
