"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class Ajoutermsg ():


     def __init__(self,driver):
        self.driver=driver


     def clickOnNotif(self):
         elementnotif = WebDriverWait(self.driver, 20).until(
             EC.element_to_be_clickable((By.XPATH, "//*[@id='navbarNav']/ul/li[2]/a/span")))

         elementnotif.click()
         navbar=self.driver.find_element_by_xpath("/html/body/app-root/app-parent/main/div/div/div[2]/app-list-chat-parent/html/body/div/div/div/div[1]/div/div")
         navbar.click()
         aj_dis=self.driver.find_element_by_xpath("/html/body/app-root/app-parent/main/div/div/div[2]/app-list-chat-parent/html/body/div/div/div/div[1]/div/div/div/div/a")
         aj_dis.click()"""""



