import pytest
import time
from page_objects.login_page import LoginPage
from page_objects.pool_page import PoolPage
from page_objects.create_person_modal_page import CreatePersonModal
from page_objects.FixtureData.fixture_data import FixturesInternalPerson
from settings import Setup, Execute
from urls import Urls


"""Test Pool page fields correctness"""
@pytest.mark.regression
@pytest.mark.e2e_6
class TestPoolPageFieldsCorrectness:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        Setup.setup_help(browser, browser)

    """Internal tab fields"""
    def test_internal_fields(self, browser):
        internal = PoolPage(browser, Urls.POOL_INTERNAL)
        internal.open()
        internal.should_be_correct_fields_internal()

    """External tab fields"""
    def test_external_fields(self, browser):
        external = PoolPage(browser, Urls.POOL_EXTERNAL)
        external.open()
        external.should_be_correct_fields_external_blacklist()

    """Blacklist tab fields"""
    def test_blacklist_fields(self, browser):
        blacklist = PoolPage(browser, Urls.POOL_BLACKLIST)
        blacklist.open()
        blacklist.should_be_correct_fields_external_blacklist()


"""Test Pool page filters appeared"""
@pytest.mark.regression
@pytest.mark.e2e_7
class TestPoolPageFiltersCorrectness:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        Setup.setup_help(browser, browser)

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


"""Test Pool->Internal page correct filtering"""
@pytest.mark.regression
@pytest.mark.e2e_8
class TestPoolPageInternalFiltering:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        Setup.setup_help(browser, browser)

    @pytest.fixture(scope="function", autouse=True)
    def open_pool_internal(self, browser):
        internal = PoolPage(browser, Urls.POOL_INTERNAL)
        internal.open()

    """Test searching"""
    def test_internal_search(self, browser):
        internal = PoolPage(browser, Urls.POOL_INTERNAL)
        internal.search_for_person(FixturesInternalPerson.first_name, FixturesInternalPerson.last_name)

    """Bench label filtering"""
    def test_internal_filter_by_label(self, browser):
        internal = PoolPage(browser, Urls.POOL_INTERNAL)
        internal.filter_label("Bench", tab="Internal")
        internal.reset_filter_label()

    """Filtering by type"""
    @pytest.mark.parametrize('person_type',
                             ("Long-term", "Short-term", "Contractor"))
    def test_internal_filter_by_type(self, browser, person_type):
        internal = PoolPage(browser, Urls.POOL_INTERNAL)
        internal.filter_type_internal(person_type)
        internal.reset_filter_type_internal()

    """Filter by Role"""
    @pytest.mark.parametrize('role',
                             ("SDET", "HR Manager"))
    def test_internal_filter_in_search_by_role(self, browser, role):
        internal = PoolPage(browser, Urls.POOL_INTERNAL)
        internal.filter_role(role, tab="Internal")
        internal.reset_filter_role(tab="Internal")

    """Filter by Skills"""
    @pytest.mark.parametrize('skill',
                             ("python", "sql"))
    def test_filter_in_search_by_skills(self, browser, skill):
        internal = PoolPage(browser, Urls.POOL_INTERNAL)
        internal.filter_skills(skill, tab="Internal", loading_time=Execute().loading_time)
        internal.reset_filter_skills(tab="Internal")

    """Filter by city"""
    def test_filter_in_search_by_city(self, browser):
        internal = PoolPage(browser, Urls.POOL_INTERNAL)
        internal.filter_city("United States", "Los Angeles", tab="Internal", loading_time=Execute().loading_time)
        internal.reset_filter_cities(tab="Internal")

    """Filter by office"""
    @pytest.mark.parametrize('office',
                             ("Kazan", "Ivanovo"))
    def test_filter_by_office(self, browser, office):
        internal = PoolPage(browser, Urls.POOL_INTERNAL)
        internal.filter_office(office, tab="Internal")
        internal.reset_filter_office(tab="Internal")

    """Filter by Eng level"""
    @pytest.mark.parametrize('eng_level',
                             ("Beginner", "Advanced"))
    def test_filter_by_eng_level(self, browser, eng_level):
        internal = PoolPage(browser, Urls.POOL_INTERNAL)
        internal.clear_filters()
        internal.filter_eng_level(eng_level, tab="Internal")
        internal.reset_filter_eng_level(tab="Internal")

    @pytest.mark.skip
    def test_filter_in_search_by_visa(self, browser):
        ...

    @pytest.mark.skip
    def test_filter_in_search_by_active_projects(self, browser):
        ...

    @pytest.mark.skip
    def test_filter_by_hr(self, browser):
        ...


@pytest.mark.regression
@pytest.mark.skip
class TestPoolPageExternalFiltering:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        Setup.setup_help(browser, browser)

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


@pytest.mark.regression
@pytest.mark.skip
class TestPoolPageBlacklistFiltering:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        Setup.setup_help(browser, browser)

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



