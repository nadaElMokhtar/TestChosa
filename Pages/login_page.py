from time import sleep

class LoginPage :
    button_login_xpath="//button[2]"
    textbox_username_id="email"
    #button_nextu_id="identifierNext"
    textbox_password_id="pass"
    button_nextp_id="//*[@id='loginbutton']"



    def __init__(self,driver):
        self.driver=driver

    def clickOnLogin(self):
        self.driver.implicitly_wait(4)
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def setUserName(self,username):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
        sleep(3)
        #self.driver.find_element_by_id(self.button_nextu_id).click()

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)
        sleep(3)
        self.driver.find_element_by_xpath(self.button_nextp_id).click()
        self.driver.implicitly_wait(4)








