"""
Steps to archive credentials from hr portal page steps
"""

from behave import then
from pages.hr_pages.hr_archive_credential import HRArchiveCredentialPage


@then("HR User clicked on Fire safety credential which needs to archive")
def hr_portal_click_fire_safety_credential(context):
    """Step to click on fire safety credential to archive"""
    context.hr_portal_archive_credential_page = HRArchiveCredentialPage(context.driver)
    context.hr_portal_archive_credential_page.hr_portal_click_on_fire_safety_credential()


@then("HR User validates the credential page header and click on archive this credential")
def hr_portal_validate_header_click_continue(context):
    """Step to validate the credential page header and click on archive this credential"""
    context.hr_portal_archive_credential_page.hr_portal_click_on_archive_this_credential_link()


@then("HR User validates credential archived heading and click on back to Users passport link")
def hr_portal_validate_heading_click_back(context):
    """Step to validate the credential page header and click on back"""
    context.hr_portal_archive_credential_page.hr_portal_credential_archive_success_message()
    context.hr_portal_archive_credential_page.hr_portal_click_on_back_to_user_passport_link()


@then("HR User clicks on Include archived credentials")
def hr_portal_click_on_include_archived_creds(context):
    """Step to click on Include archived credentials"""
    context.hr_portal_archive_credential_page = HRArchiveCredentialPage(context.driver)
    context.hr_portal_archive_credential_page.hr_portal_click_on_include_archived_credentials()


@then("HR User clicks on Fire safety archived credential")
def hr_portal_click_on_fire_safety_archived_creds(context):
    """Step to click on Fire safety credential archive creds"""
    context.hr_portal_archive_credential_page.hr_portal_click_on_fire_safety_credential()


@then("Validates Fire safety archived message successfully")
def hr_portal_validate_fire_safety_archived_message(context):
    """Step to validate Fire safety credential archive message successfully"""
    context.hr_portal_archive_credential_page.hr_portal_credential_archive_page_success_message()


@then("HR User clicks on Fire safety auto archived credential")
def hr_portal_click_fire_safety_auto_archived(context):
    """Step to click on Fire safety auto archived credential"""
    context.hr_portal_archive_credential_page.hr_portal_click_on_auto_archived_fire_safety_credential()


@then("Validates Fire safety auto archived message successfully")
def hr_portal_validate_auto_archived_fire_safety(context):
    """Step to validate success message Fire safety auto archived credential"""
    context.hr_portal_archive_credential_page.hr_portal_credential_archive_page_success_message()


@then("Restore archived credentials and validate its success message")
def hr_portal_restore_archived_creds_validate_message(context):
    """Step to restore archived credentials"""
    context.hr_portal_archive_credential_page.hr_portal_click_on_restore_archived_credential_link()
    context.hr_portal_archive_credential_page.hr_portal_credential_archived_restore_page_success_message()
