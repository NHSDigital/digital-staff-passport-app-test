"""this class contains methods for the page actions
of HR Archive credential page"""
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities import custom_logger

logger = custom_logger.get_logger()


class HRArchiveCredentialPage(BasePage):
    """ Elements for the HR Portal-Archive credential page"""

    Fire_safety_link_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"Fire safety\"]"
    Moving_and_handling_cred_list_xpath = AppiumBy.XPATH, ""
    Fire_safety_credential_list_xpath = AppiumBy.XPATH, ""
    Credential_page_heading_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"Credential: Fire safety\"]"
    Credential_archived_restore_link_xpath = AppiumBy.XPATH, ("//XCUIElementTypeStaticText[@name=\"Restore this "
                                                              "credential\"]")
    Credential_restore_page_heading_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"Credential restored\"]"
    Archive_this_credential_link_xpath = AppiumBy.XPATH, ("//XCUIElementTypeStaticText[@name=\"Archive this "
                                                          "credential\"]")
    Credential_archived_success_heading_xpath = AppiumBy.XPATH, ("//XCUIElementTypeStaticText[@name=\"Credential "
                                                                 "archived\"]")
    Credential_archived_success_txt = "Credential archived"
    Back_to_users_passport_link_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[contains(@name, \"'s passport\")]"
    Passport_history_link_xpath = AppiumBy.XPATH, ""
    Passport_history_page_archive_creds_heading_xpath = AppiumBy.XPATH, ""
    Passport_history_page_archive_creds_heading_text = " Passport History: Username"
    Include_archived_credentials_xpath = AppiumBy.XPATH, ("//XCUIElementTypeStaticText[@name=\"Include archived "
                                                          "credentials\"]")
    Credential_archived_txt_xpath = AppiumBy.XPATH, ('//XCUIElementTypeOther[@name="main"]/XCUIElementTypeOther['
                                                     '7]/XCUIElementTypeStaticText')
    Credential_archived_txt = "This credential has been archived"
    Credential_restore_heading_txt = "Credential restored"

    def hr_portal_click_on_fire_safety_credential(self):
        """click on Fire safety credential link on staff passport page"""
        if self.verify_element_displayed(self.Fire_safety_link_xpath):
            self.click_element(self.Fire_safety_link_xpath, "Click")

    def hr_portal_click_on_moving_and_handling_credential(self):
        """click on auto archived moving and handling link on staff passport page"""
        mh_element_count = self.get_element_count("xpath", self.Moving_and_handling_cred_list_xpath)
        if mh_element_count > 0:
            moving_handling_cred_arch_xpath = By.XPATH, (f"(//a[contains(text(),'Moving and handling ("
                                                                      f"Level 1)')])[{mh_element_count}]")
            print(moving_handling_cred_arch_xpath)
            if self.verify_element_displayed(moving_handling_cred_arch_xpath):
                self.click_element(moving_handling_cred_arch_xpath, "Click")

    def hr_portal_click_on_auto_archived_fire_safety_credential(self):
        """click on auto archived Fire safety credential link on staff passport page"""
        fs_element_count = self.get_element_count("xpath", self.Fire_safety_credential_list_xpath)
        if fs_element_count > 0:
            fire_safety_cred_archived_xpath = By.XPATH, f"(//a[contains(text(),'Fire safety')])[{fs_element_count}]"
            if self.verify_element_displayed(fire_safety_cred_archived_xpath):
                self.click_element(fire_safety_cred_archived_xpath, "Click")

    def hr_portal_click_on_archive_this_credential_link(self):
        """function to check credential page heading and click on archive this credential link"""
        if self.verify_element_displayed(self.Credential_page_heading_xpath):
            self.click_element(self.Archive_this_credential_link_xpath, "click")

    def hr_portal_credential_archive_success_message(self):
        """function to check credential archived success heading"""
        if self.verify_element_displayed(self.Credential_archived_success_heading_xpath):
            message = self.read_value_from_element(self.Credential_archived_success_heading_xpath)
            assert message in self.Credential_archived_success_txt
            self.take_screenshot("PASS")

    def hr_portal_click_on_back_to_user_passport_link(self):
        """Function to click on go back to users passport link"""
        if self.verify_element_displayed(self.Back_to_users_passport_link_xpath):
            self.click_element(self.Back_to_users_passport_link_xpath, "click")

    def hr_portal_click_on_include_archived_credentials(self):
        """function to check credential page heading and click on Include archived credentials check box"""
        if self.verify_element_displayed(self.Include_archived_credentials_xpath):
            self.click_element(self.Include_archived_credentials_xpath, "click")

    def hr_portal_credential_archive_page_success_message(self):
        """function to check credential archived success message"""
        if self.verify_element_displayed(self.Credential_archived_txt_xpath):
            message = self.read_value_from_element(self.Credential_archived_txt_xpath)
            assert self.Credential_archived_txt in message
            self.take_screenshot("PASS")

    def hr_portal_click_on_restore_archived_credential_link(self):
        """Function to click restore archived credentials link"""
        if self.verify_element_displayed(self.Credential_archived_restore_link_xpath):
            self.click_element(self.Credential_archived_restore_link_xpath, "click")

    def hr_portal_credential_archived_restore_page_success_message(self):
        """function to check archived credential restore success message"""
        self.user_defined_wait(2)
        if self.verify_element_displayed(self.Credential_restore_page_heading_xpath):
            message = self.read_value_from_element(self.Credential_restore_page_heading_xpath)
            assert self.Credential_restore_heading_txt in message
            self.take_screenshot("PASS")
            self.close_safari()
