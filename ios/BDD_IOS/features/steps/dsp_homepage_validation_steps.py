"""Step definitions for android app poc feature"""
import logging

from behave import given, when, then
from pages.base_page import BasePage
from pages.ios_pages.dsp_org_accept_id import DspOrgAcceptID


@when("user enters the pin and click on continue")
def dsp_app_enter_pin(context):
    context.dsp_app_homepage = DspOrgAcceptID(context.driver)
    context.dsp_app_homepage.app_enter_pin()
    context.dsp_app_homepage.app_enter_pin_continue()

@then("user verify the welcome message on the homepage")
def dsp_app_validate_welcome_message(context):
    context.dsp_app_homepage.app_homepage_welcome_message()

@then("user validates if question icon is present")
def dsp_app_validate_question_icon(context):
    context.dsp_app_homepage.app_homepage_question_icon_validation()

@then("user validates if account icon is present")
def dsp_app_validate_account_icon(context):
    context.dsp_app_homepage.app_homepage_account_icon_validation()

@then("user validates if homepage has action section present")
def dsp_app_validate_homepage_tab(context):
    context.dsp_app_homepage.app_homepage_action_validate()

@then("user validates if credentials tab is present")
def dsp_app_validate_homepage_credentials_tab(context):
    context.dsp_app_homepage.app_homepage_credentials_tab_validate()

@then("user validate that new provided credentials are visible on homepage")
def dsp_app_validate_new_provided_creds_on_homepage(context):
    context.dsp_app_homepage.validate_new_provided_credentials_on_homepage()


@then("user validate the tag present on the new credentials")
def dsp_app_validate_tag_on_new_credentials(context):
    context.dsp_app_homepage.validate_tag_on_new_credentials()
