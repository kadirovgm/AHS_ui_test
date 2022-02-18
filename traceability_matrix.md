# Automated test cases
### Execute using pytest: `pytest -s -v --tb=line -m e2e_1`

All tests are marked in [pytest.ini](ahs_selenium/pytest.ini) file

> #### Login page [test_login_page.py](ahs_selenium/test_login_page.py) 

`e2e_1` **TEST FOR CORRECT LOGIN PAGE** `[PASSED]`

    1. Open Login page
    2. Check for correct Login page:
        - Should be login url
        - Should be login form
        - Should be "Forgot password" link

`e2e_2` **TEST RESET PASSWORD PAGE** `[PASSED]`

    1. Open Login page
    2. Click on "Forgot password" link
    3. Check for all elements exist and present correct

`e2e_3` **TEST USER CAN LOG IN** `[TODO]`
    
    1. Open Login page
    2. Enter login/password
    3. Click on "My Profile" 
    4. Check that my profile has opened and correct

> #### Base page [test_base_page.py](ahs_selenium/test_base_page.py)

`e2e_3` **TEST USER CAN GO TO MAIN PAGES** `[PASSED]`

    1. Go to "Positions page" and check that it's correct 
    2. Go to "Pool page" and check that it's correct
    3. Go to "Clients & Projects" page and check that is correct
    4. Go to "Reports page" and check that it's correct
    5. Go to "Help center page" and check that it's correct




   
### test_base_page.py
3. e2e_3 - test can go to main pages (positions, pool, clients, reports, help center) [PASSED]

### test_person_create_modal.py
4. e2e_4 - test person create modal (+ correct elements presenting) [PASSED]

### test_position_create.py
5. e2e_11 - test checking that client project positions elements presenting [PASSED]
5. e2e_12 - test create client project position [PASSED]
   
### test_pool_page.py
6. e2e_5 - test correct pool page fields (internal, external, blacklist tabs) [PASSED]
7. e2e_6 - test correct pool page filters (internal, external, blacklist tabs) [PASSED]
8. e2e_9 - test correct filtering [IN PROGRESS]

### test_positions_page.py
9. e2e_7 - test correct position page fields (Active, Mine, History) [PASSED]
10. e2e_8 - test correct position page filters (Active, Mine, History) [PASSED]
11. e2e_10 - test correct filtering [IN PROGRESS]






### test_clients_projects_page.py
- test correct clients&projects page fields (Active, History)
- test correct filtering
- test create client
- test create project



# Create documentation
# Integrate with CI (docker+gitlab ci?)
# Create reports 
