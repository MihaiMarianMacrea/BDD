from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    URL = "https://the-internet.herokuapp.com/login"

    EMAIL_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "radius")
    FLASH_CONTAINER = (By.ID, "flash-messages")

    def navigate_to_page(self):
        self.driver.get(self.URL)

    def set_email(self, email):
        self.type(self.EMAIL_INPUT, email)

    def set_password(self, password):
        self.type(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def is_message_displayed(self):
        return self.wait_for_element(self.FLASH_CONTAINER, 10).is_displayed()

    def get_message_text(self):
        return self.get_element_text(self.FLASH_CONTAINER)