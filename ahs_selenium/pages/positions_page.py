from .base_page import BasePage
from .locators.locators import PositionPageLocators


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

    """Correct Active/Mine/History"""
    def should_be_correct_fields_active(self):
        active_fields_locator = \
            [PositionPageLocators.NAME_a, PositionPageLocators.CL_PROJ_a, PositionPageLocators.LOC_a,
             PositionPageLocators.OFFICE_a, PositionPageLocators.REQ_CAN_a, PositionPageLocators.DEAD_a,
             PositionPageLocators.STAT_a, PositionPageLocators.HR_a]
        active_fields_text = \
            ["Position name", "Client | Project", "Position location", "Office", "Required | Candidates",
             "Deadline", "Status", "HR’s"]
        self.checking_fields(active_fields_locator, active_fields_text)

    # difference from active tab is "HR" tab's absence
    def should_be_correct_fields_mine(self):
        mine_fields_locator = \
            [PositionPageLocators.NAME_a, PositionPageLocators.CL_PROJ_a, PositionPageLocators.LOC_a,
             PositionPageLocators.OFFICE_a, PositionPageLocators.REQ_CAN_a, PositionPageLocators.DEAD_a,
             PositionPageLocators.STAT_a]
        mine_fields_text = \
            ["Position name", "Client | Project", "Position location", "Office", "Required | Candidates",
             "Deadline", "Status"]
        self.checking_fields(mine_fields_locator, mine_fields_text)

    def should_be_correct_fields_history(self):
        history_fields_locator = \
            [PositionPageLocators.NAME_a, PositionPageLocators.CL_PROJ_a, PositionPageLocators.CREATE_DATE,
             PositionPageLocators.FINISH_DATE, PositionPageLocators.LOC_h, PositionPageLocators.REASON,
             PositionPageLocators.STAT_a, PositionPageLocators.HR_a]
        history_fields_text = \
            ["Position name", "Client | Project", "Creation Date", "Finish Date", "Position location",
             "Reason", "Status", "HR’s"]
        self.checking_fields(history_fields_locator, history_fields_text)
