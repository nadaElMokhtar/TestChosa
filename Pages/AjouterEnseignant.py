from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class AjouterEN():
    def __init__(self, driver):
        self.driver = driver

    def ajoutenfantdansjardin(self):
        sleep(5)
        navbarflech1 = self.driver.find_element_by_xpath( "/html/body/app-root/app-jardin/app-dashboard/html/body/div/div/div/div[1]/div/div/div")
        sleep(1)
        navbarflech1.click()
        ajouterenf = self.driver.find_element_by_xpath("/html/body/app-root/app-jardin/app-dashboard/html/body/div/div/div/div[1]/div/div/div/div/a[1]")
        sleep(1)
        ajouterenf.click()
        self.driver.find_element_by_xpath("//*[@id='code']").send_keys("26804600")
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/app-root/app-jardin/app-add-enfant/html/body/div/div/div/div[3]/button").click()
        sleep(2)
        btn=self.driver.find_element_by_xpath("/html/body/app-root/app-jardin/app-verif-to-add/html/body/div/div/div/div[3]/button")
        sleep(1)
        btn.click()
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/app-root/app-jardin/app-dashboard/html/body/div/div/div/div[2]/div[4]/app-list-enfant/html/body/div[1]/div/div/div/div/h4").click()

    def supprimeenfant(self):
        sleep(5)
        navbarflech2 = self.driver.find_element_by_xpath("/html/body/app-root/app-jardin/app-detail-enfant/html/body/div[1]/div/div/div[1]/div/div")
        sleep(1)
        navbarflech2.click()
        suppenf = self.driver.find_element_by_xpath("/html/body/app-root/app-jardin/app-detail-enfant/html/body/div[1]/div/div/div[1]/div/div/div/div/a[2]")
        sleep(1)
        suppenf.click()
        btnsupp=self.driver.find_element_by_xpath("//*[@id='remove']/div/div/div[2]/button[2]")
        btnsupp.click()


    def clickonaddclass(self):
        navbarflech3 = self.driver.find_element_by_xpath("/html/body/app-root/app-jardin/app-dashboard/html/body/div/div/div/div[1]/div/div/div")
        sleep(1)
        navbarflech3.click()
        ajouterclasse = self.driver.find_element_by_xpath("/html/body/app-root/app-jardin/app-dashboard/html/body/div/div/div/div[1]/div/div/div/div/a[3]")
        sleep(1)
        ajouterclasse.click()

    def addclass(self):
        box=self.driver.find_element_by_xpath("//*[@id='name']").send_keys("classe 1")
        sleep(2)
        imageclasse=self.driver.find_element_by_xpath("//*[@id='img11']").click()
        sleep(4)
        butt_classe=self.driver.find_element_by_xpath("/html/body/app-root/app-jardin/app-cree-class/html/body/div/div/div/div[3]/button").click()

    def clickonaddteacher(self):
            sleep(5)
            navbarflech = self.driver.find_element_by_xpath("/html/body/app-root/app-jardin/app-dashboard/html/body/div/div/div/div[1]/div/div/div")
            sleep(1)
            navbarflech.click()
            ajouterenseignat = self.driver.find_element_by_xpath("/html/body/app-root/app-jardin/app-dashboard/html/body/div/div/div/div[1]/div/div/div/div/a[2]")
            sleep(1)
            ajouterenseignat.click()


    def addteacher(self):
            elajoutmembre = self.driver.find_element_by_xpath("/html/body/app-root/app-jardin/app-add-animateur/html/body/div/div/div/div[2]/form/div/input").send_keys("ng084")
            sleep(1)
            self.driver.find_element_by_xpath("/html/body/app-root/app-jardin/app-add-animateur/html/body/div/div/div/div[2]/div/button").click()
            sleep(2)
            self.driver.find_element_by_xpath("/html/body/app-root/app-jardin/app-teacher-verif-to-add/html/body/div/div/div/div[3]/button").click()






