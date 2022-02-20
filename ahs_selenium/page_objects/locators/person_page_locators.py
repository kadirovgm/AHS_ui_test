from selenium.webdriver.common.by import By


class PersonPageLocators:
    NAME = (By.XPATH, "/html/body/div/section/section/div/div/main/div[2]/div[1]/div/div/div/div[1]/div/div/span[1]")
    PERSON_ROLE = (By.XPATH, "/html/body/div/section/section/div/div/main/div[2]/div[1]/div/div/div/div[1]/div/div/div/span")