from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    """Login user"""
    def login_new_user(self):
        email = "admin@admin.com"
        password = "P@ssw0rd1"
        self.should_be_login_page()
        self.fill_login_form(email, password)
        time.sleep(1)
        # should be authorized user ?

    def can_go_forgot_password_link(self):
        forgot_link = self.browser.find_element(*LoginPageLocators.FORGOT_LINK)
        forgot_link.click()

    """Checking for correct login page"""
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_forgot_password_link()

    def should_be_login_url(self):
        assert self.browser.current_url in self.url, "Incorrect Login page URL!"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.WELCOME_TEXT), "Welcome text isn't present!"
        assert self.browser.find_element(*LoginPageLocators.WELCOME_TEXT).text == "Welcome back", \
            "Incorrect welcome text!"
        assert self.is_element_present(*LoginPageLocators.EMAIL), "Email field doesn't appear!"
        assert self.is_element_present(*LoginPageLocators.PASSWORD), "Password field doesn't appear!"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button doesn't appear!"

    def should_be_forgot_password_link(self):
        assert self.is_element_present(*LoginPageLocators.FORGOT_LINK), "Forgot link element doesn't appear!"

    """Filling with correct data"""
    def fill_login_form(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        input_password.send_keys(password)
        button_login = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        button_login.click()


