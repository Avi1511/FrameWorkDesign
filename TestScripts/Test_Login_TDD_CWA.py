import time
import datetime


import pytest

from PageObject.LoginPageObject import LoginPage
from Utilities import XLUtilies
from Utilities.logs import Log


@pytest.mark.usefixtures("Setup")
class LoginCWA_TDD(): #Add test to run
    logs = Log.logs_generation()
    path = r"C:\Users\x257555\PycharmProjects1\FrameWorkDesign\TestData\TestData.xlsx"

    @pytest.mark.tdd
    def test_login_To_CWA_functionality_TDD(self):
        self.logs.info("Test Case ID #4945&&")
        data=self.config
        driver=self.driver
        rows=XLUtilies.getRowCount(self.path,"Sheet1")
        for r in range(2,rows+1):
            username1=XLUtilies.readData(self.path,"Sheet1",r,1)
            pswd1=XLUtilies.readData(self.path,"Sheet1",r,2)
            username2 = XLUtilies.readData(self.path, "Sheet1", r, 3)
            pswd2 = XLUtilies.readData(self.path, "Sheet1", r, 4)
            #exp=XLUtilies.readData(self.path,"Sheet1",r,5)
            log_in= LoginPage(driver)
            driver.implicitly_wait(10)
            log_in.get_screen1_username().send_keys(username1)
            self.logs.info("Sending username for IF as "+username1)
            log_in.get_screen1_pswd().send_keys(pswd1)
            self.logs.info("Entered first password in screen-1")
            log_in.click_submit_Btn_screen1().click()
            self.logs.info("Clicked on submit button on screen-1")
            log_in.get_screen2_username().send_keys(username2)
            self.logs.info("Sending username for IF as "+username2)
            log_in.get_screen2_pswd().send_keys(pswd2)
            self.logs.info("Entered first password in screen-2")
            log_in.click_submit_Btn_screen2().click()
            self.logs.info("Clicked on submit button on screen-2")
            time.sleep(5)
            title_of_screen=driver.title
            self.logs.info("Grabbed title of the page"+title_of_screen)
            ls_result=[]
            if title_of_screen=="eipSessionJsp/EipFrameset.jsp: Used by Apps":
                ls_result.append("True")
                self.logs.info("Title of the page is correct")
            else:
                x = datetime.datetime.now().strftime("%m_%d_%Y, %H:%M:%S").replace(" ", "_").replace(",", "").replace(":",
                                                                                                                     "_")
                self.logs.error("Title of the page does not match")
                driver.save_screenshot(r"C:\Users\x257555\PycharmProjects1\FrameWorkDesign\Reports\Failed_Title"+ x +".png")






