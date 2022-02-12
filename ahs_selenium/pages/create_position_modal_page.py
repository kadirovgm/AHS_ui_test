from .base_page import BasePage
from .locators.locators import CreatePositionModalLocators
from .randomData.random_data import RandomPersonData
from selenium.webdriver.common.keys import Keys
import time


class CreateClientPositionModal(BasePage):
    # TODO
    def should_be_correct_client_position_modal(self):
        ...

    def add_new_client_project_position(self, loading_time):
        print(f"Adding a new client project position")


