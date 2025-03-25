"""Step definitions for sign in after initial setup steps"""
from behave import when, then
from pages.ios_pages.app_sign_in_after_initial_setup import SignInAfterInitialSetup
from pages.base_page import BasePage


@when("User Click on I've forgotton my pin link")
def initial_setup_forgot_pin(context):
    """ Step to click on I;ve forgotten my pin link"""
    context.sign_in_after_initial_setup = SignInAfterInitialSetup(context.driver)
    context.sign_in_after_initial_setup.click_on_forgotton_pin_link()


@then("User Verifies forgotten pin message is displaying")
def initial_setup_forgot_pin_message(context):
    """ Steo to verify forgotten pin message"""
    context.sign_in_after_initial_setup.forgotten_pin_error()


@when("User enters incorrect pin on enter your pin box")
def initial_setup_incorrect_pin_enter(context):
    """ Step to enter incorrect pin on enter your pin box"""
    context.sign_in_after_initial_setup.enter_incorrect_pin_value_in_input_box()
    BasePage.get_test_data("IdentityReview", "Incorrect_pin",
                           "test_data.yaml")


@then("User clicks on Continue button on log in page")
def initial_setup_click_continue(context):
    """ Step to click on Continue button on log in page"""
    context.sign_in_after_initial_setup.click_continue_button()


@then("User verifies Incorrect Pin error message on UI screen for 2 attempts remaining")
def initial_setup_incorrect_pin_error_message(context):
    """ Step to verify Incorrect pin. you have (2) tries remaining"""
    context.sign_in_after_initial_setup.incorrect_pin_2attempts_remaining_error()


@then("User re-enters incorrect pin on enter your pin box")
def initial_setup_reenter_incorrect_pin(context):
    """step to re-enter incorrect pin on enter your pin box"""
    context.sign_in_after_initial_setup.enter_incorrect_pin_value_in_input_box()


@then("User verifies Incorrect Pin error message on UI screen for 1 attempts remaining")
def initial_setup_verify_incorrect_pin(context):
    """step to verify Incorrect pin. you have (1) tries remaining"""
    context.sign_in_after_initial_setup.incorrect_pin_1attempts_remaining_error()


@then("User verifies maximum number of login attempt exceeded")
def initial_setup_max_number_login_attempt(context):
    """Step to verify maximum number of login attempt exceeded"""
    context.sign_in_after_initial_setup.maximum_number_of_login_exceeded_error()
