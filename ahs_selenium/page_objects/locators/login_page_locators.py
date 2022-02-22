from selenium.webdriver.common.by import By


class LoginPageLocators:
    WELCOME_TEXT = (By.XPATH, "//div[@class='ant-card-head-title']")
    EMAIL = (By.CSS_SELECTOR, "#email")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    FORGOT_LINK = (By.XPATH, "//span[text()='Forgot password?']")


class ResetPageLocators:
    RESET_TEXT = (By.XPATH, "//div[@class='ant-card-head-title']")
    EMAIL = (By.CSS_SELECTOR, "#email")
    SEND_BUTTON = (By.XPATH, "//button[@type='submit']")
    GO_BACK_TO_LOGIN = (By.XPATH, "//span[text()='Back to Log In']")