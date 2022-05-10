from Pages.AjouterJardin import Ajouterjardin
from Pages.login_page import LoginPage
from Utilities.customLogger import loggeneration
from time import sleep
import pytest


class Test_addGarden:
    baseURL = "https://app.v2.chosa.net/parent/accueil"
    username = "ranasoltani2000@yahoo.fr"
    password = "ranaranim"
    logger=loggeneration.loggen()
    @pytest.mark.sanity
    def test_ajouteJardin(self,setup):
        self.logger.info("******** TEST ADD GARDEN ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.clickOnLogin()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.logger.info("***** START ADDING GARDEN ******")
        self.addgar= Ajouterjardin(self.driver)
        self.addgar.clickOnNavBar()
        sleep(1)
        self.addgar.setGardenName("mon ecole doudi")
        self.addgar.setCountry()
        self.addgar.setville("tunisie")
        self.addgar.setAdress("benarous")
        sleep(2)
        #SO WE CAN ACCESS THE GARDENS'LIST
        self.addgar.clickOnNavBarsecond()
        sleep(1)
        self.addgar.Addacimage()
        """sleep(3)
        self.addgar.Addacpdf()"""
        sleep(2)
        self.driver.close()