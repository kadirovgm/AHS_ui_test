import pytest
import time
from page_objects.login_page import LoginPage
from page_objects.pool_page import PoolPage
from page_objects.create_person_modal_page import CreatePersonModal
from page_objects.FixtureData.fixture_data import FixturesInternalPerson
from settings import Urls, Setup


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

    """Test searching"""
    @pytest.mark.skip
    def test_internal_search(self, browser):
        internal = PoolPage(browser, Urls.POOL_INTERNAL)
        internal.open()
        internal.search_for_person(FixturesInternalPerson.first_name, FixturesInternalPerson.last_name)

    """Bench label filtering"""
    @pytest.mark.skip
    def test_internal_filter_by_label(self, browser):
        internal = PoolPage(browser, Urls.POOL_INTERNAL)
        internal.open()
        internal.filter_label("Bench", tab="Internal")

    """Reset Filtering by label (depends on filtering)"""
    @pytest.mark.skip
    def test_internal_reset_filter_by_label(self, browser):
        internal = PoolPage(browser, browser.current_url)
        internal.reset_filter_label()

    """Filtering by type"""
    @pytest.mark.skip
    @pytest.mark.parametrize('person_type',
                             ("Long-term", "Contractor", "Short-term"))
    def test_internal_filter_by_type(self, browser, person_type):
        internal = PoolPage(browser, Urls.POOL_INTERNAL)
        internal.open()
        internal.clear_filters()
        internal.filter_type_internal(person_type)
        internal.reset_filter_type_internal()

    """Filter by Role"""
    @pytest.mark.skip
    @pytest.mark.parametrize('role',
                             ("SDET", "HR Manager"))
    def test_internal_filter_in_search_by_role(self, browser, role):
        internal = PoolPage(browser, Urls.POOL_INTERNAL)
        internal.open()
        internal.filter_role(role, tab="Internal")
        internal.reset_filter_role(tab="Internal")

    """Filter by Skills"""
    @pytest.mark.skip
    def test_filter_in_search_by_skills(self, browser):
        internal = PoolPage(browser, Urls.POOL_INTERNAL)
        internal.open()
        internal.filter_skills("python", tab="Internal")
        internal.reset_filter_skills(tab="Internal")

    """Filter by city"""
    def test_filter_in_search_by_city(self, browser):
        internal = PoolPage(browser, Urls.POOL_INTERNAL)
        internal.open()
        internal.filter_city("United States", "Los Angeles", tab="Internal")
        internal.reset_filter_cities(tab="Internal")

    @pytest.mark.skip
    def test_filter_by_office(self, browser):
        ...

    @pytest.mark.skip
    def test_filter_by_eng_level(self, browser):
        ...

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



