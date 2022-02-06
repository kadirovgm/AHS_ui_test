import pytest
import time
from pages.login_page import LoginPage
from links import LINK_LOGIN_PAGE


@pytest.mark.e2e_1
class TestLoginPage:
    def test_correct_login_page(self, browser):
        link = LINK_LOGIN_PAGE
        page = LoginPage(browser, link)
        page.open()
        time.sleep(0.5)
        page.should_be_login_page()


@pytest.mark.e2e_2
class TestResetPage:
    def test_correct_reset_password_page(self, browser):
        link = LINK_LOGIN_PAGE
        page = LoginPage(browser, link)
        page.open()
        time.sleep(0.5)
        page.go_forgot_password_link()
        page.should_be_reset_password_page()



