import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from PageObject.BidInputTTGAPageObject import TTGA
from Utilities.BaseClass import BaseClass
from Utilities.logs import Log


class Test_TTGA(BaseClass):
    logs = Log.logs_generation()

    @pytest.mark.order3
    def test_ttga_flow(self):
        self.login_To_CWA_functionality()
        driver=self.driver
        driver.implicitly_wait(10)
        ttga=TTGA(driver)
        ttga.click_BidInput().click()
        ttga.gotTo_TTGApage().click()
        assert ttga.click_AckButton().is_displayed();
        action=ActionChains(driver)
        action.move_to_element(ttga.select_Trip_MyAssmts()).perform()
        action.double_click(ttga.select_Trip_MyAssmts()).perform()
        handles=driver.window_handles
        parent_window=handles[0]
        child_window=handles[1]
        driver.switch_to.window(child_window)
        title_child_window=driver.title
        a="Trip DA8Q on 04/06/2021"
        assert a==title_child_window
        driver.switch_to.window(parent_window)
        drp_down_posting=Select(ttga.select_FromTTGApostingDrpdwn())
        drp_down_posting.select_by_value("ttga")
        ttga.click_RefreshButton()
        time.sleep(4)



