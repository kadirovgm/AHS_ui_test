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