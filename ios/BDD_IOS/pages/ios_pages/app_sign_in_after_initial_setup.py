"""page object file for sign in after initial setup steps"""
from appium.webdriver.common.appiumby import AppiumBy
from utilities import custom_logger
from pages.base_page import BasePage

# Set up logging configuration
logger = custom_logger.get_logger()


class SignInAfterInitialSetup(BasePage):
    """this class contains methods for the page actions
     of dsp app sign in after initial setup page"""

    Log_into_NHS_DSP_heading_xpath = AppiumBy.XPATH, '//XCUIElementTypeStaticText[name == "Login to NHS Digital Staff Passport"]'
    # pin_input_xpath = AppiumBy.XPATH, '//XCUIElementTypeStaticText[name == "Enter your 6 digit PIN"]'
    pin_input_xpath = AppiumBy.ACCESSIBILITY_ID, "login pin-inputField"
    ive_forgotton_pin_link_xpath = AppiumBy.ACCESSIBILITY_ID, "I've forgotten my PIN"
    continue_button_initial_page_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@label=\'Continue\']"
    continue_button_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='undefined-text' and @label='Continue']"
    forgotten_pin_heading_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='undefined-heading-text']"
    your_account_must_be_reset_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='undefined-text' and @label='Your account must be reset and you will need to start again.']"
    your_account_must_be_reset_txt = "Your account must be reset and you will need to start again."
    contact_the_organisation_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='undefined-text' and @label='Contact the organisation's HR team and ask them to delete your details and send you a new invitation email.']"
    contact_the_organisation_txt = "Contact the organisation's HR team and ask them to delete your details and send you a new invitation email."
    incorrect_pin_4attempt_remaining_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='login pin-error-text']"
    incorrect_pin_3attempt_remaining_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='login pin-error-text']"
    incorrect_pin_2attempt_remaining_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='login pin-error-text']"
    incorrect_pin_1attempt_remaining_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='login pin-error-text']"
    maximum_number_of_login_exceeded_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='login pin-error-text']"
    def click_on_forgotton_pin_link(self):
        """Function to click on I have forgotten pin link"""
        self.click_element(self.ive_forgotton_pin_link_xpath, "forgotten pin link")

    def verify_pin_input_box(self):
        """Function to verify pin input box"""
        self.verify_element_displayed(self.pin_input_xpath)

    def enter_incorrect_pin_value_in_input_box(self, value):
        """Function to enter incorrect pin into the input box"""
        self.type_element(self.pin_input_xpath, value)
        self.tap_on_coordinates(244, 340 )

    def verify_log_into_nhs_dsp_heading(self):
        """Function  to verify log into nhs dsp heading"""
        self.verify_element_displayed(self.Log_into_NHS_DSP_heading_xpath)

    def click_continue_button_on_initial_page(self):
        """function to click on continue button"""
        self.click_element(self.continue_button_initial_page_xpath, "Click")

    def click_continue_button(self):
        """function to click on continue button"""
        self.click_element(self.continue_button_xpath, "Click")

    def forgotten_pin_error(self):
        """Function to verify forgotten pin error message"""
        self.verify_element_displayed(self.forgotten_pin_heading_xpath)
        self.take_screenshot("PASS")
        return self.read_value_from_element(self.forgotten_pin_heading_xpath)

    def incorrect_pin_4attempts_remaining_error(self):
        """function to verify incorrect pin 4 attempts remaining error message"""
        self.verify_element_displayed(self.incorrect_pin_4attempt_remaining_xpath)
        self.take_screenshot("PASS")
        return self.read_value_from_element(self.incorrect_pin_4attempt_remaining_xpath)

    def incorrect_pin_3attempts_remaining_error(self):
        """function to verify incorrect pin 3 attempts remaining error message"""
        self.verify_element_displayed(self.incorrect_pin_3attempt_remaining_xpath)
        self.take_screenshot("PASS")
        return self.read_value_from_element(self.incorrect_pin_3attempt_remaining_xpath)

    def incorrect_pin_2attempts_remaining_error(self):
        """function to verify incorrect pin 2 attempts remaining error message"""
        self.verify_element_displayed(self.incorrect_pin_2attempt_remaining_xpath)
        self.take_screenshot("PASS")
        return self.read_value_from_element(self.incorrect_pin_2attempt_remaining_xpath)

    def incorrect_pin_1attempts_remaining_error(self):
        """function to verify incorrect pin 1 attempt remaining error message"""
        self.verify_element_displayed(self.incorrect_pin_1attempt_remaining_xpath)
        self.take_screenshot("PASS")
        return self.read_value_from_element(self.incorrect_pin_1attempt_remaining_xpath)

    def maximum_number_of_login_exceeded_error(self):
        """function to verify incorrect pin attempts exceeded error message"""
        self.verify_element_displayed(self.maximum_number_of_login_exceeded_xpath)
        self.take_screenshot("PASS")
        return self.read_value_from_element(self.maximum_number_of_login_exceeded_xpath)

