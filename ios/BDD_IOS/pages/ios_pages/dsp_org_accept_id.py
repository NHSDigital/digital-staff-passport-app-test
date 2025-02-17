"""this class contains methods for the page actions
of dsp app homepage"""
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class DspOrgAcceptID(BasePage):
    """ Methods for the DSP APP """

    pin_input_xpath = AppiumBy.XPATH, ''
    continue_button_xpath = AppiumBy.XPATH, ''
    homepage_welcome_xpath = AppiumBy.XPATH, ''
    homepage_welcome_text = "Welcome"
    homepage_question_icon_xpath = AppiumBy.XPATH, ''
    homepage_account_icon_xpath = AppiumBy.XPATH, ''
    homepage_action_text_xpath = AppiumBy.XPATH, ''
    app_homepage_credentials_tab_xpath = AppiumBy.XPATH, ''
    credential_ready_to_review_text = AppiumBy.XPATH, ''
    homepage_action_tag_xpath = AppiumBy.XPATH, ''
    homepage_action_tag_text = "ready to review"


    def app_enter_pin(self):
        """Function to enter pin on app startup"""
        if self.verify_element_displayed(self.pin_input_xpath):
            self.type_element(self.pin_input_xpath, "Click")

    def app_enter_pin_continue(self):
        """Function to click on the continue button after user enters pin on app startup"""
        if self.verify_element_displayed(self.continue_button_xpath):
            self.click_element(self.continue_button_xpath, "Click")

    def app_homepage_welcome_message(self):
        """Function to validate the welcome message on home page"""
        if self.verify_element_displayed(self.homepage_welcome_xpath):
            message = self.read_value_from_element(self.homepage_welcome_xpath)
            assert self.homepage_welcome_text in message
            self.take_screenshot("PASS")

    def app_homepage_question_icon_validation(self):
        """Function to validate the question icon on home page"""
        if self.verify_element_displayed(self.homepage_question_icon_xpath):
            pass

    def app_homepage_account_icon_validation(self):
        """Function to validate the account icon on home page"""
        if self.verify_element_displayed(self.homepage_account_icon_xpath):
            pass

    def app_homepage_action_validate(self):
        """Function to validate the action on home page"""
        if self.verify_element_displayed(self.homepage_action_text_xpath):
            pass

    def app_homepage_credentials_tab_validate(self):
        """Function to validate the credentials on home page"""
        if self.verify_element_displayed(self.app_homepage_credentials_tab_xpath):
            pass

    def app_homepage_validate_new_provided_creds(self):
        """Function to validate the new provided credentials on home page"""
        if self.verify_element_displayed(self.app_homepage_credentials_tab_xpath):
            message = self.read_value_from_element(self.app_homepage_credentials_tab_xpath)
            assert self.credential_ready_to_review_text in message
            self.take_screenshot("PASS")

    def app_homepage_creds_tag_validate(self):
        """Function to validate the tag present on credentials on home page"""
        if self.verify_element_displayed(self.homepage_action_tag_xpath):
            message = self.read_value_from_element(self.homepage_action_tag_xpath)
            assert self.homepage_action_tag_text in message
            self.take_screenshot("PASS")
