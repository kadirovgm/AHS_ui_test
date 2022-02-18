from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from .locators.locators import BasePageLocators


class BasePage:
    """Constructor for BasePage"""
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    """Open browser"""
    def open(self):
        self.browser.get(self.url)

    """Abstract method for waiting for an 'element to appear'"""
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    """Abstract method for waiting for an `element NOT to appear"""
    def is_not_element_present(self, how, what, timeout=1):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    """Abstract method for waiting for element present"""
    def waiting_for_element_present(self, how, what, timeout=1):
        try:
            WebDriverWait(self.browser, timeout, 0.05, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    """An abstract method for checking that element disappears"""
    def is_disappeared(self, how, what, timeout=3):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    """***Fields checking***"""
    def checking_fields_for_naming(self, locators, fields):
        for locator, field in zip(locators, fields):
            if self.is_element_present(*locator):
                assert self.browser.find_element(*locator).text == field, \
                    f"Incorrect value of field: {field}"
            else:
                assert f"{field} field is NOT present!"

    """Is element clickable"""
    def is_element_clickable(self, how, what, timeout=2):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False, "Element isn't clickable"
        return True

    """Are array of elements present"""
    def are_elements_present(self, array_of_locators):
        try:
            for locator in array_of_locators:
                assert self.is_element_present(*locator), f"{locator} filter doesn't present!"
        except NoSuchElementException:
            return False
        return True

    """Check that URL is correct"""
    def is_correct_url(self, expected_url):
        assert expected_url in self.browser.current_url, \
            f"Incorrect URL: Expected - {expected_url} Actual - {self.browser.current_url}!"

    # COMMON ACTIONS FROM ALL PAGES

    def go_to_positions_page(self):
        positions = self.browser.find_element(*BasePageLocators.POSITIONS_ICON)
        positions.click()

    def go_to_pool_page(self):
        pool = self.browser.find_element(*BasePageLocators.POOL_ICON)
        pool.click()

    def go_to_clients_projects_page(self):
        clients_projects = self.browser.find_element(*BasePageLocators.CLIENTS_PROJECTS_ICON)
        clients_projects.click()

    def go_to_reports_page(self):
        reports = self.browser.find_element(*BasePageLocators.REPORTS_ICON)
        reports.click()

    def go_to_help_page(self):
        help_center = self.browser.find_element(*BasePageLocators.HELP_CENTER_ICON)
        help_center.click()

