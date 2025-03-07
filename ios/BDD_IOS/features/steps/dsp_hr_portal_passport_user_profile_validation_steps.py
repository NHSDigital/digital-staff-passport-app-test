"""
Steps definition w.r.t hr portal user profile validation
"""
from behave import then
from pages.hr_pages.hr_passport_user_profile_validation import HrPortalPassportUserProfileValidation
from pages.base_page import BasePage


@then('Validate the passport status w.r.t pending credential')
def hr_portal_passport_status_pending_creds(context):
    """Steps to validate the passport status w.r.t pending credential"""
    context.hr_portal_passport_page = HrPortalPassportUserProfileValidation(context.driver)
    context.hr_portal_passport_page.hr_portal_passport_page_initial_status_validation()


@then('Click on the Show all detail by perform a scroll')
def hr_portal_passport_scroll_to_element(context):
    """Steps to click on the Show all detail by perform a scroll"""
    context.hr_portal_passport_page = HrPortalPassportUserProfileValidation(context.driver)
    context.hr_portal_passport_page.hr_portal_passport_page_click_on_show_details()


@then('Verify that fname is displayed')
def hr_portal_passport_fname_validation(context):
    """Steps to verify that fname is displayed"""
    context.hr_portal_passport_page.hr_portal_passport_page_firstname(
        BasePage.get_test_data("RegisterUser", "name", "test_data.yaml"))


@then('Verify that lname is displayed')
def hr_portal_passport_lname_validation(context):
    """Steps to verify that lname is displayed"""
    context.hr_portal_passport_page.hr_portal_passport_page_lastname(
        BasePage.get_test_data("RegisterUser", "surname", "test_data.yaml"))


@then('Verify that date of birth is displayed')
def hr_portal_passport_date_of_birth_displayed(context):
    """Steps to verify that date of birth is displayed"""
    context.hr_portal_passport_page.hr_portal_passport_page_dob(
        BasePage.get_test_data("RegisterUser", "dob", "test_data.yaml"))


@then('Verify that telephone number is displayed')
def hr_portal_passport_telephone_number_displayed(context):
    """Steps to verify that telephone number is displayed"""
    context.hr_portal_passport_page.hr_portal_passport_page_telephone(
        BasePage.get_test_data("RegisterUser", "phone_number", "test_data.yaml"))


@then('Verify that email is displayed')
def hr_portal_passport_email_displayed(context):
    """Steps to verify that email is displayed"""
    context.hr_portal_passport_page.hr_portal_passport_page_email_address(
        BasePage.get_test_data("RegisterUser", "email", "test_data.yaml"))


@then('Verify that staff group is displayed')
def hr_portal_passport_staff_group_displayed(context):
    """Steps to verify that staff group is displayed"""
    context.hr_portal_passport_page.hr_portal_passport_page_staff_group(
        BasePage.get_test_data("RegisterUser", "staff_group", "test_data.yaml"))


@then('Verify that employment type is displayed')
def hr_portal_passport_employment_type_displayed(context):
    """Steps to verify that employment type is displayed"""
    context.hr_portal_passport_page.hr_portal_passport_page_emp_type(
        BasePage.get_test_data("IdentityReview", "employment_type1", "test_data.yaml"))


@then('Verify that employment status is displayed')
def hr_portal_passport_employment_status_displayed(context):
    """Steps to verify that employment status is displayed"""
    context.hr_portal_passport_page.hr_portal_passport_page_emp_stat(
        BasePage.get_test_data("RegisterUser", "emp_status", "test_data.yaml"))


@then('User clicks on the complete credential required & validate the same')
def hr_portal_passport_page_complete_creds_required(context):
    """Steps to verify that user clicks on the complete credential required & validate"""
    context.hr_portal_passport_page = HrPortalPassportUserProfileValidation(context.driver)
    context.hr_portal_passport_page.hr_portal_passport_page_complete_creds_required()


@then('Validate the passport status w.r.t complete credential')
def hr_portal_passport_status_complete_creds(context):
    """Steps to validate the passport status w.r.t complete credential"""
    context.hr_portal_passport_page = HrPortalPassportUserProfileValidation(context.driver)
    context.hr_portal_passport_page.hr_portal_passport_page_complete_status_validation()
