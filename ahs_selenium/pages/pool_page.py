from .base_page import BasePage
from .locators import PoolPageLocators
import time


class PoolPage(BasePage):
    def should_be_pool_page_text(self):
        assert self.is_element_present(*PoolPageLocators.POOL_TEXT), "Pool text doesn't appear!"
        assert self.browser.find_element(*PoolPageLocators.POOL_TEXT).text == "Pool", "Incorrect pool page!"
        assert self.is_element_present(*PoolPageLocators.ADD_PERSON), "Add person button doesn't appear!"

    def add_person_button_click(self):
        add_person = self.browser.find_element(*PoolPageLocators.ADD_PERSON)
        add_person.click()

