"""Step definitions for app accounts and settings page steps"""
import logging

from behave import given, when, then
from pages.ios_pages.app_id_rejected import IdRejectedPage
from pages.base_page import BasePage


@then("User validates your identity could not be confirm message")
def sign_in_after_initial_setup_steps(context):
    """ Step to click on accounts and settings tab"""
    context.App_Id_Rejected_page = IdRejectedPage(context.driver)
    context.Id_rejected_heading_xpath.verify_id_rejected_heading()


@then("User validates question mark present on page")
def sign_in_after_initial_setup_steps(context):
    """ Step to validate accounts and settings page heading"""
    context.IdRejectedPage.verify_and_click_on_question_mark()

@then("User validates HR team will contact message on Page")
def sign_in_after_initial_setup_steps(context):
    """ Step to validate accounts and settings page heading"""
    context.IdRejectedPage.verify_hr_team_will_contact_txt()
