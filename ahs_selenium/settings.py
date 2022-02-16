import time
import os
from pages.login_page import LoginPage
from selenium.webdriver.chrome.service import Service


"""Project's path and selecting chromdriver version"""
class Execute:
    # TODO include to dockerfile
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    # DRIVER_BIN = os.path.join(PROJECT_ROOT, "../bin/chromedriver")    # execute in mac
    DRIVER_BIN = os.path.join(PROJECT_ROOT, "../bin/chromedriver.exe")  # execute in windows
    ser = Service(DRIVER_BIN)


"""Setup method, that required for logging"""
class Setup:
    def setup_help(self, browser):
        page = LoginPage(browser, Urls.LINK_LOGIN_PAGE)
        page.open()
        page.login_new_user(email="admin@admin.com", password="P@ssw0rd1")


"""Project's URLs"""
class Urls:

    host = f"http://192.168.52.122/"  # Stage
    # host = f"http://192.168.52.137/"  # QA-137
    # host = f"http://192.168.52.139/"  # QA-139
    # host = f"http://192.168.52.152/"  # Demo
    # host = f"http://192.168.52.115/"  # Production

    """LOGIN"""
    LINK_LOGIN_PAGE = f"{host}login"

    """POSITIONS"""
    POSITIONS_ACTIVE = f"{host}positions/active"
    POSITIONS_MINE = f"{host}positions/mine"
    POSITIONS_HISTORY = f"{host}positions/history"

    """POOL"""
    POOL_EXTERNAL = f"{host}pool/external"
    POOL_INTERNAL = f"{host}pool/internal"
    POOL_BLACKLIST = f"{host}pool/blacklisted"

    """CLIENTS&PROJECTS"""
    PROJECTS_ACTIVE = f"{host}projects/active" 
    PROJECTS_HISTORY = f"{host}projects/history"