from selenium.webdriver.common.by import By


class BasePageLocators:
    POSITIONS_ICON = (By.XPATH, "//a[@href='/positions/active']")
    POOL_ICON = (By.XPATH, "//a[@href='/pool/internal']")
    CLIENTS_PROJECTS_ICON = (By.XPATH, "//a[@href='/projects/active']")
    REPORTS_ICON = (By.XPATH, "//a[@href='/reports']")
    HELP_CENTER_ICON = (By.XPATH, "//a[@href='/help']")