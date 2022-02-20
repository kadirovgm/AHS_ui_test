from .base_page import BasePage
from .locators.pool_page_locators import PoolPageLocators
from .locators.create_person_modal_locators import CreatePersonModalLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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

    """Add new person"""
    def add_person_button_click(self):
        add_person = self.browser.find_element(*PoolPageLocators.ADD_PERSON)
        add_person.click()

    def add_person_modal_should_be_opened(self):
        assert self.is_element_present(*CreatePersonModalLocators.CREATE_NEW_PERSON_TEXT), \
            "Create person modal incorrect appeared"

    """Internal tab"""
    def should_be_correct_fields_internal(self):
        internal_fields_locators = \
            ["NAME_i", "TYPE_i", "ROLE_i", "SKILLS_i", "CITY_COUNTRY_i", "OFFICE_i", "ENG_LEVEL_i",
             "VISA_i", "ACTIVE_PROJECTS_i", "HR_i"]
        internal_fields_locators = [eval("PoolPageLocators." + i) for i in internal_fields_locators]
        internal_fields_text = \
            ["Name", "Type", "Roles", "Skills", "City | Country", "Office", "Eng. level",
             "Visa status", "Active projects", "HR"]
        self.checking_fields_for_naming(internal_fields_locators, internal_fields_text)

    def should_be_filters_internal(self):
        internal_filters_locators = \
            ["F_LABEL", "F_TYPE_i", "F_ROLE_i", "F_SKILLS_i", "F_CITY_i", "F_OFFICE_i",
             "F_ENG_i", "F_VISA_i", "F_ACTIVE_I", "F_HR_I"]
        internal_filters_locators = [eval("PoolPageLocators." + i) for i in internal_filters_locators]
        for locator in internal_filters_locators:
            assert self.is_element_present(*locator), f"{locator} filter doesn't present!"

    """External (Blacklist) tab"""
    def should_be_correct_fields_external_blacklist(self):
        external_fields_locators = \
            ["NAME_e", "ROLE_e", "SKILLS_e", "CITY_COUNTRY_e", "OFFICE_e", "ENG_LEVEL_e", "VISA_e", "HR_e"]
        external_fields_locators = [eval("PoolPageLocators." + i) for i in external_fields_locators]
        external_fields_text = ["Name", "Roles", "Skills", "City | Country", "Office", "Eng. level", "Visa status", "HR"]
        self.checking_fields_for_naming(external_fields_locators, external_fields_text)

    def should_be_filters_external_blacklist(self):
        external_filters_locators = \
            ["F_LABEL", "F_ROLE_e", "F_SKILLS_e", "F_CITY_e", "F_OFFICE_e", "F_ENG_e", "F_VISA_e", "F_HR_e"]
        external_filters_locators = [eval("PoolPageLocators." + i) for i in external_filters_locators]
        for locator in external_filters_locators:
            assert self.is_element_present(*locator), f"{locator} filter doesn't present!"

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
            if self.waiting_for_element_present(*PoolPageLocators.FIRST_PERSON):
                assert self.browser.find_element(*PoolPageLocators.FIRST_PERSON_NAME).text == first_name+" "+second_name, \
                    "The results don't match the search! Searching does not work!"
            else:
                raise AssertionError("Page hasn't loaded or there is no such person")
        else:
            raise AssertionError("There is no Person suitable for search!")

    """*Clear filters [All tabs]*"""
    def clear_filters(self):
        _ = self.browser.find_element(*PoolPageLocators.CLEAR_FILTERS).click()
        # check that filters was reset
        if self.waiting_for_element_present(*PoolPageLocators.FIRST_PERSON):
            return True

    """*Clicking to filters in Pool [All tabs]*"""
    def click_to_filter_by(self, filter_locator):
        # if filter is enable - click
        if self.is_element_clickable(*filter_locator):
            self.browser.find_element(*filter_locator).click()
        else:
            raise AssertionError(f"Filter by {filter_locator} doesn't clickable")

    """*Check that filter works*"""
    def is_filter_works(self, filter_object, expected_locator):
        if self.waiting_for_element_present(*PoolPageLocators.FIRST_PERSON):
            assert self.browser.find_element(*expected_locator).text == filter_object, \
                f"Incorrect filtering by {str(filter_object)}: {filter_object}"
        else:
            raise AssertionError(f"Probably there is no person with {str(filter_object)}: {filter_object}")

    """*Reset any filters [All tabs]*"""
    def is_filter_reset(self, filter_locator, reset_locator):
        # open filter
        self.click_to_filter_by(filter_locator)
        # resetting
        if self.waiting_for_element_present(*reset_locator):
            if self.browser.find_element(*reset_locator).is_enabled():
                self.browser.find_element(*reset_locator).click()
            else:
                raise AssertionError("Reset button is not enabled after filtering")
        else:
            raise AssertionError("There is no Reset button after filtering")
        # checking that reset is disabled
        self.click_to_filter_by(filter_locator)
        if not self.browser.find_element(*reset_locator).is_enabled():
            return True
        else:
            raise AssertionError(f"Error - Filter hasn't reset")

    """Filtering"""
    """Universal filter by label [Internal/External/Blacklist]"""
    def filter_label(self, label, tab=0):
        print(f"Filtering by label {label}")
        locator_label = ...
        if label == "Bench":
            locator_label = PoolPageLocators.F_LABEL_i_bench
        elif label == "Pre-offer":
            locator_label = PoolPageLocators.F_LABEL_e_PRE_OFFER
        elif label == "Dismiss":
            locator_label = PoolPageLocators.F_LABEL_e_Dismiss
        elif label == "Dismiss" and tab == "Blacklist":
            locator_label = PoolPageLocators.F_LABEL_b_Dismiss
        else:
            raise AssertionError("Please specify as label - 'Bench', 'Pre-offer', 'Dismiss'")
        # open filter
        self.click_to_filter_by(PoolPageLocators.F_LABEL)
        # filtering
        if self.is_element_present(*locator_label):
            _ = self.browser.find_element(*locator_label).click()
        else:
            raise AssertionError(f"There is no {label} label")
        _ = self.browser.find_element(*PoolPageLocators.F_LABEL_OK).click()

        # check filtering (label, expected label)
        self.is_filter_works(label, PoolPageLocators.FIRST_PERSON_LABEL)

    """Reset filter by label [Internal/External/Blacklist]"""
    def reset_filter_label(self):
        label_filter_locator = PoolPageLocators.F_LABEL
        reset_locator = PoolPageLocators.F_LABEL_RESET
        self.is_filter_reset(label_filter_locator, reset_locator)

    """Filter by type [Internal]"""
    def filter_type_internal(self, person_type):
        """ Only for internal tab"""
        locator_type = ...
        if person_type == "Long-term":
            locator_type = PoolPageLocators.F_TYPE_i_LONG_TERM
        elif person_type == "Contractor":
            locator_type = PoolPageLocators.F_TYPE_i_CONTRACTOR
        elif person_type == "Short-term":
            locator_type = PoolPageLocators.F_TYPE_i_SHORT_TERM
        else:
            raise AssertionError("Please specify as internal person types - 'Long-term', 'Contractor', 'Short-term'")
        print(f"Filtering by type")
        # Open filter by type
        self.click_to_filter_by(PoolPageLocators.F_TYPE_i)
        # Filtering
        if self.is_element_present(*locator_type):
            _ = self.browser.find_element(*locator_type).click()
        else:
            raise AssertionError(f"There is no {person_type} label")
        _ = self.browser.find_element(*PoolPageLocators.F_TYPE_i_OK).click()
        # check filtering
        self.is_filter_works(person_type, PoolPageLocators.FIRST_PERSON_TYPE)

    """Reset filter by person type [Internal]"""
    def reset_filter_type_internal(self):
        type_filter_locator = PoolPageLocators.F_TYPE_i
        reset_locator = PoolPageLocators.F_TYPE_RESET
        self.is_filter_reset(type_filter_locator, reset_locator)

    """Filter by role [Internal]"""
    def filter_role_internal(self, role):
        # Open filter by role
        self.click_to_filter_by(PoolPageLocators.F_ROLE_i)
        # Filtering
        if self.is_element_present(*PoolPageLocators.F_ROLE_i_SELECT):
            role_input = self.browser.find_element(*PoolPageLocators.F_ROLE_i_SELECT)
            role_input.send_keys(role, Keys.ENTER)
        else:
            raise AssertionError(f"There is no input for filtering by role")
        _ = self.browser.find_element(*PoolPageLocators.F_ROLE_i_OK).click()
        # Check filtering
        self.is_filter_works(role, PoolPageLocators.FIRST_PERSON_ROLE)

    """Reset Filter by role"""
    def reset_filter_role(self):
        role_filter_locator = PoolPageLocators.F_ROLE_i
        reset_locator = PoolPageLocators.F_ROLE_i_RESET
        self.is_filter_reset(role_filter_locator, reset_locator)

    """Filter by Skills"""
    def filter_skills_internal(self, skill, loading_time=0.7):
        # Open filter by skills
        self.click_to_filter_by(PoolPageLocators.F_SKILLS_i)
        # Filtering
        if self.are_elements_present({PoolPageLocators.F_SKILLS_i_SELECT, PoolPageLocators.F_GRADE_i_SELECT}):
            skill_input = self.browser.find_element(*PoolPageLocators.F_SKILLS_i_SELECT)
            skill_input.send_keys(skill)
            time.sleep(loading_time)
            skill_input.send_keys(Keys.ENTER)

            grade = self.browser.find_element(*PoolPageLocators.F_GRADE_i_SELECT)
            ActionChains(self.browser).move_to_element(grade).click(grade).send_keys(Keys.DOWN + Keys.ENTER).perform()
        else:
            raise AssertionError(f"There is no input for filtering by Skill and Grade")
        _ = self.browser.find_element(*PoolPageLocators.F_SKILLS_i_OK).click()

        # Check filtering
        self.is_filter_works(skill, PoolPageLocators.FIRST_PERSON_SKILL)

    """Reset filter by skills"""
    def reset_filter_skills(self):
        skill_filter_locator = PoolPageLocators.F_SKILLS_i
        reset_locator = PoolPageLocators.F_SKILLS_i_RESET
        self.is_filter_reset(skill_filter_locator, reset_locator)

























