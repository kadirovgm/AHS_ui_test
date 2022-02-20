from selenium.webdriver.common.by import By

class CreatePositionModalLocators:
    NEW_PROJ_POSITION_TEXT = (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[1]/div")

    """tabs"""
    POS_DETAIL_TAB = (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/form/div/div[1]/div[1]/div/div[1]")
    ASSIGNS_TAB = (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/form/div/div[1]/div[1]/div/div[2]")
    REQUESTS_TAB = (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/form/div/div[1]/div[1]/div/div[3]")

    """Position details tab"""
    UNCONFIRMED_RADIO = (By.CSS_SELECTOR, "#is_confirmed > label:nth-child(1) > span.ant-radio")
    CONFIRMED_RADIO = (By.CSS_SELECTOR, "#is_confirmed > label:nth-child(2) > span.ant-radio")
    PRIORITY = (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/form/div/div[2]/div/div[1]/section[1]/div[2]/div[1]/div/div[2]/div/div/div/div/span[1]")
    CLIENT = (By.CSS_SELECTOR, "#client")
    PROJECT = (By.CSS_SELECTOR, "#project")
    ORIG_LOCATION = (By.CSS_SELECTOR, "#origin_location_country")
    REMOTE_TYPE = (By.CSS_SELECTOR, "#remote_types")
    COMMENT = (By.CSS_SELECTOR, "#comment")
    POS_NAME = (By.CSS_SELECTOR, "#title")
    ROLE = (By.CSS_SELECTOR, "#role")
    ENG_LEVEL = (By.CSS_SELECTOR, "#english_level")
    ADD_ONE_MORE_SKILL = (By.CSS_SELECTOR, "#rc-tabs-0-panel-details > section:nth-child(3) > section > div > div.ant-col.ant-form-item-control > div > div > div > div > div > div > button")
    SKILL = (By.CSS_SELECTOR, "#skills_0_skill")
    GRADE = (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/form/div/div[2]/div/div[1]/section[3]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/div/span[1]/input")

    """Assigns tab"""
    PRIMARY_OFFICE = (By.CSS_SELECTOR, "#primary_offices")
    OTHER_OFFICE = (By.CSS_SELECTOR, "#other_offices")
    ALL_OFFICES_CHECK = (By.CSS_SELECTOR, "#all_offices")
    RECRUITERS = (By.CSS_SELECTOR, "#recruiters")

    """Requests tab"""
    ADD_CR = (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/form/div/div[2]/div/div[3]/section/div/div/div/div/div/div/button")
    NEW_BUSINESS_RADIO = (By.CSS_SELECTOR, "#candidate_requests_0_engagement_type > label:nth-child(1) > span.ant-radio > input")
    UPSELL_RADIO = (By.CSS_SELECTOR, "#candidate_requests_0_engagement_type > label:nth-child(2) > span.ant-radio > input")
    BILLABLE_STAT = (By.CSS_SELECTOR, "#candidate_requests_0_billable_status")
    JOB_TYPE = (By.CSS_SELECTOR, "#candidate_requests_0_job_type")
    HOURS = (By.CSS_SELECTOR, "#candidate_requests_0_hours_per_day")
    DEADLINE = (By.CSS_SELECTOR, "#candidate_requests_0_deadline")
    REQUIRED = (By.CSS_SELECTOR, "#candidate_requests_0_required")

    """buttons"""
    CANCEL = (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/form/div/div[2]/div/div[1]/div/div[1]/button")
    NEXT_DETAILS = (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/form/div/div[2]/div/div[1]/div/div[2]/button")
    NEXT_ASSIGNS = (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/form/div/div[2]/div/div[2]/section/div[4]/div[2]/button")
    SUBMIT = (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/form/div/div[2]/div/div[3]/div/div[2]/button")
