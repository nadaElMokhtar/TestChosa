import pytest
from selenium import webdriver
from Pages.login_page import LoginPage
from time import sleep
from Utilities.customLogger import loggeneration
class Test_001_login:
    baseURL="https://app.v2.chosa.net/parent/accueil"
    username="ranasoltani2000@yahoo.fr"
    password="ranaranim"
    logger=loggeneration.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("******** LOGIN TEST ********")
        self.logger.info("******** VERIFYING LOGIN TEST ********")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.clickOnLogin()
        #we use self so we can access the variable of the class
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        sleep(5)
        act2_title=self.driver.title

        if act2_title == "Chosa, Construisez de merveilleuses communautés de classe avec les parents et les élèves":
            assert True
            self.logger.info("******** LOGIN TEST PASSED ********")
            sleep(2)
            self.driver.close()
        else:
            assert False
            self.logger.error("******** LOGIN TEST FAILED ********")














