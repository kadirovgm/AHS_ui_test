import pytest
from page_objects.login_page import LoginPage
from settings import Urls


"""Check for correct login page"""
@pytest.mark.e2e_1
class TestLoginPage:
    def test_correct_login_page(self, browser):
        page = LoginPage(browser, Urls.LINK_LOGIN_PAGE)
        page.open()
        page.should_be_login_page()


"""Check for correct Reset password page"""
@pytest.mark.e2e_2
class TestResetPage:
    def test_correct_reset_password_page(self, browser):
        page = LoginPage(browser, Urls.LINK_LOGIN_PAGE)
        page.open()
        page.go_forgot_password_link()
        page.should_be_reset_password_page()


"""Test user can Log In"""
@pytest.mark.e2e_3
class TestUserLogin:
    def test_user_can_login(self, browser):
        page = LoginPage(browser, Urls.LINK_LOGIN_PAGE)
        page.open()
        page.login_new_user(email="admin@admin.com", password="P@ssw0rd1")

    def test_user_logged_in_to_correct_account(self, browser):
        page = LoginPage(browser, Urls.MY_PROFILE)
        page.open()
        page.should_be_correct_profile_after_logging(expected_name="Olga Shakirova")


# TODO inheritance q.: https://stackoverflow.com/questions/21430900/py-test-skips-test-class-if-constructor-is-defined
