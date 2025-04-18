"""Step definitions for app accounts and settings page steps"""
from behave import then
from pages.ios_pages.app_accounts_and_settings import AppAccountsandSettings


@then("User clicks on accounts and settings tab")
def sign_in_after_initial_setup_steps(context):
    """ Step to click on accounts and settings tab"""
    context.App_accounts_and_settings_page = AppAccountsandSettings(context.driver)
    context.AppAccountsandSettings.click_account_and_settings_tab()


@then("User validate accounts and settings page heading")
def validate_account_and_settings_heading(context):
    """ Step to validate accounts and settings page heading"""
    context.AppAccountsandSettings.verify_account_and_settings_heading()


@then("User Validate question mark icon on account and settings Page")
def validate_question_mark_settings(context):
    """ Step to validate question mark icon on account and settings Page"""
    context.AppAccountsandSettings.verify_and_click_question_mark_icon()


@then("User clicks on back link on account and settings page")
def click_back_link_on_account_settings_page(context):
    """ Step to clicks on back link on account and settings page """
    context.AppAccountsandSettings.click_on_back_link()


@then("User validate delete your NHS digital staff passport on Page")
def validate_delete_your_nhs_dsp(context):
    """ Step to validate delete your NHS digital staff passport on Page"""
    context.AppAccountsandSettings.verify_delete_your_staff_passport_page()


@then("User clicks on terms of use and other policies link")
def click_on_terms_of_use(context):
    """step to clicks on terms of use and other policies link """
    context.AppAccountsandSettings.click_on_terms_of_use_and_other_policies()
