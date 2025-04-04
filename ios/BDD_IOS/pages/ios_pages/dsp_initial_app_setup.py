"""this class contains methods for the page actions of dsp initial app setup"""
from pyexpat.errors import messages

from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class DspInitialAppSetup(BasePage):
    """this class contains methods for the page actions of dsp initial app setup"""

    # DSP app first page elements
    first_page_NHS_logo_xpath = AppiumBy.XPATH, "//XCUIElementTypeOther[@name=\"NHS logo\"]"
    first_page_NHS_logo_text = 'NHS'  # Need to check if this can be readable
    first_page_setup_dsp_text_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@label="Set up your NHS Digital\nStaff Passport"]',
    )
    first_page_setup_dsp_text = 'Set up your NHS Digital'
    # DSP app Create PIN page elements
    create_pin_page_header_xpath = AppiumBy.XPATH, "(//XCUIElementTypeOther[@name=\"Create a PIN\"])[2]"
    create_pin_page_header_text = 'Create a PIN'
    pin_input_xpath = AppiumBy.XPATH, "//XCUIElementTypeSecureTextField[@name=\"pin-inputField\"]"
    pin_confirm_input_xpath = AppiumBy.XPATH, "//XCUIElementTypeSecureTextField[@name=\"confirm-pin-inputField\"]"
    continue_button_xpath = AppiumBy.XPATH, "//XCUIElementTypeButton[@name=\"continue-button\"]"
    question_button_xpath = AppiumBy.XPATH, "//XCUIElementTypeOther[@name=\"navigation-icon-help-icon\"]"
    term_of_user_link_xpath = AppiumBy.XPATH, ("//XCUIElementTypeStaticText[@name=\"bulletPoint-link-text\" and "
                                               "@label=\"terms of use\"]")
    privacy_notice_link_xpath = AppiumBy.XPATH, ("//XCUIElementTypeStaticText[@name=\"bulletPoint-link-text\" and "
                                                 "@label=\"privacy notice\"]")
    terms_and_conditions_link_xpath = AppiumBy.XPATH, ("//XCUIElementTypeStaticText[@name=\"bulletPoint-link-text\" "
                                                       "and @label=\"terms and conditions\"]")
    create_a_pin_continue_button_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@label=\"Continue\"]"

    # DSP app Fingerprint page elements
    fingerprint_page_header_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@value=\"Fingerprint recognition\"]"
    fingerprint_page_header_text = 'Fingerprint recognition'
    enable_fingerprint_recognition_toggle_xpath = AppiumBy.XPATH, ''
    fingerprint_disable_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@label=\"Fingerprint recognition has been disabled on your device\"]"
    fingerprint_disable_text = 'Fingerprint recognition has been disabled on your device'

    # DSP app Prove who you are page elements
    prove_who_you_are_page_header_xpath = AppiumBy.XPATH, ('//XCUIElementTypeStaticText[@label="NHS Digital Staff '
                                                           'Passport"]')
    prove_who_you_are_page_header_text = 'NHS Digital Staff Passport'
    prove_who_you_are_page_sub_header_xpath = AppiumBy.XPATH, ('//XCUIElementTypeStaticText[@label="Prove who you are '
                                                               'to get full access"]')
    prove_who_you_are_page_sub_header_text = 'Prove who you are to get full access'
    prove_who_you_are_page_text_xpath = AppiumBy.XPATH, ('//XCUIElementTypeStaticText[@label="You\'ll need to prove '
                                                         'your identity before you can use NHS Digital Staff '
                                                         'Passport"]')
    prove_who_you_are_page_text = 'You\'ll need to prove your identity before you can use NHS Digital Staff Passport'

    # DSP app Prove your identity page elements
    prove_your_identity_page_header_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@value="Prove your Identity"]',
    )
    prove_your_identity_page_header_text = 'Prove your Identity'
    prove_your_identity_page_sub_header1_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@label="What to expect"]',
    )
    prove_your_identity_page_sub_header1_text = 'What to expect'
    prove_your_identity_page_sub_header2_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@label="What happens then"]',
    )
    prove_your_identity_page_sub_header2_text = 'What happens then'
    prove_your_identity_page_in_person_link_xpath = AppiumBy.XPATH, ('//XCUIElementTypeStaticText[@label="I\'ll prove '
                                                                     'my identity in person instead"]')
    prove_your_identity_page_in_person_link_text = 'I\'ll prove my identity in person instead'

    def verify_question_icon(self):
        """Function to verify question icon"""
        return self.verify_element_displayed(self.question_button_xpath), "first page question icon"

    def verify_nhs_logo_first_page(self):
        """method to verify nhs logo"""
        return self.verify_element_displayed(self.first_page_NHS_logo_xpath, "nhs logo")

    def verify_app_first_page_nhs_logo(self):
        """this method checks NHS logo on the app first page"""
        return self.verify_element_displayed(self.first_page_NHS_logo_xpath), "NHS logo"

    def verify_app_first_page_setup_dsp_text(self):
        """this method checks text on the app first page"""
        self.verify_element_displayed(self.first_page_setup_dsp_text_xpath)
        message = self.read_value_from_element(self.first_page_setup_dsp_text_xpath)
        assert self.first_page_setup_dsp_text in message
        self.take_screenshot("PASS")

    def click_continue(self):
        """Function to click continue on dsp app page"""
        self.click_element_with_wait(self.continue_button_xpath, "Continue")

    def create_a_pin_click_continue(self):
        """Function to create a pin click continue on dsp app page"""
        self.click_element_with_wait(self.create_a_pin_continue_button_xpath, "Continue")

    def verify_create_pin_page_header(self):
        """this method checks header of the create pin page"""
        self.verify_element_displayed(self.create_pin_page_header_xpath)
        message = self.read_value_from_element(self.create_pin_page_header_xpath)
        assert self.create_pin_page_header_text in message
        self.take_screenshot("PASS")

    def verify_create_pin_term_of_use_link(self):
        """Function to verify term of use agreement link on create pin page"""
        return self.verify_element_displayed(self.term_of_user_link_xpath), "create pin term of use link"

    def verify_create_pin_privacy_link(self):
        """Function to verify privacy agreement link on create pin page"""
        return self.verify_element_displayed(self.privacy_notice_link_xpath), "create pin privacy notice"

    def verify_create_pin_terms_link(self):
        """Function to verify terms agreement link on create pin page"""
        return self.verify_element_displayed(self.terms_and_conditions_link_xpath), "create pin terms"

    def set_create_pin(self, value):
        """Function to enter pin on app initial setup"""
        self.verify_element_displayed(self.pin_input_xpath)
        self.type_element(self.pin_input_xpath, value)

    def confirm_create_pin(self, value):
        """Function to confirm pin on app initial setup"""
        self.verify_element_displayed(self.pin_confirm_input_xpath)
        self.type_element(self.pin_confirm_input_xpath, value)
        self.tap_on_coordinates(140, 360)

    def verify_fingerprint_page_header(self):
        """Function to validate Fingerprint page heading of app initial setup"""
        self.verify_element_displayed(self.fingerprint_page_header_xpath)
        message = self.read_value_from_element(self.fingerprint_page_header_xpath)
        assert self.fingerprint_page_header_text in message
        self.take_screenshot("PASS")

    def enable_disable_figer_print_recognition(self):
        """Function to click toggle button to enable or disable fingerprint recognition"""
        self.click_element_with_wait(self.enable_fingerprint_recognition_toggle_xpath, "fingerprint toggle")

    def verify_prove_who_you_are_page_header(self):
        """Function to validate who you are page header of app initial setup validation"""
        self.verify_element_displayed(self.prove_who_you_are_page_header_xpath)
        message = self.read_value_from_element(self.prove_who_you_are_page_header_xpath)
        assert self.prove_who_you_are_page_header_text in message
        self.take_screenshot("PASS")

    def verify_prove_who_you_are_sub_header(self):
        """Function to validate who you are sub header of app initial setup"""
        self.verify_element_displayed(self.prove_who_you_are_page_sub_header_xpath)
        message = self.read_value_from_element(self.prove_who_you_are_page_sub_header_xpath)
        assert self.prove_who_you_are_page_sub_header_text in message
        self.take_screenshot("PASS")

    def verify_prove_who_you_are_page_text(self):
        """Function to validate who you are page text of app initial setup"""
        self.verify_element_displayed(self.prove_who_you_are_page_text_xpath)
        message = self.read_value_from_element(self.prove_who_you_are_page_text_xpath)
        assert self.prove_who_you_are_page_text in message
        self.take_screenshot("PASS")

    def verify_prove_your_identity_header(self):
        """Function to validate prove your identity header of app initial setup"""
        self.verify_element_displayed(self.prove_your_identity_page_header_xpath)
        message = self.read_value_from_element(self.prove_your_identity_page_header_xpath)
        assert self.prove_your_identity_page_header_text in message
        self.take_screenshot("PASS")

    def verify_prove_identity_what_to_expect_heading(self):
        """Function to validate prove identity what to expect heading of app initial setup"""
        self.verify_element_displayed(self.prove_your_identity_page_sub_header1_xpath)
        message = self.read_value_from_element(self.prove_your_identity_page_sub_header1_xpath)
        assert self.prove_your_identity_page_sub_header1_text in message
        self.take_screenshot("PASS")

    def verify_prove_identity_what_happens_heading(self):
        """Function to validate prove identity what happens heading of app initial setup"""
        self.verify_element_displayed(self.prove_your_identity_page_sub_header2_xpath)
        message = self.read_value_from_element(self.prove_your_identity_page_sub_header2_xpath)
        assert self.prove_your_identity_page_sub_header2_text in message
        self.take_screenshot("PASS")

    def verify_prove_identity_in_person_link(self):
        """Function to validate prove identity in_person link of app initial setup"""
        return self.verify_element_displayed(self.prove_your_identity_page_in_person_link_xpath), ("prove identity "
                                                                                                   "in-person link")

    def verify_fingerprint_toggle_disable(self):
        """Function to verify if the toggle is disabled"""
        self.verify_element_displayed(self.fingerprint_disable_xpath)
        message = self.read_value_from_element(self.fingerprint_disable_xpath)
        assert message in self.fingerprint_disable_text
        self.take_screenshot("PASS")
