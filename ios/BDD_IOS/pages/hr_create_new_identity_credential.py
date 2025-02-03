"""this class contains methods for the page actions
of HR portal to create new identity credential user page"""
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities import custom_logger
# logger = custom_logger.get_logger()


class HRPortalCreateNewIdentityCredentialPage(BasePage):
    """ Elements for the HR Portal for staff passport for user page"""

    login_page_id = By.ID, 'Login'
    Create_new_identity_credential_link_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"Create a new identity credential\"]"
    Create_new_identity_cred_for_user_heading_xpath = AppiumBy.XPATH, "//XCUIElementTypeOther[@name=\"main\"]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText"
    Create_new_identity_cred_for_user_heading_text = "Create a new identity credential"
    Create_new_ID_Continue_button_xpath = AppiumBy.XPATH, "//XCUIElementTypeButton[@name=\"Continue\"]"
    Confirm_users_details_heading_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[contains(@name, \"Confirm\") and contains(@name, \"details\")]"
    Yes_provide_credential_radio_button_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"Yes, provide credential\"]"
    No_go_back_radio_button_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"No, go back\"]"
    New_Identity_credential_provided_success_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"New Identity credential provided\"]"
    New_Identity_credential_provided_success_heading_txt = "New Identity credential provided"

    New_Identity_back_to_user_passport_link_xpath = AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name=\"Go to staff member\'s passport\"]'
    New_Identity_Passport_history_link_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"Passport history\"]"
    Passport_history_page_heading_new_id_creds_xpath = AppiumBy.XPATH, "//XCUIElementTypeOther[@name=\"main\"]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText"
    Passport_history_page_heading_new_id_creds_txt = "Passport History"
    Passport_history_event_txt_new_id_creds_xpath = AppiumBy.XPATH, '//XCUIElementTypeOther[@name="main"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeStaticText[2]'
    Passport_history_event_new_id_creds_txt = "dentity"

    def hr_portal_create_a_new_identity_credential(self):
        """ Function to create a new identity credential"""
        if self.verify_element_displayed(self.Create_new_identity_credential_link_xpath):
            self.click_element(self.Create_new_identity_credential_link_xpath, "Click")

    def hr_portal_create_new_identity_credential_details_continue(self):
        """ Function to verify Create a new identity credential for user page and click on continue button """
        if self.verify_element_displayed(self.Create_new_identity_cred_for_user_heading_xpath):
            message = self.read_value_from_element(self.Create_new_identity_cred_for_user_heading_xpath)
            assert self.Create_new_identity_cred_for_user_heading_text in message
        if self.verify_element_displayed(self.Create_new_ID_Continue_button_xpath):
            self.click_element(self.Create_new_ID_Continue_button_xpath, "Click")

    def hr_portal_create_new_identity_cred_yes_radio_button(self):
        """Function to confirm users details page and click yes provide credential radio button"""
        if self.verify_element_displayed(self.Confirm_users_details_heading_xpath):
            self.click_element(self.Yes_provide_credential_radio_button_xpath, "Click")
            self.click_element(self.Create_new_ID_Continue_button_xpath, "Click")

    def hr_portal_new_identity_credential_provided_success(self):
        """ Function to verify New Identity credential provided success message"""
        if self.verify_element_displayed(self.New_Identity_credential_provided_success_xpath):
            message = self.read_value_from_element(self.New_Identity_credential_provided_success_xpath)
            assert message in self.New_Identity_credential_provided_success_heading_txt
            self.take_screenshot("PASS")

    def hr_portal_new_identity_creds_passport_history_event_details(self):
        """Function to verify passport history heading and event"""
        if self.verify_element_displayed(self.New_Identity_back_to_user_passport_link_xpath):
            self.click_element(self.New_Identity_back_to_user_passport_link_xpath, "click")
        if self.verify_element_displayed(self.New_Identity_Passport_history_link_xpath):
            self.click_element(self.New_Identity_Passport_history_link_xpath, "click")
        if self.verify_element_displayed(self.Passport_history_page_heading_new_id_creds_xpath):
            message = self.read_value_from_element(self.Passport_history_event_txt_new_id_creds_xpath)
            assert self.Passport_history_event_new_id_creds_txt in message
            self.take_screenshot("PASS")
            self.close_safari()

