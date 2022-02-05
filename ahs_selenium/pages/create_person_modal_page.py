from .base_page import BasePage
from .locators import CreatePersonModalLocators
# from ahs_selenium.pages.random_person import RandomPersonData
from .random_data_person import RandomPersonData
from selenium.webdriver.support.ui import Select            # for dropdown list
from selenium.webdriver.common.keys import Keys
import time


class CreatePersonModal(BasePage):
    def should_be_create_person_modal(self):
        assert self.is_element_present(*CreatePersonModalLocators.CREATE_NEW_PERSON_TEXT), "Text in top doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.UPLOAD_PHOTO), "Upload photo field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.UPLOAD_OTHER_CV), \
            "Upload other cv field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.ENTER_AKVELON_CV), \
            "Enter Akvelon CV field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.FIRST_NAME), "First name field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.LAST_NAME), "Last name field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.MIDDLE_NAME), "Middle name field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.RECRUITER), "Recruiter field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.ROLES), "Roles field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.OFFICE), "Office field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.COUNTRY), "Country field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.CITY), "City field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.CONTEXT_COMMENT), \
            "Context comment field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.SALARY_TEXT), "Salary field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.ENGLISH_LEVEL), "English level field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.ENGLISH_COMMENT), \
            "English comment field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.PRIMARY_SKILL), "primary skills field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.PRIMARY_SKILL_GRADE), \
            "primary skills grade field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.CONFIRMED_SKILL_CHECKBOX), \
            "confirmed skills field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.ADD_PRIMARY_SKILL), "Add skills field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.OTHER_SKILL), "Other skills field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.RESIDENCE_COUNTRY), "Residences field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.RESIDENCE_TYPE), \
            "Residences type field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.ADD_RESIDENCE), "Add Residence field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.WANT_RELOCATE), "Want relocate field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.WANT_RELOCATE_COMMENT), \
            "Want relocate comment field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.ADD_ONE_MORE_CONTACT), \
            "Add contact field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.CONTACT_TYPE), "Contact type field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.CONTACT_VALUE), "Contact value field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.CREATE_PERSON_BUTTON), \
            "CREATE_PERSON_BUTTON doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.CANCEL_CREATE_PERSON_BUTTON), \
            "CANCEL_CREATE_PERSON_BUTTON doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.CROSS_EXIT), "Exit cross doesn't appear!"

    def add_new_person(self):
        first_name = self.browser.find_element(*CreatePersonModalLocators.FIRST_NAME).send_keys(RandomPersonData.first_name)
        last_name = self.browser.find_element(*CreatePersonModalLocators.LAST_NAME).send_keys(RandomPersonData.last_name)

        # TODO How to handle "Select with search field" in ant-design? This is not works
        # recruiter = Select(self.browser.find_element(*CreatePersonModalLocators.RECRUITER))
        # recruiter.select_by_visible_text(RandomPersonData.recruiter)  # select_by_visible_text

        # TODO: My kostylnyi decision))
        recruiter = self.browser.find_element(*CreatePersonModalLocators.RECRUITER)
        recruiter.send_keys(RandomPersonData.recruiter, Keys.ENTER)
        roles = self.browser.find_element(*CreatePersonModalLocators.ROLES)
        roles.send_keys(RandomPersonData.role, Keys.ENTER)
        office = self.browser.find_element(*CreatePersonModalLocators.OFFICE)
        office.send_keys(RandomPersonData.office, Keys.ENTER)
        country = self.browser.find_element(*CreatePersonModalLocators.COUNTRY)
        country.send_keys(RandomPersonData.country)
        time.sleep(0.7)     # wait for the countries to load
        country.send_keys(Keys.ENTER)
        city = self.browser.find_element(*CreatePersonModalLocators.CITY)
        city.send_keys(RandomPersonData.city)
        time.sleep(0.7)  # wait for the countries to load
        city.send_keys(Keys.ENTER)
        # _ = self.browser.find_element(*CreatePersonModalLocators.CREATE_NEW_PERSON_TEXT).click()
        context_comment = self.browser.find_element(*CreatePersonModalLocators.CONTEXT_COMMENT)
        context_comment.send_keys(RandomPersonData.context_comment)
        english_level = self.browser.find_element(*CreatePersonModalLocators.ENGLISH_LEVEL)
        english_level.send_keys(RandomPersonData.english_level, Keys.ENTER)
        primary_skill = self.browser.find_element(*CreatePersonModalLocators.PRIMARY_SKILL)
        primary_skill.send_keys(RandomPersonData.skill1)
        time.sleep(0.7)
        primary_skill.send_keys(Keys.ENTER)
        grade = self.browser.find_element(*CreatePersonModalLocators.PRIMARY_SKILL_GRADE)
        grade.send_keys(RandomPersonData.grade)
        time.sleep(0.7)
        grade.send_keys(Keys.ENTER)
        contact_type = self.browser.find_element(*CreatePersonModalLocators.CONTACT_TYPE)
        contact_type.send_keys(RandomPersonData.contact_type, Keys.DOWN, Keys.ENTER)
        contact_value = self.browser.find_element(*CreatePersonModalLocators.CONTACT_VALUE)
        contact_value.send_keys(RandomPersonData.email)
        create_person_button = self.browser.find_element(*CreatePersonModalLocators.CREATE_PERSON_BUTTON)
        create_person_button.click()
















