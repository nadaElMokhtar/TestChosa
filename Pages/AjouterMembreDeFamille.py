from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class AjouterMembre():

    def __init__(self, driver):
        self.driver = driver

    def clickOnAddmembre(self):
        elementmember = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='navbarNav']/ul/li[4]/a")))

        elementmember.click()
        am = self.driver.find_element_by_xpath("/html/body/app-root/app-parent-profil/html/body/div/div/div/div[2]/a[3]")
        sleep(2)
        am.click()

    def addMembre(self):
        self.driver.find_element_by_id("code").send_keys("j9mgz")
        sleep(3)
        drpdownrelation = self.driver.find_element_by_name('role')
        ddrelation = Select(drpdownrelation)
        sleep(2)
        ddrelation.select_by_value("Mere/Pere")
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/app-root/app-parent/main/div/div/div[2]/app-family-role/html/body/div/div/div/div[2]/div[2]/button").click()