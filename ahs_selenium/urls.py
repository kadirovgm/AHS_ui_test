import time
from pages.login_page import LoginPage


class Setup:
    def setup_help(self, browser):
        page = LoginPage(browser, Urls.LINK_LOGIN_PAGE)
        page.open()
        time.sleep(0.5)
        page.login_new_user(email="admin@admin.com", password="P@ssw0rd1")


class Urls:

    # TODO: include in dockerfile?

    host = "http://192.168.52.122/"

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
