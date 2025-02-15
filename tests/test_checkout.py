import json
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from configparser import ConfigParser
from utilities.driver_manager import DriverManager

config = ConfigParser()
config.read("config/config.ini")


def load_test_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


test_data = load_test_data("test_data/test_data.json")


@pytest.fixture
def driver():
    driver = DriverManager.get_driver()
    yield driver
    driver.quit()


@pytest.mark.parametrize("checkout_info", test_data['checkout_info'])
def test_checkout_flow(driver, checkout_info):
    # Login
    login_page = LoginPage(driver)
    driver.get(config.get("APP", "base_url"))
    login_page.login(config.get("APP", "valid_username"), config.get("APP", "valid_password"))
    
    # Add product to cart
    products_page = ProductsPage(driver)
    products_page.add_product_to_cart()
    products_page.go_to_cart()
    
    # Checkout
    cart_page = CartPage(driver)
    cart_page.click_checkout()
    
    # Fill checkout info
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_checkout_info(checkout_info["first_name"], checkout_info["last_name"], checkout_info["zip_code"])
    assert "checkout-complete.html" in driver.current_url
