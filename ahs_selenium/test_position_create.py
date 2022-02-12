import pytest
import time
from pages.login_page import LoginPage
from settings import Setup


@pytest.mark.skip
class TestClientProjectPosition:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        Setup.setup_help(browser, browser)
    
    def test_create_client_project_position(self, browser):
        ...


@pytest.mark.skip
class TestInternalProjectPosition:
    ...


@pytest.mark.skip
class TestBenchPosition:
    ...


@pytest.mark.skip
class TestPreOfferPosition:
    ...


@pytest.mark.skip
class TestTraineePosition:
    ...