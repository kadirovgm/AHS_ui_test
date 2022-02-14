# UI testing for AHS
### `Tools:` Python, Pytest, Selenium Webdriver
# 


As default tests running only on Chrome browser.

In the future, test can be run in Firefox too. (Scalability opportunities in conftest.py)

pytest.ini - for marking test cases

chromedriver.exe - driver for chrome


# Project's catalog
```
📦AHS_ui_test
 ┣ 📂.git
 ┣ 📂.idea
 ┣ 📂ahs_selenium
 ┃ ┣ 📂pages
 ┃ ┃ ┣ 📂locators
 ┃ ┃ ┃    ┗ 📜locators.py
 ┃ ┃ ┣ 📂randomData
 ┃ ┃ ┃    ┗ 📜random_data.py
 ┃ ┃ ┣ 📜base_page.py
 ┃ ┃ ┣ 📜clients_projects_page.py
 ┃ ┃ ┣ 📜create_person_modal_page.py
 ┃ ┃ ┣ 📜create_position_modal_page.py
 ┃ ┃ ┣ 📜help_center_page.py
 ┃ ┃ ┣ 📜login_page.py
 ┃ ┃ ┣ 📜pool_page.py
 ┃ ┃ ┣ 📜positions_page.py
 ┃ ┗ ┗ 📜reports_page.py
 ┣ 📜conftest.py
 ┣ 📜pytest.ini
 ┣ 📜settings.py
 ┣ 📜test_base_page.py
 ┣ 📜test_clients_projects_page.py
 ┣ 📜test_login_page.py
 ┣ 📜test_person_create_modal.py
 ┣ 📜test_pool_page.py
 ┣ 📜test_positions_page.py
 ┗ 📜test_position_create.py
 ┣ 📂bin
 ┃    ┣ 📜chromedriver
 ┃    ┗ 📜chromedriver.exe
 ┣ 📜.gitignore
 ┣ 📜pytest_commands.sh
 ┣ 📜README.md
 ┣ 📜requirements.txt
 ┗ 📜traceability_matrix.md
```