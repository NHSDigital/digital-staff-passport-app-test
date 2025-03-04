"""this class contains methods for the page actions
of dsp initial setup for pin errors"""
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class DspBiometricPinError(BasePage):
    """ Methods for the error validation for pin creation """

    pin_error_pin1_xpath = AppiumBy.XPATH, ''
    pin_error_pin2_xpath = AppiumBy.XPATH, ''
    pin_error_pin_does_not_change_xpath = AppiumBy.XPATH, ''
    pin_does_not_change_text_xpath = AppiumBy.XPATH, ''
    create_pin_continue_xpath = AppiumBy.XPATH, ''
    pin_error_empty_xpath = AppiumBy.XPATH, ''
    pin_error_empty_text_xpath = ''
    pin_error1_xpath = 'PINs do not match'
    pin_error2_xpath = 'PIN must be 6 digits, with no number repeated 3 times, and not sequential'


    def app_pin_error_enter_pin1(self):
        """Function to enter in pin1"""
        if self.verify_element_displayed(self.pin_error_pin1_xpath):
            self.click_element(self.pin_error_pin1_xpath, "Click")

    def app_pin_error_enter_pin2(self):
        """Function to enter in pin2"""
        if self.verify_element_displayed(self.pin_error_pin2_xpath):
            self.click_element(self.pin_error_pin2_xpath, "Click")

    def app_create_pin_continue_button(self):
        """Function to click on continue button"""
        self.click_element(self.create_pin_continue_xpath, "Create a pin continue button")

    def app_pin_does_not_match_validation(self, error_pin_do_not_match):
        """Function to validate error message when pin does not match"""
        if self.verify_element_displayed(self.pin_error_pin_does_not_change_xpath):
            message = self.read_value_from_element(self.pin_does_not_change_text_xpath)
            return error_pin_do_not_match in message
        return None

    def app_pin_empty_validation(self, error_pin_not_six_digit):
        """Function to validate error message when pin is empty"""
        if self.verify_element_displayed(self.pin_error_empty_xpath):
            message = self.read_value_from_element(self.pin_error_empty_xpath)
            assert error_pin_not_six_digit in message


    def app_pin_alpha_numeric_validation(self, error_pin_not_six_digit):
        """Function to validate error message when alpha numeric value is entered"""
        if self.verify_element_displayed(self.pin_error_empty_xpath):
            message = self.read_value_from_element(self.pin_error_empty_xpath)
            assert error_pin_not_six_digit in message


    def app_pin_special_character_validation(self, error2):
        """Function to validate error message when special character is entered"""
        if self.verify_element_displayed(self.pin_error_empty_xpath):
            message = self.read_value_from_element(self.pin_error_empty_xpath)
            assert error2 in message


    def app_pin_sequential_validation(self, error_pin_not_six_digit):
        """Function to validate error message when sequential number is entered"""
        if self.verify_element_displayed(self.pin_error_empty_xpath):
            message = self.read_value_from_element(self.pin_error_empty_xpath)
            assert error_pin_not_six_digit in message


    def app_pin_reverse_sequential_validation(self, error_pin_not_six_digit):
        """Function to validate error message when reverse sequential number is entered"""
        if self.verify_element_displayed(self.pin_error_empty_xpath):
            message = self.read_value_from_element(self.pin_error_empty_xpath)
            assert error_pin_not_six_digit in message


    def app_pin_not_repeated_validation(self, error_pin_do_not_match):
        """Function to validate error message when pin is not repeated"""
        if self.verify_element_displayed(self.pin_error_empty_xpath):
            message = self.read_value_from_element(self.pin_error_empty_xpath)
            assert error_pin_do_not_match in message


    def app_pin_not_repeated_viceversa_validation(self, error_pin_not_six_digit):
        """Function to validate error message when pin is not repeated viceversa"""
        if self.verify_element_displayed(self.pin_error_empty_xpath):
            message = self.read_value_from_element(self.pin_error_empty_xpath)
            assert error_pin_not_six_digit in message

    def app_pin_not_six_digit_validation(self, error_pin_not_six_digit):
        """Function to validate error message when pin is not six digit"""
        if self.verify_element_displayed(self.pin_error_empty_xpath):
            message = self.read_value_from_element(self.pin_error_empty_xpath)
            assert error_pin_not_six_digit in message
