from Pages.AjouterEnfant import AjouterEnfant
from Pages.login_page import LoginPage
from Utilities.customLogger import loggeneration
from Pages.AjouterStatut import AjouterStatut
from time import sleep
import pytest


class Test_addkid:
    baseURL = "https://app.v2.chosa.net/parent/accueil"
    username = "ranasoltani2000@yahoo.fr"
    password = "ranaranim"
    logger=loggeneration.loggen()

    @pytest.mark.sanity
    def test_ajouterEnfant(self,setup):
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
        self.logger.info("******** START ADDING KID TEST ********")

        self.ajout=AjouterEnfant(self.driver)
        sleep(5)
        self.ajout.clickOnAddKid()

        self.logger.info("******** PROVIDING KID INFO ********")
        #to generate random name
        self.ajout.setprenom("RAMI")
        self.ajout.setGender("Male")
        self.ajout.setDescription("mon enfant a une allergie alimentaire(fraise) ")
        self.ajout.pick_Avatar()
        self.ajout.click_On_Submit()
        self.logger.info("******** saving kid info ********")
        self.logger.info("*********** ADD KID TEST PASSED************")
        sleep(1)
        self.logger.info("******* START ADDING STATUT ********")
        self.ajoutstatut=AjouterStatut(self.driver)
        self.ajoutstatut.clickOnAddstat()
        self.ajoutstatut.AddStat()
        self.ajoutstatut.choisirstatut()
        self.ajoutstatut.choisirdescrption()
        self.driver.implicitly_wait(10)
        self.msg=self.driver.find_element_by_xpath("/html/body/app-root/app-parent/main/div/div/div[2]/app-details/html/body/div[1]/div/div[2]/div[3]/h3").text
        print(self.msg)
        if'votre status a été modifié' in self.msg:
            assert True == True
            self.logger.info("*********** ADD status passed************")
            sleep(5)
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_Ajouterstatut_scr.png")#screenshot
            self.logger.error("********** ADD statut TEST FAILED*************")
            assert True == False













        """def Upper_Lower_string(length):  # define the function and pass the length as argument
            # Print the string in Lowercase
            chaine = ''.join(
                (random.choice(string.ascii_lowercase) for x in range(length)))  # run loop until the define length
            return chaine
            
            sleep(3)
        self.driver.refresh()
        sleep(2)
            """













