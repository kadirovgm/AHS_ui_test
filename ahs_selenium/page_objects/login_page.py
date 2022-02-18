from .base_page import BasePage
from .locators.locators import LoginPageLocators
from .locators.locators import ResetPageLocators
import time


class LoginPage(BasePage):

    """Login user (Setup)"""
    def login_new_user(self, email, password):
        self.fill_login_form(email, password)
        time.sleep(0.5)

    """Filling with correct data"""
    def fill_login_form(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        input_password.send_keys(password)
        button_login = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        button_login.click()

    """Checking for correct login page"""
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_forgot_password_link()

    def should_be_login_url(self):
        assert self.browser.current_url in self.url, "Incorrect Login page URL!"

    def should_be_login_form(self):
        elements = ["WELCOME_TEXT", "EMAIL", "PASSWORD", "LOGIN_BUTTON"]
        elements = [eval("LoginPageLocators." + i) for i in elements]
        self.are_elements_present(elements)

    def should_be_forgot_password_link(self):
        assert self.is_element_present(*LoginPageLocators.FORGOT_LINK), "Forgot link element doesn't appear!"

    """Reset password"""
    def go_forgot_password_link(self):
        forgot_link = self.browser.find_element(*LoginPageLocators.FORGOT_LINK)
        forgot_link.click()

    def should_be_reset_password_page(self):
        assert self.is_element_present(*ResetPageLocators.RESET_TEXT), "'Reset password' text isn't present!"
        assert self.browser.find_element(*ResetPageLocators.RESET_TEXT).text == "Reset password", \
            "Incorrect Reset text!"
        assert self.is_element_present(*ResetPageLocators.EMAIL), "Email field doesn't appear!"
        assert self.is_element_present(*ResetPageLocators.SEND_BUTTON), "'Send link' button doesn't appear!"
        assert self.is_element_present(*ResetPageLocators.GO_BACK_TO_LOGIN), "'Back to login button doesn't appear'"

