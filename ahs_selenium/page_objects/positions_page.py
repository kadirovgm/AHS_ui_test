from .base_page import BasePage
from .locators.positions_page_locators import PositionPageLocators


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
        self.browser.find_element(*PositionPageLocators.ADD_CLIENT_PROJECT_POS).click()

    """Add new Internal Project Position"""
    def add_internal_project_position_button_click(self):
        self.add_position_button_click()
        self.browser.find_element(*PositionPageLocators.ADD_INTERNAL_PROJECT_POS).click()

    """Add new Bench Position"""
    def add_bench_position_button_click(self):
        self.add_position_button_click()
        self.browser.find_element(*PositionPageLocators.ADD_BENCH_POS).click()

    """Add new Pre-offer Position"""
    def add_pre_offer_position_button_click(self):
        self.add_position_button_click()
        self.browser.find_element(*PositionPageLocators.ADD_PRE_OFFER_POS).click()
    
    """Add new Trainee Position"""
    def add_trainee_position_button_click(self):
        self.add_position_button_click()
        self.browser.find_element(*PositionPageLocators.ADD_TRAINEE_POS).click()

    """Go to Internal, External, Blacklist tabs"""
    def go_to_active_tab(self):
        _ = self.browser.find_element(*PositionPageLocators.ACTIVE_TAB).click()

    def go_to_mine_tab(self):
        _ = self.browser.find_element(*PositionPageLocators.MINE_TAB).click()

    def go_to_history_tab(self):
        _ = self.browser.find_element(*PositionPageLocators.HISTORY_TAB).click()

    """Correct Active"""
    def should_be_correct_fields_active(self):
        active_fields_locator = \
            [PositionPageLocators.NAME_a, PositionPageLocators.CL_PROJ_a, PositionPageLocators.LOC_a,
             PositionPageLocators.OFFICE_a, PositionPageLocators.REQ_CAN_a, PositionPageLocators.DEAD_a,
             PositionPageLocators.STAT_a, PositionPageLocators.HR_a]
        active_fields_text = \
            ["Position name", "Client | Project", "Position location", "Office", "Required | Candidates",
             "Deadline", "Status", "HR’s"]
        self.checking_fields_for_naming(active_fields_locator, active_fields_text)

    def should_be_correct_filters_active(self):
        active_filters_locators = \
            ["F_PRIORITY", "F_TYPE", "F_CLIENT", "F_LOCATION", "F_OFFICE", "S_REQUIRED_UP", "S_REQUIRED_DOWN",
             "S_DEADLINE_UP", "S_DEADLINE_DOWN", "F_STATUS", "F_HRS"]
        active_filters_locators = [eval("PositionPageLocators." + i) for i in active_filters_locators]
        for locator in active_filters_locators:
            assert self.is_element_present(*locator), f"{locator} filter doesn't present!"
            # assert self.is_element_clickable(*locator), f"{locator} filter doesn't clickable!"

    """Correct Mine"""
    # difference from active tab is "HR" tab's absence
    def should_be_correct_fields_mine(self):
        mine_fields_locator = \
            [PositionPageLocators.NAME_a, PositionPageLocators.CL_PROJ_a, PositionPageLocators.LOC_a,
             PositionPageLocators.OFFICE_a, PositionPageLocators.REQ_CAN_a, PositionPageLocators.DEAD_a,
             PositionPageLocators.STAT_a]
        mine_fields_text = \
            ["Position name", "Client | Project", "Position location", "Office", "Required | Candidates",
             "Deadline", "Status"]
        self.checking_fields_for_naming(mine_fields_locator, mine_fields_text)

    def should_be_correct_filters_mine(self):
        mine_filters_locators = \
            ["F_PRIORITY", "F_TYPE", "F_CLIENT", "F_LOCATION", "F_OFFICE", "S_REQUIRED_UP", "S_REQUIRED_DOWN",
             "S_DEADLINE_UP", "S_DEADLINE_DOWN", "F_STATUS"]
        mine_filters_locators = [eval("PositionPageLocators." + i) for i in mine_filters_locators]
        for locator in mine_filters_locators:
            assert self.is_element_present(*locator), f"{locator} filter doesn't present!"
            # assert self.is_element_clickable(*locator), f"{locator} filter doesn't clickable!"

    """Correct History"""
    def should_be_correct_fields_history(self):
        history_fields_locator = \
            [PositionPageLocators.NAME_a, PositionPageLocators.CL_PROJ_a, PositionPageLocators.CREATE_DATE,
             PositionPageLocators.FINISH_DATE, PositionPageLocators.LOC_h, PositionPageLocators.REASON,
             PositionPageLocators.STAT_a, PositionPageLocators.HR_a]
        history_fields_text = \
            ["Position name", "Client | Project", "Creation Date", "Finish Date", "Position location",
             "Reason", "Status", "HR’s"]
        self.checking_fields_for_naming(history_fields_locator, history_fields_text)

    def should_be_correct_filters_history(self):
        active_filters_locators = \
            ["F_PRIORITY", "F_TYPE", "F_CLIENT", "S_CREATE_DATE_UP", "S_CREATE_DATE_DOWN", "S_FINISH_DATE_UP", "S_FINISH_DATE_DOWN", "F_LOCATION_h", "F_STATUS", "F_HRS"]
        active_filters_locators = [eval("PositionPageLocators." + i) for i in active_filters_locators]
        for locator in active_filters_locators:
            assert self.is_element_present(*locator), f"{locator} filter doesn't present!"
            # assert self.is_element_clickable(*locator), f"{locator} filter doesn't clickable!"

    """*Searching in positions page*"""
    def search_for_position(self, position_name):
        print(f"Searching for {position_name} in Positions page")
        if self.waiting_for_element_present(*PositionPageLocators.FIRST_POSITION):
            _ = self.browser.find_element(*PositionPageLocators.SEARCH).send_keys(position_name)
            if self.waiting_for_element_present(*PositionPageLocators.FIRST_POSITION):
                assert self.browser.find_element(
                    *PositionPageLocators.FIRST_POSITION_TITLE).text == position_name, \
                    "The results don't match the search! Searching does not work!"
            else:
                raise AssertionError("Page hasn't loaded or there is no such position")
        else:
            raise AssertionError("There is no Position suitable for search!")

    # TODO improve for checking by pos_number
    """Checking status of position"""
    def checking_status_of_position(self, status, pos_number=1):
        print(f"Checking that Position's status = {status}")
        if self.is_element_present(*PositionPageLocators.FIRST_POSITION):
            assert self.browser.find_element(*PositionPageLocators.FIRST_STATUS).text == status, \
                f"Status of position is not {status}"
        else:
            raise AssertionError("There is no Position in list!")
