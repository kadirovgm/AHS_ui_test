from .base_page import BasePage
from .locators import PositionPageLocators
import time


class PositionsPage(BasePage):
    def should_be_positions_page_text(self):
        assert self.is_element_present(*PositionPageLocators.POSITIONS_TEXT), \
            "Position text doesn't appear!"
        assert self.browser.find_element(*PositionPageLocators.POSITIONS_TEXT).text == \
               "Positions", "Incorrect Positions page!"
    
    
