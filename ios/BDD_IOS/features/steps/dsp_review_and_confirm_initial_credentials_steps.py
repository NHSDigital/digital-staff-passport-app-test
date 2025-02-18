"""steps for review and confirm initial credentials"""
from behave import then, when
from pages.review_and_confirm_initial_credentials_page import ReviewAndConfirmInitialCredentialsPage


@then("user verifies the page heading")
def user_verifies_page_heading(context):
    """step to call read page heading and assert the expected value"""
    context.review_creds = ReviewAndConfirmInitialCredentialsPage(context.driver)
    assert "Page heading" in context.review_creds.read_identity_page_heading()


@then("user verifies question mark icon is present")
def user_verifies_question_mark_icon(context):
    """step to verify question mark icon is present"""
    assert context.review_creds.verify_question_mark_icon()


@then("user verifies user account icon is present")
def user_verifies_user_account_icon(context):
    """step to verify user account icon is present"""
    assert context.review_creds.verify_user_account_icon()


@then("user verifies Home button is displayed")
def user_verifies_home_button(context):
    """step to verify Home button is displayed"""
    assert context.review_creds.verify_home_button()


@then("user verifies credentials button is displayed")
def user_verifies_credentials_button(context):
    """step to verify credentials button is displayed"""
    assert context.review_creds.verify_credentials_button()


@then("user verifies credentials to confirm has identity credential listed with action required")
def user_verifies_identity_credential(context):
    """step to verify identity credential is listed with action required"""
    assert context.review_creds.verify_identity_credential()


@then("user verifies credentials to confirm has right to work credential listed with action required")
def user_verifies_right_to_work_credential(context):
    """step to verify right to work credential is listed with action required"""
    assert context.review_creds.verify_right_to_work_credential()


@then("user verifies credentials to confirm has DBS supporting documents listed with action required")
def user_verifies_dbs_supporting_documents(context):
    """step to verify DBS supporting documents is listed with action required"""
    assert context.review_creds.verify_dbs_supporting_documents()


@then('user verifies confirmed credentials has "No credentials yet"')
def user_verifies_no_credentials_yet(context):
    """step to verify no credentials yet message is displayed"""
    assert context.review_creds.verify_no_credentials_yet()


@when("user click identity credential")
def user_click_identity_credential(context):
    """step to click on identity credential"""
    context.review_creds.click_identity_credential()


@then("user verifies provided by Trust")
def user_verifies_provided_by_trust(context):
    """step to verify provided by Trust"""
    assert context.review_creds.verify_provided_by_trust()


@then("user verifies the identity credential details - Name,DOB, Legal gender, Nationality, issued on")
def user_verifies_identity_credential_details(context):
    """step to verify identity credential details"""
    assert context.review_creds.verify_identity_credential_details()


@then("user verifies link something is not right")
def user_verifies_something_not_right_link(context):
    """step to verify something is not right link"""
    assert context.review_creds.verify_something_not_right_link()


@when("user clicks confirm credential button")
def user_click_confirm_credential_button(context):
    """step to click confirm credential button"""
    context.review_creds.click_confirm_credential_button()


@then("user see Confirming credential spinner")
def user_see_confirming_credential_spinner(context):
    """step to verify confirming credential spinner"""
    assert context.review_creds.verify_confirming_credential_spinner()


@then("user lands on credentials confirmed page")
def user_lands_on_credentials_confirmed_page(context):
    """step to verify user lands on credentials confirmed page"""
    assert context.review_creds.verify_credentials_confirmed_page()


@then("user verifies the text on the page")
def user_verifies_text_on_page(context):
    """step to verify the text on the page"""
    assert context.review_creds.verify_text_on_page()


@when("user clicks on Back to my credentials button")
def user_click_back_to_my_credentials_button(context):
    """step to click back to my credentials button"""
    context.review_creds.click_back_to_my_credentials_button()


@then("user lands on credentials page")
def user_lands_on_credentials_page(context):
    """step to verify user lands on credentials page"""
    assert context.review_creds.verify_credentials_page()


@then("user verifies identity credential is removed from credentials to confirm")
def user_verifies_identity_credential_removed(context):
    """step to verify identity credential is removed from credentials to confirm"""
    assert context.review_creds.verify_identity_credential_removed()


@then("user verifies identity is listed under confirmed credentials")
def user_verifies_identity_listed(context):
    """step to verify identity is listed under confirmed credentials"""
    assert context.review_creds.verify_identity_listed()


@when("user click right to work credential")
def user_click_right_to_work_credential(context):
    """step to click right to work credential"""
    context.review_creds.click_right_to_work_credential()


@then(
    "user verifies the right to work credential details - Photo of your face, name, DOB, Biometric page, passport expiry date")
def user_verifies_right_to_work_credential_details(context):
    """step to verify right to work credential details"""
    assert context.review_creds.verify_right_to_work_credential_details()


@then("user verifies link something went wrong")
def user_verifies_something_went_wrong_link(context):
    """step to verify something went wrong link"""
    assert context.review_creds.verify_something_went_wrong_link()


@then("use click confirm credential button")
def user_click_confirm_credential_button(context):
    """step to click confirm credential button"""
    context.review_creds.click_confirm_credential_button()


@then("user see a spinner page with confirming credential")
def user_see_spinner_page_with_confirming_credential(context):
    """step to verify spinner page with confirming credential"""
    assert context.review_creds.verify_spinner_page_with_confirming_credential()


@then("user verifies right to work credential is removed from credentials to confirm")
def user_verifies_right_to_work_credential_removed(context):
    """step to verify right to work credential is removed from credentials to confirm"""
    assert context.review_creds.verify_right_to_work_credential_removed()

@then("user verifies right to work is listed under confirmed credentials")
def user_verifies_right_to_work_listed(context):
    """step to verify right to work is listed under confirmed credentials"""
    assert context.review_creds.verify_right_to_work_listed()


@when("user click DBS supporting documents")
def user_click_dbs_supporting_documents(context):
    """step to click DBS supporting documents"""
    context.review_creds.click_dbs_supporting_documents()


@then(
    "user verifies the DBS supporting documents details - Name, Date of birth, Verified current address, Resident from, Passport number, Passport nationality,Passport issue date, Confirm credential button")
def user_verifies_dbs_supporting_documents_details(context):
    """step to verify DBS supporting documents details"""
    assert context.review_creds.verify_dbs_supporting_documents_details()


@then("user click confirm credential button")
def user_click_confirm_credential_button(context):
    """step to click confirm credential button"""
    context.review_creds.click_confirm_credential_button()


@then("user verifies DBS supporting documents is removed from credentials to confirm")
def user_verifies_dbs_supporting_documents_removed(context):
    """step to verify DBS supporting documents is removed from credentials to confirm"""
    assert context.review_creds.verify_dbs_supporting_documents_removed()


@then("user verifies DBS supporting documents is listed under confirmed credentials")
def user_verifies_dbs_supporting_documents_listed(context):
    """step to verify DBS supporting documents is listed under confirmed credentials"""
    assert context.review_creds.verify_dbs_supporting_documents_listed()
