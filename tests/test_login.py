import pytest
from pages.login_page import LoginPage
from utilities.driver_manager import DriverManager
from configparser import ConfigParser

config = ConfigParser()
config.read("config/config.ini")

@pytest.fixture
def driver():
    driver = DriverManager.get_driver()
    yield driver
    driver.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    driver.get(config.get("APP", "base_url"))
    login_page.login(config.get("APP", "valid_username"), config.get("APP", "valid_password"))
    assert "inventory.html" in driver.current_url

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    driver.get(config.get("APP", "base_url"))
    login_page.login("invalid_user", "invalid_pass")
    assert login_page.find_element(login_page.ERROR_MSG).is_displayed()