from selenium.webdriver.common.by import By


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