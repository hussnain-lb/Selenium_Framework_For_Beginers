import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="drivers/chromedriver")
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.close()
