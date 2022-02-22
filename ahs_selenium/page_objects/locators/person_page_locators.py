from selenium.webdriver.common.by import By


class PersonPageLocators:
    NAME = (By.XPATH, "//span[@class='ant-typography sc-pliRl hJMUmJ']")
    PERSON_ROLE = (By.XPATH, "//div[@class='sc-pQdCa itHYSn']/child::span")