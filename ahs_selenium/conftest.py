# pytest -s -v --browser_name=chrome test_parser.py
# pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py - for rerun
# pytest --language=es test_items.py - for language
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

LINK_LOGIN_PAGE = "http://192.168.52.122/login"
POOL_EXTERNAL_TAB = "http://192.168.52.122/pool/internal"


# default options
def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language',
                     action='store',
                     default="None",
                     help="Choose language: ru, en")


@pytest.fixture(scope="class")  # "function" if want to initialize on every function
def browser(request):
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    DRIVER_BIN = os.path.join(PROJECT_ROOT, "bin/chromedriver_for_mac") # execute in mac
    # DRIVER_BIN = os.path.join(PROJECT_ROOT, "bin/chromedriver_for_win.exe") # execute in windows

    browser_name = request.config.getoption("browser_name")
    # user_language = request.config.getoption("language")
    user_language = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

        print("\nStart chrome browser for test..")
        browser = webdriver.Chrome(options=options, executable_path = DRIVER_BIN)
        browser.maximize_window()                   # maximize window
        browser.implicitly_wait(3)                  # implicitly wait

    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nStart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser

    print("\nquit browser..")
    browser.quit()


# Basic browser
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()