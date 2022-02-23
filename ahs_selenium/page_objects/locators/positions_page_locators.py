from selenium.webdriver.common.by import By


class PositionPageLocators:
    """'Positions' text"""
    POSITIONS_TEXT = (By.XPATH, "//b[text()='Positions']")
    """Searching"""
    SEARCH = (By.XPATH, "//input[@placeholder='Enter position' and @type='text']")

    """First position"""
    FIRST_POSITION = (By.XPATH, "//tr[@class='ant-table-row ant-table-row-level-0'][1]")
    FIRST_POSITION_TITLE = (By.XPATH, "//tr[1]/td[2]/div/span[1]")
    FIRST_STATUS = (By.XPATH, "//tr[1]/td[8]/span/span[1]")

    """Add position"""
    ADD_POSITION = (By.XPATH, "//button[@class='ant-btn sc-pmigq kFqyms ant-dropdown-trigger']")
    ADD_CLIENT_PROJECT_POS = (By.XPATH, "//li[@class='ant-dropdown-menu-item'][1]")
    ADD_INTERNAL_PROJECT_POS = (By.XPATH, "//li[@class='ant-dropdown-menu-item'][2]")
    ADD_BENCH_POS = (By.XPATH, "//li[@class='ant-dropdown-menu-item'][3]")
    ADD_PRE_OFFER_POS = (By.XPATH, "//li[@class='ant-dropdown-menu-item'][4]")
    ADD_TRAINEE_POS = (By.XPATH, "//li[@class='ant-dropdown-menu-item'][5]")

    """TABS"""
    ACTIVE_TAB = (By.XPATH, "//header/div/div/ul/li[2]")
    MINE_TAB = (By.XPATH, "//header/div/div/ul/li[4]")
    HISTORY_TAB = (By.XPATH, "//header/div/div/ul/li[6]")

    """Active/Mine tab fields"""
    NAME_a = (By.XPATH, "//th[2]/div/span[1]")
    CL_PROJ_a = (By.XPATH, "//th[3]/div/span[1]")
    LOC_a = (By.XPATH, "//th[4]/div/span[1]")
    OFFICE_a = (By.XPATH, "//th[5]/div/span[1]")
    REQ_CAN_a = (By.XPATH, "//th[6]/div/span[1]")
    DEAD_a = (By.XPATH, "//th[7]/div/div")
    STAT_a = (By.XPATH, "//th[8]/div/span[1]")
    HR_a = (By.XPATH, "//th[9]/div/span[1]")

    """History tab fields"""
    CREATE_DATE = (By.XPATH, "//th[4]/div/div")
    FINISH_DATE = (By.XPATH, "//th[5]/div/div")
    LOC_h = (By.XPATH, "//th[6]/div/span[1]")
    REASON = (By.XPATH, "//th[7]")

    """Active/Mine tab filters"""
    F_PRIORITY = (By.XPATH, "//th[@id='priority']/descendant::span[@role='button']")
    F_TYPE = (By.XPATH, "//th[2]/div/span[2]/span")
    F_CLIENT = (By.XPATH, "//th[3]/div/span[2]/span")
    F_LOCATION = (By.XPATH, "//th[4]/div/span[2]/span")
    F_OFFICE = (By.XPATH, "//th[5]/div/span[2]/span")
    S_REQUIRED_UP = (By.XPATH, "//span[@class='anticon anticon-caret-up']")
    S_REQUIRED_DOWN = (By.XPATH, "//span[@class='anticon anticon-caret-down']")
    S_DEADLINE_UP = (By.XPATH, "//span[@class='anticon anticon-caret-up ant-table-column-sorter-up']")
    S_DEADLINE_DOWN = (By.XPATH, "//span[@class='anticon anticon-caret-down ant-table-column-sorter-down']")
    F_STATUS = (By.XPATH, "//th[8]/div/span[2]/span")
    F_HRS = (By.XPATH, "//th[9]/div/span[2]/span")

    """History tab filters"""
    S_CREATE_DATE_UP = (By.XPATH, "(//span[@class='anticon anticon-caret-up ant-table-column-sorter-up'])[1]")
    S_CREATE_DATE_DOWN = (By.XPATH, "(//span[@class='anticon anticon-caret-down ant-table-column-sorter-down'])[1]")
    S_FINISH_DATE_UP = (By.XPATH, "(//span[@class='anticon anticon-caret-up ant-table-column-sorter-up'])[2]")
    S_FINISH_DATE_DOWN = (By.XPATH, "(//span[@class='anticon anticon-caret-down ant-table-column-sorter-down'])[2]")
    F_LOCATION_h = (By.XPATH, "//tr/th[6]/div/span[2]/span")
