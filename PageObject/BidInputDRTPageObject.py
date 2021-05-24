from selenium.webdriver.common.by import By

from TestScripts.conftest import read_file


class DRT_Bids:
    data=read_file()
    drtDate=data["drt_date"]
    Menu_BidInput_ID=(By.ID, "bidInputMenu-menu")
    drpdwn_DRTbidding_Xpath=(By.XPATH,"//a[text()='DRT Bidding']")
    calendar_DRT_Xpath=(By.XPATH,"//img[@class='ui-datepicker-trigger']")
    select_DRTdate_Xpath=(By.XPATH,"(//td/a[contains(@class,'ui-state-default')])["+drtDate+"]")
    btn_SubmitDRTBid_ID=(By.ID,"newBidButton")


    def __init__(self,driver):
        self.driver=driver

    def click_BidInput(self):
        return self.driver.find_element(*DRT_Bids.Menu_BidInput_ID)

    def goTo_DRTScreen(self):
        return self.driver.find_element(*DRT_Bids.drpdwn_DRTbidding_Xpath)

    def goTo_datepicker(self):
        return self.driver.find_element(*DRT_Bids.calendar_DRT_Xpath)

    def select_DRTDate(self):
        return self.driver.find_element(*DRT_Bids.calendar_DRT_Xpath)

    def click_submitDRTbtn(self):
        return self.driver.find_element(*DRT_Bids.btn_SubmitDRTBid_ID)

