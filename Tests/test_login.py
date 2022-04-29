from requests import request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from Pages.login_Page import LoginPage

# @pytest.mark.usefixtures("test_setDriver")
class TestSitelockLogin():
    pass

    # @pytest.fixture(autouse=True)
    # def test_setDriver(self):
    #     global driver
    #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #     #driver = webdriver.Chrome('C:/Python_Selenium/chromedriver.exe')
    #     driver.get("https://secure.sitelock.com/login")
    #     driver.maximize_window()
    

    def test_login(self, Driver):
        #driver = TestSetdriver.test_setDriver.driver
        Driver.get("https://secure.sitelock.com/login")
        Driver.maximize_window()
        login = LoginPage(Driver)
        login.enter_username("sectigo_test_0")
        login.enter_password("$ectigo_Test1@")
        login.enter_submit()
        
        
