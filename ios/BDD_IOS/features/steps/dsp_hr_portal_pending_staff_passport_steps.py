"""
Steps definition for Pending staff passport features
"""
from behave import then, when
from pages.hr_pages.hr_pending_staff_passport import HRPendingStaffPassportPage
from pages.base_page import BasePage


@then('Click on the Pending Staff Passport Tab under HR Portal')
def hr_portal_pending_staff_passport(context):
    """step implementation Click on the Pending Staff Passport Tab under HR Portal"""
    context.hr_portal_pending_staff_passport_page = HRPendingStaffPassportPage(context.driver)
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_staff_passport_tab()


@then('Enter the user details in the search button - Pending Staff Passport')
def hr_portal_pending_staff_username_search(context):
    """step implementation Enter the user details in the search button - Pending Staff Passport"""
    context.hr_portal_pending_staff_passport_page = HRPendingStaffPassportPage(context.driver)
    # context.hr_portal_pending_staff_passport_page.hr_portal_pending_search_username(
    #     BasePage.get_test_data("IdentityReview", "username",
    #                            "test_data.yaml"))
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_search_username("JACOB SEBASTIAN")





@then('Click on the Search button - Pending Staff Passport')
def hr_portal_pending_staff_search_submit(context):
    """step implementation Click on the Search button - Pending Staff Passport"""
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_search_submit_click()


@then('Result is displayed & click on the same - Pending Staff Passport')
def hr_portal_pending_staff_search_result(context):
    """step implementation Result is displayed & click on the same - Pending Staff Passport"""
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_search_result()


@then('Click on the Alert link w.r.t review Credentials request')
def hr_portal_pending_staff_review_credentials_request(context):
    """step implementation to click on alert link wrt to review credentials request"""
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_click_review_credentials_request()


@then('Click on Provide Credentials Button')
def hr_portal_pending_staff_provide_credentials_button(context):
    """step implementation to click on provide credentials button"""
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_provide_credentials_button()


@then('Review the credentials request & select the provide radio button & Continue')
def hr_portal_pending_staff_provide_credentials(context):
    """step implementation Review the credentials request & select the provide radio button & Continue"""
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_provide_credentials()
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_provide_credentials_continue()


@then('Confirm on Yes radio button w.r.t credential request & Click Continue')
def hr_portal_pending_staff_confirm_yes_continue(context):
    """step implementation Confirm on Yes radio button w.r.t credential request & Click Continue"""
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_provide_credentials_confirm_yes()
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_provide_credentials_confirm_continue()


@then('Request reviewed successfully and message is displayed')
def hr_portal_pending_staff_review_request(context):
    """step implementation Request reviewed successfully and message is displayed"""
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_provide_credentials_reviewed_success()


@then('Click on Connect to ESR Link')
def hr_portal_pending_staff_connect_esr(context):
    """step implementation Click on Connect to ESR Link"""
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_connect_esr()


@then('Enter the ESR Number & click on confirm button')
def hr_portal_pending_staff_enter_esr_confirm(context):
    """step implementation Enter the ESR Number & click on confirm button"""
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_enter_esr_number(
        BasePage.get_test_data("CredentialReview", "esr_cov",
                               "test_data.yaml"))
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_confirm_esr_number()


@then('Click on Connect to Passport Link & connect button')
def hr_portal_pending_staff_connect_passport(context):
    """step implementation Click on Connect to Passport Link & connect button"""
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_connect_to_passport()
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_passport_connect_proceed()


@then('Select Yes radio button & click on continue button')
def select_yes_radio_button_click_continue(context):
    """step implementation Select Yes radio button & click on continue button"""
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_connect_to_passport_confirm_yes()
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_connect_to_passport_confirm_continue()


@then('Click on Provide Credentials Link')
def hr_portal_pending_staff_provide_credentials_link(context):
    """step implementation Click on Provide Credentials Link"""
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_provide_credentials_link()


@then('Click on the back link to navigate back to passport page')
def hr_portal_pending_staff_go_back_link_passport_page(context):
    """step implementation Click on the back link to navigate back to passport page"""
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_back_link_passport_page()


@then('Click on Manage Passport Link')
def hr_portal_pending_staff_manage_passport_link(context):
    """step implementation Click on Manage Passport Link"""
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_manage_passport_link()


@then('Click on Delete Passport Link')
def hr_portal_pending_staff_delete_passport_link(context):
    """step implementation Click on Delete Passport Link"""
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_delete_passport_link()


@then('Click on Delete Passport Continue button')
def hr_portal_pending_staff_delete_passport_button(context):
    """step implementation Click on Delete Passport Continue button"""
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_delete_passport_continue()


@then('Click on Delete Passport data button')
def hr_portal_pending_staff_delete_passport_data_button(context):
    """step implementation Click on Delete Passport data button"""
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_delete_passport_data()


@then('Verify the message is displayed w.r.t Delete passport')
def hr_portal_pending_staff_delete_passport_message(context):
    """step implementation Verify the message is displayed w.r.t Delete passport"""
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_delete_passport_message()


@then('Enter the auto user details in the search button - Pending Staff Passport')
def hr_portal_pending_staff_auto_username_search(context):
    """step implementation Enter the user details in the search button - Pending Staff Passport"""
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_search_username(
        BasePage.get_test_data("IdentityReview", "username",
                               "test_data.yaml"))


@then("Click on the Alert link w.r.t review Shared Credentials request")
def hr_portal_pending_staff_shared_review_credentials_request(context):
    """step implementation to click on alert link wrt to review Shared credentials request"""
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_click_shared_review_credentials_request()


@then("Confirm on Accept radio button w.r.t credential request & Click Continue")
def hr_portal_pending_staff_shared_review_creds_accept_continue(context):
    """step implementation Confirm on Accept radio button w.r.t Shared credential request & Click Continue"""
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_click_shared_review_accept_radio_button()
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_click_shared_provide_credentials_confirm_continue()


@then("Confirm on Yes radio button w.r.t Shared credential request & Click Continue")
def hr_portal_pending_staff_shared_review_creds_confirm_yes_continue(context):
    """step implementation Confirm on Yes radio button w.r.t Shared credential request & Click Continue"""
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_click_shared_provide_credentials_confirm_yes()
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_click_shared_provide_credentials_confirm_continue()


@then("Shared cred request reviewed successfully and message is displayed")
def hr_portal_pending_staff_shared_creds_review_request_success(context):
    """step implementation Shared cred request reviewed successfully and message is displayed"""
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_provide_shared_credentials_reviewed_success()


@then("Click on view credential inside 3 pending credential banner")
def hr_portal_pending_staff_view_credential(context):
    """step implementation Click on view credential inside 3 pending credential banner"""
    context.hr_portal_pending_staff_passport_page.hr_portal_click_pending_view_credential()

@then("verify back link is displayed")
def verify_back_link_displayed(context):
    """step implementation verify back link is displayed"""
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_back_link_displayed()

@then("verify the link - remind username to review credential")
def verify_remind_username_review_credential_link(context):
    """step implementation verify the link - remind username to review credential"""
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_remind_username_review_credential_link()

@then("verify credential heading has identity and new starter information sub heading")
def verify_credential_heading_sub_heading(context):
    """step implementation verify credential heading has identity and new starter information sub heading"""
    context.hr_portal_pending_staff_passport_page.hr_portal_pending_credential_heading_sub_heading()

@when("user clicks on expand button for DBS supporting information")
def click_expand_button_dbs_supporting_info(context):
    """step implementation user clicks on expand button for DBS supporting information"""
    context.hr_portal_pending_staff_passport_page.hr_portal_click_pending_view_credential_button()

@then("user verify the credentials details should match")
def verify_credentials_details_match(context):
    """step implementation user verify the credentials details should match"""
    mismatches = {}

    for row in context.table:
        attribute = row["attribute"]
        expected_value = row["expected_value"]
        actual_value = context.hr_portal_pending_staff_passport_page.hr_portal_read_the_supplied_attribute(attribute)

        if expected_value != actual_value:
            mismatches[attribute] = {"expected": expected_value, "actual": actual_value}

    assert not mismatches, f"Data Mismatch Found: {mismatches}"
