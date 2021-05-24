from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import pytest
driver = None


#code to read data from TestData.txt
def read_file():
    with open(r"C:\Users\x257555\PycharmProjects1\FrameWorkDesign\TestData\TestData") as td:
        content=td.readlines()
        #creating dictionary to store the data from test data file in key:value format
        dict={}
        for i in content:
            key=i.split("==")[0]
            if key=='\n':
                break
            value=i.split("==")[1]
            if '\n' in value:
                value=value.replace("\n","")
            dict[key]=value
        return dict





@pytest.fixture()
def Setup(request):
    global driver
    data=read_file()
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.get(data["url"])

    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver=driver
    request.cls.config=data
    yield
    driver.close()

########## Pytest HTML Hooks #######
def pytest_configure(config):
    config._metadata["Project Name"] = 'CREW'
    config._metadata["Module Name"] =  'CWA'
    config._metadata["QMO Tester"] =  'Avi Acharya'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Plugins",None)
    metadata.pop("Packages",None)

#code to screenshot to HTML file
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)



