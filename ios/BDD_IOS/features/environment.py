import logging

from pages.hr_pages.hr_login_mob import HRPortalLoginMob
from pages.base_page import BasePage


def before_scenario(context, scenario):
    if "app" not in context.feature.name:
        context.driver = logging.FileHandler.selenium_driver = BasePage.open_browser_mobile(context)
        context.base_page = BasePage(context.driver)
        context.base_page.hr_portal_login_homepage()
        context.base_page.click_login_page()


def before_feature(context, feature):
    if "app" in context.feature.name:
        context.driver = logging.FileHandler.selenium_driver = BasePage.open_ios_app(context)
        context.ios_app_homepage = BasePage(context.driver)

def after_scenario(context, scenario):
    if "app" not in context.feature.name:
        context.driver = logging.FileHandler.selenium_driver = BasePage.close_app(context)
        return

def after_feature(context, feature):
    context.driver.quit()
