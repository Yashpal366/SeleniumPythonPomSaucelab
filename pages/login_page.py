from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, ".error-message-container")

    # Actions
    def login(self, username, password):
        self.find_element(self.USERNAME).send_keys(username)
        self.find_element(self.PASSWORD).send_keys(password)
        self.find_element(self.LOGIN_BUTTON).click()