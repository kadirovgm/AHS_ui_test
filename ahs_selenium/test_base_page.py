import pytest
import time


LINK_LOGIN_PAGE = "http://192.168.52.122/login"

class TestBasePageActions:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = LINK_LOGIN_PAGE
        self.page = ...
