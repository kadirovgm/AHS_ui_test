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
1.1. Install Python from [python.org](https://www.python.org/downloads/)

1.1. Clone this repository
`git clone https://github.com/kadirovgm/AHS_ui_test.git`

1.2. Open project on any code editor (e.g. VScode)

1.3. Create/activate virtual environment:

Go on project's path: `cd my-selenium-project/`

Create virtual environment: `python -m venv ./venv_name`

Activate for Mac/Linux users: `python source venv_name/bin/activate`

Activate for Windows users: `python venv_name\Scripts\activate`

Deactivating: `deactivate`

## 2. Page objects
## 3. Running tests

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