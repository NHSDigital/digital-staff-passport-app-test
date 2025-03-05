"""steps for review and confirm initial credentials"""
from behave import then, when
from pages.ios_pages.review_confirm_initial_creds_page import ReviewAndConfirmInitialCredentialsPage
from pages.base_page import BasePage


@then("user verifies the page heading")
def user_verifies_page_heading(context):
    """step to call read page heading and assert the expected value"""
    context.review_creds = ReviewAndConfirmInitialCredentialsPage(context.driver)
    assert "Page heading" in context.review_creds.read_identity_page_heading(), "Page heading is not displayed"


@then("user verifies question mark icon is present")
def user_verifies_question_mark_icon(context):
    """step to verify question mark icon is present"""
    assert context.review_creds.verify_question_mark_icon(), "Question mark icon is not displayed"


@then("user verifies user account icon is present")
def user_verifies_user_account_icon(context):
    """step to verify user account icon is present"""
    assert context.review_creds.verify_user_account_icon(), "User account icon is not displayed"


@then("user verifies Home button is displayed")
def user_verifies_home_button(context):
    """step to verify Home button is displayed"""
    assert context.review_creds.verify_home_button(), "Home button is not displayed"


@then("user verifies credentials button is displayed")
def user_verifies_credentials_button(context):
    """step to verify credentials button is displayed"""
    assert context.review_creds.verify_credentials_button(), "Credentials button is not displayed"


@then("user verifies credentials to confirm has identity credential listed with action required")
def user_verifies_identity_credential(context):
    """step to verify identity credential is listed with action required"""
    assert context.review_creds.verify_identity_credential(), "Identity credential is not displayed"


@then("user verifies credentials to confirm has right to work credential listed with action required")
def user_verifies_right_to_work_credential(context):
    """step to verify right to work credential is listed with action required"""
    assert context.review_creds.verify_right_to_work_credential(), "Right to work credential is not displayed"


@then("user verifies credentials to confirm has DBS supporting documents listed with action required")
def user_verifies_dbs_supporting_documents(context):
    """step to verify DBS supporting documents is listed with action required"""
    assert context.review_creds.verify_dbs_supporting_documents(), "DBS supporting documents is not displayed"


@then('user verifies confirmed credentials has "No credentials yet"')
def user_verifies_no_credentials_yet(context):
    """step to verify no credentials yet message is displayed"""
    assert context.review_creds.verify_no_credentials_yet(), "No credentials yet message is not displayed"


@when("user click identity credential")
def user_click_identity_credential(context):
    """step to click on identity credential"""
    context.review_creds.click_identity_credential()


@then("user verifies provided by Trust")
def user_verifies_provided_by_trust(context):
    """step to verify provided by Trust"""
    assert context.review_creds.verify_provided_by_trust(), "Provided by Trust is not displayed"


@then('user verifies the identity credential details - "{field}"')
def user_verifies_identity_credential_details(context, field):
    """step to verify identity credential details"""
    actual_details_mapping = {"Name": context.review_creds.read_name_on_identity_credentials_page,
                      "DOB": context.review_creds.read_dob_on_identity_credentials_page,
                      "Legal gender": context.review_creds.read_legal_gender_on_identity_credentials_page,
                      "Nationality": context.review_creds.read_nationality_on_identity_credentials_page,
                      "issued on": context.review_creds.read_issued_on_on_identity_credentials_page}

    assert actual_details_mapping[field]() == BasePage.get_test_data("IdentityCredentials", field), f"{field} mismatch"


@then("user verifies link something is not right")
def user_verifies_something_not_right_link(context):
    """step to verify something is not right link"""
    assert context.review_creds.verify_something_not_right_link(), "Something is not right link is not displayed"


@when("user clicks confirm credential button")
def user_click_confirm_credential_button(context):
    """step to click confirm credential button"""
    context.review_creds.click_confirm_credential_button()


@then("user see Confirming credential spinner")
def user_see_confirming_credential_spinner(context):
    """step to verify confirming credential spinner"""
    assert context.review_creds.verify_confirming_credential_spinner(), "Confirming credential spinner is not displayed"


@then("user lands on credentials confirmed page")
def user_lands_on_credentials_confirmed_page(context):
    """step to verify user lands on credentials confirmed page"""
    assert context.review_creds.verify_credentials_confirmed_page(), "User is not on credentials confirmed page"


@then("user verifies the text on the page")
def user_verifies_text_on_page(context):
    """step to verify the text on the page"""
    assert context.review_creds.verify_text_on_page(), "Text is not displayed on the page"


@when("user clicks on Back to my credentials button")
def user_click_back_to_my_credentials_button(context):
    """step to click back to my credentials button"""
    context.review_creds.click_back_to_my_credentials_button()


@then("user lands on credentials page")
def user_lands_on_credentials_page(context):
    """step to verify user lands on credentials page"""
    assert context.review_creds.verify_credentials_page(), "User is not on credentials page"


@then("user verifies identity credential is removed from credentials to confirm")
def user_verifies_identity_credential_removed(context):
    """step to verify identity credential is removed from credentials to confirm"""
    assert not context.review_creds.verify_identity_credential_removed(), "Identity credential is not removed"


@then("user verifies identity is listed under confirmed credentials")
def user_verifies_identity_listed(context):
    """step to verify identity is listed under confirmed credentials"""
    assert context.review_creds.verify_identity_listed(), "Identity is not listed under confirmed credentials"


@when("user click right to work credential")
def user_click_right_to_work_credential(context):
    """step to click right to work credential"""
    context.review_creds.click_right_to_work_credentials()


@then('user verifies the right to work credential details - "{fields}"')
def user_verifies_right_to_work_credential_details(context, fields):
    """step to verify right to work credential details"""
    actual_values_mapping = {"Name": context.review_creds.read_name_on_right_to_work_page,
                             "DOB": context.review_creds.read_dob_on_right_to_work_page,
                             "Passport expiry date": context.review_creds.read_passport_expiry_date_on_right_to_work_page}
    assert actual_values_mapping[fields]() == BasePage.get_test_data("RightToWork", fields), f"{fields} mismatch"
@then("user verifies link something went wrong")
def user_verifies_something_went_wrong_link(context):
    """step to verify something went wrong link"""
    assert context.review_creds.verify_something_went_wrong_link(), "Something went wrong link is not displayed"



@then("user see a spinner page with confirming credential")
def user_see_spinner_page_with_confirming_credential(context):
    """step to verify spinner page with confirming credential"""
    assert context.review_creds.verify_spinner_page_with_confirming_credential(), "Spinner page is not displayed"


@then("user verifies right to work credential is removed from credentials to confirm")
def user_verifies_right_to_work_credential_removed(context):
    """step to verify right to work credential is removed from credentials to confirm"""
    assert not context.review_creds.verify_right_to_work_credential_removed(), "Right to work credential is not removed"


@then("user verifies right to work is listed under confirmed credentials")
def user_verifies_right_to_work_listed(context):
    """step to verify right to work is listed under confirmed credentials"""
    assert context.review_creds.verify_right_to_work_listed(), "Right to work is not listed under confirmed credentials"


@when("user click DBS supporting documents")
def user_click_dbs_supporting_documents(context):
    """step to click DBS supporting documents"""
    context.review_creds.click_dbs_supporting_documents()


@then(
    'user verifies the DBS supporting documents details - "{fields}"')
def user_verifies_dbs_supporting_documents_details(context, fields):
    """step to verify DBS supporting documents details"""
    actual_values_mapping = {"Name": context.review_creds.read_name_on_dbs_supporting_documents_page,
                                "DOB": context.review_creds.read_dob_on_dbs_supporting_documents_page,
                                "Verified current address": context.review_creds.read_verified_current_address_on_dbs_supporting_documents_page,
                                "Resident from": context.review_creds.read_resident_from_on_dbs_supporting_documents_page,
                                "Passport number": context.review_creds.read_passport_number_on_dbs_supporting_documents_page,
                                "Passport nationality": context.review_creds.read_passport_nationality_on_dbs_supporting_documents_page,
                                "Passport issue date": context.review_creds.read_passport_issue_date_on_dbs_supporting_documents_page}
    assert actual_values_mapping[fields]() == BasePage.get_test_data("DBSSupportingDocuments", fields), f"{fields} mismatch"


@then("user verifies DBS supporting documents is removed from credentials to confirm")
def user_verifies_dbs_supporting_documents_removed(context):
    """step to verify DBS supporting documents is removed from credentials to confirm"""
    assert not context.review_creds.verify_dbs_supporting_documents_removed(), "DBS supporting documents is not removed"


@then("user verifies DBS supporting documents is listed under confirmed credentials")
def user_verifies_dbs_supporting_documents_listed(context):
    """step to verify DBS supporting documents is listed under confirmed credentials"""
    assert context.review_creds.verify_dbs_supporting_documents_listed(), "DBS supporting documents is not listed under confirmed credentials"


@then("user click account icon")
def user_click_account_icon(context):
    """step to click account icon"""
    context.review_creds.click_account_icon()


@then("user is accounts and settings page")
def verify_user_account_and_settings_page(context):
    """step to verify user is on account and settings page"""
    assert context.review_creds.verify_account_and_settings_page(), "account and setting page not displayed"



@then("user see delete your NHS digital staff passport section and verifies the message inside")
def verify_delete_nhs_digital_staff_passport_section(context):
    """step to verify delete your NHS digital staff passport section"""
    assert context.review_creds.verify_delete_nhs_digital_staff_passport_section(), "Delete your NHS digital staff passport section is not displayed"


@then('user see security and privacy section and a link "terms of use and other policies" inside')
def verify_security_and_privacy_section(context):
    """step to verify security and privacy section"""
    assert context.review_creds.verify_security_and_privacy_section(), "Security and privacy section is not displayed"


@then("user see question icon")
def verify_question_icon(context):
    """step to verify question icon"""
    assert context.review_creds.verify_question_icon(), "Question icon is not displayed"


@when("user clicks on back link")
def click_on_back_link(context):
    """step to click on back link"""
    context.review_creds.click_back_link()


@then("user is on home page")
def verify_user_home_page(context):
    """step to verify user is on home page"""
    assert context.review_creds.verify_home_page(), "User is not on home page"

@when("user clicks on identity credential")
def click_on_identity_credential(context):
    """step to click on identity credential"""
    context.review_creds.click_identity_credential()


@then("user is on credentials page with dates")
def verify_user_credentials_page_with_dates(context):
    """step to verify user is on credentials page with dates"""
    assert context.review_creds.verify_credentials_page(), "User is not on credentials page with dates"


@when("user clicks on right to work credential")
def click_on_right_to_work_credential(context):
    """step to click on right to work credential"""
    context.review_creds.click_right_to_work_credentials()


@when("user clicks on DBS supporting documents")
def click_on_dbs_supporting_documents(context):
    """step to click on DBS supporting documents"""
    context.review_creds.click_dbs_supporting_documents()


@then("user verifies back link is present")
def verify_back_link(context):
    """step to verify back link is present"""
    assert context.review_creds.verify_back_link(), "Back link is not displayed"


@then("User validates no credentials present")
def verify_no_credentials_is_present(context):
    """step to call method from page class that checks and returns the element no credentials"""
    assert context.review_creds.verify_no_credentials(), "No credentials message is not displayed"

