import pytest
from page_objects.pool_page import PoolPage
from page_objects.create_person_modal_page import CreatePersonModal
from settings import Urls, Setup


"""Test Add Person"""
@pytest.mark.e2e_5
class TestAddPerson:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        Setup.setup_help(browser, browser)

    """Open Create Person Modal"""
    def test_go_to_create_person_modal(self, browser):
        pool_page = PoolPage(browser, Urls.POOL_INTERNAL)
        pool_page.open()
        pool_page.add_person_button_click()
        pool_page.add_person_modal_should_be_opened()

    """Check Create Person Modal fields"""
    def test_check_create_person_modal(self, browser):
        person_create_modal = CreatePersonModal(browser, browser.current_url)
        person_create_modal.should_be_create_person_modal()

    """Fill Create Person Modal and check that person was created"""
    def test_add_person(self, browser):
        person_create_page = CreatePersonModal(browser, browser.current_url)
        created_first_name, created_second_name = person_create_page.add_new_person(loading_time=0.7)
        external_tab = PoolPage(browser, browser.current_url)
        external_tab.go_to_external_tab()
        external_tab.search_for_person(created_first_name, created_second_name)


