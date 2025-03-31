"""Contains login functions for HR login for mobile"""

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities import custom_logger


logger = custom_logger.get_logger()

# user_name = ReadProperty.get_user_id()
# pwd = ReadProperty.get_pwd()

USER_NAME = "tushar.dandwate1@nhs.net"
# USER_NAME = "parth.prajapati1@nhs.net"
# PWD = "Password@123"
PWD = "bPspG@251994"

global sms_text_body, passcode_sms


class HRPortalLoginMob(BasePage):
    """contains the page actions & objects related to the hr portal form"""

    # appium version locators
    login_page_xpath = AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Login"]'
    login_id = By.ID, 'signInName'
    password_id = By.ID, 'password'
    login_button = By.ID, 'next'
    digital_staff_passport_portal_text_xpath = By.XPATH, "//h1[contains(text(),' Digital Staff Passport Portal ')]"
    # selenium version locators
    login_page_xpath_selenium = 'xpath://XCUIElementTypeStaticText[@name="Login"]'

    def hr_portal_login_credentials_username(self):
        """Enter the username"""
        self.user_defined_wait(5)
        self.type_element(self.login_id, USER_NAME, "username field")

    def hr_portal_login_credentials_password(self):
        """Enter the password"""
        self.type_element(self.password_id, PWD, "password field")

    def hr_portal_click_login_button(self):
        """Click on login button"""
        # self.verify_element_displayed(self.login_button, "Login button")
        self.click_element_with_wait(self.login_button, "login button")

    def hr_portal_homepage(self):
        """Validate that home page is displayed"""
        self.verify_element_displayed(self.digital_staff_passport_portal_text_xpath)
        self.take_screenshot("PASS")
        return self.read_value_from_element(self.digital_staff_passport_portal_text_xpath)

    def hr_portal_login_homepage_share_journey(self, value):
        """Browser is open and user clicks on HR login link"""
        self.navigate_url(value)
        if self.verify_element_displayed(self.login_page_xpath):
            self.click_element_with_wait(self.login_page_xpath, "Click")
            self.user_defined_wait(5)
