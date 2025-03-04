"""Step definitions for dsp initial app setup"""

import logging

from behave import given, when, then
from pages.base_page import BasePage
from pages.ios_pages.dsp_initial_app_setup import DspInitialAppSetup


@when("user verifies the question icon present")
def dsp_app_verify_question_icon(context):
    context.dsp_app_initial_setup = DspInitialAppSetup(context.driver)
    assert context.dsp_app_initial_setup.verify_question_icon(), "first page question icon is not present"



@then("user verifies the text on the “First page”")
def dsp_app_verify_first_page_text(context):
    context.dsp_app_initial_setup.verify_app_first_page_setup_dsp_text()


@then("user clicks on “Continue” button")
def dsp_app_click_continue(context):
    assert context.dsp_app_initial_setup.click_continue(), "Continue button is not present"


@then("user verifies “Create a PIN” opened")
def dsp_app_verify_create_pin_header(context):
    context.dsp_app_initial_setup.verify_create_pin_page_header()


@then("user verifies term of use link present")
def dsp_app_verify_terms_of_use_agreement_link(context):
    assert context.dsp_app_initial_setup.verify_terms_of_use_link(), "term of use link is not present"


@then("user verifies privacy notice link present")
def dsp_app_verify_privacy_agreement_link(context):
    assert context.dsp_app_initial_setup.verify_privacy_agreement_link(), "privacy notice link is not present"


@then("user verifies terms link present")
def dsp_app_verify_terms_agreement_link(context):
    assert context.dsp_app_initial_setup.verify_terms_agreement_link(), "terms link is not present"


@then("user sets new PIN")
def dsp_app_create_pin_sets_new(context):
    context.dsp_app_initial_setup.app_create_pin_enter(
        BasePage.get_test_data("CreatePin", "set_pin",
                               "test_data.yaml"))


@then("user confirms new PIN")
def dsp_app_create_pin_confirm(context):
    context.dsp_app_initial_setup.app_create_pin_confirm(
        BasePage.get_test_data("CreatePin", "confirm_pin",
                               "test_data.yaml"))


@then("user verifies “Fingerprint” page opened")
def dsp_app_verify_finger_print_header(context):
    context.dsp_app_initial_setup.verify_fingerprint_page_header()


@then("user verifies account and setting icon present")
def dsp_app_verify_account_icon(context):
    assert context.dsp_app_initial_setup.verify_account_icon(), "account icon is not present"


@then("user clicks “Enable Fingerprint recognition” toggle to enable")
def dsp_app_verify_finger_print_enable(context):
    assert context.dsp_app_initial_setup.enable_disable_figer_print_recognition(), "finger print toggle is not present"


@then("user clicks “Enable Fingerprint recognition” toggle to disable")
def dsp_app_verify_finger_print_disable(context):
    assert context.dsp_app_initial_setup.enable_disable_figer_print_recognition(), "finger print toggle is not present"


@then("user verifies “Prove who you are” page opened")
def verify_prove_who_you_are_page_header(context):
    context.dsp_app_initial_setup.verify_prove_who_you_are_page_header()


@then("user verifies the text on the “Prove who you are” page")
def verify_prove_who_you_are_page_text(context):
    context.dsp_app_initial_setup.verify_prove_who_you_are_sub_header()
    context.dsp_app_initial_setup.verify_prove_who_you_are_page_text()


@then("user verifies “Prove your identity” page opened")
def verify_prove_your_identity_header(context):
    context.dsp_app_initial_setup.verify_prove_your_identity_header()


@then("user verifies what to expect heading")
def verify_prove_identity_what_to_expect_heading(context):
    context.dsp_app_initial_setup.verify_prove_identity_what_to_expect_heading()


@then("user verifies what happens then heading")
def verify_prove_identity_what_happens_heading(context):
    context.dsp_app_initial_setup.verify_prove_identity_what_happens_heading()


@then("user verifies my identity in person link present")
def verify_prove_identity_in_person_link(context):
    assert context.dsp_app_initial_setup.verify_prove_identity_in_person_link(), ("identity in person link is not "
                                                                                  "present")
