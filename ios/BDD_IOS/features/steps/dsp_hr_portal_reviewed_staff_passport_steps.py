"""
Steps definition for Reviewed staff passport features
"""
from behave import then
from pages.base_page import BasePage
from pages.hr_pages.hr_reviewed_staff_passport import HRReviewedStaffPassportPage


@then('Click on the Reviewed Staff Passport Tab under HR Portal')
def hr_portal_reviewed_staff_passport(context):
    """step implementation Click on the Reviewed Staff Passport Tab under HR Portal"""
    context.hr_portal_reviewed_staff_passport_page = HRReviewedStaffPassportPage(context.driver)
    context.hr_portal_reviewed_staff_passport_page.hr_portal_reviewed_staff_passport_tab()


@then('Enter the user details in the search button - Reviewed Staff Passport')
def hr_portal_reviewed_staff_username_search(context):
    """step implementation Enter the user details in the search button - Reviewed Staff Passport"""
    context.hr_portal_reviewed_staff_passport_page.hr_portal_reviewed_search_username(
        BasePage.get_test_data("IdentityReview", "username",
                               "test_data.yaml"))


@then('Click on the Search button - Reviewed Staff Passport')
def hr_portal_reviewed_staff_search_submit(context):
    """step implementation Click on the Search button - Reviewed Staff Passport"""
    context.hr_portal_reviewed_staff_passport_page.hr_portal_reviewed_search_submit_click()


@then('Validate the passport status - Reviewed Staff Passport')
def hr_portal_reviewed_staff_search_result(context):
    """step implementation Validate the passport status - Reviewed Staff Passport"""
    context.hr_portal_reviewed_staff_passport_page.hr_portal_reviewed_validate_search_result()


@then('Click on the passport user - Reviewed Staff Passport')
def click_on_passport_user_reviewed_passport(context):
    """step implementation Click on the passport user - Reviewed Staff Passport"""
    context.hr_portal_reviewed_staff_passport_page.hr_portal_reviewed_click_search_result()
