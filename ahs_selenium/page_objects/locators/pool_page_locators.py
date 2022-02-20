from selenium.webdriver.common.by import By


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
    FIRST_PERSON_TYPE = (By.CSS_SELECTOR, "#root > section > section > main > div > div:nth-child(2) > div > div > div > div > div > div > table > tbody > tr:nth-child(1) > td.ant-table-cell.ant-table-cell-ellipsis")
    FIRST_PERSON_ROLE = (By.CSS_SELECTOR, "#root > section > section > main > div > div:nth-child(2) > div > div > div > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > div > span.ant-typography.sc-AxgMl.sc-qWfCM.hHzgZA")

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
    F_TYPE_i_LONG_TERM = (By.CSS_SELECTOR, "body > div:nth-child(6) > div > div > div > ul > li:nth-child(1) > label > span > input")
    F_TYPE_i_SHORT_TERM = (By.CSS_SELECTOR, "body > div:nth-child(6) > div > div > div > ul > li:nth-child(2) > label > span > input")
    F_TYPE_i_CONTRACTOR = (By.CSS_SELECTOR, "body > div:nth-child(6) > div > div > div > ul > li:nth-child(3) > label > span > input")
    F_TYPE_i_OK = (By.XPATH, "/html/body/div[2]/div/div/div/div/button[2]")
    F_TYPE_RESET = (By.XPATH, "/html/body/div[2]/div/div/div/div/button[1]")
    F_ROLE_i = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[3]/div/span[2]/span")
    F_ROLE_i_SELECT = (By.CSS_SELECTOR, "#rc_select_0")
    F_ROLE_i_OK = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/button[2]")
    F_ROLE_i_RESET = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/button[1]")
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
