import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(executable_path="drivers/chromedriver")
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    driver.close()
