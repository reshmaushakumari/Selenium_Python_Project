import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(autouse=True)
def Driver():
    # global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.close()
    # driver.get("https://secure.sitelock.com/login")
    # driver.maximize_window()
    
  
