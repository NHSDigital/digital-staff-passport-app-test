"""this class contains methods for the page actions of dsp app access link"""
from pyexpat.errors import messages

from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class DspNotification(BasePage):
    """this class contains methods for the page actions of dsp app access link"""

    signup_email_xpath = AppiumBy.XPATH, ("//XCUIElementTypeStaticText[@label=\"Sign up for NHS Digital Staff "
                                          "Passport\"]")
    email_notification_open_xpath = AppiumBy.XPATH, "//XCUIElementTypeButton[@name=\"swipe-action-button-identifier\"]"
    start_now_link_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"Start now\"]"


    def signup_email_click(self):
        """clicks on signup email on iphone notification"""
        self.open_notification()
        self.click_element_with_wait(self.signup_email_xpath)
        self.click_element_with_wait(self.email_notification_open_xpath)

    def email_goto_start_now_link(self):
        """User goes to start now link and save the url in yaml"""
        self.click_element_with_wait(self.start_now_link_xpath)
