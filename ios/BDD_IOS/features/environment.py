import logging

from pages.hr_pages.hr_login_mob import HRPortalLoginMob
from pages.base_page import BasePage


def before_scenario(context, scenario):
    context.driver = logging.FileHandler.selenium_driver = BasePage.open_browser_mobile(context)
    context.base_page = BasePage(context.driver)
    context.base_page.hr_portal_login_homepage()
    context.base_page.click_login_page()
