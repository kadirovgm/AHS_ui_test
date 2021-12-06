from .base_page import BasePage
from .locators import PoolPageLocators
import time


class PoolPage(BasePage):
    def should_be_pool_page_text(self):
        assert self.is_element_present(*PoolPageLocators.POOL_TEXT), "Pool text doesn't appear!"
        assert self.browser.find_element_by(*PoolPageLocators.POOL_TEXT).text == "Pool", "Incorrect pool page!"
