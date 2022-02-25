from selenium.webdriver.common.by import By


class PoolPageLocators:

    # Make sure: 
    # item_i - works only in "Internal" tab
    # item_e - works only in "External" and "Blacklist" tabs
    # item - works on All tabs!

    POOL_TEXT = (By.XPATH, "//b[text()='Pool']")
    ADD_PERSON = (By.XPATH, "//span[text()='+ Add person']")

    """Tabs"""
    INTERNAL_TAB = (By.XPATH, "//header/div/div/ul/li[2]")
    EXTERNAL_TAB = (By.XPATH, "//header/div/div/ul/li[4]")
    BLACKLIST_TAB = (By.XPATH, "//header/div/div/ul/li[6]")

    """FIRST PERSON"""
    SEARCH_NAME = (By.XPATH, "//input[@placeholder='Enter name']")
    FIRST_PERSON_NAME = (By.XPATH, "//tr[1]/td[1]/a/div/span")
    FIRST_PERSON = (By.XPATH, "(//td[@class='ant-table-cell'])[1]")
    FIRST_PERSON_LABEL = (By.XPATH, "(//span[@status])[1]")
    FIRST_PERSON_TYPE_i = (By.XPATH, "(//td[@title])[1]")
    FIRST_PERSON_ROLE = (By.XPATH, "(//span[@class='ant-typography sc-AxheI sc-pTUxa clsLqG' and @color='blue'])[1]")
    FIRST_PERSON_SKILL_i = (By.XPATH, "(//td[4]/div/div[1]/span[1])[1]")
    FIRST_PERSON_SKILL_e = (By.XPATH, "(//td[3]/div/div/span[1])[1]")
    FIRST_PERSON_CITY_i = (By.XPATH, "(//td[5])[1]")
    FIRST_PERSON_CITY_e = (By.XPATH, "(//td[4])[1]")
    FIRST_PERSON_OFFICE_i = (By.XPATH, "(//td[6])[1]")
    FIRST_PERSON_OFFICE_e = (By.XPATH, "(//td[5])[1]")

    """Internal fields"""
    NAME = (By.XPATH, "(//span[@class='ant-table-filter-column-title'])[1]")
    TYPE_i = (By.XPATH, "(//span[@class='ant-table-filter-column-title'])[2]")
    ROLE_i = (By.XPATH, "(//span[@class='ant-table-filter-column-title'])[3]")
    SKILLS_i = (By.XPATH, "(//span[@class='ant-table-filter-column-title'])[4]")
    CITY_COUNTRY_i = (By.XPATH, "(//span[@class='ant-table-filter-column-title'])[5]")
    OFFICE_i = (By.XPATH, "(//span[@class='ant-table-filter-column-title'])[6]")
    ENG_LEVEL_i = (By.XPATH, "(//span[@class='ant-table-filter-column-title'])[7]")
    VISA_i = (By.XPATH, "(//span[@class='ant-table-filter-column-title'])[8]")
    ACTIVE_PROJECTS_i = (By.XPATH, "(//span[@class='ant-table-filter-column-title'])[9]")
    HR_i = (By.XPATH, "(//span[@class='ant-table-filter-column-title'])[10]")

    """External fields (Blacklist the same)"""
    ROLE_e = (By.XPATH, "(//span[@class='ant-table-filter-column-title'])[2]")
    SKILLS_e = (By.XPATH, "(//span[@class='ant-table-filter-column-title'])[3]")
    CITY_COUNTRY_e = (By.XPATH, "(//span[@class='ant-table-filter-column-title'])[4]")
    OFFICE_e = (By.XPATH, "(//span[@class='ant-table-filter-column-title'])[5]")
    ENG_LEVEL_e = (By.XPATH, "(//span[@class='ant-table-filter-column-title'])[6]")
    VISA_e = (By.XPATH, "(//span[@class='ant-table-filter-column-title'])[7]")
    HR_e = (By.XPATH, "(//span[@class='ant-table-filter-column-title'])[8]")

    """Internal filters"""
    F_OK = (By.XPATH, "//div[@class='ant-table-filter-dropdown-btns']/button[2]")
    F_RESET = (By.XPATH, "//div[@class='ant-table-filter-dropdown-btns']/button[1]")

    F_LABEL = (By.XPATH, "(//span[@class='ant-table-filter-trigger-container'])[1]")
    F_LABEL_bench = (By.XPATH, "//li[@class='ant-dropdown-menu-item']/child::span[text()='Bench']")
    F_LABEL_pre_offer = (By.XPATH, "//li[@class='ant-dropdown-menu-item']/child::span[text()='Pre-offer']")
    F_LABEL_dismiss = (By.XPATH, "//li[@class='ant-dropdown-menu-item']/child::span[text()='Dismiss']")
    
    F_TYPE_i = (By.XPATH, "(//span[@class='ant-table-filter-trigger-container'])[2]")
    F_TYPE_i_LONG_TERM = (By.XPATH, "(//span[@class='ant-checkbox'])[1]")
    F_TYPE_i_SHORT_TERM = (By.XPATH, "(//span[@class='ant-checkbox'])[2]")
    F_TYPE_i_CONTRACTOR = (By.XPATH, "(//span[@class='ant-checkbox'])[3]")
    
    F_ROLE_i = (By.XPATH, "(//span[@class='ant-table-filter-trigger-container'])[3]")
    F_ROLE_SELECT = (By.CSS_SELECTOR, "#rc_select_0")

    F_SKILLS_i = (By.XPATH, "(//span[@class='ant-table-filter-trigger-container'])[4]")
    F_SKILLS_SELECT = (By.CSS_SELECTOR, "#rc_select_0")
    F_GRADE_SELECT = (By.CSS_SELECTOR, "#rc_select_1")
    
    F_CITY_i = (By.XPATH, "(//span[@class='ant-table-filter-trigger-container'])[5]")
    F_CITY_COUNTRY_SELECT = (By.CSS_SELECTOR, "#rc_select_0")
    F_CITY_CITY_SELECT = (By.CSS_SELECTOR, "#rc_select_1")
    
    F_OFFICE_i = (By.XPATH, "(//span[@class='ant-table-filter-trigger-container'])[6]")
    F_OFFICE_SELECT = (By.CSS_SELECTOR, "#rc_select_0")
    
    F_ENG_i = (By.XPATH, "(//span[@class='ant-table-filter-trigger-container'])[7]")
    F_VISA_i = (By.XPATH, "(//span[@class='ant-table-filter-trigger-container'])[8]")
    F_ACTIVE_I = (By.XPATH, "(//span[@class='ant-table-filter-trigger-container'])[9]")
    F_HR_I = (By.XPATH, "(//span[@class='ant-table-filter-trigger-container'])[10]")

    """External filters (Blacklist the same)"""
    
    F_ROLE_e = (By.XPATH, "(//span[@class='ant-table-filter-trigger-container'])[2]")
    F_SKILLS_e = (By.XPATH, "(//span[@class='ant-table-filter-trigger-container'])[3]")
    F_CITY_e = (By.XPATH, "(//span[@class='ant-table-filter-trigger-container'])[4]")
    F_OFFICE_e = (By.XPATH, "(//span[@class='ant-table-filter-trigger-container'])[5]")
    F_ENG_e = (By.XPATH, "(//span[@class='ant-table-filter-trigger-container'])[6]")
    F_VISA_e = (By.XPATH, "(//span[@class='ant-table-filter-trigger-container'])[7]")
    F_HR_e = (By.XPATH, "(//span[@class='ant-table-filter-trigger-container'])[8]")

    CLEAR_FILTERS = (By.XPATH, "//div[2]/button")
