from .base_page import BasePage
from .locators import PoolPageLocators
from .locators import PersonPageLocators
import time


class PoolPage(BasePage):
    """Correct Pool page"""
    def should_be_pool_page_text(self):
        assert self.is_element_present(*PoolPageLocators.POOL_TEXT), "Pool text doesn't appear!"
        assert self.browser.find_element(*PoolPageLocators.POOL_TEXT).text == "Pool", "Incorrect pool page!"
        assert self.is_element_present(*PoolPageLocators.ADD_PERSON), "Add person button doesn't appear!"
    
    # TODO not working right now!
    def should_be_correct_fields_internal(self):
        print("Start to check internal pool page fields")
        internal_fields_locator = ["NAME", "TYPE", "ROLE", "SKILLS", "CITY_COUNTRY", "OFFICE", "ENG_LEVEL", "VISA", "ACTIVE_PROJECTS", "HR"]
        internal_fields_text = ["Name", "Type", "Roles", "Skills", "City | Country", "Ofice", "Eng. level", "Visa status", "Active projects", "HR"]
        for locator, field in zip(internal_fields_locator, internal_fields_text):
            print(f"This is locator's value {locator}")
            if self.is_element_present(*PoolPageLocators.locator): # Как сделать так чтобы .locator был равен значению итерации?
                assert self.browser.find_element(*PoolPageLocators.locator).text == field, \
                f"Incorrect value of field: {locator} is not equal to {field}"
            else:
                assert f"{field} field is NOT present!"

    """Add new person"""
    def add_person_button_click(self):
        add_person = self.browser.find_element(*PoolPageLocators.ADD_PERSON)
        add_person.click()

    """Go to Internal, External, Blacklist tabs"""
    def go_to_internal_tab(self):
        _ = self.browser.find_element(*PoolPageLocators.INTERNAL_TAB).click()

    def go_to_external_tab(self):
        _ = self.browser.find_element(*PoolPageLocators.EXTERNAL_TAB).click()

    def go_to_blacklist_tab(self):
        _ = self.browser.find_element(*PoolPageLocators.BLACKLIST_TAB).click()


    """Searching in pool"""
    def search_for_person(self, first_name, second_name):
        print(f"Searching for {first_name} {second_name} in Pool->External")
        if self.is_element_present(*PoolPageLocators.FIRST_PERSON):
            _ = self.browser.find_element(*PoolPageLocators.SEARCH_NAME).send_keys(first_name+" "+second_name)
            time.sleep(1.5)  # waiting for searching results
            assert self.browser.find_element(*PoolPageLocators.FIRST_PERSON_NAME).text == first_name+" "+second_name, \
                "Person wasn't created or not in External tab!"
        else:
            assert "There is no Person suitable for search!"




