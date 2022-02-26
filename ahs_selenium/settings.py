import os
from page_objects.login_page import LoginPage
from selenium.webdriver.chrome.service import Service
from page_objects.FixtureData.fixture_users import *


class Execute:
    def __init__(self):
        self.default_browser = "chrome"          # variants: chrome, firefox
        self.operation_system = "win"            # variants: mac, win
        self.user = "head"                       # variants: head, lead, recruiter
        self.env = "137"                         # variants: 122 (Stage), 137 (QA-137), 139 (QA-139), 152 (Demo), 115 (Production)
        self.loading_time = 1                    # time for loading huge data (depends on internet connection, default=0.7)
        self.language = None                     # language - in feature


"""Project's path and selecting chromdriver version"""
class Driver:
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    chromedriver_mac = Service(os.path.join(PROJECT_ROOT, "../bin/chromedriver"))       # execute in mac
    chromedriver_win = Service(os.path.join(PROJECT_ROOT, "../bin/chromedriver.exe"))   # execute in windows


"""Setup method, that required for logging"""
class Setup:
    def setup_help(self, browser):
        page = LoginPage(browser, f"http://192.168.52.{Execute().env}/login")
        page.open()
        page.login_new_user(UserHead)  # "UserHead", "UserLead", UserRecruiter


# TODO Users and environment