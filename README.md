Automated Testing for Swag Lab
### Web Automation Using Selenium Web Driver

- Pre req Python 3 must be there in your system
 
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


#### Execute Single Test Case 
     'pytest ./user_interface/tests/test_all_login_cases.py'

- The above command will run all the test cases that are available in test_all_login_cases file

      'pytest ./user_interface/tests/test_all_login_cases.py' -k "name of the test case"

- The above command will run only specific test case

### Reporting
 
    pytest --html=report.html --log-cli-level=INFO --log-file=pytest.log

- the above command will run all the test cases adn will create an html report as well 
- when you load the report in any browser you will be able to see logs as well for all the test cases


### Details About Conftest and Driver
- we have a directory named as drivers in that directory you need to place the chrome driver with specific version
- that you have installed in your system for browsing
- https://chromedriver.chromium.org/downloads use this link to download
- in conftest file ==> driver.get("https://www.saucedemo.com/") just replace the url of your app 
