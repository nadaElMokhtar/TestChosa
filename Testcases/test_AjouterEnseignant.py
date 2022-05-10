from Pages.AjouterJardin import Ajouterjardin
from Pages.AjouterEnseignant import AjouterEN
from Pages.login_page import LoginPage
from Utilities.customLogger import loggeneration
from time import sleep
import pytest


class Test_addTeacher:
    baseURL = "https://app.v2.chosa.net/parent/accueil"
    username = "ranasoltani2000@yahoo.fr"
    password = "ranaranim"
    logger=loggeneration.loggen()

    @pytest.mark.sanity
    def test_ajouterEnseignant(self,setup):
        self.logger.info("******** TEST ADD TEACHER ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.clickOnLogin()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.logger.info("******** LOGIN AS GARDEN PASSED ********")
        self.logger.info("***** ADD GARDEN ******")
        self.addgar = Ajouterjardin(self.driver)
        self.addgar.clickOnNavBar()
        sleep(1)
        self.addgar.setGardenName("mon ecole 2")
        self.addgar.setCountry()
        self.addgar.setville("France")
        self.addgar.setAdress("PARIS")
        sleep(2)
        self.addgar.clickOnNavBarsecond()
        self.logger.info("********  ADDING GARDEN PASSED ********")

        self.ajoutens = AjouterEN(self.driver)

        self.logger.info("******** START TEST ADDING KID TO THE GARDEN ********")
        self.ajoutens.ajoutenfantdansjardin()
        self.logger.info("********  TEST ADDING KID TO THE GARDEN PASSED ********")
        self.logger.info("******** TEST DELETE KID FROM THE GARDEN ********")
        self.ajoutens.supprimeenfant()
        self.logger.info("******** TEST DELETE KID FROM THE GARDEN PASSED ********")
        self.logger.info("******** TEST ADDING CLASS ********")
        sleep(4)
        self.ajoutens.clickonaddclass()
        self.ajoutens.addclass()
        self.logger.info("******** TEST ADDING CLASS PASSED ********")
        self.logger.info("******** TEST ADDING TEACHER ********")
        self.ajoutens.clickonaddteacher()
        self.ajoutens.addteacher()
        self.logger.info("******* TEST ADD MEMBER PASSED *******")
        self.logger.error("********** TEST ADD MEMBER FAILED*************")
        sleep(2)
        self.driver.close()








