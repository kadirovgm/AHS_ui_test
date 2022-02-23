from selenium.webdriver.common.by import By


class PoolPageLocators:

    # Make sure: 
    # item_i - works only in "Internal" tab
    # item_e - works only in "External" and "Blacklist" tabs
    # item - works on All tabs!

    POOL_TEXT = (By.XPATH, "//b[@class='sc-pZOBi sc-oTNDV jzKNzB']")
    ADD_PERSON = (By.XPATH, "//button[@class='ant-btn sc-pmigq kFqyms']")

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
    FIRST_PERSON_SKILL_e = (By.XPAT, "(//td[3]/div/div/span[1])[1]")
    FIRST_PERSON_CITY_i = (By.XPATH, "(//td[5])[1]")
    FIRST_PERSON_CITY_e = (By.XPATH, "(//td[4])[1]")
    FIRST_PERSON_OFFICE_i = (By.XPATH, "(//td[6])[1]")
    FIRST_PERSON_OFFICE_e = (By.XPATH, "(//td[5])[1]")

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
    F_TYPE_i_RESET = (By.XPATH, "/html/body/div[2]/div/div/div/div/button[1]")
    F_ROLE_i = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[3]/div/span[2]/span")
    F_ROLE_i_SELECT = (By.CSS_SELECTOR, "#rc_select_0")
    F_ROLE_i_OK = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/button[2]")
    F_ROLE_i_RESET = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/button[1]")
    F_SKILLS_i = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[4]/div/span[2]/span")
    F_SKILLS_SELECT = (By.CSS_SELECTOR, "#rc_select_0")
    F_GRADE_SELECT = (By.CSS_SELECTOR, "#rc_select_1")
    F_SKILLS_RESET = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/button[1]")
    F_SKILLS_OK = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/button[2]")
    F_CITY_i = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[5]/div/span[2]/span")
    F_CITY_COUNTRY_SELECT = (By.CSS_SELECTOR, "#rc_select_0")
    F_CITY_CITY_SELECT = (By.CSS_SELECTOR, "#rc_select_1")
    F_CITY_OK = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/button[2]")
    F_CITY_RESET = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/button[1]")
    F_OFFICE_i = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[6]/div/span[2]/span")
    F_OFFICE_SELECT = (By.CSS_SELECTOR, "#rc_select_0")
    F_OFFICE_OK = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/button[2]")
    F_OFFICE_RESET = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/button[1]")
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
    F_ROLE_e_SELECT = (By.CSS_SELECTOR, "#rc_select_0")
    F_ROLE_e_OK = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/button[2]")
    F_ROLE_e_RESET = (By.XPATH, "/html/body/div[3]/div/div/div/div[2]/button[1]")
    F_SKILLS_e = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[3]/div/span[2]/span")
    F_CITY_e = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[4]/div/span[2]/span")
    F_OFFICE_e = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[5]/div/span[2]/span")
    F_ENG_e = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[6]/div/span[2]/span")
    F_VISA_e = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[7]/div/span[2]/span")
    F_HR_e = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[8]/div/span[2]/span")

    CLEAR_FILTERS = (By.CSS_SELECTOR, "#root > section > section > main > div > div:nth-child(1) > div > div:nth-child(2) > button")
