"""
Steps definition for Pending staff passport features
"""
from behave import given, when, then
from pages.hr_pages.hr_pending_staff_passport import HRPendingStaffPassportPage
from pages.base_page import BasePage


@then('Click on the Pending Staff Passport Tab under HR Portal')
def hr_portal_pending_staff_passport(context):
    context.hr_portal_pending_staff_passport_page = HRPendingStaffPassportPage(context.driver)
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_staff_passport_tab()


@then('Enter the user details in the search button - Pending Staff Passport')
def hr_portal_pending_staff_username_search(context):
    context.hr_portal_pending_staff_passport_page = HRPendingStaffPassportPage(context.driver)
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_search_username(
        BasePage.get_test_data("IdentityReview", "username",
                               "test_data.yaml"))


@then('Click on the Search button - Pending Staff Passport')
def hr_portal_pending_staff_search_submit(context):
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_search_submit_click()


@then('Result is displayed & click on the same - Pending Staff Passport')
def hr_portal_pending_staff_search_result(context):
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_search_result()

@then('Click on the Alert link w.r.t review Credentials request')
def hr_portal_pending_staff_review_credentials_request(context):
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_click_review_credentials_request()


@then('Click on Provide Credentials Button')
def hr_portal_pending_staff_provide_credentials_button(context):
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_provide_credentials_button()


@then('Review the credentials request & select the provide radio button & Continue')
def hr_portal_pending_staff_provide_credentials(context):
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_provide_credentials()
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_provide_credentials_continue()

@then('Confirm on Yes radio button w.r.t credential request & Click Continue')
def hr_portal_pending_staff_confirm_yes_continue(context):
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_provide_credentials_confirm_yes()
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_provide_credentials_confirm_continue()

@then('Request reviewed successfully and message is displayed')
def hr_portal_pending_staff_review_request(context):
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_provide_credentials_reviewed_success()

@then('Click on Connect to ESR Link')
def hr_portal_pending_staff_connect_esr(context):
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_connect_esr()


@then('Enter the ESR Number & click on confirm button')
def hr_portal_pending_staff_enter_esr_confirm(context):
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_enter_esr_number(
        BasePage.get_test_data("CredentialReview", "esr_cov",
                               "test_data.yaml"))
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_confirm_esr_number()


@then('Click on Connect to Passport Link & connect button')
def hr_portal_pending_staff_connect_passport(context):
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_connect_to_passport()
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_passport_connect_proceed()


@then('Select Yes radio button & click on continue button')
def hr_portal_pending_staff_confirm_yes_continue(context):
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_connect_to_passport_confirm_yes()
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_connect_to_passport_confirm_continue()


@then('Click on Provide Credentials Link')
def hr_portal_pending_staff_provide_credentials_link(context):
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_provide_credentials_link()


@then('Click on the back link to navigate back to passport page')
def hr_portal_pending_staff_go_back_link_passport_page(context):
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_back_link_passport_page()

@then('Click on Manage Passport Link')
def hr_portal_pending_staff_manage_passport_link(context):
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_manage_passport_link()

@then('Click on Delete Passport Link')
def hr_portal_pending_staff_delete_passport_link(context):
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_delete_passport_link()


@then('Click on Delete Passport Continue button')
def hr_portal_pending_staff_delete_passport_button(context):
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_delete_passport_continue()


@then('Click on Delete Passport data button')
def hr_portal_pending_staff_delete_passport_data_button(context):
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_delete_passport_data()


@then('Verify the message is displayed w.r.t Delete passport')
def hr_portal_pending_staff_delete_passport_message(context):
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_delete_passport_message()

@then('Enter the auto user details in the search button - Pending Staff Passport')
def hr_portal_pending_staff_auto_username_search(context):
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_search_username(
        BasePage.get_test_data("IdentityReview", "username",
                               "test_data.yaml"))

@then("Click on the Alert link w.r.t review Shared Credentials request")
def hr_portal_pending_staff_shared_review_credentials_request(context):
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_click_shared_review_credentials_request()


@then("Confirm on Accept radio button w.r.t credential request & Click Continue")
def hr_portal_pending_staff_shared_review_creds_accept_continue(context):
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_click_shared_review_accept_radio_button()
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_click_shared_provide_credentials_confirm_continue()


@then("Confirm on Yes radio button w.r.t Shared credential request & Click Continue")
def hr_portal_pending_staff_shared_review_creds_confirm_yes_continue(context):
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_click_shared_provide_credentials_confirm_yes()
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_click_shared_provide_credentials_confirm_continue()


@then("Shared cred request reviewed successfully and message is displayed")
def hr_portal_pending_staff_shared_creds_review_request_success(context):
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_provide_shared_credentials_reviewed_success()
