import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(autouse=True)
def test_setDriver():
    # global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    # driver.get("https://secure.sitelock.com/login")
    # driver.maximize_window()
    
  