"""Step definitions for android app poc feature"""

from behave import when, then
from pages.base_page import BasePage
from pages.ios_pages.dsp_org_accept_id import DspOrgAcceptID


@when("click on continue button on finger recognition page")
def dsp_app_continue_click_on_finger_recognition_page(context):
    """step implementation to click on continue button on finger recognition page"""
    context.dsp_app_homepage = DspOrgAcceptID(context.driver)
    context.dsp_app_homepage.app_finger_recog_continue_click()


@then("user enters the pin and click on continue")
def dsp_app_enter_pin(context):
    """step implementation to enter pin and click on continue"""
    context.dsp_app_homepage.app_enter_pin(
        BasePage.get_test_data("", "", "test_data.yaml")
    )
    context.dsp_app_homepage.app_enter_pin_continue()


@then("validate the trust name and waiting message")
def dsp_app_trust_name_and_waiting_message(context):
    """step implementation to validate trust name and waiting message"""
    assert "some text abc" in context.dsp_app_homepage.app_trust_name_validate(), "Unable to validate trusted name"
    assert "some text abc" in context.dsp_app_homepage.app_waiting_message_validate(), ("Unable to validate waiting "
                                                                                        "message")


@then("user verify the welcome message on the homepage")
def dsp_app_validate_welcome_message(context):
    """step implementation to validate welcome message"""
    assert "some text" in context.dsp_app_homepage.app_homepage_welcome_message(), "Unable to validate welcome message"


@then("user validates if question icon is present")
def dsp_app_validate_question_icon(context):
    """step implementation to validate question icon"""
    assert context.dsp_app_homepage.app_homepage_question_icon_validation()


@then("user validates if account icon is present")
def dsp_app_validate_account_icon(context):
    """step implementation to validate account icon"""
    assert context.dsp_app_homepage.app_homepage_account_icon_validation()


@then("user validates if homepage has action section present")
def dsp_app_validate_homepage_tab(context):
    """step implementation to validate homepage action section"""
    assert "Action" in context.dsp_app_homepage.app_homepage_action_validate()


@then("user validates if credentials tab is present")
def dsp_app_validate_homepage_credentials_tab(context):
    """step implementation to validate homepage credentials tab"""
    assert context.dsp_app_homepage.app_homepage_credentials_tab_validate()


@then("user validate that new provided credentials are visible on homepage")
def dsp_app_validate_new_provided_creds_on_homepage(context):
    """step implementation to validate new provided credentials on homepage"""
    context.dsp_app_homepage.app_homepage_validate_new_provided_creds()


@then("user validate the tag present on the new credentials")
def dsp_app_validate_tag_on_new_credentials(context):
    """step implementation to validate tag on new credentials"""
    assert "some text" in context.dsp_app_homepage.app_homepage_creds_tag_validate(), "Unable to validate tag"


@then("validate receive an email message on screen")
def dsp_app_validate_receive_email_message(context):
    """step implementation to validate receive email message"""
    assert (
        "some text abc"
        in context.dsp_app_homepage.validate_receive_email_message_validate()
    ), "Unable to validate receive email message"
