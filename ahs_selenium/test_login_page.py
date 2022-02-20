import pytest
from page_objects.login_page import LoginPage
from settings import Urls
from page_objects.FixtureData.fixture_users import *


"""Check for correct login page"""
@pytest.mark.regression
@pytest.mark.e2e_1
class TestLoginPage:
    def test_correct_login_page(self, browser):
        page = LoginPage(browser, Urls.LINK_LOGIN_PAGE)
        page.open()
        page.should_be_login_page()


"""Check for correct Reset password page"""
@pytest.mark.regression
@pytest.mark.e2e_2
class TestResetPage:
    def test_correct_reset_password_page(self, browser):
        page = LoginPage(browser, Urls.LINK_LOGIN_PAGE)
        page.open()
        page.go_forgot_password_link()
        page.should_be_reset_password_page()


"""Test user can Log In"""
@pytest.mark.regression
@pytest.mark.e2e_3
class TestUserLogin:
    @pytest.mark.parametrize('user', (UserHead, UserLead, UserRecruiter))
    def test_user_can_login(self, browser_login, user):
        page = LoginPage(browser_login, Urls.LINK_LOGIN_PAGE)
        page.open()
        page.login_new_user(user)
        page.is_user_successfully_logged_in()

        page = LoginPage(browser_login, Urls.MY_PROFILE)
        page.open()
        page.should_be_correct_profile_after_logging(user)

# TODO inheritance q.: https://stackoverflow.com/questions/21430900/py-test-skips-test-class-if-constructor-is-defined
