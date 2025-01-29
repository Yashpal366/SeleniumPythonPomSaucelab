from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsPage(BasePage):
    # Locators
    PRODUCT_HEADER = (By.CLASS_NAME, "title")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    # Actions
    def add_product_to_cart(self):
        self.find_element(self.ADD_TO_CART_BUTTON).click()

    def go_to_cart(self):
        self.find_element(self.CART_ICON).click()