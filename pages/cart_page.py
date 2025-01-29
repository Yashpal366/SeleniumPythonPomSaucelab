from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    # Locators
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEM = (By.CLASS_NAME, "cart_item")

    # Actions
    def click_checkout(self):
        self.find_element(self.CHECKOUT_BUTTON).click()