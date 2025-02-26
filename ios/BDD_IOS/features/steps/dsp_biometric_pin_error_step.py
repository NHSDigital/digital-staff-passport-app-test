import logging


from behave import given, when, then
from pages.base_page import BasePage
from pages.ios_pages.dsp_biometric_pin_error import DspBiometricPinError


@then('user enter "{pin1}" & "{pin2}" that does not match')
def dsp_pin_error_enter_pin(context, pin1, pin2):
    context.pin_error = DspBiometricPinError(context.driver)
    context.pin_error.app_pin_error_enter_pin1()
    context.pin_error.app_pin_error_enter_pin1()

@then("user clicks on continue button - create a pin page")
def dsp_app_create_pin_continue_button(context):
    context.pin_error.app_create_pin_continue_button()


@then('user validates the error "{message}"')
def dsp_pin_error_validation(context, message):
    error_pin_do_not_match = 'PINs do not match'
    error_pin_not_six_digit = 'PIN must be 6 digits, with no number repeated 3 times, and not sequential'
    messages_provide = {
        "PIN doesn’t match": (context.pin_error.app_pin_does_not_match_validation, error_pin_do_not_match),
        "Empty input fields": (context.pin_error.app_pin_empty_validation, error_pin_not_six_digit),
        "Enter alpha numeric": (context.pin_error.app_pin_alpha_numeric_validation, error_pin_not_six_digit),
        "Enter special character": (context.pin_error.app_pin_special_character_validation, error_pin_not_six_digit),
        "Cannot use sequential PIN": (context.pin_error.app_pin_sequential_validation, error_pin_not_six_digit),
        "Cannot use reverse sequential as well": (context.pin_error.app_pin_reverse_sequential_validation, error_pin_not_six_digit),
        "PIN not repeated": (context.pin_error.app_pin_not_repeated_validation, error_pin_do_not_match),
        "PIN not repeated vice versa": (context.pin_error.app_pin_not_repeated_viceversa_validation, error_pin_not_six_digit),
        "PIN not 6 digits": (context.pin_error.app_pin_not_six_digit_validation, error_pin_not_six_digit)
    }
    assert messages_provide[message][0] == messages_provide[message][1]
