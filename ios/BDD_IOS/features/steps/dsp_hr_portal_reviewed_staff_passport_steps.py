"""
Steps definition for Reviewed staff passport features
"""
from behave import given, when, then
from ios.BDD_IOS.pages.base_page import BasePage
from ios.BDD_IOS.pages.hr_reviewed_staff_passport import HRReviewedStaffPassportPage


@then('Click on the Reviewed Staff Passport Tab under HR Portal')
def hr_portal_reviewed_staff_passport(context):
    context.hr_portal_reviewed_staff_passport_page = HRReviewedStaffPassportPage(context.driver)
    context.hr_portal_reviewed_staff_passport_page.hr_portal_reviewed_staff_passport_tab()


@then('Enter the user details in the search button - Reviewed Staff Passport')
def hr_portal_reviewed_staff_username_search(context):
    context.hr_portal_reviewed_staff_passport_page.hr_portal_reviewed_search_username(
        BasePage.get_test_data("IdentityReview", "username",
                               "test_data.yaml"))


@then('Click on the Search button - Reviewed Staff Passport')
def hr_portal_reviewed_staff_search_submit(context):
    context.hr_portal_reviewed_staff_passport_page.hr_portal_reviewed_search_submit_click()


@then('Validate the passport status - Reviewed Staff Passport')
def hr_portal_reviewed_staff_search_result(context):
    context.hr_portal_reviewed_staff_passport_page.hr_portal_reviewed_validate_search_result()


@then('Click on the passport user - Reviewed Staff Passport')
def hr_portal_reviewed_staff_search_result(context):
    context.hr_portal_reviewed_staff_passport_page.hr_portal_reviewed_click_search_result()
