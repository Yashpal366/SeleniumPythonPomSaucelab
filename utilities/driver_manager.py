from selenium import webdriver

class DriverManager:
    @staticmethod
    def get_driver():
        driver = webdriver.Chrome()
        driver.maximize_window()
        return driver