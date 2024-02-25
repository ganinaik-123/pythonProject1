import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
from pyjavaproperties import Properties
from selenium.webdriver.chrome.options import Options as Chromeoptions
from selenium.webdriver.firefox.options import Options as Firefoxoptions
from selenium.webdriver import Remote


class BaseTest:
    @pytest.fixture(autouse=True)
    def pre_condition(self):
        print("reading the config properties")
        p = Properties()
        p.load(open("../config.properties"))
        grid=p['GRID']
        grid_url=p['GRID_URL']
        browser=p['BROWSER']
        app_url=p['APP_URL']
        ito=p['ITO']
        eto=p['ETO']
        if grid.lower()=='yes':
            print("using grid")
            if browser.lower()=='firefox':
                print("open the firefox browser")
                options=Firefoxoptions()
            else:
                print("open the chrome browser")
                options=Chromeoptions()
            self.driver=Remote(command_executor=grid_url,options=options)
        else:
            print("using local system")
            if browser.lower()=='firefox':
                print("open the firefox browser")
                self.driver=Firefox()
            else:
                self.driver=Chrome()
                print("open the chrome browser")
        print("enter the url:",app_url)
        self.driver.get(app_url)
        print("set the ITO:",ito)
        self.driver.implicitly_wait(ito)
        print("set the ETO:", eto)
        self.wait=WebDriverWait(self.driver,eto)
        print("maximize the browser")
        self.driver.maximize_window()

    @pytest.fixture(autouse=True)
    def post_condition(self):
        yield
        print("close the browser")
        self.driver.close()
