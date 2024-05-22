from behave import *

@given('I am on the alerts page')
def step_impl(context):
    context.alerts_page.navigate_to_page()

@when('I click on Click for JS alert button')
def step_impl(context):
    context.alerts_page.click_ok_alert()

@when('I accept OK alert')
def step_impl(context):
    context.alerts_page.accept_ok_alert()

@then('The message for alerts page is "{message}"')
def step_impl(context, message):
    assert message in context.alerts_page.get_result_text()