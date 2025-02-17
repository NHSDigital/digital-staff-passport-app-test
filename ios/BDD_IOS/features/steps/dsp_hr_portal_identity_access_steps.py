"""
Steps definition w.r.t (Identity & Access) features
"""
from behave import given, when, then

from pages.hr_pages.hr_identity_and_access import HRIdentityAndAccessPage
from pages.base_page import BasePage



@then('Click on the Identity & Access Tab with HR Portal')
def hr_portal_identity_access(context):
    context.hr_portal_identity_access_page = HRIdentityAndAccessPage(context.driver)
    context.hr_portal_identity_access_page.hr_portal_identity_and_access_tab()


@then('Click on invitation of Single Passport link')
def hr_portal_identity_access_invitation_link(context):
    context.hr_portal_identity_access_page.hr_portal_identity_invitation_link()

@then('Select the single passport form radio button')
def hr_portal_identity_access_single_passport_radio_btn(context):
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_rdio_btn()


@then('Click on Continue button w.r.t single passport form')
def hr_portal_identity_access_single_passport_continue_btn(context):
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_continue()


@then('Enter First name w.r.t single passport form')
def hr_portal_identity_access_single_passport_first_name(context):
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_first_name(
        BasePage.get_test_data("RegisterUser", "name",
                               "test_data.yaml"))


@then('Enter Last name w.r.t single passport form')
def hr_portal_identity_access_single_passport_last_name(context):
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_last_name(
        BasePage.get_test_data("RegisterUser", "surname",
                               "test_data.yaml"))


@then('Enter Day - DOB w.r.t single passport form')
def hr_portal_identity_access_single_passport_dob_day(context):
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_dob_day(
        BasePage.get_test_data("RegisterUser", "dob_dd",
                               "test_data.yaml"))


@then('Enter Month - DOB w.r.t single passport form')
def hr_portal_identity_access_single_passport_dob_month(context):
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_dob_month(
        BasePage.get_test_data("RegisterUser", "dob_mm",
                               "test_data.yaml"))


@then('Enter Year - DOB w.r.t single passport form')
def hr_portal_identity_access_single_passport_dob_year(context):
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_dob_year(
        BasePage.get_test_data("RegisterUser", "dob_yyyy",
                               "test_data.yaml"))


@then('Enter Email address w.r.t single passport form')
def hr_portal_identity_access_single_passport_email(context):
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_email(
        BasePage.get_test_data("RegisterUser", "email",
                               "test_data.yaml"))


@then('Enter Phone number w.r.t single passport form')
def hr_portal_identity_access_single_passport_phone(context):
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_phone(
        BasePage.get_test_data("RegisterUser", "phone_number",
                               "test_data.yaml"))


@then('Select the Staff group dropdown w.r.t single passport form')
def hr_portal_identity_access_single_passport_staff_group(context):
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_staff_group()


@then('Select the Emp Type dropdown w.r.t single passport form')
def hr_portal_identity_access_single_passport_emp_type(context):
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_emp_type()


@then('Select the Emp Status dropdown w.r.t single passport form')
def hr_portal_identity_access_single_passport_emp_status(context):
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_emp_status()


@then('Click on continue button w.r.t single passport forms')
def hr_portal_identity_access_single_passport_details_continue(context):
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_details_continue_btn()


@then('Select create passport radio button w.r.t single passport form')
def hr_portal_identity_access_single_passport_create_radio_btn(context):
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_create_passport_radio_btn()


@then('Click continue button button w.r.t create passport')
def hr_portal_identity_access_single_passport_create_continue_btn(context):
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_create_passport_continue_btn()


@then('Verify the status of the request under Identity & access search form')
def hr_portal_identity_access_single_passport_create_message(context):
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_create_passport_message()


@then('Enter the user details in the search button - Identity & Access')
def hr_portal_identity_access_username_search(context):
    context.hr_portal_identity_access_page.hr_portal_identity_search_username(
        BasePage.get_test_data("IdentityReview", "username",
                               "test_data.yaml"))

@then('Click on the Search button - Identity & Access')
def hr_portal_identity_access_search_submit(context):
    context.hr_portal_identity_access_page.hr_portal_identity_search_submit_click()


@then('Result is displayed & click on the same - Identity & Access')
def hr_portal_identity_access_search_result(context):
    context.hr_portal_identity_access_page.hr_portal_identity_search_result()


@then('Click on the Review Identity Link')
def hr_portal_identity_access_review_identity(context):
    context.hr_portal_identity_access_page.hr_portal_identity_review_details()

@then('Employment - Permanent details selected from dropdown list')
def hr_portal_identity_access_hr_employment_permanent(context):
    context.hr_portal_identity_access_page.hr_portal_identity_select_employment_type_permanent()

@then('Click on the Continue button - post selected Employment details')
def hr_portal_identity_access_hr_employment_continue(context):
    context.hr_portal_identity_access_page.hr_portal_identity_continue_button()

@then('Click on the confirm button for identity review')
def hr_portal_identity_access_confirm_identity(context):
    context.hr_portal_identity_access_page.hr_portal_identity_confirm_user_radiobutton()

@then('Click on the Continue button - post confirm button selected')
def hr_portal_identity_access_confirm_identity_continue(context):
    context.hr_portal_identity_access_page.hr_portal_identity_continue_button()


@then('Gender - Male details selected from dropdown list')
def hr_portal_identity_access_gender_male(context):
    context.hr_portal_identity_access_page.hr_portal_identity_select_gender_dropdown_male()


@then('Gender - Female details selected from dropdown list')
def hr_portal_identity_access_gender_female(context):
    context.hr_portal_identity_access_page.hr_portal_identity_select_gender_dropdown_female()


@then('Nationality details selected from dropdown list')
def hr_portal_identity_access_nationality(context):
    context.hr_portal_identity_access_page.hr_portal_identity_select_nationality_dropdown()


@then('Enter details in the address 1 field')
def hr_portal_identity_access_address1(context):
    context.hr_portal_identity_access_page.hr_portal_identity_enter_address_line_1_details(
        BasePage.get_test_data("IdentityReview", "address_1",
                               "test_data.yaml"))


@then('Enter details in the address 2 field')
def hr_portal_identity_access_address2(context):
    context.hr_portal_identity_access_page.hr_portal_identity_enter_address_line_2_details(
        BasePage.get_test_data("IdentityReview", "address_2",
                               "test_data.yaml"))


@then('Enter details in the town field')
def hr_portal_identity_access_town(context):
    context.hr_portal_identity_access_page.hr_portal_identity_enter_town_details(
        BasePage.get_test_data("IdentityReview", "town",
                               "test_data.yaml"))


@then('Enter details in the Postcode field')
def hr_portal_identity_access_postcode(context):
    context.hr_portal_identity_access_page.hr_portal_identity_enter_postcode_details(
        BasePage.get_test_data("IdentityReview", "postcode",
                               "test_data.yaml"))


@then('Enter details in the Country field')
def hr_portal_identity_access_country(context):
    context.hr_portal_identity_access_page.hr_portal_identity_country_dropdown()


@then('Click on the Continue button - post personal details entered')
def hr_portal_identity_access_details_continue(context):
    context.hr_portal_identity_access_page.hr_portal_identity_continue_button()


@then('Click on the Confirm button to proceed for review')
def hr_portal_identity_access_confirm_review(context):
    context.hr_portal_identity_access_page.hr_portal_identity_confirm_review_button()


@then('Click on the Continue button - post confirm review')
def hr_portal_identity_access_proceed_review(context):
    context.hr_portal_identity_access_page.hr_portal_identity_yes_confirm_radio_xpath()
    context.hr_portal_identity_access_page.hr_portal_identity_continue_button()


@then('Request reviewed and success message is displayed')
def hr_portal_identity_access_review_success(context):
    context.hr_portal_identity_access_page.hr_portal_identity_review_request_success_message()

@then('Click on the Delete passport from records link')
def hr_portal_delete_passport_from_record_link(context):
    context.hr_portal_identity_access_page.hr_portal_delete_passport_link()

@then('User selected yes for delete staff passport from record button')
def hr_portal_yes_delete_passport_from_record_radio_button(context):
    context.hr_portal_identity_access_page.hr_portal_yes_delete_passport_radio_btn()

@then('User selected no for delete staff passport from record button')
def hr_portal_no_delete_passport_from_record_radio_button(context):
    context.hr_portal_identity_access_page.hr_portal_no_delete_passport_radio_btn()

@then('User clicks on Continue button on delete passport page')
def hr_portal_delete_passport_continue_button(context):
    context.hr_portal_identity_access_page.hr_portal_continue_btn_delete_passport()

@then('Verify that user profile is visible')
def hr_portal_user_profile_validation(context):
    context.hr_portal_identity_access_page.hr_portal_user_profile_validation()

@then('Verify the confirmation message displayed w.r.t passport delete')
def hr_portal_passport_deleted_confirmation_message_page(context):
    context.hr_portal_identity_access_page.hr_portal_delete_passport_message()
