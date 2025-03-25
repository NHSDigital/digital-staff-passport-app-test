"""Contains login functions for HR login for mobile"""

from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from utilities import custom_logger

logger = custom_logger.get_logger()

# user_name = ReadProperty.get_user_id()
# pwd = ReadProperty.get_pwd()

USER_NAME = "parth.prajapati1@nhs.net"
PWD = "Password@123"

global sms_text_body, passcode_sms


class HRPortalLoginMob(BasePage):
    """contains the page actions & objects related to the hr portal form"""

    login_page_xpath = AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Login"]'
    login_id_xpath = AppiumBy.XPATH, '//XCUIElementTypeTextField[@name="Email address"]'
    password_id_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeSecureTextField[@name="Password"]',
    )
    login_button_xpath = AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Login"]'
    digital_staff_passport_portal_text_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeStaticText[@name="Digital Staff Passport Portal"]'
    )
    login_id = '//XCUIElementTypeButton[@name="Login"]'
    digital_staff_passport_portal_text = "Digital Staff Passport Portal"

    # def hr_portal_login_homepage(self):
    #     """Browser is open and user clicks on register link"""
    #     self.open_dsp_hr_portal_application_url()
    #     self.user_defined_wait(5)
    #     if self.verify_element_displayed(self.login_page_xpath):
    #         self.click_element(self.login_page_xpath, "Click")
    #         self.user_defined_wait(5)

    def hr_portal_login_credentials_username(self):
        """Enter the username"""
        # self.scroll_to_element("xpath", self.login_id)
        if self.verify_element_displayed(self.login_id_xpath):
            self.type_element(self.login_id_xpath, USER_NAME)

    def hr_portal_login_credentials_password(self):
        """Enter the password"""
        if self.verify_element_displayed(self.password_id_xpath):
            self.type_element(self.password_id_xpath, PWD)

    def hr_portal_click_login_button(self):
        """Click on login button"""
        if self.verify_element_displayed(self.login_button_xpath):
            self.click_element(self.login_button_xpath, "Click")

    def hr_portal_homepage(self):
        """Validate that home page is displayed"""
        if self.verify_element_displayed(self.digital_staff_passport_portal_text_xpath):
            message = self.read_value_from_element(
                self.digital_staff_passport_portal_text_xpath
            )
            assert message in self.digital_staff_passport_portal_text
            print(message)
            self.take_screenshot("PASS")

    def hr_portal_login_homepage_share_journey(self, value):
        """Browser is open and user clicks on HR login link"""
        self.navigate_url(value)
        if self.verify_element_displayed(self.login_page_xpath):
            self.click_element(self.login_page_xpath, "Click")
            self.user_defined_wait(5)
