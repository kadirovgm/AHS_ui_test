from selenium.webdriver.common.by import By


class BasePageLocators:
    POSITIONS_ICON = (By.XPATH, "/html/body/div/section/aside/div/div/div[2]/a[1]")
    POOL_ICON = (By.XPATH, "/html/body/div/section/aside/div/div/div[2]/a[2]")
    CLIENTS_PROJECTS_ICON = (By.XPATH, "/html/body/div/section/aside/div/div/div[2]/a[3]")
    REPORTS_ICON = (By.XPATH, "/html/body/div/section/aside/div/div/div[2]/a[4]")
    HELP_CENTER_ICON = (By.CSS_SELECTOR, "#root>section>aside>div>div>a>svg")