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
        self.logger.info("******** TEST ADD KID PARENT ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()


        #creer login object
        self.lp=LoginPage(self.driver)
        self.lp.clickOnLogin()
        # we still need to login
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.logger.info("******** LOGIN SUCCESSFUL ********")
        self.logger.info("*********** START ADDING MEMBER OF FAMILY************")
        self.member=AjouterMembre(self.driver)
        self.member.clickOnAddmembre()
        self.member.addMembre()
        self.logger.error("********** ADD MEMBER TEST FAILED*************")
        self.driver.save_screenshot(".\\screenshots\\" + "test_Ajoutermembre_scr.png")
        self.driver.close()
        sleep(1)
        self.aria51=self.driver.find_element_by_class_name("toast-message ng-star-inserted").get_attribute("aria-label")
        if 'Changer le code' in self.aria51:
            assert True == True
            self.logger.info("*********** ADD MEMBER PASSED ************")
            sleep(5)
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_Ajoutermembre_scr.png")  # screenshot
            self.logger.error("********** ADD MEMBER TEST FAILED*************")
            assert True == False