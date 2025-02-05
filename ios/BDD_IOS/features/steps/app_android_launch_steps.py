"""Step definitions for android app poc feature"""
import logging

from behave import given, when, then
from ios.BDD_IOS.pages.app_safari_launch import SafariAppAutomation
from ios.BDD_IOS.pages.base_page import BasePage


@given("Uninstall the app if present")
def step_given_app_not_installed(context):
    context.driver = logging.FileHandler.selenium_driver = SafariAppAutomation(context)
    context.android_app_automation = SafariAppAutomation(context.driver)
    context.android_app_automation.check_app_not_installed()


@when("user install the app using APKs")
def step_when_install_app(context):
    context.android_app_automation.install_aos_app()


@then("the app should be installed successfully")
def step_then_app_installed_successfully(context):
    context.android_app_automation.check_app_installed()


@given("the app is already installed")
def step_given_app_already_installed(context):
    context.driver = logging.FileHandler.selenium_driver = SafariAppAutomation(context)
    context.android_app_automation = SafariAppAutomation(context.driver)
    context.android_app_automation.check_app_installed()


@given("the app is launched with the specified activity")
def step_when_launch_app_with_multiple_activities(context):
    context.driver = logging.FileHandler.selenium_driver = SafariAppAutomation.open_ios_app(context)
    context.android_app_automation = SafariAppAutomation(context.driver)
    context.android_app_automationn.click_on_continue_button()


@when("the user logs in with username and password")
def step_app_android_login_screen(context):
    context.android_app_automation.app_username(
        (BasePage.get_test_data("LoginCredentials", "username", "test_data.yaml")))
    context.android_app_automation.app_password((BasePage.get_test_data("LoginCredentials",
                                                                        "password", "test_data.yaml")))
    context.android_app_automation.app_login_click()


@then("the user navigates to the home screen")
def step_app_android_navigate_home_screen(context):
    context.android_app_automation.app_navigate_to_home_screen()


@then("searches for the NHS profile")
def step_app_android_search_profile(context):
    context.android_app_automation.app_search_tab_click()
    context.android_app_automation.profile_search_text_enter("nhs")


@then("user attempt to close mobile app")
def step_app_android_close_mobile_app(context):
    context.android_app_automation.close_app()
