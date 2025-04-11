"""Step definitions for accessing the notification and emails"""
import logging

from behave import given, when, then
from pages.base_page import BasePage
from pages.ios_pages.app_notification import DspNotification

@given('user opens the received email from iphone notification')
def received_email_notification_click(context):
    """Step file to open notification and click on received email"""
    context.driver = logging.FileHandler.selenium_driver = DspNotification(context)
    context.dsp_app_notification = DspNotification(context.driver)
    context.dsp_app_notification.signup_email_click()


@when('user scroll till start now and saves the start now link present')
def user_save_start_now_lnk_(context):
    """Step file to search start now and save start now link present"""
    context.dsp_app_notification.email_goto_start_now_link()
