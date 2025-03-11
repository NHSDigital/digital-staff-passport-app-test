"""
Steps definition w.r.t hr portal login mobile feature
"""

import logging

from behave import given, when, then

from pages.base_page import BasePage
from pages.hr_pages.hr_login_mob import HRPortalLoginMob  # Import the NHSAppAutomation class


@given('Browser is open and user clicks on HR login link')
def get_browser_register_link(context):
    """Step to hr login link after browser is open"""
    # context.driver = logging.FileHandler.selenium_driver = HRPortalLoginMob.open_browser_mobile(context)
    # context.driver = logging.FileHandler.selenium_driver = HRPortalLoginMob.open_browser_mobile_simulator(context)
    context.hr_portal_login = HRPortalLoginMob(context.driver)
    # context.hr_portal_login.hr_portal_login_homepage()


@when('Enter the credentials & click on login button')
def hr_portal_login_credentials(context):
    """Step to enter credentials & click on login button"""
    context.hr_portal_login.hr_portal_login_credentials_username()
    context.hr_portal_login.hr_portal_login_credentials_password()
    context.hr_portal_login.hr_portal_click_login_button()


@then('Verify the HR portal homepage is displayed')
def hr_portal_homepage_displayed(context):
    """Step to verify the HR portal homepage is displayed"""
    context.hr_portal_login.hr_portal_homepage()


@given('Browser is open and user clicks on STH HR login link - share journey')
def get_browser_hr_login_link_share_journey(context):
    """Step to hr login link after browser is open - sth trust"""
    context.driver = logging.FileHandler.selenium_driver = HRPortalLoginMob.open_browser_mobile(context)
    context.hr_portal_login = HRPortalLoginMob(context.driver)
    context.hr_portal_login.hr_portal_login_homepage_share_journey(
        (BasePage.get_test_data("Share_Journey", "Sheffield_hr_url", "test_data.yaml")))
