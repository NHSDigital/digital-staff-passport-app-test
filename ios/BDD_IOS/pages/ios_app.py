"""page object file for app logon"""
from selenium.common import TimeoutException
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from utilities import custom_logger

# Set up logging configuration
logger = custom_logger.get_logger()


class IosAppAutomation(BasePage):
    """Methods to launch android app"""

    pre_continue_button_xpath = AppiumBy.XPATH, "(//XCUIElementTypeOther[@name=\"Continue\"])[2]"
    prove_identity_continue_button_xpath = AppiumBy.XPATH, "(//XCUIElementTypeOther[@name=\"Continue\"])[2]"
    post_continue_button_xpath = AppiumBy.XPATH, "(//XCUIElementTypeOther[@name=\"Continue\"])[2]"
    identity_confirmed_continue_button_xpath = AppiumBy.XPATH, "(//XCUIElementTypeOther[@name=\"Continue\"])[3]"
    action_ready_to_review_xpath = AppiumBy.XPATH, "//XCUIElementTypeOther[@name=\"1 credentials ready to review\"]"
    credentials_xpath = AppiumBy.XPATH, "//XCUIElementTypeButton[@name=\"Credentials, tab, 2 of 7\"]"
    connections_xpath = AppiumBy.XPATH, "//XCUIElementTypeButton[@name=\"Connections, tab, 3 of 7\"]"
    message_xpath = AppiumBy.XPATH, "//XCUIElementTypeButton[@name=\"Messages, tab, 4 of 7\"]"

    def ios_app_homepage_click_on_continue_button(self):
        """Function to click on the continue button on the app homepage"""
        if self.verify_element_displayed(self.pre_continue_button_xpath):
            self.click_element(self.pre_continue_button_xpath, "Click")

    def ios_app_prove_identity_pre_click_on_continue_button(self):
        """Function to click on the prove identity page continue button"""
        if self.verify_element_displayed(self.pre_continue_button_xpath):
            self.click_element(self.pre_continue_button_xpath, "Click")

    def ios_app_prove_identity_post_click_on_continue_button(self):
        """Function to click on the prove identity page continue button"""
        if self.verify_element_displayed(self.post_continue_button_xpath):
            self.click_element(self.post_continue_button_xpath, "Click")

    def ios_app_identity_confirmed_continue_button(self):
        """Function to click on the identity confirmed continue button"""
        if self.verify_element_displayed(self.identity_confirmed_continue_button_xpath):
            self.click_element(self.identity_confirmed_continue_button_xpath, "Click")
            self.click_element(self.identity_confirmed_continue_button_xpath, "Click")

    def credentials_ready_to_review_xpath(self):
        """Function to click on the credentials page continue button"""
        if self.verify_element_displayed(self.action_ready_to_review_xpath):
            self.click_element(self.action_ready_to_review_xpath, "Click")

    def credentials_tab_xpath(self):
        """Function to click on the credentials page continue button"""
        if self.verify_element_displayed(self.credentials_xpath):
            self.click_element(self.credentials_xpath, "Click")

    def connection_tab_xpath(self):
        """Function to click on the connection page continue button"""
        if self.verify_element_displayed(self.connections_xpath):
            self.click_element(self.connections_xpath, "Click")

    def messages_tab_xpath(self):
        """Function to click on the messages page continue button"""
        if self.verify_element_displayed(self.message_xpath):
            self.click_element(self.message_xpath, "Click")
            self.close_safari()
