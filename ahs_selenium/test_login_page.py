import pytest
import time
from pages.login_page import LoginPage
from settings import Urls


@pytest.mark.e2e_1
class TestLoginPage:
    def test_correct_login_page(self, browser):
        page = LoginPage(browser, Urls.LINK_LOGIN_PAGE)
        page.open()
        page.should_be_login_page()


@pytest.mark.e2e_2
class TestResetPage:
    def test_correct_reset_password_page(self, browser):
        page = LoginPage(browser, Urls.LINK_LOGIN_PAGE)
        page.open()
        page.go_forgot_password_link()
        page.should_be_reset_password_page()

# TODO inheritance q.: https://stackoverflow.com/questions/21430900/py-test-skips-test-class-if-constructor-is-defined
