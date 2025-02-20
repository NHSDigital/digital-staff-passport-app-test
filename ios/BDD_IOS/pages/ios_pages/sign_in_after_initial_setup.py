"""page object file for sign in after initial setup steps"""

from selenium.common import TimeoutException
from appium.webdriver.common.appiumby import AppiumBy
from utilities import custom_logger
from pages.base_page import BasePage

# Set up logging configuration
logger = custom_logger.get_logger()


class SignInAfterInitialSetup(BasePage):

    Log_into_NHS_DSP_heading_xpath = AppiumBy.XPATH, ''
    pin_input_xpath = AppiumBy.XPATH, ''
    ive_forgotton_pin_link_xpath = AppiumBy.XPATH, ''
    continue_button_xpath = AppiumBy.XPATH, ''
    forgotten_pin_heading_xpath = AppiumBy.XPATH, ''
    Forgotten_pin_text = "your account must be reset and you will need to start again"
    your_account_must_be_reset_txt = AppiumBy.XPATH, ''
    incorrect_pin_2attempt_remaining_xpath = AppiumBy.XPATH, ''
    incorrect_pin_2attempt_remaining_text = "Incorrect pin. you have (2) tries remaining"
    incorrect_pin_1attempt_remaining_xpath = AppiumBy.XPATH, ''
    incorrect_pin_1attempt_remaining_text = "Incorrect pin. you have (1) tries remaining"
    maximum_number_of_login_exceeded_xpath = AppiumBy.XPATH, ''
    maximum_number_of_login_exceeded_text = "Maximum number of login attempts exceeded. you can try again in [x] minutes"


    def click_on_forgotton_pin_link(self):
        """Function to click on I have forgotten pin link"""
        self.click_element(self.ive_forgotton_pin_link_xpath, "Ive forgotton pin link")


    def verify_pin_input_box(self):
        """Function to verify pin input box"""
        return self.verify_element_displayed(self.pin_input_xpath, "Pin input text box")


    def enter_incorrect_pin_value_in_input_box(self, value):
        """Function to enter incorrect pin into the input box"""
        self.type_element(self.pin_input_xpath, value, "Enter incorrect pin value")


    def verify_log_into_nhs_dsp_heading(self):
        """Function  to verify log into nhs dsp heading"""
        return self.verify_element_displayed(self.Log_into_NHS_DSP_heading_xpath, "Log into NHS DSP heading")


    def click_continue_button(self):
        """function to click on continue button"""
        self.click_element(self.continue_button_xpath, "Click")


    def forgotten_pin_error(self):
        """Function to verify forgotten pin error message"""
        return self.verify_element_displayed(self.forgotten_pin_heading_xpath, "forgotten pin heading")

        message = self.read_value_from_element(self.forgotten_pin_heading_xpath)
        assert self.Forgotten_pin_text in message
        self.take_screenshot("PASS")


    def incorrect_pin_2attempts_remaining_error(self):
        """function to verify incorrect pin 2 attempts remaining error message"""
        return self.verify_element_displayed(self.incorrect_pin_2attempt_remaining_xpath, "incorrect pin 2 attempts remaining error message")

        message = self.read_value_from_element(self.incorrect_pin_2attempt_remaining_xpath)
        assert self.incorrect_pin_2attempt_remaining_text in message
        self.take_screenshot("PASS")


    def incorrect_pin_1attempts_remaining_error(self):
        """function to verify incorrect pin 1 attempts remaining error message"""
        return self.verify_element_displayed(self.incorrect_pin_1attempt_remaining_xpath, "incorrect pin 1 attempts remaining error message")

        message = self.read_value_from_element(self.incorrect_pin_1attempt_remaining_xpath)
        assert self.incorrect_pin_1attempt_remaining_text in message
        self.take_screenshot("PASS")

    def maximum_number_of_login_exceeded_xpath(self):
        """function to verify incorrect pin attempts exceeded error message"""
        return self.verify_element_displayed(self.maximum_number_of_login_exceeded_xpath, "incorrect pin attempts exceeded error message")

        message = self.read_value_from_element(self.maximum_number_of_login_exceeded_xpath)
        assert self.maximum_number_of_login_exceeded_text in message
        self.take_screenshot("PASS")
