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


