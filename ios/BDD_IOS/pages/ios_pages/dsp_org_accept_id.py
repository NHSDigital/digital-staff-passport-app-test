"""this class contains methods for the page actions
of dsp app homepage"""
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class DspOrgAcceptID(BasePage):
    """ Methods for the DSP APP """

    finger_recog_continue_button_xpath = AppiumBy.XPATH, ''
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
    waiting_org_review_xpath = AppiumBy.XPATH, ''
    trust_name_xpath = AppiumBy.XPATH, ''
    receive_message_xpath = AppiumBy.XPATH, ''

    def app_finger_recog_continue_click(self):
        """Function to click on continue button on fingerprint recognition page"""
        self.click_element_with_wait(
            self.finger_recog_continue_button_xpath, "finger recognition click button xpath"
        )

    def app_enter_pin(self, value):
        """Function to enter pin on app startup"""
        self.verify_element_displayed(self.pin_input_xpath)
        self.type_element(self.pin_input_xpath, value, "enter pin input")

    def app_enter_pin_continue(self):
        """Function to click on the continue button after user enters pin on app startup"""
        self.click_element_with_wait(self.continue_button_xpath, "continue button xpath")

    def app_homepage_welcome_message(self):
        """Function to validate the welcome message on home page"""
        return self.read_value_from_element(self.homepage_welcome_xpath), "welcome message"

    def app_homepage_question_icon_validation(self):
        """Function to validate the question icon on home page"""
        return (
            self.verify_element_displayed(self.homepage_question_icon_xpath),
            "question icon validation",
        )

    def app_homepage_account_icon_validation(self):
        """Function to validate the account icon on home page"""
        return (
            self.verify_element_displayed(self.homepage_account_icon_xpath),
            "account icon validation",
        )

    def app_homepage_action_validate(self):
        """Function to validate the action on home page"""
        return (
            self.verify_element_displayed(self.homepage_action_text_xpath),
            "action validation",
        )

    def app_homepage_credentials_tab_validate(self):
        """Function to validate the credentials on home page"""
        return self.verify_element_displayed(
            self.app_homepage_credentials_tab_xpath, "credentials tab validation"
        )

    def app_homepage_validate_new_provided_creds(self):
        """Function to validate the new provided credentials on home page"""
        return self.read_value_from_element(
            self.app_homepage_credentials_tab_xpath, "new provided credentials validation"
        )

    def app_homepage_creds_tag_validate(self):
        """Function to validate the tag present on credentials on home page"""
        return self.read_value_from_element(
            self.homepage_action_tag_xpath, "tag present on credentials validation"
        )

    def app_trust_name_validate(self):
        """Function to validate the trusted name on waiting page"""
        return (
            self.read_value_from_element(self.trust_name_xpath),
            "trusted name validation",
        )

    def app_waiting_message_validate(self):
        """Function to validate the waiting for organisation to review"""
        return (
            self.read_value_from_element(self.waiting_org_review_xpath),
            "waiting message validation",
        )

    def validate_receive_email_message_validate(self):
        """Function to validate the receive_email message on waiting page"""
        return (
            self.verify_element_displayed(self.receive_message_xpath),
            "receive_email message validation",
        )
