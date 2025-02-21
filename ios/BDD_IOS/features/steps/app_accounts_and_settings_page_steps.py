"""Step definitions for app accounts and settings page steps"""
import logging

from behave import given, when, then
from pages.ios_pages.app_accounts_and_settings import AppAccountsandSettings
from pages.base_page import BasePage


@then("User clicks on accounts and settings tab")
def sign_in_after_initial_setup_steps(context):
    """ Step to click on accounts and settings tab"""
    context.App_accounts_and_settings_page = AppAccountsandSettings(context.driver)
    context.AppAccountsandSettings.click_account_and_settings_tab()


@then("User validate accounts and settings page heading")
def sign_in_after_initial_setup_steps(context):
    """ Step to validate accounts and settings page heading"""
    context.AppAccountsandSettings.verify_account_and_settings_heading()


@then("User Validate question mark icon on account and settings Page")
def sign_in_after_initial_setup_steps(context):
    """ Step to validate question mark icon on account and settings Page"""
    context.AppAccountsandSettings.verify_and_click_question_mark_icon()


@then("User clicks on back link on account and settings page")
def sign_in_after_initial_setup_steps(context):
    """ Step to clicks on back link on account and settings page """
    context.AppAccountsandSettings.click_on_back_link()


@then("User validate delete your NHS digital staff passport on Page")
def sign_in_after_initial_setup_steps(context):
    """ Step to validate delete your NHS digital staff passport on Page"""
    context.AppAccountsandSettings.verify_delete_your_staff_passport_page()


@then("User clicks on terms of use and other policies link")
def sign_in_after_initial_setup_steps(context):
    """step to clicks on terms of use and other policies link """
    context.AppAccountsandSettings.click_on_terms_of_use_and_other_policies()

