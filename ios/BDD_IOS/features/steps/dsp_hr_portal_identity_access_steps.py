"""
Steps definition w.r.t (Identity & Access) features
"""
from behave import then

from pages.hr_pages.hr_identity_and_access import HRIdentityAndAccessPage
from pages.base_page import BasePage


@then('Click on the Identity & Access Tab with HR Portal')
def hr_portal_identity_access(context):
    """Step to click on identity and access tab on HR Portal"""
    context.hr_portal_identity_access_page = HRIdentityAndAccessPage(context.driver)
    context.hr_portal_identity_access_page.hr_portal_menu_click()


@then('Click on invitation of Single Passport link')
def hr_portal_identity_access_invitation_link(context):
    """Step to click on invitation of Single Passport link"""
    context.hr_portal_identity_access_page.hr_portal_identity_invitation_link()


@then('Select the single passport form radio button')
def hr_portal_identity_access_single_passport_radio_btn(context):
    """Step to select single passport form radio button"""
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_rdio_btn()


@then('Click on Continue button w.r.t single passport form')
def hr_portal_identity_single_passport_continue_btn(context):
    """Step to click on continue button w.r.t single passport form"""
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_continue()


@then('Enter First name w.r.t single passport form')
def hr_portal_identity_single_passport_first_name(context):
    """Step to enter First name w.r.t single passport form"""
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_first_name(
        BasePage.get_test_data("RegisterUser", "name",
                               "test_data.yaml"))


@then('Enter Last name w.r.t single passport form')
def hr_portal_identity_single_passport_last_name(context):
    """Step to enter Last name w.r.t single passport form"""
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_last_name(
        BasePage.get_test_data("RegisterUser", "surname",
                               "test_data.yaml"))


@then('Enter Day - DOB w.r.t single passport form')
def hr_portal_identity_single_passport_dob_day(context):
    """Step to enter Day w.r.t single passport form"""
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_dob_day(
        BasePage.get_test_data("RegisterUser", "dob_dd",
                               "test_data.yaml"))


@then('Enter Month - DOB w.r.t single passport form')
def hr_portal_identity_single_passport_dob_month(context):
    """Step to enter Month - DOB w.r.t single passport form"""
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_dob_month(
        BasePage.get_test_data("RegisterUser", "dob_mm",
                               "test_data.yaml"))


@then('Enter Year - DOB w.r.t single passport form')
def hr_portal_identity_single_passport_dob_year(context):
    """Step to enter Year - DOB w.r.t single passport form"""
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_dob_year(
        BasePage.get_test_data("RegisterUser", "dob_yyyy",
                               "test_data.yaml"))


@then('Enter Email address w.r.t single passport form')
def hr_portal_identity_single_passport_email(context):
    """Step to enter Email address w.r.t single passport form"""
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_email(
        BasePage.get_test_data("RegisterUser", "email",
                               "test_data.yaml"))


@then('Enter Phone number w.r.t single passport form')
def hr_portal_identity_single_passport_phone(context):
    """Step to enter Phone number w.r.t single passport form"""
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_phone(
        BasePage.get_test_data("RegisterUser", "phone_number",
                               "test_data.yaml"))


@then('Select the Staff group dropdown w.r.t single passport form')
def hr_portal_identity_single_passport_staff_group(context):
    """Steps to select staff group dropdown w.r.t single passport form"""
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_staff_group()


@then('Select the Emp Type dropdown w.r.t single passport form')
def hr_portal_identity_single_passport_emp_type(context):
    """Step to select emp type dropdown w.r.t single passport form"""
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_emp_type()


@then('Select the Emp Status dropdown w.r.t single passport form')
def hr_portal_identity_single_passport_emp_status(context):
    """Step to select emp status dropdown w.r.t single passport form"""
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_emp_status()


@then('Click on continue button w.r.t single passport forms')
def hr_portal_identity_single_passport_details_continue(context):
    """Step to click on continue button w.r.t single passport forms"""
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_details_continue_btn()


@then('Select create passport radio button w.r.t single passport form')
def hr_portal_identity_single_passport_create_radio_btn(context):
    """Step to select create passport radio button"""
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_create_passport_radio_btn()


@then('Click continue button button w.r.t create passport')
def hr_portal_identity_passport_create_continue_btn(context):
    """Step to click continue button w.r.t create passport"""
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_create_passport_continue_btn()


@then('Verify the status of the request under Identity & access search form')
def hr_portal_identity_single_passport_create_message(context):
    """Step to verify the status of the request under Identity & access search form"""
    context.hr_portal_identity_access_page.hr_portal_identity_single_passport_create_passport_message()


@then('Enter the user details in the search button - Identity & Access')
def hr_portal_identity_access_username_search(context):
    """Step to enter the user details in the search button - Identity & Access"""
    context.hr_portal_identity_access_page.hr_portal_identity_search_username(
        BasePage.get_test_data("IdentityReview", "username",
                               "test_data.yaml"))


@then('Click on the Search button - Identity & Access')
def hr_portal_identity_access_search_submit(context):
    """Step to enter the user details in the search button - Identity & Access"""
    context.hr_portal_identity_access_page.hr_portal_identity_search_submit_click()


@then('Result is displayed & click on the same - Identity & Access')
def hr_portal_identity_access_search_result(context):
    """Step to enter the user details in the search button - Identity & Access"""
    context.hr_portal_identity_access_page.hr_portal_identity_search_result()


@then('Click on the Review Identity Link')
def hr_portal_identity_access_review_identity(context):
    """Step to enter the user details in the search button - Review Identity Link"""
    context.hr_portal_identity_access_page.hr_portal_identity_review_details()


@then('Employment - Permanent details selected from dropdown list')
def hr_portal_identity_access_hr_employment_permanent(context):
    """Step to select dropdown permanent details"""
    context.hr_portal_identity_access_page.hr_portal_identity_select_employment_type_permanent()


@then('Click on the Continue button - post selected Employment details')
def hr_portal_identity_access_hr_employment_continue(context):
    """Step to click on the Continue button - post selected Employment details"""
    context.hr_portal_identity_access_page.hr_portal_identity_continue_button()


@then('Click on the confirm button for identity review')
def hr_portal_identity_access_confirm_identity(context):
    """Step to clcik on confirm button for identity review"""
    context.hr_portal_identity_access_page.hr_portal_identity_confirm_user_radiobutton()


@then('Click on the Continue button - post confirm button selected')
def hr_portal_identity_access_confirm_identity_continue(context):
    """Step to click on the Continue button - post confirm button"""
    context.hr_portal_identity_access_page.hr_portal_identity_continue_button()


@then('Gender - Male details selected from dropdown list')
def hr_portal_identity_access_gender_male(context):
    """Step to select dropdown male gender details"""
    context.hr_portal_identity_access_page.hr_portal_identity_select_gender_dropdown_male()


@then('Gender - Female details selected from dropdown list')
def hr_portal_identity_access_gender_female(context):
    """Step to select dropdown female gender details"""
    context.hr_portal_identity_access_page.hr_portal_identity_select_gender_dropdown_female()


@then('Nationality details selected from dropdown list')
def hr_portal_identity_access_nationality(context):
    """Step to select dropdown nationality details"""
    context.hr_portal_identity_access_page.hr_portal_identity_select_nationality_dropdown()


@then('Enter details in the address 1 field')
def hr_portal_identity_access_address1(context):
    """Step to enter the user details in the address 1 field"""
    context.hr_portal_identity_access_page.hr_portal_identity_enter_address_line_1_details(
        BasePage.get_test_data("IdentityReview", "address_1",
                               "test_data.yaml"))


@then('Enter details in the address 2 field')
def hr_portal_identity_access_address2(context):
    """Step to enter the user details in the address 2 field"""
    context.hr_portal_identity_access_page.hr_portal_identity_enter_address_line_2_details(
        BasePage.get_test_data("IdentityReview", "address_2",
                               "test_data.yaml"))


@then('Enter details in the town field')
def hr_portal_identity_access_town(context):
    """Step to enter the user details in the town field"""
    context.hr_portal_identity_access_page.hr_portal_identity_enter_town_details(
        BasePage.get_test_data("IdentityReview", "town",
                               "test_data.yaml"))


@then('Enter details in the Postcode field')
def hr_portal_identity_access_postcode(context):
    """Step to enter the user details in the postcode field"""
    context.hr_portal_identity_access_page.hr_portal_identity_enter_postcode_details(
        BasePage.get_test_data("IdentityReview", "postcode",
                               "test_data.yaml"))


@then('Enter details in the Country field')
def hr_portal_identity_access_country(context):
    """Step to enter the user details in the country field"""
    context.hr_portal_identity_access_page.hr_portal_identity_country_dropdown()


@then('Click on the Continue button - post personal details entered')
def hr_portal_identity_access_details_continue(context):
    """Step to click on the Continue button - post personal details"""
    context.hr_portal_identity_access_page.hr_portal_identity_continue_button()


@then('Click on the Confirm button to proceed for review')
def hr_portal_identity_access_confirm_review(context):
    """Step to click on the Confirm button to proceed for review"""
    context.hr_portal_identity_access_page.hr_portal_identity_confirm_review_button()


@then('Click on the Continue button - post confirm review')
def hr_portal_identity_access_proceed_review(context):
    """Step to click on the Continue button - post confirm review"""
    context.hr_portal_identity_access_page.hr_portal_identity_yes_confirm_radio_xpath()
    context.hr_portal_identity_access_page.hr_portal_identity_continue_button()


@then('Request reviewed and success message is displayed')
def hr_portal_identity_access_review_success(context):
    """Step to click on the Request reviewed and success message is displayed"""
    context.hr_portal_identity_access_page.hr_portal_identity_review_request_success_message()


@then('Click on the Delete passport from records link')
def hr_portal_delete_from_record_link(context):
    """Step to click on the Delete passport from records link"""
    context.hr_portal_identity_access_page.hr_portal_delete_passport_link()


@then('User selected yes for delete staff passport from record button')
def hr_portal_yes_delete_from_record_radio_button(context):
    """Step to click on yes for delete staff passport from record button"""
    context.hr_portal_identity_access_page.hr_portal_yes_delete_passport_radio_btn()


@then('User selected no for delete staff passport from record button')
def hr_portal_no_delete_from_record_radio_button(context):
    """Step to click on no for delete staff passport from record button"""
    context.hr_portal_identity_access_page.hr_portal_no_delete_passport_radio_btn()


@then('User clicks on Continue button on delete passport page')
def hr_portal_delete_passport_continue_button(context):
    """Step to click on Continue button on delete passport page"""
    context.hr_portal_identity_access_page.hr_portal_continue_btn_delete_passport()


@then('Verify that user profile is visible')
def hr_portal_user_profile_validation(context):
    """Step to verify that user profile is visible"""
    context.hr_portal_identity_access_page.hr_portal_user_profile_validation()


@then('Verify the confirmation message displayed w.r.t passport delete')
def hr_portal_passport_deleted_confirmation_message(context):
    """Step to verify that user profile is visible"""
    context.hr_portal_identity_access_page.hr_portal_delete_passport_message()


@then("identity and access page is opened for the user")
def verify_identity_and_access_page(context):
    """verify identity and access page is opened for the user"""
    context.hr_portal_identity_access_page = HRIdentityAndAccessPage(context.driver)
    assert context.hr_portal_identity_access_page.verify_identity_and_access_page_opened()


@then("Click on the Review Identity details")
def click_on_review_id_details(context):
    """Click on the Review Identity details"""
    context.hr_portal_identity_access_page.click_on_review_identity_details()


@then("user verifies the page title - Confirm identity")
def verify_page_title(context):
    """
    verify page title
    """
    assert context.hr_portal_identity_access_page.verify_page_title_confirm_identity(
        "Confirm identity"
    ), "Page title does not match"


@then("user selects yes radio button")
def select_radio_button_yes(context):
    """click on yes radio button to accept credential"""
    context.hr_portal_identity_access_page.select_yes_radio_button()


@then("user clicks on continue button")
def click_continue_button(context):
    """click on continue button"""
    context.hr_portal_identity_access_page.click_continue_button()


@then("user verifies the page title - Provide right to work")
def verify_page_title(context):
    """
    verify page title
    """
    assert context.hr_portal_identity_access_page.verify_page_title(
        "Provide right to work"
    ), "Page title does not match"


@then("user verifies the page title - Provide DBS supporting information")
def verify_page_title_DBS(context):
    """
    verify page title
    """
    assert context.hr_portal_identity_access_page.verify_page_title_dbs(
        "Provide DBS supporting information"
    ), "Page title does not match"


@then("user see success page")
def verify_success(context):
    """
    verify success page
    """
    assert context.hr_portal_identity_access_page.verify_success_page(
        "New Identity credential provided"
    ), "Success page does not match"


@then("user verifies the credential status is confirmed and provided - identity")
def verify_credential_status(context):
    """
    verify credential status
    """
    assert context.hr_portal_identity_access_page.verify_identity_status_confirmed(
        "Identity credential provided"
    ), "Credential status does not match"
    assert context.hr_portal_identity_access_page.verify_rtw_status_confirmed()

@then("user verifies the credential status is confirmed and provided - right to work")
def verify_rtw_status(context):
    """
    verify credential status
    """
    assert context.hr_portal_identity_access_page.verify_rtw_status_confirmed(
        "DBS credential provided"
    ), "Credential status does not match"


@then("user verifies the credential status is confirmed and provided - dbs")
def verify_dbs_status(context):
    """
    verify credential status
    """
    assert context.hr_portal_identity_access_page.verify_dbs_status_confirmed(
        "DBS credential provided"
    ), "Credential status does not match"
