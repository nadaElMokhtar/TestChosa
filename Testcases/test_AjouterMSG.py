"""""""""from Pages.login_page import LoginPage
from Pages.AjouterMSG import Ajoutermsg
from Utilities.customLogger import loggeneration
from time import sleep


class Test_addsms:
    baseURL = "https://app.v2.chosa.net/parent/accueil"
    username = "ranasoltani2000@yahoo.fr"
    password = "ranaranim"
    logger=loggeneration.loggen()

    def test_ajoutermsg(self,setup):
        self.logger.info("******** TEST ADD TEACHER ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.clickOnLogin()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        #creer login object
        self.lp=LoginPage(self.driver)
        self.lp.clickOnLogin()
        # we still need to login
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)

        self.logger.info("********  ********")

        self.addSMS=Ajoutermsg(self.driver)
        self.addSMS.clickOnNotif()"""""

from Pages.login_page import LoginPage
from Utilities.customLogger import loggeneration
from Pages.AjouterMembreDeFamille import AjouterMembre
from time import sleep
import pytest


class Test_addmember:
    baseURL = "https://app.v2.chosa.net/parent/accueil"
    username = "ranasoltani2000@yahoo.fr"
    password = "ranaranim"
    logger=loggeneration.loggen()

    @pytest.mark.sanity
    def test_ajoutermembre(self,setup):
        self.logger.info("******** TEST ADD MESSAGE ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()



        self.logger.info("******** PROVIDING MESSAGE INFORMATION  ********")
        self.logger.info("*********** START TEST ADD MESSAGE************")

        C=3
        b=6
        if (C>=b):
            assert True == True
            self.logger.info("*********** ************")
            sleep(5)
        else:
            self.logger.error("********** ADD MESSAGE TEST FAILED*************")
            assert True == False
            self.driver.close()



