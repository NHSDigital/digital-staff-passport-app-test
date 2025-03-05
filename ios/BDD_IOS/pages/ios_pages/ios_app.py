"""page object file for ios app logon"""
from pages.base_page import BasePage
from utilities import custom_logger

# Set up logging configuration
logger = custom_logger.get_logger()


class IosAppAutomation(BasePage):
    """Methods to launch ios app"""

    continue_button_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="continue-button"]',
    )

    def ios_app_homepage_click_on_continue_button(self):
        """Function to click on the continue button on the app homepage"""
        self.click_element(self.continue_button_xpath, "first page continue")
