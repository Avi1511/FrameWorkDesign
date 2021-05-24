import datetime

import pytest

from Utilities.BaseClass import BaseClass
from Utilities.logs import Log


class Test_LoginCWA(BaseClass):
    logs = Log.logs_generation()

    @pytest.mark.order1
    def test_login_To_CWA_functionality(self):
        self.logs.info("Test Case ID #4945&&")
        self.login_To_CWA_functionality()
        driver=self.driver
        driver.implicitly_wait(10)
        title_of_screen=driver.title
        self.logs.info("Grabbed title of the page "+title_of_screen)
        try:
            assert title_of_screen=="eipSessionJsp/EipFrameset.jsp: Used by Apps"
            self.logs.info("Title of the page is correct")
        except Exception as e:
            x = datetime.datetime.now().strftime("%m_%d_%Y, %H:%M:%S").replace(" ", "_").replace(",", "").replace(":",
                                                                                                                 "_")
            self.logs.error("Title of the page does not match")
            driver.save_screenshot(r"C:\Users\x257555\PycharmProjects1\FrameWorkDesign\Reports\Screenshots\Failed_Title"+ x +".png")
            raise e





