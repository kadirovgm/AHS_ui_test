from selenium.webdriver.common.by import By


class PositionPageLocators:
    """'Positions' text"""
    POSITIONS_TEXT = (By.CSS_SELECTOR, "#root > section > section > header > div > div > div > b")
    """Searching"""
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
