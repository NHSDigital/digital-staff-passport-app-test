"""
Steps definition w.r.t create a new identity credential features
"""
from behave import then
from pages.hr_pages.hr_create_new_identity_credential import HRPortalCreateNewIdentityCredentialPage


@then('Click on create a new identity credential link on staff passport for user page')
def hr_portal_create_a_new_identity_credential(context):
    """Steps tp create a new identity credential"""
    context.hr_portal_create_new_identity_credential_page = HRPortalCreateNewIdentityCredentialPage(
        context.driver)
    context.hr_portal_create_new_identity_credential_page.hr_portal_create_a_new_identity_credential()


@then('Verify user details on page and click on continue')
def hr_portal_verify_user_details(context):
    """Steps to verify user details on page and click on continue"""
    context.hr_portal_create_new_identity_credential_page.hr_portal_create_new_identity_credential_details_continue()


@then('Confirm users details and select yes provide credential radio button and proceed')
def hr_portal_select_yes_provide_credential(context):
    """Steps to confirm user details on page and click on continue"""
    context.hr_portal_create_new_identity_credential_page.hr_portal_create_new_identity_cred_yes_radio_button()


@then('User verify success message on webpage')
def hr_portal_verify_success_message(context):
    """Steps to verify success message on webpage"""
    context.hr_portal_create_new_identity_credential_page.hr_portal_new_identity_credential_provided_success()


@then('HR user validates the passport history event details w.r.t New Identity')
def hr_portal_verify_new_identity_creds_passport_event(context):
    """Steps to validate passport history event details w.r.t New Identity"""
    context.hr_portal_create_new_identity_credential_page.hr_portal_new_identity_creds_passport_history_event_details()
