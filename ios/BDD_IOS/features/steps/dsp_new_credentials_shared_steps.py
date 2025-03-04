"""steps for review and confirm initial credentials"""
from behave import given, then, when
from pages.ios_pages.review_confirm_initial_creds_page import ReviewAndConfirmInitialCredentialsPage


@given("user has received an email")
def user_received_an_email(context):
    """step to verify email received"""
    context.review_and_confirm_initial_creds_page = ReviewAndConfirmInitialCredentialsPage(context.driver)

@then("user verifies the content of email is matched")
def user_verifies_email_content(context):
    """step to verify email content"""
    context.review_and_confirm_initial_creds_page.verify_email_content()
@then("user verifies the user name in the email")
def user_verifies_user_name_in_email(context):
    """step to verify user name in email"""
    context.review_and_confirm_initial_creds_page.verify_user_name_in_email()


@given("user is on splash screen")
def user_on_splash_screen(context):
    """step to verify splash screen"""
    context.review_and_confirm_initial_creds_page.verify_user_name_in_email()
@then("user verifies the splash screen content and nhs logo")
def user_verifies_splash_screen_content(context):
    """step to verify splash screen content"""
    context.review_and_confirm_initial_creds_page.verify_splash_screen_content()

@when("user provide wrong face")
def user_provide_wrong_face(context):
    """step to provide wrong face"""
    context.review_and_confirm_initial_creds_page.provide_wrong_face()

@then("user gets an error message")
def user_gets_error_message(context):
    """step to get error message"""
    context.review_and_confirm_initial_creds_page.wrong_face_error_message()

@then("user verifies the subject of an email")
def user_verifies_email_subject(context):
    """step to verify email subject"""
    context.review_and_confirm_initial_creds_page.verify_email_subject()

@then("user verifies the splash screen content nhs logo")
def user_verifies_splash_screen_content(context):
    """step to verify splash screen content"""
    context.review_and_confirm_initial_creds_page.verify_splash_screen_content()

@then("user verifies the NHS logo")
def user_verifies_nhs_logo(context):
    """step to verify nhs logo"""
    assert context.review_and_confirm_initial_creds_page.verify_nhs_logo()


@then("user verifies the version number")
def user_verifies_version_number(context):
    """step to verify version number"""
    context.review_and_confirm_initial_creds_page.verify_version_number()


@then("user is landed on home page")
def user_landed_on_home_page(context):
    """step to verify home page"""
    context.review_and_confirm_initial_creds_page.verify_home_page()
