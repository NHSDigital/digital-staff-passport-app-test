"""Step definitions for android app poc feature"""
import logging

from behave import given
from pages.ios_pages.ios_app import IosAppAutomation



@given("the ios app is launched with the specified activity")
def step_when_launch_app_with_multiple_activities(context):
    """Step to launch the ios app with the specified activity"""
    context.driver = logging.FileHandler.selenium_driver = IosAppAutomation.open_ios_app(context)
    context.ios_app_homepage = IosAppAutomation(context.driver)
    context.ios_app_homepage.ios_app_homepage_click_on_continue_button()
