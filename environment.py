from driver import Driver
from pages.login_page import LoginPage
from pages.alerts_page import AlertsPage

def before_all(context):
    context.browser = Driver()
    context.login_page = LoginPage()
    context.alerts_page = AlertsPage()

def after_all(context):
    context.browser.close()