from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AjouterEnfant():
    menu_xpath = "/html/body/app-root/app-parent/main/div/div/div[2]/app-acceuil/html/body/app-child-dash/html/body/div/div/div/div/div/div/div/div[1]/div/div"

    txtName_Id = "prenom"
    rdMaleGender_ID = "contactChoice2"
    rdFemaleGender_ID = "contactChoice1"
    txtdescription_xpath = "//*[@id='description']"
    avatar_xpath = "//*[@id='img1']"
    button_submition_id = "submit1"


    def __init__(self, driver):
        self.driver = driver


    def clickOnAddKid(self):
       element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-parent/main/div/div/div[2]/app-acceuil/html/body/app-child-dash/html/body/div/div/div/div/div/div/div/div[1]/div/div" )))

       element.click()
       b2 = self.driver.find_element_by_xpath("/html/body/app-root/app-parent/main/div/div/div[2]/app-acceuil/html/body/app-child-dash/html/body/div/div/div/div/div/div/div/div[1]/div/div/div/div/a")
       b2.click()

    def setprenom(self, prenom):
        self.driver.find_element_by_id(self.txtName_Id).send_keys(prenom)
        sleep(2)

    def setGender(self, gender):
        if gender == 'Female':
            self.driver.find_element_by_id(self.rdFemaleGender_ID).click()
        elif gender == 'Male':
            self.driver.find_element_by_id(self.rdMaleGender_ID).click()
        else:
            self.driver.find_element_by_id(self.rdFemaleGender_ID).click()

    def setDescription(self, dob):
        self.driver.find_element_by_xpath(self.txtdescription_xpath).send_keys(dob)
        sleep(10)

    def pick_Avatar(self):
        av = self.driver.find_element_by_xpath(self.avatar_xpath)
        av.location_once_scrolled_into_view
        sleep(2)
        av.click()
        av.click()

    def click_On_Submit(self):
        self.driver.find_element_by_id(self.button_submition_id).click()
        self.driver.implicitly_wait(10)










