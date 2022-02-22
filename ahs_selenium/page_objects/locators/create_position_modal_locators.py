from selenium.webdriver.common.by import By

class CreatePositionModalLocators:
    NEW_PROJ_POSITION_TEXT = (By.CSS_SELECTOR, "#rcDialogTitle0")

    """tabs"""
    POS_DETAIL_TAB = (By.XPATH, "//form/div/div[1]/div[1]/div/div[1]")
    ASSIGNS_TAB = (By.XPATH, "//form/div/div[1]/div[1]/div/div[2]")
    REQUESTS_TAB = (By.XPATH, "//form/div/div[1]/div[1]/div/div[3]")

    """Position details tab"""
    UNCONFIRMED_RADIO = (By.CSS_SELECTOR, "#is_confirmed > label:nth-child(1) > span.ant-radio")
    CONFIRMED_RADIO = (By.CSS_SELECTOR, "#is_confirmed > label:nth-child(2) > span.ant-radio")
    PRIORITY = (By.CSS_SELECTOR, "#priority")
    CLIENT = (By.CSS_SELECTOR, "#client")
    PROJECT = (By.CSS_SELECTOR, "#project")
    ORIG_LOCATION = (By.CSS_SELECTOR, "#origin_location_country")
    REMOTE_TYPE = (By.CSS_SELECTOR, "#remote_types")
    COMMENT = (By.CSS_SELECTOR, "#comment")
    POS_NAME = (By.CSS_SELECTOR, "#title")
    ROLE = (By.CSS_SELECTOR, "#role")
    ENG_LEVEL = (By.CSS_SELECTOR, "#english_level")
    ADD_ONE_MORE_SKILL = (By.XPATH, "//span[text()='+ Add one more skill']")
    SKILL = (By.CSS_SELECTOR, "#skills_0_skill")
    GRADE = (By.CSS_SELECTOR, "#rc_select_10")

    """Assigns tab"""
    PRIMARY_OFFICE = (By.CSS_SELECTOR, "#primary_offices")
    OTHER_OFFICE = (By.CSS_SELECTOR, "#other_offices")
    ALL_OFFICES_CHECK = (By.CSS_SELECTOR, "#all_offices")
    RECRUITERS = (By.CSS_SELECTOR, "#recruiters")

    """Requests tab"""
    ADD_CR = (By.XPATH, "//span[text()='+ Add candidate request']")
    NEW_BUSINESS_RADIO = (By.XPATH, "(//input[@type='radio' and @value='new_business'])[last()]")                 # every time select from last CR
    UPSELL_RADIO = (By.XPATH, "(//input[@type='radio' and @value='upsell'])[last()]")
    BILLABLE_STAT = (By.CSS_SELECTOR, "#candidate_requests_0_billable_status")
    JOB_TYPE = (By.CSS_SELECTOR, "#candidate_requests_0_job_type")
    HOURS = (By.CSS_SELECTOR, "#candidate_requests_0_hours_per_day")
    DEADLINE = (By.CSS_SELECTOR, "#candidate_requests_0_deadline")
    REQUIRED = (By.CSS_SELECTOR, "#candidate_requests_0_required")

    """buttons"""
    CANCEL_DETAILS = (By.CSS_SELECTOR, "#rc-tabs-0-panel-details > div > div:nth-child(1) > button")
    NEXT_DETAILS = (By.CSS_SELECTOR, "#rc-tabs-0-panel-details > div > div:nth-child(2) > button")

    NEXT_ASSIGNS = (By.CSS_SELECTOR, "#rc-tabs-0-panel-assigns > section > div.ant-row.ant-row-end > div:nth-child(2) > button")
    CANCEL_ASSIGNS = (By.CSS_SELECTOR, "#rc-tabs-0-panel-assigns > section > div.ant-row.ant-row-end > div:nth-child(1) > button")

    CANCEL_REQUESTS = (By.CSS_SELECTOR, "#rc-tabs-0-panel-requests > div > div.ant-col.ant-col-3 > button")
    CREATE_POSITION = (By.CSS_SELECTOR, "#rc-tabs-0-panel-requests > div > div.ant-col.ant-col-4 > button")
