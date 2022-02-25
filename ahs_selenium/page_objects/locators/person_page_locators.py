from selenium.webdriver.common.by import By


class PersonPageLocators:
    NAME = (By.XPATH, "//span[@labeltype]/preceding-sibling::span")
    PERSON_TYPE = (By.XPATH, "//span[@labeltype]")
    PERSON_ROLE = (By.XPATH, "//span[@labeltype]/following-sibling::div/span[1]")