import datetime
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObject.BidInputDRTPageObject import DRT_Bids
from PageObject.LoginPageObject import LoginPage
from TestScripts.conftest import read_file
from Utilities.BaseClass import BaseClass
from Utilities.logs import Log


class Test_SubmitDRTBids(BaseClass):
    logs = Log.logs_generation()
    @pytest.mark.order2
    def test_SubmitDRTBids(self):
        self.logs.info("Login to CWA with IF test case is called")
        self.login_To_CWA_functionality()
        data = self.config
        driver = self.driver
        self.logs.info("Login to CWA successful"+data["usrid_scrn1_if"])
        drt_bid=DRT_Bids(driver)
        drt_bid.click_BidInput().click()
        self.logs.info("Click on Bid Input")
        time.sleep(3)
        drt_bid.goTo_DRTScreen().click()
        self.logs.info("Click on DRT Bidding on Bid Input Dropdown")
        time.sleep(3)
        drt_bid.goTo_datepicker().click()
        wait=WebDriverWait(driver, 10)
        wait.until(expected_conditions.visibility_of_element_located(drt_bid.select_DRTdate_Xpath))
        self.logs.info("Click on Calendar on DRT screen")
        drt_bid.select_DRTDate().click()
        time.sleep(3)
        self.logs.info("Selected date on Calendar is "+data["drt_date"])
        drt_bid.click_submitDRTbtn().click()
        self.logs.info("DRT bids are submitted successfully")






