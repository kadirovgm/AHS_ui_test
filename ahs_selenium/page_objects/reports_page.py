from .base_page import BasePage
from .locators.reports_page_locators import ReportsPageLocators


class ReportsPage(BasePage):
    def should_be_reports_page_text(self):
        assert self.is_element_present(*ReportsPageLocators.REPORTS_TEXT), \
            "Reports text doesn't appear!"
        assert self.browser.find_element(*ReportsPageLocators.REPORTS_TEXT).text == \
               "Reports", "Incorrect Reports page!"
