import time

import pytest

from PageObject.LoginPageObject import LoginPage


@pytest.mark.usefixtures("Setup")
class BaseClass:


    def login_To_CWA_functionality(self):
        data=self.config
        driver=self.driver
        log_in= LoginPage(driver)
        driver.implicitly_wait(10)
        log_in.get_screen1_username().send_keys(data["usrid_scrn1_if"])
        self.logs.info("Sending username for IF as " + data["usrid_scrn1_if"])
        log_in.get_screen1_pswd().send_keys(data["pswrd_scrn1_ifo"])
        self.logs.info("Entered first password in screen-1")
        log_in.click_submit_Btn_screen1().click()
        self.logs.info("Clicked on submit button on screen-1")
        log_in.get_screen2_username().send_keys(data["usrid_scrn2_if"])
        self.logs.info("Sending username for IF as " + data["usrid_scrn2_if"])
        log_in.get_screen2_pswd().send_keys(data["pswrd_scrn2_if"])
        self.logs.info("Entered first password in screen-2")
        log_in.click_submit_Btn_screen2().click()
        self.logs.info("Clicked on submit button on screen-2")
        time.sleep(2)
        driver.switch_to.frame("appMainFrame")
