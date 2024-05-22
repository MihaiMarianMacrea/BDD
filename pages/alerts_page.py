from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AlertsPage(BasePage):

    URL = "https://the-internet.herokuapp.com/javascript_alerts"

    ALERT_OK_BUTTON_SELECTOR = (By.XPATH, "//button[contains(text(), 'Click for JS Alert')]")
    RESULT_SELECTOR = (By.ID, "result")

    def navigate_to_page(self):
        self.driver.get(self.URL)

    def click_ok_alert(self):
        self.click(self.ALERT_OK_BUTTON_SELECTOR)

    def accept_ok_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def accept_second_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def cancel_second_alert(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def get_result_text(self):
        return self.get_element_text(self.RESULT_SELECTOR)
