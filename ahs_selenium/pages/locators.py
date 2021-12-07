from selenium.webdriver.common.by import By


class LoginPageLocators:
    WELCOME_TEXT = (By.CSS_SELECTOR, "#root > div > div > div.ant-card-head > div > div")
    EMAIL = (By.CSS_SELECTOR, "#email")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.XPATH, "/html/body/div/div/div/div[2]/form/div[4]/div/div/div/button/span")
    FORGOT_LINK = (By.CSS_SELECTOR, "#root > div > div > div.ant-card-body > form > div.sc-fzoxnE.GqMIW > a")


class BasePageLocators:
    POSITIONS_ICON = (By.XPATH, "/html/body/div/section/aside/div/div/div[2]/a[1]")
    POOL_ICON = (By.XPATH, "/html/body/div/section/aside/div/div/div[2]/a[2]")
    CLIENTS_PROJECTS_ICON = (By.XPATH, "/html/body/div/section/aside/div/div/div[2]/a[3]")
    REPORTS_ICON = (By.XPATH, "/html/body/div/section/aside/div/div/div[2]/a[4]")
    HELP_CENTER_ICON = (By.CSS_SELECTOR, "#root>section>aside>div>div>a>svg")


class PoolPageLocators:
    POOL_TEXT = (By.CSS_SELECTOR, "#root > section > section > header > div > div > div > b")


