"""steps for review and confirm initial credentials"""
from behave import then, when
from pages.ios_pages.review_and_confirm_initial_credentials_page import ReviewAndConfirmInitialCredentialsPage


@given("user has received an email")
def user_received_an_email(context):
    """step to verify email"""
    pass

@then("user verifies the content of email is matched")
def user_verifies_email_content(context):
    """step to verify email content"""
    pass

@then("user verifies the user name in the email")
def user_verifies_user_name_in_email(context):
    """step to verify user name in email"""
    pass


@given("user is on splash screen")
def user_on_splash_screen(context):
    """step to verify splash screen"""
    pass

@then("user verifies the splash screen content and nhs logo")
def user_verifies_splash_screen_content(context):
    """step to verify splash screen content"""
    pass

@when("user provide wrong face")
def user_provide_wrong_face(context):
    """step to provide wrong face"""
    pass

@then("user gets an error message")
def user_gets_error_message(context):
    """step to get error message"""
    pass

@then("user verifies the subject of an email")
def user_verifies_email_subject(context):
    """step to verify email subject"""
    pass

@then("user verifies the splash screen content nhs logo")
def user_verifies_splash_screen_content(context):
    """step to verify splash screen content"""
    pass

@then("user verifies the nhs logo")
def user_verifies_nhs_logo(context):
    """step to verify nhs logo"""
    pass


@then("user verifies the version number")
def user_verifies_version_number(context):
    """step to verify version number"""
    pass

@then("user is landed on home page")
def user_landed_on_home_page(context):
    """step to verify home page"""
    pass
