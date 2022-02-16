from selenium.webdriver.common.by import By


class LoginPageLocators:
    WELCOME_TEXT = (By.CSS_SELECTOR, "#root > div > div > div.ant-card-head > div > div")
    EMAIL = (By.CSS_SELECTOR, "#email")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.XPATH, "/html/body/div/div/div/div[2]/div/div/form/button")
    FORGOT_LINK = (By.XPATH, "/html/body/div/div/div/div[2]/div/div/form/div[2]/div[2]/div/div/button")


class ResetPageLocators:
    RESET_TEXT = (By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div")
    EMAIL = (By.CSS_SELECTOR, "#email")
    SEND_BUTTON = (By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/form/div[2]/button")
    GO_BACK_TO_LOGIN = (By.XPATH, "/html/body/div/div/div/div[2]/div/div/div[2]/button")


class BasePageLocators:
    POSITIONS_ICON = (By.XPATH, "/html/body/div/section/aside/div/div/div[2]/a[1]")
    POOL_ICON = (By.XPATH, "/html/body/div/section/aside/div/div/div[2]/a[2]")
    CLIENTS_PROJECTS_ICON = (By.XPATH, "/html/body/div/section/aside/div/div/div[2]/a[3]")
    REPORTS_ICON = (By.XPATH, "/html/body/div/section/aside/div/div/div[2]/a[4]")
    HELP_CENTER_ICON = (By.CSS_SELECTOR, "#root>section>aside>div>div>a>svg")


# Position page
class PositionPageLocators:
    """Add position buttons"""
    POSITIONS_TEXT = (By.CSS_SELECTOR, "#root > section > section > header > div > div > div > b")
    SEARCH = (By.XPATH, "/html/body/div[1]/section/section/main/div[1]/div[1]/div/div[1]/span/input")

    """Add position"""
    ADD_POSITION = (By.CSS_SELECTOR, "#root > section > section > header > div > div > div > button")
    ADD_CLIENT_PROJECT_POS = (By.XPATH, "/html/body/div[2]/div/div/ul/li[1]")
    ADD_INTERNAL_PROJECT_POS = (By.XPATH, "/html/body/div[6]/div/div/ul/li[2]")
    ADD_BENCH_POS = (By.XPATH, "/html/body/div[6]/div/div/ul/li[3]")
    ADD_PRE_OFFER_POS = (By.XPATH, "/html/body/div[6]/div/div/ul/li[4]")
    ADD_TRAINEE_POS = (By.XPATH, "/html/body/div[6]/div/div/ul/li[5]")

    """TABS"""
    ACTIVE_TAB = (By.XPATH, "/html/body/div[1]/section/section/header/div/div/ul/li[2]")
    MINE_TAB = (By.XPATH, "/html/body/div[1]/section/section/header/div/div/ul/li[4]")
    HISTORY_TAB = (By.XPATH, "/html/body/div[1]/section/section/header/div/div/ul/li[6]")

    """Active/Mine tab fields"""
    NAME_a = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div/div/div/div/table/thead/tr/th[2]/div/span[1]")
    CL_PROJ_a = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div/div/div/div/table/thead/tr/th[3]/div/span[1]")
    LOC_a = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div/div/div/div/table/thead/tr/th[4]/div/span[1]")
    OFFICE_a = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div/div/div/div/table/thead/tr/th[5]/div/span[1]")
    REQ_CAN_a = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div/div/div/div/table/thead/tr/th[6]/div/span[1]")
    DEAD_a = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div/div/div/div/table/thead/tr/th[7]/div/div")
    STAT_a = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div/div/div/div/table/thead/tr/th[8]/div/span[1]")
    HR_a = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div/div/div/div/table/thead/tr/th[9]/div/span[1]")

    FIRST_POSITION = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div/div/div/div/table/tbody/tr[1]")
    FIRST_POSITION_TITLE = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[2]/div/span[1]")
    FIRST_STATUS = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[8]/span/span")

    """Active/Mine tab filters"""
    F_PRIORITY = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div/div/div/div/table/thead/tr/th[1]/div/span[2]/span")
    F_TYPE = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div/div/div/div/table/thead/tr/th[2]/div/span[2]/span")
    F_CLIENT = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div/div/div/div/table/thead/tr/th[3]/div/span[2]/span")
    F_LOCATION = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div/div/div/div/table/thead/tr/th[4]/div/span[2]/span")
    F_OFFICE = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div/div/div/div/table/thead/tr/th[5]/div/span[2]/span")
    S_REQUIRED = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div/div/div/div/table/thead/tr/th[6]/div/span[2]/span")
    S_DEADLINE = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div/div/div/div/table/thead/tr/th[7]/div/div")
    F_STATUS = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div/div/div/div/table/thead/tr/th[8]/div/span[2]/span")
    F_HRS = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div/div/div/div/table/thead/tr/th[9]/div/span[2]/span")

    """History tab"""
    CREATE_DATE = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div"
                             "/div/div/div/table/thead/tr/th[4]/div/div")
    FINISH_DATE = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div"
                             "/div/div/div/div/table/thead/tr/th[5]/div/div")
    LOC_h = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div"
                       "/div/div/div/table/thead/tr/th[6]/div/span[1]")
    REASON = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div/div/div/div/table/thead/tr/th[7]")

    """History tab filters"""
    S_CREATE_DATE = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div/div/div/div/table/thead/tr/th[4]/div/div/span[2]")
    S_FINISH_DATE = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div/div/div/div/table/thead/tr/th[5]/div/div/span[2]")
    F_LOCATION_h = (By.XPATH, "/html/body/div[1]/section/section/main/div[2]/div/div/div/div/div/div/table/thead/tr/th[6]/div/span[2]/span")


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
    ADD_ONE_MORE_SKILL = (By.CSS_SELECTOR, "#rc-tabs-0-panel-details > section:nth-child(2) > section > div > div.ant-col.ant-form-item-control > div > div > div > div > div > div > button")
    SKILL = (By.CSS_SELECTOR, "#rc_select_7")
    GRADE = (By.CSS_SELECTOR, "#rc_select_8")

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


# Pool page
class PoolPageLocators:
    POOL_TEXT = (By.CSS_SELECTOR, "#root > section > section > header > div > div > div > b")
    ADD_PERSON = (By.CSS_SELECTOR, "#root > section > section > header > div > div > div > button")

    INTERNAL_TAB = (By.CSS_SELECTOR, "#root > section > section > header > div > div > ul > li:nth-child(2)")
    EXTERNAL_TAB = (By.CSS_SELECTOR, "#root > section > section > header > div > div > ul > li:nth-child(4)")
    BLACKLIST_TAB = (By.CSS_SELECTOR, "#root > section > section > header > div > div > ul > li:nth-child(6)")

    """FIRST PERSON"""
    SEARCH_NAME = (By.XPATH, "/html/body/div/section/section/main/div/div[1]/div/div[1]/div/div[1]/span/input")
    FIRST_PERSON_NAME = (By.XPATH, "/html/body/div/section/section/main/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/a/div/span")
    FIRST_PERSON = (By.XPATH, "/html/body/div/section/section/main/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[1]")
    FIRST_PERSON_LABEL = (By.CSS_SELECTOR, "#root > section > section > main > div > div:nth-child(2) > div > div > div > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > a > div > div > span")

    """Internal fields"""
    NAME_i = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[1]/div/span[1]")
    TYPE_i = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[2]/div/span[1]")
    ROLE_i = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[3]/div/span[1]")
    SKILLS_i = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[4]/div/span[1]")
    CITY_COUNTRY_i = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[5]/div/span[1]")
    OFFICE_i = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[6]/div/span[1]")
    ENG_LEVEL_i = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[7]/div/span[1]")
    VISA_i = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[8]/div/span[1]")
    ACTIVE_PROJECTS_i = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[9]/div/span[1]")
    HR_i = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[10]/div/span[1]")

    """Internal filters"""
    F_LABEL = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[1]/div/span[2]/span")
    F_LABEL_i_bench = (By.CSS_SELECTOR, "body > div:nth-child(6) > div > div > div > ul > li")
    F_LABEL_OK = (By.CSS_SELECTOR, "body > div:nth-child(6) > div > div > div > div > button.ant-btn.ant-btn-primary.ant-btn-sm")
    F_LABEL_RESET = (By.XPATH, "/html/body/div[2]/div/div/div/div/button[1]")
    F_TYPE_i = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[2]/div/span[2]/span")
    F_TYPE_i_LONG_TERM = (By.XPATH, "/html/body/div[4]/div/div/div/ul/li[1]")
    F_TYPE_i_SHORT_TERM = (By.CSS_SELECTOR, "body > div:nth-child(8) > div > div > div > ul > li:nth-child(2)")
    F_TYPE_i_CONTRACTOR = (By.CSS_SELECTOR, "body > div:nth-child(8) > div > div > div > ul > li:nth-child(3)")
    F_TYPE_i_OK = (By.CSS_SELECTOR, "body > div:nth-child(8) > div > div > div > div > button.ant-btn.ant-btn-primary.ant-btn-sm")
    F_ROLE_i = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[3]/div/span[2]/span")
    F_SKILLS_i = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[4]/div/span[2]/span")
    F_CITY_i = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[5]/div/span[2]/span")
    F_OFFICE_i = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[6]/div/span[2]/span")
    F_ENG_i = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[7]/div/span[2]/span")
    F_VISA_i = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[8]/div/span[2]/span")
    F_ACTIVE_I = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[9]/div/span[2]/span")
    F_HR_I = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[10]/div/span[2]/span")

    """External fields (Blacklist the same)"""
    NAME_e = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[1]/div/span[1]")
    ROLE_e = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[2]/div/span[1]")
    SKILLS_e = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[3]/div/span[1]")
    CITY_COUNTRY_e = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[4]/div/span[1]")
    OFFICE_e = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[5]/div/span[1]")
    ENG_LEVEL_e = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[6]/div/span[1]")
    VISA_e = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[7]/div/span[1]")
    HR_e = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[8]/div/span[1]")

    """External filters (Blacklist the same)"""
    F_LABEL_e = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[1]/div/span[2]/span")
    F_LABEL_e_PRE_OFFER = (By.CSS_SELECTOR, "body > div:nth-child(6) > div > div > div > ul > li:nth-child(1)")
    F_LABEL_e_Dismiss = (By.CSS_SELECTOR, "body > div:nth-child(6) > div > div > div > ul > li:nth-child(2)")
    F_LABEL_b_Dismiss = (By.CSS_SELECTOR, "body > div:nth-child(6) > div > div > div > ul > li:nth-child(1)")
    F_ROLE_e = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[2]/div/span[2]/span")
    F_SKILLS_e = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[3]/div/span[2]/span")
    F_CITY_e = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[4]/div/span[2]/span")
    F_OFFICE_e = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[5]/div/span[2]/span")
    F_ENG_e = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[6]/div/span[2]/span")
    F_VISA_e = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[7]/div/span[2]/span")
    F_HR_e = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[8]/div/span[2]/span")

    CLEAR_FILTERS = (By.CSS_SELECTOR, "#root > section > section > main > div > div:nth-child(1) > div > div:nth-child(2) > button")



class PersonPageLocators:
    NAME = (By.XPATH, "/html/body/div/section/section/div/div/main/div[2]/div[1]/div/div/div/div[1]/div/div/span[1]")


# Create person
class CreatePersonModalLocators:

    CREATE_NEW_PERSON_TEXT = (By.CSS_SELECTOR, "#rcDialogTitle0")
    UPLOAD_PHOTO = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]"
                              "/form/div/div[1]/div[1]/div/div/div/div/span/div/span/input")
    UPLOAD_OTHER_CV = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[1]/div[2]"
                                 "/div[2]/div/div/div/span/div/span/button")
    ENTER_AKVELON_CV = (By.CSS_SELECTOR, "#akvelon_cv")
    FIRST_NAME = (By.CSS_SELECTOR, "#first_name")
    LAST_NAME = (By.CSS_SELECTOR, "#last_name")
    MIDDLE_NAME = (By.CSS_SELECTOR, "#middle_name")
    RECRUITER = (By.CSS_SELECTOR, "#assigned_hr")
    ROLES = (By.CSS_SELECTOR, "#roles")
    OFFICE = (By.CSS_SELECTOR, "#office")
    COUNTRY = (By.CSS_SELECTOR, "#country-select-default")
    CITY = (By.CSS_SELECTOR, "#city-select-default")
    CONTEXT_COMMENT = (By.CSS_SELECTOR, "#comment")
    SALARY_TEXT = (By.CSS_SELECTOR, "#PersonForm > div > div:nth-child(2) > section:nth-child(2) > h2 > div > span")
    SALARY_ICON = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div"
                                    "/div[2]/section[2]/h2/div/button")
    FULL_SALARY = (By.CSS_SELECTOR, "#salaryInfoSalaryAmount")
    BENCH_SALARY = (By.CSS_SELECTOR, "#salaryInfoBenchSalaryAmount")
    SALARY_COMMENT = (By.CSS_SELECTOR, "#salaryInfoComment")
    ENGLISH_LEVEL = (By.CSS_SELECTOR, "#english_level")
    ENGLISH_COMMENT = (By.CSS_SELECTOR, "#english_comment")
    PRIMARY_SKILL = (By.CSS_SELECTOR, "#rc_select_5")
    PRIMARY_SKILL_GRADE = (By.CSS_SELECTOR, "#rc_select_6")
    CONFIRMED_SKILL_CHECKBOX = (By.CSS_SELECTOR, "#primary_skills_0_is_confirmed")
    ADD_PRIMARY_SKILL = (By.CSS_SELECTOR, "#PersonForm > div > div:nth-child(2) > section:nth-child(4) > "
                                          "div:nth-child(2) > div.ant-col.ant-form-item-control > div > div > button")
    OTHER_SKILL = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[2]/section[4]"
                             "/div[2]/div[2]/div/div/div/div/div")
    RESIDENCE_COUNTRY = (By.CSS_SELECTOR, "#residence-country-select")
    RESIDENCE_TYPE = (By.CSS_SELECTOR, "#residence-type-select")
    ADD_RESIDENCE = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[2]"
                               "/section[5]/div[1]/div/div[2]/div/div/div/button")
    WANT_RELOCATE = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[2]/section[5]"
                               "/div[2]/div[1]/div/div[2]/div/div/div/div")
    WANT_RELOCATE_COMMENT = (By.CSS_SELECTOR, "#relocation_comment")
    ADD_ONE_MORE_CONTACT = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[2]/section[6]/div/div/button")
    CONTACT_TYPE = (By.CSS_SELECTOR, "#contacts_0_contact_type")
    CONTACT_VALUE = (By.CSS_SELECTOR, "#contacts_0_value")

    CREATE_PERSON_BUTTON = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]")
    CANCEL_CREATE_PERSON_BUTTON = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[1]")

    CROSS_EXIT = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/button")


# Clients&Projects page
class ClientsProjectsPageLocators:
    CLIENTS_PROJECTS_TEXT = (By.CSS_SELECTOR, "#root > section > section > header > div > div > div > b")


# Reports page
class ReportsPageLocators:
    REPORTS_TEXT = (By.CSS_SELECTOR, "#root > section > section > header > div > div > div > b")


# Help center
class HelpCenterLocators:
    HELP_CENTER_TEXT = (By.CSS_SELECTOR, "#root > section > section > aside > div > h5")

