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

`e2e_3` **TEST USER CAN LOG IN** `[PASSED]`
    
    1. Open Login page
    2. Enter login/password
    3. Click on "My Profile" 
    4. Check that my profile has opened and correct

> #### Base page [test_base_page.py](ahs_selenium/test_base_page.py)

`e2e_4` **TEST USER CAN GO TO MAIN PAGES** `[PASSED]`

    1. Go to "Positions page" and check that it's correct 
    2. Go to "Pool page" and check that it's correct
    3. Go to "Clients & Projects" page and check that is correct
    4. Go to "Reports page" and check that it's correct
    5. Go to "Help center page" and check that it's correct

> #### Person Create Modal Page [test_person_create_modal.py](ahs_selenium/test_person_create_modal.py)

`e2e_5` **Test Person Create Modal** `[PASSED]`

    1. Open Pool page
    2. Open "Create person modal" and check that it has opened
    3. Check that "Create Person modal" fileds are correct
    4. Fill with data and click on "Create" button
    5. Go to Pool->External tab
    6. Search for currently created person and check that he was created

> #### Pool page [test_pool_page.py](ahs_selenium/test_pool_page.py)

`e2e_6` **Test correct Pool Page fields (Internal/External/Blacklist)** `[PASSED]`

    1. Open Pool page -> Internal
    2. Check that all fields appeared and correct
    3. Open Pool page -> External
    4. Check that all fields appeared and correct
    5. Open Pool page -> Blacklist
    6. Check that all fields appeared and correct

`e2e_7` **Test correct Pool Page filters (Internal/External/Blacklist)** `[PASSED]`

    1. Open Pool page -> Internal
    2. Check that all filters appeared and clickable
    3. Open Pool page -> External
    4. Check that all filters appeared and clickable
    5. Open Pool page -> Blacklist
    6. Check that all filters appeared and clickable
   
`e2e_8` **Test Pool page correct filtering [Internal tab]** `[IN PROGRESS]`
    
    1. Open Pool page->Internal tab
    [Searching]
    2. Test searching and check that works correct
    [label filter]
    3. Filter by "bench" label and check that works correct and the reset filter
    [person type filter]
    4. Filter by types ["Long-term", "Contractor", "Short-term"]
    5. Check that filter works correct and the reset filter
    [filter by roles]
    [filter by skills]
    [filter by city]
    [filter by office]
    [filter by english level]
    [filter by vise type]
    [filter by active projects]
    [filter by hr]

> #### Positions page [test_positions_page.py](ahs_selenium/test_positions_page.py)

`e2e_9` **Test correct Position Page fields (Active/Mine/History)** `[PASSED]`
    
    1. Open Positions -> Active tab
    2. Check that all fields are appeared and correct
    3. Open Positions -> Mine tab
    4. Check that all fields are appeared and correct
    5. Open Positions -> History tab
    6. Check that all fields are appeared and correct

`e2e_10` **Test correct Position Page filters (Active/Mine/History)** `[PASSED]`
    
    1. Open Positions -> Active tab
    2. Check that all filters appeared and clickable
    3. Open Positions -> Mine tab
    4. Check that all filters appeared and clickable
    5. Open Positions -> History tab
    6. Check that all filters appeared and clickable

`e2e_11` **Test Positions page correct filtering [Active tab]** `[IN PROGRESS]`

> #### Create position page [test_position_create.py](ahs_selenium/test_position_create.py)

`e2e_12` **Test "Create Client Project Position modal" fields correctness** `[PASSED]`

    1. Open Create Client Project position modal
    2. Go to "Position detail" tab and check for elements appearing and correctness
    3. Go to "Assigns" tab and check for elements appearing and correctness
    4. Go to "Requests" tab and check for elements appearing and correctness

`e2e_13` **Test Create "Client Project Position"** `[PASSED]`

    1. Open create position modal
    2. Fill all required fileds with relevant data and create new Position
    3. Go to Positions->Active tab
    4. Search for currently creted Postition
    5. Check searching results and status of found Position


> #### Clients&Projects page [test_clients_projects_page.py](ahs_selenium/test_clients_projects_page.py) 

- [DRAFT] test correct clients&projects page fields (Active, History)
- [DRAFT] test correct filtering
- [DRAFT] test create client
- [DRAFT] test create project


# TODO
## Create documentation
## Integrate with CI (docker+gitlab ci?)
## Create reports 
