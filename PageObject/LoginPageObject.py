from selenium.webdriver.common.by import By
from selenium import webdriver



class LoginPage:

    # all the locators are written for module Login Page
    text_userId_screen1_Xpath= (By.XPATH, "//input[@autocomplete='username']")
    text_password_screen1_Xpath= (By.XPATH, "//div/input[@type='password']")
    button_submit_screen1_Xpath=(By.XPATH, "//a[@title='Submit']")
    #screen-2 of authentication
    text_userId_screen2_Xpath=(By.XPATH, "//input[@placeholder='UserId']")
    text_password_screen2_Xpath=(By.XPATH,"//input[@placeholder='Password']" )
    button_submit_screen2_ID =(By.ID,"button-1")

    #Driver initialization, this driver will be passed from test cases file.
    def __init__(self,driver):
        self.driver=driver


    #Action Methods
    def get_screen1_username(self):
        return self.driver.find_element(*LoginPage.text_userId_screen1_Xpath)

    def get_screen1_pswd(self):
        return self.driver.find_element(*LoginPage.text_password_screen1_Xpath)

    def click_submit_Btn_screen1(self):
        return self.driver.find_element(*LoginPage.button_submit_screen1_Xpath)

    def get_screen2_username(self):
        return self.driver.find_element(*LoginPage.text_userId_screen2_Xpath)

    def get_screen2_pswd(self):
        return self.driver.find_element(*LoginPage.text_password_screen2_Xpath)

    def click_submit_Btn_screen2(self):
        return self.driver.find_element(*LoginPage.button_submit_screen2_ID)