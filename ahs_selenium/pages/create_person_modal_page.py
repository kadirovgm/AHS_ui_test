from .base_page import BasePage
from .locators.locators import CreatePersonModalLocators
from .randomData.random_data import RandomPersonData
from selenium.webdriver.common.keys import Keys
import time


class CreatePersonModal(BasePage):
    def should_be_create_person_modal(self):
        print("Checking that 'Add person modal' is correct")
        create_person_locator = \
            ["CREATE_NEW_PERSON_TEXT", "UPLOAD_PHOTO", "UPLOAD_OTHER_CV", "ENTER_AKVELON_CV", "FIRST_NAME", "LAST_NAME",
             "MIDDLE_NAME", "RECRUITER", "ROLES", "OFFICE", "COUNTRY", "CITY", "CONTEXT_COMMENT", "SALARY_TEXT",
             "ENGLISH_LEVEL", "ENGLISH_COMMENT", "PRIMARY_SKILL", "PRIMARY_SKILL_GRADE", "CONFIRMED_SKILL_CHECKBOX",
             "ADD_PRIMARY_SKILL", "OTHER_SKILL", "RESIDENCE_COUNTRY", "RESIDENCE_TYPE", "ADD_RESIDENCE", "WANT_RELOCATE",
             "WANT_RELOCATE_COMMENT", "ADD_ONE_MORE_CONTACT", "CONTACT_TYPE", "CONTACT_VALUE", "CREATE_PERSON_BUTTON",
             "CANCEL_CREATE_PERSON_BUTTON", "CROSS_EXIT"]

        # create_person_locator=[CreatePersonModalLocators.CREATE_NEW_PERSON_TEXT ...]
        create_person_locator = [eval("CreatePersonModalLocators."+i) for i in create_person_locator]
        for locator in create_person_locator:
            assert self.is_element_present(*locator), f"{locator} field doesn't present!"

    def add_new_person(self):
        # TODO to think about loading time!
        loading_time = 0.7  # city,country,skills
        print(f"Creating a new external person!")
        _ = self.browser.find_element(*CreatePersonModalLocators.FIRST_NAME).send_keys(RandomPersonData.first_name)
        _ = self.browser.find_element(*CreatePersonModalLocators.LAST_NAME).send_keys(RandomPersonData.last_name)

        # TODO How to handle "Select with search field" in ant-design? This is not works
        # recruiter = Select(self.browser.find_element(*CreatePersonModalLocators.RECRUITER))
        # recruiter.select_by_visible_text(RandomPersonData.recruiter)  # select_by_visible_text

        # TODO: My kostylnyi decision:
        recruiter = self.browser.find_element(*CreatePersonModalLocators.RECRUITER)
        recruiter.send_keys(RandomPersonData.recruiter, Keys.ENTER)
        roles = self.browser.find_element(*CreatePersonModalLocators.ROLES)
        roles.send_keys(RandomPersonData.role, Keys.ENTER)
        office = self.browser.find_element(*CreatePersonModalLocators.OFFICE)
        office.send_keys(RandomPersonData.office, Keys.DOWN, Keys.ENTER)
        country = self.browser.find_element(*CreatePersonModalLocators.COUNTRY)
        country.send_keys(RandomPersonData.country)
        time.sleep(loading_time)     # wait for the countries to load
        country.send_keys(Keys.ENTER)
        city = self.browser.find_element(*CreatePersonModalLocators.CITY)
        city.send_keys(RandomPersonData.city)
        time.sleep(loading_time)  # wait for the cities to load 
        city.send_keys(Keys.ENTER)
        _ = self.browser.find_element(*CreatePersonModalLocators.CREATE_NEW_PERSON_TEXT).click()
        context_comment = self.browser.find_element(*CreatePersonModalLocators.CONTEXT_COMMENT)
        context_comment.send_keys(RandomPersonData.context_comment)
        english_level = self.browser.find_element(*CreatePersonModalLocators.ENGLISH_LEVEL)
        english_level.send_keys(RandomPersonData.english_level, Keys.ENTER)
        primary_skill = self.browser.find_element(*CreatePersonModalLocators.PRIMARY_SKILL)
        primary_skill.send_keys(RandomPersonData.skill1)
        time.sleep(loading_time)  # wait for the skills to load 
        primary_skill.send_keys(Keys.ENTER)
        grade = self.browser.find_element(*CreatePersonModalLocators.PRIMARY_SKILL_GRADE)
        grade.send_keys(RandomPersonData.grade)
        # time.sleep(0.7) 
        grade.send_keys(Keys.ENTER)
        contact_type = self.browser.find_element(*CreatePersonModalLocators.CONTACT_TYPE)
        contact_type.send_keys(RandomPersonData.contact_type, Keys.DOWN, Keys.ENTER)
        contact_value = self.browser.find_element(*CreatePersonModalLocators.CONTACT_VALUE)
        contact_value.send_keys(RandomPersonData.email)
        create_person_button = self.browser.find_element(*CreatePersonModalLocators.CREATE_PERSON_BUTTON)
        create_person_button.click()

        print(f"Created person's name is: {RandomPersonData.first_name}")
        return RandomPersonData.first_name, RandomPersonData.last_name   # for checking that person is created and in external tab
















