from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    # Locators
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")   
    FINISH_BUTTON = (By.ID, "finish")   

    # Actions
    def enter_checkout_info(self, first_name, last_name, zip_code):
        self.find_element(self.FIRST_NAME_INPUT).send_keys(first_name)
        self.find_element(self.LAST_NAME_INPUT).send_keys(last_name)
        self.find_element(self.ZIP_CODE_INPUT).send_keys(zip_code)
        self.find_element(self.CONTINUE_BUTTON).click()
        self.find_element(self.FINISH_BUTTON).click()
