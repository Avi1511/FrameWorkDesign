from selenium.webdriver.common.by import By


class TTGA():
    def __init__(self,driver):
        self.driver=driver

    Menu_BidInput_ID = (By.ID, "bidInputMenu-menu")
    drpdwn_TTGA_Id=(By.ID,"tripTradeGiveAway")
    btn_AckAssgmt_Id=(By.ID,"ackNotification")
    puck_Trip_Xpath=(By.XPATH,"(//div[@class='newpuck trip'])[1]")
    drpdwn_TTGAPostings_Id=(By.ID,"postingFilter")
    btn_Refresh_Id=(By.ID,"refresh")

    def click_BidInput(self):
        return self.driver.find_element(*TTGA.Menu_BidInput_ID)

    def gotTo_TTGApage(self):
        return self.driver.find_element(*TTGA.drpdwn_TTGA_Id)

    def click_AckButton(self):
        return self.driver.find_element(*TTGA.btn_AckAssgmt_Id)

    def select_Trip_MyAssmts(self):
        return self.driver.find_element(*TTGA.puck_Trip_Xpath)

    def select_FromTTGApostingDrpdwn(self):
        return self.driver.find_element(*TTGA.drpdwn_TTGAPostings_Id)

    def click_RefreshButton(self):
        return self.driver.find_element(*TTGA.btn_Refresh_Id)