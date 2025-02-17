"""
Steps to revoke credentials in the wallet and validate its success by the HR user
"""

from behave import given, when, then

from pages.hr_pages.hr_archive_credential import HRArchiveCredentialPage
from pages.base_page import BasePage



@then("HR User clicked on Fire safety credential which needs to archive")
def hr_portal_click_on_fire_safety_credential_to_archive(context):
    context.hr_portal_archive_credential_page = HRArchiveCredentialPage(context.driver)
    context.hr_portal_archive_credential_page.hr_portal_click_on_fire_safety_credential()


@then("HR User validates the credential page header and click on archive this credential")
def hr_portal_click_on_fire_safety_credential_to_archive(context):
    context.hr_portal_archive_credential_page.hr_portal_click_on_archive_this_credential_link()


@then("HR User validates credential archived heading and click on back to Users passport link")
def hr_portal_click_on_fire_safety_credential_to_archive(context):
    context.hr_portal_archive_credential_page.hr_portal_credential_archive_success_message()
    context.hr_portal_archive_credential_page.hr_portal_click_on_back_to_user_passport_link()


@then("HR User clicks on Include archived credentials")
def hr_portal_click_on_fire_safety_credential_to_archive(context):
    context.hr_portal_archive_credential_page = HRArchiveCredentialPage(context.driver)
    context.hr_portal_archive_credential_page.hr_portal_click_on_include_archived_credentials()


@then("HR User clicks on Fire safety archived credential")
def hr_portal_click_on_fire_safety_credential_to_archive(context):
    context.hr_portal_archive_credential_page.hr_portal_click_on_fire_safety_credential()


@then("Validates Fire safety archived message successfully")
def hr_portal_click_on_fire_safety_credential_to_archive(context):
    context.hr_portal_archive_credential_page.hr_portal_credential_archive_page_success_message()


@then("HR User clicks on Fire safety auto archived credential")
def hr_portal_click_on_fire_safety_credential_to_archive(context):
    context.hr_portal_archive_credential_page.hr_portal_click_on_auto_archived_fire_safety_credential()


@then("Validates Fire safety auto archived message successfully")
def hr_portal_click_on_fire_safety_credential_to_archive(context):
    context.hr_portal_archive_credential_page.hr_portal_credential_archive_page_success_message()


@then("Restore archived credentials and validate its success message")
def hr_portal_click_on_fire_safety_credential_to_archive(context):
    context.hr_portal_archive_credential_page.hr_portal_click_on_restore_archived_credential_link()
    context.hr_portal_archive_credential_page.hr_portal_credential_archived_restore_page_success_message()
