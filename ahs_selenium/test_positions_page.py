import pytest
import time
from pages.login_page import LoginPage
from pages.positions_page import PositionsPage
from urls import Urls


@pytest.mark.e2e_6
class TestPoolPageFieldsCorrectness:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, Urls.LINK_LOGIN_PAGE)
        page.open()
        time.sleep(0.5)
        page.login_new_user(email="admin@admin.com", password="P@ssw0rd1")

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
