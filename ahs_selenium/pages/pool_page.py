from .base_page import BasePage
from .locators.locators import PoolPageLocators
from .locators.locators import CreatePersonModalLocators
import time

# TODO For future:
# class PoolPageCommonActions
# class PoolPageInternal, PoolPageExternal, PoolPageBlacklist


class PoolPage(BasePage):
    """Correct Pool page"""
    def should_be_pool_page_text(self):
        assert self.is_element_present(*PoolPageLocators.POOL_TEXT), "Pool text doesn't appear!"
        assert self.browser.find_element(*PoolPageLocators.POOL_TEXT).text == "Pool", "Incorrect pool page!"
        assert self.is_element_present(*PoolPageLocators.ADD_PERSON), "Add person button doesn't appear!"
    
    """Internal"""
    def should_be_correct_fields_internal(self):
        # internal_fields_locator = ["NAME", "TYPE", "ROLE", "SKILLS", "CITY_COUNTRY", "OFFICE", "ENG_LEVEL", "VISA", "ACTIVE_PROJECTS", "HR"]
        # internal_fields_locator = [eval("PoolPageLocators."+i) for i in internal_fields_locator]
        internal_fields_locator = \
            [PoolPageLocators.NAME_i, PoolPageLocators.TYPE_i, PoolPageLocators.ROLE_i, PoolPageLocators.SKILLS_i,
             PoolPageLocators.CITY_COUNTRY_i, PoolPageLocators.OFFICE_i, PoolPageLocators.ENG_LEVEL_i,
             PoolPageLocators.VISA_i, PoolPageLocators.ACTIVE_PROJECTS_i, PoolPageLocators.HR_i]
        internal_fields_text = \
            ["Name", "Type", "Roles", "Skills", "City | Country", "Office", "Eng. level",
             "Visa status", "Active projects", "HR"]
        self.checking_fields(internal_fields_locator, internal_fields_text)

    def should_be_filters_internal(self):
        internal_filters_locators = \
            ["F_LABEL_i", "F_TYPE_i", "F_ROLE_i", "F_SKILLS_i", "F_CITY_i", "F_OFFICE_i",
             "F_ENG_i", "F_VISA_i", "F_ACTIVE_I", "F_HR_I"]
        internal_filters_locators = [eval("PoolPageLocators." + i) for i in internal_filters_locators]
        for locator in internal_filters_locators:
            assert self.is_element_present(*locator), f"{locator} filter doesn't present!"

    """External (Blacklist)"""
    def should_be_correct_fields_external_blacklist(self):
        external_fields_locator = \
            [PoolPageLocators.NAME_e, PoolPageLocators.ROLE_e, PoolPageLocators.SKILLS_e, PoolPageLocators.CITY_COUNTRY_e,
             PoolPageLocators.OFFICE_e, PoolPageLocators.ENG_LEVEL_e, PoolPageLocators.VISA_e, PoolPageLocators.HR_e]
        external_fields_text = ["Name", "Roles", "Skills", "City | Country", "Office", "Eng. level", "Visa status", "HR"]
        self.checking_fields(external_fields_locator, external_fields_text)

    def should_be_filters_external_blacklist(self):
        external_filters_locators = \
            ["F_LABEL_e", "F_ROLE_e", "F_SKILLS_e", "F_CITY_e", "F_OFFICE_e", "F_ENG_e", "F_VISA_e", "F_HR_e"]
        external_filters_locators = [eval("PoolPageLocators." + i) for i in external_filters_locators]
        for locator in external_filters_locators:
            assert self.is_element_present(*locator), f"{locator} filter doesn't present!"

    """Add new person"""
    def add_person_button_click(self):
        add_person = self.browser.find_element(*PoolPageLocators.ADD_PERSON)
        add_person.click()
        assert self.is_element_present(*CreatePersonModalLocators.CREATE_NEW_PERSON_TEXT), \
            "Create person modal incorrect appeared"

    """Go to Internal, External, Blacklist tabs"""
    def go_to_internal_tab(self):
        _ = self.browser.find_element(*PoolPageLocators.INTERNAL_TAB).click()

    def go_to_external_tab(self):
        _ = self.browser.find_element(*PoolPageLocators.EXTERNAL_TAB).click()

    def go_to_blacklist_tab(self):
        _ = self.browser.find_element(*PoolPageLocators.BLACKLIST_TAB).click()

    """*Searching in pool*"""
    def search_for_person(self, first_name, second_name):
        print(f"Searching for {first_name} {second_name} in Pool->External")
        if self.is_element_present(*PoolPageLocators.FIRST_PERSON):
            _ = self.browser.find_element(*PoolPageLocators.SEARCH_NAME).send_keys(first_name+" "+second_name)
            time.sleep(1.5)  # waiting for searching results
            assert self.browser.find_element(*PoolPageLocators.FIRST_PERSON_NAME).text == first_name+" "+second_name, \
                "Person wasn't created or not in External tab!"
        else:
            assert "There is no Person suitable for search!"




