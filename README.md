# UI testing for AHS

![](https://c.tenor.com/7FNVoy6XUd8AAAAM/mr-bean-jumping.gif)

### `Tools:` Python, Pytest, Selenium Webdriver
### Official documentations:
1. [Pytest documentation](https://docs.pytest.org/en/6.2.x/getting-started.html)
2. [Selenium-python documentation](https://selenium-python.readthedocs.io/getting-started.html)
3. [Selenium official documentation](https://www.selenium.dev/documentation/)
4. [Webdriver source code [Python]](https://www.selenium.dev/selenium/docs/api/py/api.html)

# Getting started
## 1. Installation
### 1.1. Install Python from [python.org](https://www.python.org/downloads/)

### 1.1. Clone this repository

    $ git clone https://github.com/kadirovgm/AHS_ui_test.git

### 1.2. Create/activate virtual environment:

Go on project's path: 

    $ cd my-selenium-project/

Create virtual environment: 

    $ python -m venv ./venv_name

Activate for Mac/Linux users: 

    $ python source venv_name/bin/activate

Activate for Windows users: 

    $ python venv_name\Scripts\activate

Deactivating: 

    $ deactivate

### 1.3. Install required packages

    $ pip install -r requirements.txt

### 1.4. Update drivers for browser (chromedriver, geckodriver)
As default drivers are stored in [/bin](bin/) directory. 

For updating according to your browser version, please replace actual one with currently downloaded.

You can easily update them from official sources:

| Driver      | Source |
| ----------- | ----------- |
| Chrome:     | https://sites.google.com/chromium.org/driver/       |
| Firefox:    | https://github.com/mozilla/geckodriver/releases     |


## 2. Running tests

### 2.1. Pytest - as test runner

- Check [pytest_commands.sh](/pytest_commands.sh) 
file for using basic pytest commands for effectively run tests and create reports

Example test run:

    $ pytest -sv --tb=line -m regression

### 2.2. Setting configuration for Pytest. File [conftest.py](ahs_selenium/conftest.py)
`Conftest.py` - file, that stores all fixtures required for running test cases.

- `Fixtures` are functions performed by pytest before (and sometimes after) the actual test functions. 

- Decorator `@test.fixture()` is used to tell pytest that the function is a fixture.

- Actually file `conftest.py` has fixtures that is used as `setup` and `teardown` methods

Simple example of fixture from `conftest.py`. Here is the example of setup and teardown methods when 
the fixture selects the driver relative to the selected browser 
```python
import pytest
from selenium import webdriver
@pytest.fixture(scope="class")                                              # initializing browser on every class
def browser(request, get_operation_system):
    browser_name = request.config.getoption("--browser_name")
    
    if browser_name == "chrome":
        print("\nStart chrome browser for test..")
        browser = webdriver.Chrome(service=get_operation_system)

    elif browser_name == "firefox":                                             # make sure that you have firefox driver
        print("\nStart firefox browser for test..")
        browser = webdriver.Firefox(service=get_operation_system)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser.maximize_window()  # maximize window
    browser.implicitly_wait(3)  # implicitly wait
    yield browser

    print("\nquit browser..")
    browser.quit()
```

### 2.3. Setting environment. File [settings.py](ahs_selenium/settings.py)
File `settings.py` stores some environment settings that are needed for a test run. 

You can easily change the settings of the test run relative to the needs.
```python
class Execute:
    def __init__(self):
        self.default_browser = "chrome"      # variants: chrome, firefox
        self.operation_system = "win"        # variants: mac, win
        self.user = "head"                   # variants: head, lead, recruiter
        self.env = "122"                     # variants: 122 (Stage), 137 (QA-137), 139 (QA-139), 152 (Demo), 115 (Production)
        self.loading_time = 1                # time for loading huge data (depends on internet connection, default=0.7)
        self.language = None                 # language - in feature
```

- Also `settings.py` stores drivers paths to "chromedriver" or "geckodriver"

### 2.4. Setting environment as option of pytest command [conftest.py](ahs_selenium/conftest.py).

When executing test cases you can easily set environment setting by command line:

Example from `conftest.py`
```python
def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default=Execute().default_browser,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--os',
                    action='store',
                    default=Execute().operation_system,
                    help="Choose operation system: win or mac")
    parser.addoption('--env',
                    action='store',
                    default=Execute().env,
                    help="Choose environment: 122 (Stage), 137 (QA-137), 139 (QA-139), 152 (Demo), 115 (Production)")
    parser.addoption('--user',
                    action='store',
                    default=Execute().user,
                    help="Choose system user: head, lead, recruiter")
    parser.addoption('--language',
                     action='store',
                     default=Execute().language,
                     help="Choose language: ru, en")
```

### 2.5. Marking test cases. File [pytest.ini](ahs_selenium/pytest.ini)

- For registering markers test cases use file [pytest.ini](ahs_selenium/pytest.ini)

- For executing marked test use option `-m marker`

- For more information check [pytest docs](https://docs.pytest.org/en/6.2.x/example/markers.html)

Example of registering markers in file [pytest.ini](ahs_selenium/pytest.ini):
```ini
[pytest]
markers =
    e2e_1: login page correctness
    e2e_2: reset password correctness
```
Example of marking test cases:
```python
import pytest

@pytest.mark.regression
@pytest.mark.e2e_1
class TestLoginPage:
    ...
```

## 3. Page objects

# Project's catalog
```
📦AHS_ui_test
 ┣ 📂.git
 ┣ 📂.idea
 ┣ 📂ahs_selenium
 ┃ ┣ 📂pages
 ┃ ┃ ┣ 📂FixtureData
 ┃ ┃ ┃    ┣ 📜fixture_data.py ┃ ┃ ┃    ┗ 📜fixture_users.py
 ┃ ┃ ┣ 📂locators
 ┃ ┃ ┃    ┣ 📜base_page_locators.py
 ┃ ┃ ┃    ┣ 📜clients_projects_page_locators.py
 ┃ ┃ ┃    ┣ ...
 ┃ ┃ ┃    ┗ 📜position_page_locators.py
 ┃ ┃ ┣ 📜base_page.py
 ┃ ┃ ┣ 📜clients_projects_page.py
 ┃ ┃ ┣ 📜create_person_modal_page.py
 ┃ ┃ ┣ 📜create_position_modal_page.py
 ┃ ┃ ┣ 📜help_center_page.py
 ┃ ┃ ┣ 📜login_page.py
 ┃ ┃ ┣ 📜person_page.py
 ┃ ┃ ┣ 📜pool_page.py
 ┃ ┃ ┣ 📜positions_page.py
 ┃ ┗ ┗ 📜reports_page.py
 ┣ 📜conftest.py
 ┣ 📜pytest.ini
 ┣ 📜settings.py
 ┣ 📜urls.py
 ┣ 📜test_base_page.py
 ┣ 📜test_clients_projects_page.py
 ┣ 📜test_login_page.py
 ┣ 📜test_person_create_modal.py
 ┣ 📜test_pool_page.py
 ┣ 📜test_positions_page.py
 ┗ 📜test_position_create.py
 ┣ 📂bin
 ┃    ┣ 📜chromedriver.exe
 ┃    ┣ 📜chromedriver
 ┃    ┣ 📜geckodriver.exe
 ┃    ┗ 📜geckodriver
 ┣ 📜.gitignore
 ┣ 📜pytest_commands.sh
 ┣ 📜README.md
 ┣ 📜requirements.txt
 ┗ 📜traceability_matrix.md
```