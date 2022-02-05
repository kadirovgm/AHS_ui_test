from .base_page import BasePage
from .locators import PoolPageLocators
from .locators import PersonPageLocators
import time


class PoolPage(BasePage):
    def should_be_pool_page_text(self):
        assert self.is_element_present(*PoolPageLocators.POOL_TEXT), "Pool text doesn't appear!"
        assert self.browser.find_element(*PoolPageLocators.POOL_TEXT).text == "Pool", "Incorrect pool page!"
        assert self.is_element_present(*PoolPageLocators.ADD_PERSON), "Add person button doesn't appear!"

    def add_person_button_click(self):
        add_person = self.browser.find_element(*PoolPageLocators.ADD_PERSON)
        add_person.click()

    def go_to_external_tab(self):
        _ = self.browser.find_element(*PoolPageLocators.EXTERNAL_TAB).click()

    def search_for_person(self, first_name, second_name):
        print(f"Searching for {first_name} {second_name} in Pool->External")
        if self.is_element_present(*PoolPageLocators.FIRST_PERSON):
            _ = self.browser.find_element(*PoolPageLocators.SEARCH_NAME).send_keys(first_name+" "+second_name)
            time.sleep(1.5)  # waiting for searching results
            assert self.browser.find_element(*PoolPageLocators.FIRST_PERSON_NAME).text == first_name+" "+second_name, \
                "Person wasn't created or not in External tab!"
        else:
            assert "There is no Person suitable for search!"




