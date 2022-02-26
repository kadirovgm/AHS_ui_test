# pytest -s -v --browser_name=chrome test_parser.py
# pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py - for rerun
# pytest --language=es test_items.py - for language
from email.policy import default
from urllib import request
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page_objects.FixtureData.fixture_users import *
from settings import Driver, Execute
from urls import Urls


# default options
def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default=Execute().default_browser,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--os',
                    action='store',
                    default=Execute().operation_system,
                    help="Choose operation system: win or mac")
    # TODO
    parser.addoption('--env',
                    action='store',
                    default=Execute().env,
                    help="Choose environment: 122 (Stage), 137 (QA-137), 139 (QA-139), 152 (Demo), 115 (Production)")
    # TODO
    parser.addoption('--user',
                    action='store',
                    default=Execute().user,
                    help="Choose system user: head, lead, recruiter")
    parser.addoption('--language',
                     action='store',
                     default=Execute().language,
                     help="Choose language: ru, en")


@pytest.fixture(scope="class")  
def get_operation_system(request):
    _os = request.config.getoption("--os")
    _browser = request.config.getoption("--browser_name")
    if _browser == "chrome":
        if _os == "mac":
            return Driver.chromedriver_mac
        elif _os == "win":
            return Driver.chromedriver_win
        else:
            raise pytest.UsageError("--os should be mac or win")
    elif _browser == "firefox":
        if _os == "mac":
            return Driver.geckodriver_mac
        elif _os == "win":
            return Driver.geckodriver_win
        else:
            raise pytest.UsageError("--os should be mac or win")
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")


# TODO
@pytest.fixture(scope="class")  
def get_environment(request):
    _env = request.config.getoption("--env")
    return _env


# TODO
@pytest.fixture(scope="class")
def get_user(request):
    _user = request.config.getoption("--user")
    return _user


# Initialise browser driver
@pytest.fixture(scope="class")                                              # initializing browser on every class
def browser(request, get_operation_system):
    browser_name = request.config.getoption("--browser_name")

    user_language = request.config.getoption("--language")                  # if want to launch eng version of site
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    if browser_name == "chrome":
        print("\nStart chrome browser for test..")
        browser = webdriver.Chrome(options=options, service=get_operation_system)

    elif browser_name == "firefox":                                             # make sure that you have firefox driver
        print("\nStart firefox browser for test..")
        browser = webdriver.Firefox(options=options, service=get_operation_system)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser.maximize_window()  # maximize window
    browser.implicitly_wait(3)  # implicitly wait
    yield browser

    print("\nquit browser..")
    browser.quit()


# Conf test for testing, when need to close browser in every function
@pytest.fixture(scope="function")
def browser_login(request, get_operation_system):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        print("\nStart chrome browser for test..")
        browser = webdriver.Chrome(service=Driver.chromedriver_win)

    elif browser_name == "firefox":                                             # make sure that you have firefox driver
        print("\nStart firefox browser for test..")
        browser = webdriver.Firefox(service=get_operation_system)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser

    print("\nquit browser..")
    browser.quit()
