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
                     default=Execute.default_browser,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--os',
                    action='store',
                    default=Execute.operation_system,
                    help = "Choose operation system: win or mac")
    parser.addoption('--env',
                    action='store',
                    default=Execute.env,
                    help = "Choose environment: 122 (Stage), 137 (QA-137), 139 (QA-139), 152 (Demo), 115 (Production)")
    parser.addoption('--user',
                    action='store',
                    default=Execute.user,
                    help = "Choose system user: head, lead, recruiter")
    parser.addoption('--language',
                     action='store',
                     default=Execute.language,
                     help="Choose language: ru, en")

@pytest.fixture(scope="class")  
def get_operation_system(request):
    _os = request.config.getoption("--os")
    if _os == "mac":
        return Driver.chromedriver_mac
    elif _os == "win":
        return Driver.chromedriver_win
    else:
        raise pytest.UsageError("--os should be mac or win")

# TODO
@pytest.fixture(scope="class")  
def get_environment(request):
    _env = request.config.getoption("--env")
    return _env

# TODO
def get_user(request):
    _user = request.config.getoption("--user")
    if _user == "head":
        return UserHead
    elif _user == "lead":
        return UserLead
    elif _user == "recruiter":
        return UserRecruiter
    else:
        raise pytest.UsageError("--user should be head, lead or recruiter")

@pytest.fixture(scope="class")                                              # initializing browser on every class
def browser(request, get_operation_system, get_environment):
    # TODO 
    environment = Urls()
    environment.set_env(get_environment)

    browser_name = request.config.getoption("--browser_name")
    user_language = request.config.getoption("--language")                  # if want to launch eng version of site
    
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

        print("\nStart chrome browser for test..")
        browser = webdriver.Chrome(options=options, service=get_operation_system)
        browser.maximize_window()                                           # maximize window
        browser.implicitly_wait(3)                                          # implicitly wait

    elif browser_name == "firefox":                                         # make sure that you have firefox driver
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nStart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser

    print("\nquit browser..")
    browser.quit()


# Conf test for testing, when need to close browser in every function
@pytest.fixture(scope="function")
def browser_login():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(service=Execute.env)
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    print("\nquit browser..")
    browser.quit()
