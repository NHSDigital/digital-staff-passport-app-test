"""page object file for ios app logon"""
from selenium.common import TimeoutException
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from utilities import custom_logger

# Set up logging configuration
logger = custom_logger.get_logger()


class IosAppAutomation(BasePage):
    """Methods to launch ios app"""

    continue_button_xpath = AppiumBy.XPATH, "(//XCUIElementTypeOther[@name=\"Continue\"])[2]"

    def ios_app_homepage_click_on_continue_button(self):
        """Function to click on the continue button on the app homepage"""
        if self.verify_element_displayed(self.continue_button_xpath):
            self.click_element(self.continue_button_xpath, "Click")
