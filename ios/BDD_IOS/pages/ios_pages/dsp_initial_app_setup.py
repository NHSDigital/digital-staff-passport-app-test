"""this class contains methods for the page actions of dsp initial app setup"""

from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class DspInitialAppSetup(BasePage):
    """this class contains methods for the page actions of dsp initial app setup"""

    """DSP app first page elements"""
    first_page_NHS_logo_xpath = AppiumBy.XPATH, ''
    first_page_NHS_logo_text = 'NHS' # Need to check if this can be readable
    first_page_setup_dsp_text_xpath = AppiumBy.XPATH, ''
    first_page_setup_dsp_text = 'Set up your NHS Digital Staff Passport'

    """DSP app Create PIN page elements"""
    create_pin_page_header_xpath = AppiumBy.XPATH, ''
    create_pin_page_header_text = 'Create a PIN'
    pin_input_xpath = AppiumBy.XPATH, ''
    pin_confirm_input_xpath = AppiumBy.XPATH, ''
    continue_button_xpath = AppiumBy.XPATH, ''
    question_button_xpath = AppiumBy.XPATH, ''
    term_of_user_link_xpath = AppiumBy.XPATH, ''
    privacy_notice_link_xpath = AppiumBy.XPATH, ''
    terms_and_conditions_link_xpath = AppiumBy.XPATH, ''

    """DSP app Fingerprint page elements"""
    fingerprint_page_header_xpath = AppiumBy.XPATH, ''
    fingerprint_page_header_text = 'Fingerprint recognition'
    enable_fingerprint_recognition_toggle_xpath = AppiumBy.XPATH, ''

    """DSP app Prove who you are page elements"""
    prove_who_you_are_page_header_xpath = AppiumBy.XPATH, ''
    prove_who_you_are_page_header_text = 'NHS Digital Staff Passport'
    prove_who_you_are_page_sub_header_xpath = AppiumBy.XPATH, ''
    prove_who_you_are_page_sub_header_text = 'Prove who you are to get full access'
    prove_who_you_are_page_text_xpath = AppiumBy.XPATH, ''
    prove_who_you_are_page_text = 'You\'ll need to prove your identity before you can use NHS Digital Staff Passport'

    """DSP app Prove your identity page elements"""
    prove_your_identity_page_header_xpath = AppiumBy.XPATH, ''
    prove_your_identity_page_header_text = 'Prove your identity'
    prove_your_identity_page_sub_header1_xpath = AppiumBy.XPATH, ''
    prove_your_identity_page_sub_header1_text = 'What to expect'
    prove_your_identity_page_sub_header2_xpath = AppiumBy.XPATH, ''
    prove_your_identity_page_sub_header2_text = 'What happens then'
    prove_your_identity_page_in_person_link_xpath = AppiumBy.XPATH, ''
    prove_your_identity_page_in_person_link_text = 'I\'ll prove my identity in person instead'


    def verify_question_icon(self):
        """Function to verify question icon"""
        return self.verify_element_displayed(self.question_button_xpath),"first page question icon"

    def verify_app_first_page_nhs_logo(self):
        """this method checks NHS logo on the app first page"""
        return self.verify_element_displayed(self.first_page_NHS_logo_xpath), "NHS logo"

    def verify_app_first_page_setup_dsp_text(self):
        """this method checks text on the app first page"""
        if self.verify_element_displayed(self.first_page_setup_dsp_text_xpath):
            message = self.read_value_from_element(self.first_page_setup_dsp_text_xpath)
            assert self.first_page_setup_dsp_text in message
            self.take_screenshot("PASS")

    def click_continue(self):
        """Function to click continue on dsp app page"""
        if self.verify_element_displayed(self.continue_button_xpath):
            self.click_element(self.continue_button_xpath, "Continue")

    def verify_create_pin_page_header(self):
        """this method checks header of the create pin page"""
        if self.verify_element_displayed(self.create_pin_page_header_xpath):
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
        if self.verify_element_displayed(self.pin_input_xpath):
            self.type_element(self.pin_input_xpath, value)

    def confirm_create_pin(self, value):
        """Function to confirm pin on app initial setup"""
        if self.verify_element_displayed(self.pin_confirm_input_xpath):
            self.type_element(self.pin_confirm_input_xpath, value)

    def verify_fingerprint_page_header(self):
        """Function to validate Fingerprint page heading of app initial setup"""
        if self.verify_element_displayed(self.fingerprint_page_header_xpath):
            message = self.read_value_from_element(self.fingerprint_page_header_xpath)
            assert self.fingerprint_page_header_text in message
            self.take_screenshot("PASS")

    def enable_disable_figer_print_recognition(self):
        """Function to click toggle button to enable or disable fingerprint recognition"""
        if self.verify_element_displayed(self.enable_fingerprint_recognition_toggle_xpath):
            self.click_element(self.enable_fingerprint_recognition_toggle_xpath, "fingerprint toggle")

    def verify_prove_who_you_are_page_header(self):
        """Function to validate who you are page header of app initial setup validation"""
        if self.verify_element_displayed(self.prove_who_you_are_page_header_xpath):
            message = self.read_value_from_element(self.prove_who_you_are_page_header_xpath)
            assert self.prove_who_you_are_page_header_text in message
            self.take_screenshot("PASS")

    def verify_prove_who_you_are_sub_header(self):
        """Function to validate who you are sub header of app initial setup"""
        if self.verify_element_displayed(self.prove_who_you_are_page_sub_header_xpath):
            message = self.read_value_from_element(self.prove_who_you_are_page_sub_header_xpath)
            assert self.prove_who_you_are_page_sub_header_text in message
            self.take_screenshot("PASS")

    def verify_prove_who_you_are_page_text(self):
        """Function to validate who you are page text of app initial setup"""
        if self.verify_element_displayed(self.prove_who_you_are_page_text_xpath):
            message = self.read_value_from_element(self.prove_who_you_are_page_text_xpath)
            assert self.prove_who_you_are_page_text in message
            self.take_screenshot("PASS")

    def verify_prove_your_identity_header(self):
        """Function to validate prove your identity header of app initial setup"""
        if self.verify_element_displayed(self.prove_your_identity_page_header_xpath):
            message = self.read_value_from_element(self.prove_your_identity_page_header_xpath)
            assert self.prove_your_identity_page_header_text in message
            self.take_screenshot("PASS")

    def verify_prove_identity_what_to_expect_heading(self):
        """Function to validate prove identity what to expect heading of app initial setup"""
        if self.verify_element_displayed(self.prove_your_identity_page_sub_header1_xpath):
            message = self.read_value_from_element(self.prove_your_identity_page_sub_header1_xpath)
            assert self.prove_your_identity_page_sub_header1_text in message
            self.take_screenshot("PASS")

    def verify_prove_identity_what_happens_heading(self):
        """Function to validate prove identity what happens heading of app initial setup"""
        if self.verify_element_displayed(self.prove_your_identity_page_sub_header2_xpath):
            message = self.read_value_from_element(self.prove_your_identity_page_sub_header2_xpath)
            assert self.prove_your_identity_page_sub_header2_text in message
            self.take_screenshot("PASS")

    def verify_prove_identity_in_person_link(self):
        """Function to validate prove identity in_person link of app initial setup"""
        return self.verify_element_displayed(self.prove_your_identity_page_in_person_link_xpath), ("prove identity "
                                                                                                   "in-person link")
