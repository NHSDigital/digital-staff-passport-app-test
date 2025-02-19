"""steps for review and confirm initial credentials"""
from behave import then, when
from pages.ios_pages.review_and_confirm_initial_credentials_page import ReviewAndConfirmInitialCredentialsPage

@then


@given("user has received an email")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given user has received an email')


@then("user verifies the content of email is matched")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then user verifies the content of email is matched')


@then("user verifies the user name in the email")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then user verifies the user name in the email')


@given("user is on splash screen")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given user is on splash screen')


@then("user verifies the splash screen content and nhs logo")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then user verifies the splash screen content and nhs logo')


@when("user provide wrong face")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When user provide wrong face')


@then("user gets an error message")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then user gets an error message')
