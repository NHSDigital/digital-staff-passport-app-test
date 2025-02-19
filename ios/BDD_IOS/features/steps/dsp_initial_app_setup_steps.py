"""Step definitions for dsp initial app setup"""

import logging

from behave import given, when, then
from pages.base_page import BasePage
from pages.ios_pages.dsp_initial_app_setup import DspInitialAppSetup


@when("user validates the first page and taps Continue")
def dsp_app_first_page_continue(context):
    context.dsp_app_initial_setup = DspInitialAppSetup(context.driver)
    context.dsp_app_initial_setup.app_first_page_validation()
    context.dsp_app_initial_setup.app_first_page_continue()

@then("create PIN page appears with external links")
def dsp_app_create_pin_page_checks(context):
    context.dsp_app_initial_setup.app_create_pin_question_button_validation()
    context.dsp_app_initial_setup.app_create_pin_agree_links_validation()

@then("user sets and confirms a new PIN")
def dsp_app_create_pin_enter_confirm(context):
    context.dsp_app_initial_setup.app_create_pin_enter(
        BasePage.get_test_data("CreatePin", "set_pin",
                               "test_data.yaml"))
    context.dsp_app_initial_setup.app_create_pin_confirm(
        BasePage.get_test_data("CreatePin", "confirm_pin",
                               "test_data.yaml"))

@then("app allows the user to proceed with the PIN setup")
def dsp_app_create_pin_continue_click(context):
    context.dsp_app_initial_setup.app_create_pin_continue()

@then("user views the Fingerprint page and taps Continue")
def dsp_app_fingerprint_continue_click(context):
    context.dsp_app_initial_setup.app_fingerprint_page_validation()
    context.dsp_app_initial_setup.app_fingerprint_page_continue()

@then("user navigates to the Prove who you are page and checks the content")
def dsp_app_prove_who_you_are_page_checks(context):
    context.dsp_app_initial_setup.app_prove_who_you_are_page_header_validation()
    context.dsp_app_initial_setup.app_prove_who_you_are_sub_header_validation()
    context.dsp_app_initial_setup.app_prove_who_you_are_page_text_validation()

@then("user taps Continue on the Prove who you are page")
def dsp_app_prove_who_you_are_page_continue_click(context):
    context.dsp_app_initial_setup.app_prove_who_you_are_page_continue_click()

@then("user sees Prove your identity page explaining the verification process")
def dsp_app_prove_your_identity_page_checks(context):
    context.dsp_app_initial_setup.app_prove_your_identity_page_validation()

@then("user can choose to Continue to verify their identity digitally")
def dsp_app_prove_your_identity_page_continue_click(context):
    context.dsp_app_initial_setup.app_prove_your_identity_page_continue_click()
