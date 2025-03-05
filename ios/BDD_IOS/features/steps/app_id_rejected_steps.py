"""Step definitions for app accounts and settings page steps"""
from behave import given, when, then
from pages.ios_pages.app_id_rejected import IdRejectedPage



@then("User validates your identity could not be confirm message")
def sign_in_after_initial_setup_steps(context):
    """ Step to validate your identity could not be confirm message"""
    context.App_Id_Rejected_page = IdRejectedPage(context.driver)
    context.Id_rejected_heading_xpath.verify_id_rejected_heading()


@then("User validates question mark present on page")
def validate_question_mark(context):
    """ Step to validates question mark present on page"""
    context.IdRejectedPage.verify_and_click_on_question_mark()


@then("User validates HR team will contact message on Page")
def sign_in_after_initial_setup_steps(context):
    """ Step to validates HR team will contact message on Page"""
    context.IdRejectedPage.verify_hr_team_will_contact_txt()
