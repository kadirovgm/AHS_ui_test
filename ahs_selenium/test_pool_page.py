import pytest
import time
from pages.login_page import LoginPage
from pages.pool_page import PoolPage
from pages.create_person_modal_page import CreatePersonModal
from conftest import LINK_LOGIN_PAGE


@pytest.mark.skip
class TestPoolPageInternalFiltering:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, LINK_LOGIN_PAGE)
        page.open()
        time.sleep(0.5)
        page.login_new_user(email="admin@admin.com", password="P@ssw0rd1")

    @pytest.mark.skip
    def test_main_search(self, browser):
        ...


class TestPoolPageExternalFiltering:
    ...


class TestPoolPageBlacklistFiltering:
    ...



