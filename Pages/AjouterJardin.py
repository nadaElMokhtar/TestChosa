from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class Ajouterjardin():

    def __init__(self, driver):
        self.driver = driver


    def clickOnNavBar(self):
       element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,"//*[@id='navbarNav']/ul/li[4]/a" )))

       element.click()
       aj=self.driver.find_element_by_xpath("/html/body/app-root/app-parent-profil/html/body/div/div/div/div[2]/a[4]")
       sleep(2)
       aj.click()



    def setGardenName(self, name):
        self.driver.find_element_by_id("ecoleName").send_keys(name)
        sleep(2)

    def setCountry(self):
        sleep(3)
        drpdowncountry = self.driver.find_element_by_name('country')
        dds = Select(drpdowncountry)
        sleep(2)
        dds.select_by_value("TN")

    def setville(self,ville):
        self.driver.find_element_by_xpath("//*[@id='validationVille']").send_keys(ville)
        sleep(2)

    def setAdress(self,adresse):
        adre =self.driver.find_element_by_xpath("//*[@id='validationAdresse']")
        adre.location_once_scrolled_into_view
        sleep(2)
        adre.send_keys(adresse)
        but = self.driver.find_element_by_xpath("/html/body/app-root/app-training-center-apply/html/body/div/div/div/div[2]/form/div[6]/button")
        sleep(2)
        but.click()



    def clickOnNavBarsecond(self):
        el = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='navbarNav']/ul/li[3]/a")))

        el.click()
        sleep(2)
        jardins = self.driver.find_element_by_xpath("/html/body/app-root/app-parent-profil/html/body/div/div/div/div[2]/a[5]")
        sleep(2)
        jardins.click()
        sleep(1)
        cli=self.driver.find_element_by_xpath("/html/body/app-root/app-parent/main/div/div/div[2]/app-jardin-list/html/body/div/div/div/div[2]/div/div/a")
        cli.click()


    def Addacimage(self):
        sleep(10)
        element54 = self.driver.find_element_by_xpath("/html/body/app-root/app-jardin/app-dashboard/html/body/div/div/div/div[1]/div/div/div")
        sleep(1)
        element54.click()
        b54 = self.driver.find_element_by_xpath("/html/body/app-root/app-jardin/app-dashboard/html/body/div/div/div/div[1]/div/div/div/div/a[4]")
        sleep(1)
        b54.click()
        b55 = self.driver.find_element_by_xpath("/html/body/app-root/app-jardin/app-add-post/html/body/div/div/div/div[2]/div[2]/div[1]/div")
        sleep(1)
        b55.click()
        self.driver.find_element_by_id("customFile5").send_keys("C://rana/20210723_121022.jpg")
        b56 = self.driver.find_element_by_xpath("//*[@id='add-sieste']/div/div/div[3]/button")
        sleep(2)
        b56.click()

    """def Addacpdf(self):
        butt_pdf = self.driver.find_element_by_xpath("/html/body/app-root/app-jardin/app-add-post/html/body/div/div/div/div[2]/div[3]/div[2]/div")
        sleep(1)
        butt_pdf.click()
        self.driver.find_element_by_id("customFile5").send_keys("C:/Users/nada/Downloads/pass rana.pdf")
        but= self.driver.find_element_by_xpath("//*[@id='add-sieste']/div/div/div[3]/button")
        sleep(2)
        but.click()
        
        
        def AddVideo(self):
        butt_vid = self.driver.find_element_by_xpath("/html/body/app-root/app-jardin/app-add-post/html/body/div/div/div/div[2]/div[3]/div[2]/div")
        sleep(1)
        butt_vid.click()
        self.driver.find_element_by_id("customFile5").send_keys("C:/Users/nada/Videos/Captures/Chosa, Construisez de merveilleuses communautés de classe avec les parents et les élèves - Google Chrome 2022-04-27 13-22-09.mp4")
        but2= self.driver.find_element_by_xpath("//*[@id='add-sieste']/div/div/div[3]/button")
        sleep(2)
        but2.click()

        
        """


