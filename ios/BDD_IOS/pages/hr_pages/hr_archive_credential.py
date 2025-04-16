"""this class contains methods for the page actions
of HR Archive credential page"""
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities import custom_logger

logger = custom_logger.get_logger()


class HRArchiveCredentialPage(BasePage):
    """Elements for the HR Portal-Archive credential page"""

    Fire_safety_link_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Fire safety"]',
    )
    Moving_and_handling_cred_list_xpath = AppiumBy.XPATH, ""
    Fire_safety_credential_list_xpath = AppiumBy.XPATH, ""
    Credential_page_heading_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Credential: Fire safety"]',
    )
    Credential_archived_restore_link_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeStaticText[@name="Restore this credential"]'
    )
    credential_restore_page_heading_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Credential restored"]',
    )
    Archive_this_credential_link_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeStaticText[@name="Archive this credential"]'
    )
    Credential_archived_success_heading_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeStaticText[@name="Credential archived"]'
    )
    Credential_archived_success_txt = "Credential archived"
    Back_to_users_passport_link_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[contains(@name, "\'s passport")]',
    )
    Passport_history_link_xpath = AppiumBy.XPATH, ""
    Passport_history_page_archive_creds_heading_xpath = AppiumBy.XPATH, ""
    Passport_history_page_archive_creds_heading_text = (
        "Passport History: Username"
    )
    Include_archived_credentials_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Include archived credentials"]'
    )
    Credential_archived_txt_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeOther[@name="main"]/XCUIElementTypeOther['
        "7]/XCUIElementTypeStaticText"
    )
    Credential_archived_txt = "This credential has been archived"
    Credential_restore_heading_txt = "Credential restored"

    def hr_portal_click_on_fire_safety_credential(self):
        """Click on Fire safety credentials"""
        self.click_element_with_wait(self.Fire_safety_link_xpath, "Click on fire safety")

    def hr_portal_click_on_moving_and_handling_credential(self):
        """Click on auto archived moving and handling creds"""
        mh_element_count = self.get_element_count(
            "xpath", self.Moving_and_handling_cred_list_xpath
        )
        if mh_element_count > 0:
            moving_handling_cred_arch_xpath = By.XPATH, (
                f"(//a[contains(text(),'Moving and handling ("
                f"Level 1)')])[{mh_element_count}]"
            )
            print(moving_handling_cred_arch_xpath)
            self.click_element_with_wait(moving_handling_cred_arch_xpath, "Click on moving handling")

    def hr_portal_click_on_auto_archived_fire_safety_credential(self):
        """click on auto archived Fire safety credential"""
        fs_element_count = self.get_element_count(
            "xpath", self.Fire_safety_credential_list_xpath
        )
        if fs_element_count > 0:
            fire_safety_cred_archived_xpath = (
                By.XPATH,
                f"(//a[contains(text(),'Fire safety')])[{fs_element_count}]",
            )
            self.click_element_with_wait(fire_safety_cred_archived_xpath, "Click on auto archive")

    def hr_portal_click_on_archive_this_credential_link(self):
        """Checks creds heading & click on archive credential"""
        self.click_element_with_wait(
                self.Archive_this_credential_link_xpath, "click on archive credential")

    def hr_portal_credential_archive_success_message(self):
        """function to check credential archived success heading"""
        self.verify_element_displayed(
            self.Credential_archived_success_heading_xpath
        )
        message = self.read_value_from_element(
            self.Credential_archived_success_heading_xpath
        )
        assert message in self.Credential_archived_success_txt
        self.take_screenshot("PASS")

    def hr_portal_click_on_back_to_user_passport_link(self):
        """Function to click on go back to users passport link"""
        self.click_element_with_wait(
            self.Back_to_users_passport_link_xpath, "click on back")

    def hr_portal_click_on_include_archived_credentials(self):
        """Check creds heading & clicks include archived creds checkbox"""
        self.click_element_with_wait(
                self.Include_archived_credentials_xpath, "click on include archived")

    def hr_portal_credential_archive_page_success_message(self):
        """function to check credential archived success message"""
        self.verify_element_displayed(self.Credential_archived_txt_xpath)
        message = self.read_value_from_element(self.Credential_archived_txt_xpath)
        assert self.Credential_archived_txt in message
        self.take_screenshot("PASS")

    def hr_portal_click_on_restore_archived_credential_link(self):
        """Function to click restore archived credentials link"""
        self.click_element_with_wait(
                self.Credential_archived_restore_link_xpath, "click on restore")

    def hr_portal_credential_archived_restore_page_success_message(self):
        """function to check archived credential restore success message"""
        self.user_defined_wait(2)
        self.verify_element_displayed(
        self.credential_restore_page_heading_xpath
        )
        message = self.read_value_from_element(
            self.credential_restore_page_heading_xpath
        )
        assert self.Credential_restore_heading_txt in message
        self.take_screenshot("PASS")
        self.close_safari()
