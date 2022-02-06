import pytest
import time
from pages.login_page import LoginPage
from pages.pool_page import PoolPage
from pages.create_person_modal_page import CreatePersonModal
from urls import LINK_LOGIN_PAGE, POOL_INTERNAL


@pytest.mark.e2e_5
class TestPoolPageFieldsCorrectness:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, LINK_LOGIN_PAGE)
        page.open()
        time.sleep(0.5)
        page.login_new_user(email="admin@admin.com", password="P@ssw0rd1")

    def test_internal_fileds(self, browser):
        internal = PoolPage(browser, POOL_INTERNAL)
        internal.open()
        internal.should_be_correct_fields_internal()



@pytest.mark.skip
class TestPoolPageInternalFiltering:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, LINK_LOGIN_PAGE)
        page.open()
        time.sleep(0.5)
        page.login_new_user(email="admin@admin.com", password="P@ssw0rd1")

    @pytest.mark.skip
    def test_main_search(self, browser):
        ...

@pytest.mark.skip
class TestPoolPageExternalFiltering:
    ...

@pytest.mark.skip
class TestPoolPageBlacklistFiltering:
    ...



