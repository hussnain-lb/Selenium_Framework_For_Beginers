Automated Testing for Swag Lab
### Web Automation Using Selenium Web Driver

 
### [Project Setup](https://docs.qameta.io/setup)

- Install virtual env using command
      pip3 install virtualenv

- Make virtual env using command

      python3 -m venv env_name

- Activate env

      source env_name/bin/activate
   
- Install requirements

      pip3 install -r requirements.txt

           
## Execute
Tests can be run using `pytest`

### pytest

- pytest -m "marker name" -vv

#### Execute Single Test Case 
- 'pytest ./user_interface/tests/test_all_login_cases.py'
the above command will run all the test cases that are available in test_all_login_cases file

- 'pytest ./user_interface/tests/test_all_login_cases.py' -k "name of the test case"
the above command will run only specific test case

### Reporting
- report format = html/junit-xml
