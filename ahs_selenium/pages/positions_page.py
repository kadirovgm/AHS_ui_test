from .base_page import BasePage
from .locators import PositionPageLocators
import time


class PositionsPage(BasePage):
    """Correct Positions page"""
    def should_be_positions_page_text(self):
        assert self.is_element_present(*PositionPageLocators.POSITIONS_TEXT), \
            "Position text doesn't appear!"
        assert self.browser.find_element(*PositionPageLocators.POSITIONS_TEXT).text == \
               "Positions", "Incorrect Positions page!"
    
    """Add position button"""
    def add_position_button_click(self):
        _ = self.browser.find_element(*PositionPageLocators.ADD_POSITION).click()

    """Add new Client Project Position"""
    def add_client_project_position_button_click(self):
        self.add_position_button_click()
        _ = self.browser.find_element(*PositionPageLocators.ADD_CLIENT_PROJECT_POS).click()

    """Add new Internal Project Position"""
    def add_internal_project_position_button_click(self):
        self.add_position_button_click()
        _ = self.browser.find_element(*PositionPageLocators.ADD_INTERNAL_PROJECT_POS).click()

    """Add new Bench Position"""
    def add_bench_position_button_click(self):
        self.add_position_button_click()
        _ = self.browser.find_element(*PositionPageLocators.ADD_BENCH_POS).click()

    """Add new Pre-offer Position"""
    def add_pre_offer_position_button_click(self):
        self.add_position_button_click()
        _ = self.browser.find_element(*PositionPageLocators.ADD_PRE_OFFER_POS).click()
    
    """Add new Trainee Position"""
    def add_trainee_position_button_click(self):
        self.add_position_button_click()
        _ = self.browser.find_element(*PositionPageLocators.ADD_TRAINEE_POS).click()

    """Go to Internal, External, Blacklist tabs"""
    def go_to_active_tab(self):
        _ = self.browser.find_element(*PositionPageLocators.ACTIVE_TAB).click()

    def go_to_mine_tab(self):
        _ = self.browser.find_element(*PositionPageLocators.MINE_TAB).click()

    def go_to_history_tab(self):
        _ = self.browser.find_element(*PositionPageLocators.HISTORY_TAB).click()
