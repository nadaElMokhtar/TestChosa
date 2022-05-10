import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver
########## pytest htm reports ###########
#it is hook for adding environment info to html report
def pytest_configure(config):
    config._metadata["PROJECT_NAME"] = "CHOSA"
    config._metadata["TESTERS"] = "NADA & RANA"
 #it hook for delete/modify environment info to html report
