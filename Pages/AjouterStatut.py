from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class AjouterStatut():
    

    def __init__(self, driver):
        self.driver = driver

    def clickOnAddstat(self):
        card = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-parent/main/div/div/div[2]/app-acceuil/html/body/app-child-dash/html/body/div/div/div/div/div/div/div/div/h6")))
        card.click()

        # /html/body/app-root/app-parent/main/div/div/div[2]/app-acceuil/html/body/app-child-dash/html/body/div/div/div/div/div/div/div/div/h4

    def AddStat(self):
        element=self.driver.find_element_by_xpath("/html/body/app-root/app-parent/main/div/div/div[2]/app-details/html/body/div[1]/div/div[1]/div/div/div/div")
        element.location_once_scrolled_into_view
        sleep(2)
        element.click()
        b2 = self.driver.find_element_by_xpath("/html/body/app-root/app-parent/main/div/div/div[2]/app-details/html/body/div[1]/div/div[1]/div/div/div/div/div/a[1]")
        sleep(2)
        b2.click()


    def choisirstatut(self):
        sleep(3)
        drpdownstatus=self.driver.find_element_by_name('status')
        dds= Select(drpdownstatus)
        sleep(2)
        dds.select_by_value("grincheux")

    def choisirdescrption(self):
        sleep(2)
        desc=self.driver.find_element_by_xpath("//*[@id='exampleFormControlTextarea2']")
        sleep(1)
        desc.send_keys("mon enfnt est malade je dois le ramener a la maison")
        sleep(1)
        butt_pub=self.driver.find_element_by_xpath("//*[@id='add-status']/div/div/div[3]/button")
        sleep(1)
        butt_pub.click()






