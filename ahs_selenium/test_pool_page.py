import pytest
import time
from pages.login_page import LoginPage
from pages.pool_page import PoolPage
from pages.create_person_modal_page import CreatePersonModal
from pages.randomData.random_data import FixturesInternalPerson
from urls import Urls


@pytest.mark.e2e_5
class TestPoolPageFieldsCorrectness:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, Urls.LINK_LOGIN_PAGE)
        page.open()
        time.sleep(0.5)
        page.login_new_user(email="admin@admin.com", password="P@ssw0rd1")

    def test_internal_fields(self, browser):
        internal = PoolPage(browser, Urls.POOL_INTERNAL)
        internal.open()
        internal.should_be_correct_fields_internal()
        # internal.should_be_filters_internal()
    
    def test_external_fields(self, browser):
        external = PoolPage(browser, Urls.POOL_EXTERNAL)
        external.open()
        external.should_be_correct_fields_external_blacklist()
        # external.should_be_filters_external_blacklist()
    
    def test_blacklist_fields(self, browser):
        blacklist = PoolPage(browser, Urls.POOL_BLACKLIST)
        blacklist.open()
        blacklist.should_be_correct_fields_external_blacklist()
        # blacklist.should_be_filters_external_blacklist()


@pytest.mark.e2e_6
class TestPoolPageFiltersCorrectness:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, Urls.LINK_LOGIN_PAGE)
        page.open()
        time.sleep(0.5)
        page.login_new_user(email="admin@admin.com", password="P@ssw0rd1")

    def test_internal_filters(self, browser):
        internal = PoolPage(browser, Urls.POOL_INTERNAL)
        internal.open()
        internal.should_be_filters_internal()

    def test_external_filters(self, browser):
        external = PoolPage(browser, Urls.POOL_EXTERNAL)
        external.open()
        external.should_be_filters_external_blacklist()

    def test_blacklist_filters(self, browser):
        blacklist = PoolPage(browser, Urls.POOL_BLACKLIST)
        blacklist.open()
        blacklist.should_be_filters_external_blacklist()


# TODO pool filtering
@pytest.mark.skip
class TestPoolPageInternalFiltering:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, Urls.LINK_LOGIN_PAGE)
        page.open()
        time.sleep(0.5)
        page.login_new_user(email="admin@admin.com", password="P@ssw0rd1")

    # To avoid interrupting the test
    # TODO how to improve? (remove 2 repeatable lines)
    def test_internal_search(self, browser):
        internal = PoolPage(browser, Urls.POOL_INTERNAL)
        internal.open()
        internal.search_for_person(FixturesInternalPerson.first_name, FixturesInternalPerson.last_name)

    def test_filter_by_label(self, browser):
        ...

    def test_filter_by_type(self, browser):
        ...

    def test_filter_in_search_by_role(self, browser):
        ...

    def test_filter_in_search_by_skills(self, browser):
        ...

    def test_filter_in_search_by_city(self, browser):
        ...

    def test_filter_by_office(self, browser):
        ...

    def test_filter_by_eng_level(self, browser):
        ...

    def test_filter_in_search_by_visa(self, browser):
        ...

    def test_filter_in_search_by_active_projects(self, browser):
        ...

    def test_filter_by_hr(self, browser):
        ...


@pytest.mark.skip
class TestPoolPageExternalFiltering:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, Urls.LINK_LOGIN_PAGE)
        page.open()
        time.sleep(0.5)
        page.login_new_user(email="admin@admin.com", password="P@ssw0rd1")

    def test_filter_by_label(self, browser):
        ...

    def test_filter_in_search_by_role(self, browser):
        ...

    def test_filter_in_search_by_skills(self, browser):
        ...

    def test_filter_in_search_by_city(self, browser):
        ...

    def test_filter_by_office(self, browser):
        ...

    def test_filter_by_eng_level(self, browser):
        ...

    def test_filter_in_search_by_visa(self, browser):
        ...

    def test_filter_by_hr(self, browser):
        ...


@pytest.mark.skip
class TestPoolPageBlacklistFiltering:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, Urls.LINK_LOGIN_PAGE)
        page.open()
        time.sleep(0.5)
        page.login_new_user(email="admin@admin.com", password="P@ssw0rd1")

    def test_filter_by_label(self, browser):
        ...

    def test_filter_in_search_by_role(self, browser):
        ...

    def test_filter_in_search_by_skills(self, browser):
        ...

    def test_filter_in_search_by_city(self, browser):
        ...

    def test_filter_by_office(self, browser):
        ...

    def test_filter_by_eng_level(self, browser):
        ...

    def test_filter_in_search_by_visa(self, browser):
        ...

    def test_filter_by_hr(self, browser):
        ...



