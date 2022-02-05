import pytest
import time
from pages.login_page import LoginPage
from pages.pool_page import PoolPage
from pages.create_person_modal_page import CreatePersonModal
from conftest import LINK_LOGIN_PAGE


class TestAddPerson:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, LINK_LOGIN_PAGE)
        page.open()
        time.sleep(0.5)
        page.login_new_user(email="admin@admin.com", password="P@ssw0rd1")

    @pytest.mark.skip
    def test_correct_create_person_modal(self, browser):
        pool_page = PoolPage(browser, browser.current_url)
        pool_page.go_to_pool_page()
        pool_page.add_person_button_click()
        person_create_modal_page = CreatePersonModal(browser, browser.current_url)
        person_create_modal_page.should_be_create_person_modal()

    def test_add_person(self, browser):
        pool_page = PoolPage(browser, browser.current_url)
        pool_page.go_to_pool_page()
        pool_page.add_person_button_click()
        person_create_page = CreatePersonModal(browser, browser.current_url)
        person_create_page.add_new_person()
        time.sleep(3)

