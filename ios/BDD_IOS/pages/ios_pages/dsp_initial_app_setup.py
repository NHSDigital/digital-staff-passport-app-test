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


    def app_first_page_validation(self):
        """this method checks if the app first page is open"""
        if self.verify_element_displayed(self.first_page_NHS_logo_xpath):
            if self.verify_element_displayed(self.first_page_setup_dsp_text_xpath):
                message = self.read_value_from_element(self.first_page_setup_dsp_text_xpath)
                assert self.first_page_setup_dsp_text in message
                self.take_screenshot("PASS")

    def app_first_page_continue(self):
        """Function to click continue on app first page"""
        if self.verify_element_displayed(self.continue_button_xpath):
            self.click_element(self.continue_button_xpath, "first page continue")

    def app_create_pin_question_button_validation(self):
        """Function to create pin question button validation"""
        if self.verify_element_displayed(self.question_button_xpath):
            self.click_element(self.question_button_xpath, "create pin question")

    def app_create_pin_agree_links_validation(self):
        # revisit this function to complete link web page validation and switch back to app
        """Function to create pin agreement links validation"""
        if self.verify_element_displayed(self.term_of_user_link_xpath):
            self.click_element(self.term_of_user_link_xpath, "create pin term of use link")
        if self.verify_element_displayed(self.privacy_notice_link_xpath):
            self.click_element(self.privacy_notice_link_xpath, "create pin privacy notice")
        if self.verify_element_displayed(self.terms_and_conditions_link_xpath):
            self.click_element(self.terms_and_conditions_link_xpath, "create pin terms")

    def app_create_pin_enter(self, value):
        """Function to enter pin on app initial setup"""
        if self.verify_element_displayed(self.pin_input_xpath):
            self.type_element(self.pin_input_xpath, value)

    def app_create_pin_confirm(self, value):
        """Function to confirm pin on app initial setup"""
        if self.verify_element_displayed(self.pin_confirm_input_xpath):
            self.type_element(self.pin_confirm_input_xpath, value)

    def app_create_pin_continue(self):
        """Function to click continue to create pin on app initial setup"""
        if self.verify_element_displayed(self.continue_button_xpath):
            self.click_element(self.continue_button_xpath, "create pin continue")

    def app_fingerprint_page_validation(self):
        """Function to validate Fingerprint page heading of app initial setup"""
        if self.verify_element_displayed(self.fingerprint_page_header_xpath):
            message = self.read_value_from_element(self.fingerprint_page_header_xpath)
            assert self.fingerprint_page_header_text in message
            self.take_screenshot("PASS")

    def app_fingerprint_page_continue(self):
        """Function to click continue to on Fingerprint page of app initial setup"""
        if self.verify_element_displayed(self.continue_button_xpath):
            self.click_element(self.continue_button_xpath, "fingerprint page continue")

    def app_prove_who_you_are_page_header_validation(self):
        """Function to validate who you are page header of app initial setup validation"""
        if self.verify_element_displayed(self.prove_who_you_are_page_header_xpath):
            message = self.read_value_from_element(self.prove_who_you_are_page_header_xpath)
            assert self.prove_who_you_are_page_header_text in message
            self.take_screenshot("PASS")

    def app_prove_who_you_are_sub_header_validation(self):
        """Function to validate who you are sub header of app initial setup"""
        if self.verify_element_displayed(self.prove_who_you_are_page_sub_header_xpath):
            message = self.read_value_from_element(self.prove_who_you_are_page_sub_header_xpath)
            assert self.prove_who_you_are_page_sub_header_text in message
            self.take_screenshot("PASS")

    def app_prove_who_you_are_page_text_validation(self):
        """Function to validate who you are page text of app initial setup"""
        if self.verify_element_displayed(self.prove_who_you_are_page_text_xpath):
            message = self.read_value_from_element(self.prove_who_you_are_page_text_xpath)
            assert self.prove_who_you_are_page_text in message
            self.take_screenshot("PASS")

    def app_prove_who_you_are_page_continue_click(self):
        """Function to click continue on Prove who you are page of app initial setup"""
        if self.verify_element_displayed(self.continue_button_xpath):
            self.click_element(self.continue_button_xpath, "prove who you are page continue")

    def app_prove_your_identity_page_validation(self):
        """Function to validate prove your identity page of app initial setup"""
        # elements and expected texts in pairs
        elements_to_validate = [
            (self.prove_your_identity_page_header_xpath, self.prove_your_identity_page_header_text),
            (self.prove_your_identity_page_sub_header1_xpath, self.prove_your_identity_page_sub_header1_text),
            (self.prove_your_identity_page_sub_header2_xpath, self.prove_your_identity_page_sub_header2_text),
            (self.prove_your_identity_page_in_person_link_xpath, self.prove_your_identity_page_in_person_link_text)
        ]
        # Loop through each element and validate
        for element_xpath, expected_text in elements_to_validate:
            if self.verify_element_displayed(element_xpath):
                message = self.read_value_from_element(element_xpath)
                assert expected_text in message
                self.take_screenshot("PASS")

    def app_prove_your_identity_page_continue_click(self):
        """Function to click continue on Prove your identity page of app initial setup"""
        if self.verify_element_displayed(self.continue_button_xpath):
            self.click_element(self.continue_button_xpath, "prove your identity page continue")
