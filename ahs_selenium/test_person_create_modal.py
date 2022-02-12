import pytest
import time
from pages.login_page import LoginPage
from pages.pool_page import PoolPage
from pages.create_person_modal_page import CreatePersonModal
from settings import Urls, Setup


@pytest.mark.e2e_4
class TestAddPerson:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        Setup.setup_help(browser, browser)

    def test_go_to_create_person_modal(self, browser):
        pool_page = PoolPage(browser, Urls.POOL_INTERNAL)
        pool_page.open()
        pool_page.add_person_button_click()

    def test_check_create_person_modal(self, browser):
        person_create_modal = CreatePersonModal(browser, browser.current_url)
        person_create_modal.should_be_create_person_modal()

    def test_add_person(self, browser):
        person_create_page = CreatePersonModal(browser, browser.current_url)
        created_first_name, created_second_name = person_create_page.add_new_person()
        external_tab = PoolPage(browser, browser.current_url)
        external_tab.go_to_external_tab()
        external_tab.search_for_person(created_first_name, created_second_name)
        time.sleep(1)   # just visual identifying


