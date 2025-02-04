"""Step definitions for android app poc feature"""
import logging

from behave import given, when, then
from pages.app_safari_launch import SafariAppAutomation
from pages.base_page import BasePage
from pages.ios_app import IosAppAutomation


@given("the ios app is launched with the specified activity")
def step_when_launch_app_with_multiple_activities(context):
    context.driver = logging.FileHandler.selenium_driver = IosAppAutomation.open_ios_app(context)
    context.ios_app_automation = IosAppAutomation(context.driver)
    context.ios_app_automation.ios_app_homepage_click_on_continue_button()

@when("Click on the continue button on prove your identity page")
def step_when_launch_app_with_multiple_activities(context):
    context.ios_app_automation = IosAppAutomation(context.driver)
    context.ios_app_automation.ios_app_prove_identity_pre_click_on_continue_button()
    context.ios_app_automation.ios_app_prove_identity_post_click_on_continue_button()
    context.ios_app_automation.ios_app_identity_confirmed_continue_button()

@then("Click on the credentials that are ready to review")
def step_when_launch_app_with_multiple_activities(context):
    context.ios_app_automation = IosAppAutomation(context.driver)
    context.ios_app_automation.credentials_ready_to_review_xpath()

@then("Click on credentials tab")
def step_when_launch_app_with_multiple_activities(context):
    context.ios_app_automation = IosAppAutomation(context.driver)
    context.ios_app_automation.credentials_tab_xpath()

@then("Click on connections tab")
def step_when_launch_app_with_multiple_activities(context):
    context.ios_app_automation = IosAppAutomation(context.driver)
    context.ios_app_automation.connection_tab_xpath()

@then("Click on messages tab")
def step_when_launch_app_with_multiple_activities(context):
    context.ios_app_automation = IosAppAutomation(context.driver)
    context.ios_app_automation.messages_tab_xpath()
