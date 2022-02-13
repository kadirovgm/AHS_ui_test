from .base_page import BasePage
from .locators.locators import CreatePositionModalLocators
from .randomData.random_data import RandomPositionData
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random


class CreateClientPositionModal(BasePage):
    # TODO
    def should_be_correct_client_position_modal(self):
        ...

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
        orig_loc.send_keys(RandomPositionData.orig_loc)
        time.sleep(loading_time)
        orig_loc.send_keys(Keys.ENTER)

        n = random.randint(1, 3)
        remote = self.browser.find_element(*CreatePositionModalLocators.REMOTE_TYPE)
        ActionChains(self.browser).move_to_element(remote).click(remote).send_keys(n*Keys.DOWN + Keys.ENTER).perform()

        _ = self.browser.find_element(*CreatePositionModalLocators.COMMENT).send_keys(RandomPositionData.comment)

        pos_name = self.browser.find_element(*CreatePositionModalLocators.POS_NAME).send_keys(RandomPositionData.name)

        n = random.randint(1, 20)
        role = self.browser.find_element(*CreatePositionModalLocators.ROLE)
        ActionChains(self.browser).move_to_element(role).click(role).send_keys(n * Keys.DOWN + Keys.ENTER).perform()

        eng = self.browser.find_element(*CreatePositionModalLocators.ENG_LEVEL)
        ActionChains(self.browser).move_to_element(eng).click(eng).send_keys(Keys.DOWN + Keys.ENTER).perform()

        _ = self.browser.find_element(*CreatePositionModalLocators.ADD_ONE_MORE_SKILL).click()

        skill = self.browser.find_element(*CreatePositionModalLocators.SKILL)
        skill.send_keys(RandomPositionData.skill)
        time.sleep(loading_time)
        skill.send_keys(Keys.ENTER)

        n = random.randint(1, 6)
        grade = self.browser.find_element(*CreatePositionModalLocators.GRADE)
        ActionChains(self.browser).move_to_element(grade).click(grade).send_keys(n*Keys.DOWN + Keys.ENTER).perform()

        _ = self.browser.find_element(*CreatePositionModalLocators.NEXT_DETAILS).click()

        """Assigns tab"""
        time.sleep(2)



        return pos_name



