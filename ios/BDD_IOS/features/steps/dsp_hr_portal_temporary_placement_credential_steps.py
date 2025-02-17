"""
Steps definition w.r.t Temporary credentials provided
"""
from behave import given, when, then
from pages.hr_pages.hr_temporary_placement_credential import HRTemporaryPlacementCredentialPage
from pages.base_page import BasePage



@then('HR User clicked on Create temporary placement credential link')
def hr_portal_click_on_create_temporary_placement_credential_link(context):
    context.hr_temporary_placement_credential_page = HRTemporaryPlacementCredentialPage(context.driver)
    context.hr_temporary_placement_credential_page.hr_portal_click_create_temporary_placement_credential_link()


@then('HR User validate the next page header and proceed further')
def hr_portal_validate_heading_and_proceed_further(context):
    context.hr_temporary_placement_credential_page.hr_portal_verify_heading_and_click_continue()


@then('HR User adds the details in position title field')
def hr_portal_add_details_in_position_title_field(context):
    context.hr_temporary_placement_credential_page.hr_portal_add_details_in_position_title_field(
        BasePage.get_test_data("TemporaryCredential", "position_title", "test_data.yaml")
    )


@then('HR user adds the details in position number field')
def hr_portal_add_details_in_position_number_field(context):
    context.hr_temporary_placement_credential_page.hr_portal_add_details_in_position_number(
        BasePage.get_test_data("TemporaryCredential", "position_number", "test_data.yaml")
    )


@then('HR user adds the Brief description of work pattern')
def hr_portal_add_details_in_brief_description_of_work_pattern(context):
    context.hr_temporary_placement_credential_page.hr_portal_add_details_in_brief_description_textbox(
        BasePage.get_test_data("TemporaryCredential", "Brief_description_of_work_pattern", "test_data.yaml")
    )


@then('HR User adds the temporary placement credentials start date')
def hr_portal_add_temporary_credentials_start_date(context):
    context.hr_temporary_placement_credential_page.hr_portal_add_temporary_placement_start_day(
        BasePage.get_test_data("TemporaryCredential", "start_date", "test_data.yaml")
    )
    context.hr_temporary_placement_credential_page.hr_portal_add_temporary_placement_start_month(
        BasePage.get_test_data("TemporaryCredential", "start_month", "test_data.yaml")
    )
    context.hr_temporary_placement_credential_page.hr_portal_add_temporary_placement_start_year(
        BasePage.get_test_data("TemporaryCredential", "start_year", "test_data.yaml")
    )


@then('HR User adds the temporary placement credentials end date')
def hr_portal_add_temporary_credentials_end_date(context):
    context.hr_temporary_placement_credential_page.hr_portal_add_temporary_placement_end_day(
        BasePage.get_test_data("TemporaryCredential", "end_date", "test_data.yaml")
    )
    context.hr_temporary_placement_credential_page.hr_portal_add_temporary_placement_end_month(
        BasePage.get_test_data("TemporaryCredential", "end_month", "test_data.yaml")
    )
    context.hr_temporary_placement_credential_page.hr_portal_add_temporary_placement_end_year(
        BasePage.get_test_data("TemporaryCredential", "end_year", "test_data.yaml")
    )


@then('HR user clicks on continue button for temp creation')
def hr_portal_click_on_continue_button_for_temp_creation(context):
    context.hr_temporary_placement_credential_page.hr_portal_click_on_continue_button_on_page()


@then('HR user validates the page heading and select coventry as permanent employer option from dropdown')
def hr_portal_select_coventry_as_permanent_employer_option(context):
    context.hr_temporary_placement_credential_page.hr_portal_select_permanent_employer_detail_from_dropdown(
        BasePage.get_test_data("TemporaryCredential", "Permanent_employer_coventry", "test_data.yaml")
    )


@then('HR user adds the details in department field')
def hr_portal_add_details_in_department_field(context):
    context.hr_temporary_placement_credential_page.hr_portal_add_details_in_department_field(
        BasePage.get_test_data("TemporaryCredential", "Department", "test_data.yaml")
    )


@then('HR user adds the details in department contact name field')
def hr_portal_add_details_in_department_contact_name_field(context):
    context.hr_temporary_placement_credential_page.hr_portal_add_details_in_department_contact_name_field(
        BasePage.get_test_data("TemporaryCredential", "Department_contact_name", "test_data.yaml")
    )


@then('HR user adds the details in department contact email address field')
def hr_portal_add_details_in_department_contact_email_address_field(context):
    context.hr_temporary_placement_credential_page.hr_portal_add_details_in_department_contact_email_address_field(
        BasePage.get_test_data("TemporaryCredential", "Department_contact_email_address", "test_data.yaml")
    )


@then('HR User adds the details in HR contact field')
def hr_portal_add_details_in_hr_contact_field(context):
    context.hr_temporary_placement_credential_page.hr_portal_add_details_in_hr_contact_field(
        BasePage.get_test_data("TemporaryCredential", "HR_contact", "test_data.yaml")
    )


@then('HR user adds the details in Approved by field')
def hr_portal_add_details_in_approved_by_field(context):
    context.hr_temporary_placement_credential_page.hr_portal_add_details_in_approved_by_field(
        BasePage.get_test_data("TemporaryCredential", "Approved_by", "test_data.yaml")
    )


@then('HR user verifies the Licence to attend heading and select yes radio button option')
def hr_portal_select_yes_radio_button_for_licence_to_attend_field(context):
    context.hr_temporary_placement_credential_page.hr_portal_select_licence_to_attend_yes_radio_btn()


@then('HR user confirm details and provide credential heading and select yes radio button option')
def hr_portal_confirm_details_and_select_yes_radio_button_option(context):
    context.hr_temporary_placement_credential_page.hr_portal_confirm_details_page_and_select_yes_radio_button()


@then('HR user validates the Temporary placement credential provided success message')
def hr_portal_validates_temp_placement_cred_provided_success_message(context):
    context.hr_temporary_placement_credential_page.hr_portal_temp_placement_provided_success_message()


@then('HR user validates the passport history event details w.r.t temporary placement')
def hr_portal_validates_temp_placement_cred_passport_history(context):
    context.hr_temporary_placement_credential_page.hr_portal_temp_placement_passport_history_event_details()
