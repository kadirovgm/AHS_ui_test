import pytest
import time
from pages.login_page import LoginPage
from urls import Urls

@pytest.mark.skip
class TestCreateClientPosition:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, Urls.LINK_LOGIN_PAGE)
        page.open()
        time.sleep(0.5)
        page.login_new_user(email="admin@admin.com", password="P@ssw0rd1")
