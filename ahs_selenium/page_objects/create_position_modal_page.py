from .base_page import BasePage
from .locators.create_position_modal_locators import CreatePositionModalLocators
from .FixtureData.fixture_data import CreatePositionData
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random


class CreateClientPositionModal(BasePage):
    """Go to Create Position Modal Tabs"""
    def go_to_pos_details_tab(self):
        _ = self.browser.find_element(*CreatePositionModalLocators.POS_DETAIL_TAB).click()

    def go_to_assigns_tab(self):
        _ = self.browser.find_element(*CreatePositionModalLocators.ASSIGNS_TAB).click()

    def go_to_requests_tab(self):
        _ = self.browser.find_element(*CreatePositionModalLocators.REQUESTS_TAB).click()

    """Checking for correct elements presenting in create clint project position modal"""
    def should_be_correct_client_position_modal_elements_pos_details(self):
        position_details_elements = \
            ["POS_DETAIL_TAB", "UNCONFIRMED_RADIO", "CONFIRMED_RADIO", "PRIORITY", "CLIENT", "PROJECT", "ORIG_LOCATION",
             "REMOTE_TYPE", "COMMENT", "POS_NAME", "ROLE", "ENG_LEVEL", "ADD_ONE_MORE_SKILL", "CANCEL_DETAILS", "NEXT_DETAILS"]
        position_details_elements = [eval("CreatePositionModalLocators." + i) for i in position_details_elements]
        for locator in position_details_elements:
            assert self.is_element_present(*locator), f"{locator} field doesn't present!"

    def should_be_correct_client_position_modal_elements_assigns(self):
        assigns_elements = \
            ["ASSIGNS_TAB", "PRIMARY_OFFICE", "OTHER_OFFICE", "ALL_OFFICES_CHECK", "RECRUITERS","CANCEL_ASSIGNS",  "NEXT_ASSIGNS"]
        assigns_elements = [eval("CreatePositionModalLocators." + i) for i in assigns_elements]
        for locator in assigns_elements:
            assert self.is_element_present(*locator), f"{locator} field doesn't present!"

    def should_be_correct_client_position_modal_elements_requests(self):
        _ = self.browser.find_element(*CreatePositionModalLocators.ADD_CR).click()
        requests_elements = \
            ["REQUESTS_TAB", "ADD_CR", "NEW_BUSINESS_RADIO", "UPSELL_RADIO", "BILLABLE_STAT", "JOB_TYPE", "HOURS",
             "DEADLINE", "REQUIRED", "CANCEL_REQUESTS", "CREATE_POSITION"]
        requests_elements = [eval("CreatePositionModalLocators." + i) for i in requests_elements]
        for locator in requests_elements:
            assert self.is_element_present(*locator), f"{locator} field doesn't present!"

    """Add new client project position"""
    def add_new_client_project_position(self, loading_time):
        print(f"Adding a new client project position")
        time.sleep(loading_time)

        """Position details"""
        confirm_status = [CreatePositionModalLocators.CONFIRMED_RADIO, CreatePositionModalLocators.UNCONFIRMED_RADIO]
        _ = self.browser.find_element(*(random.choice(confirm_status))).click()

        n = random.randint(1, 4)
        priority = self.browser.find_element(*CreatePositionModalLocators.PRIORITY)
        ActionChains(self.browser).move_to_element(priority).click(priority).send_keys(n*Keys.DOWN + Keys.ENTER).perform()

        n = random.randint(2, 5)
        client = self.browser.find_element(*CreatePositionModalLocators.CLIENT)
        ActionChains(self.browser).move_to_element(client).click(client).send_keys(n*Keys.DOWN + Keys.ENTER).perform()

        project = self.browser.find_element(*CreatePositionModalLocators.PROJECT)
        ActionChains(self.browser).move_to_element(project).click(project).send_keys(Keys.DOWN + Keys.ENTER).perform()

        orig_loc = self.browser.find_element(*CreatePositionModalLocators.ORIG_LOCATION)
        orig_loc.send_keys(CreatePositionData.orig_loc)
        time.sleep(loading_time)
        orig_loc.send_keys(Keys.ENTER)

        n = random.randint(1, 3)
        remote = self.browser.find_element(*CreatePositionModalLocators.REMOTE_TYPE)
        ActionChains(self.browser).move_to_element(remote).click(remote).send_keys(n*Keys.DOWN + Keys.ENTER).perform()

        _ = self.browser.find_element(*CreatePositionModalLocators.COMMENT).send_keys(CreatePositionData.comment)

        _ = self.browser.find_element(*CreatePositionModalLocators.POS_NAME).send_keys(CreatePositionData.name)

        n = random.randint(1, 20)
        role = self.browser.find_element(*CreatePositionModalLocators.ROLE)
        ActionChains(self.browser).move_to_element(role).click(role).send_keys(n * Keys.DOWN + Keys.ENTER).perform()

        eng = self.browser.find_element(*CreatePositionModalLocators.ENG_LEVEL)
        ActionChains(self.browser).move_to_element(eng).click(eng).send_keys(Keys.DOWN + Keys.ENTER).perform()

        _ = self.browser.find_element(*CreatePositionModalLocators.ADD_ONE_MORE_SKILL).click()

        skill = self.browser.find_element(*CreatePositionModalLocators.SKILL)
        skill.send_keys(CreatePositionData.skill)
        time.sleep(loading_time)
        skill.send_keys(Keys.ENTER)

        n = random.randint(1, 6)
        grade = self.browser.find_element(*CreatePositionModalLocators.GRADE)
        ActionChains(self.browser).move_to_element(grade).click(grade).send_keys(n*Keys.DOWN + Keys.ENTER).perform()

        _ = self.browser.find_element(*CreatePositionModalLocators.NEXT_DETAILS).click()

        """Assigns tab"""
        primary_office = self.browser.find_element(*CreatePositionModalLocators.PRIMARY_OFFICE)
        ActionChains(self.browser).move_to_element(primary_office).click(primary_office).send_keys(Keys.DOWN + Keys.ENTER).perform()
        _ = self.browser.find_element(*CreatePositionModalLocators.ASSIGNS_TAB).click()

        recruiter = self.browser.find_element(*CreatePositionModalLocators.RECRUITERS)
        ActionChains(self.browser).move_to_element(recruiter).click(recruiter).send_keys(Keys.DOWN + Keys.ENTER).perform()

        _ = self.browser.find_element(*CreatePositionModalLocators.NEXT_ASSIGNS).click()

        """Requests tab"""
        _ = self.browser.find_element(*CreatePositionModalLocators.ADD_CR).click()

        engagement_type = [CreatePositionModalLocators.NEW_BUSINESS_RADIO, CreatePositionModalLocators.UPSELL_RADIO]
        _ = self.browser.find_element(*(random.choice(engagement_type))).click()

        billable = self.browser.find_element(*CreatePositionModalLocators.BILLABLE_STAT)
        ActionChains(self.browser).move_to_element(billable).click(billable).send_keys(Keys.DOWN + Keys.ENTER).perform()

        jt = self.browser.find_element(*CreatePositionModalLocators.JOB_TYPE)
        ActionChains(self.browser).move_to_element(jt).click(jt).send_keys(Keys.ENTER).perform()

        # _ = self.browser.find_element(*CreatePositionModalLocators.HOURS).send_keys("8")

        _ = self.browser.find_element(*CreatePositionModalLocators.DEADLINE).send_keys(CreatePositionData.deadline + Keys.ENTER)

        _ = self.browser.find_element(*CreatePositionModalLocators.REQUIRED).send_keys("1")

        _ = self.browser.find_element(*CreatePositionModalLocators.CREATE_POSITION).click()

        print(f"Created Position's title is: {CreatePositionData.name}")
        return CreatePositionData.name  # for checking that position is created and in active tab


