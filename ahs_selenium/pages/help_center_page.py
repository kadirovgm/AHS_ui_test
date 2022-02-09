from .base_page import BasePage
from .locators.locators import HelpCenterLocators


class HelpCenterPage(BasePage):
    def should_be_help_center_page_text(self):
        assert self.is_element_present(*HelpCenterLocators.HELP_CENTER_TEXT), \
            "Help Center text doesn't appear!"
        assert self.browser.find_element(*HelpCenterLocators.HELP_CENTER_TEXT).text == \
               "Help Center", "Incorrect Help Center page!"
