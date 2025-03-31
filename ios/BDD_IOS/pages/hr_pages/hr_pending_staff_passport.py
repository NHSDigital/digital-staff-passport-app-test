"""this class contains methods for the page actions
of HR portal Pending Staff Passport page"""
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.hr_pages.hr_identity_and_access import HRIdentityAndAccessPage
from utilities import custom_logger

logger = custom_logger.get_logger()


class HRPendingStaffPassportPage(BasePage):
    """Elements for the HR Portal-Pending staff passport to provide credentials"""

    menu_toggle_xpath = HRIdentityAndAccessPage.menu_toggle_id
    pending_staff_passport_page_link_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeStaticText[@name="Pending staff passports"]'
    )
    click_review_cred_request_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeStaticText[@name="Review credential requests"]'
    )
    provide_credentials_button_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Provide Credentials"]',
    )
    radio_button_elements = '(//XCUIElementTypeOther[@value="0"])'
    pending_search_input_xpath = By.ID, "SearchInput"
    pending_search_submit_xpath = By.XPATH, "//button[@type='submit']"
    pending_search_result_xpath = By.XPATH, "//table[@role='table']/tbody/tr[1]/td/a"
    connect_to_esr_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Connect to ESR"]',
    )
    enter_esr_number_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeTextField[@name="ESR assignment number"]',
    )
    confirm_esr_number_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="Confirm"]',
    )
    connect_passport_to_esr_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Connect passport to ESR"]',
    )
    connect_button_xpath = AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Connect"]'
    yes_radio_btn_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Yes, this is the correct staff member"]',
    )
    no_radio_btn_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="No, edit the ESR assignment number"]',
    )
    continue_btn_xpath = AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Continue"]'
    provide_credentials_link_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Provide Credentials"]',
    )
    back_link_pending_staff_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeStaticText[@name="Not now - go back to '
        "AutomationTwo User's passport\"]"
    )
    provide_creds_count = '(//XCUIElementTypeOther[@value="0"])[{position_number}]'
    review_credentials_confirm_yes_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeStaticText[@name="Yes, continue with this selection"]'
    )
    review_credentials_success_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeStaticText[@name="Credential requests reviewed"]'
    )
    review_credentials_success_txt = "Credential requests reviewed"
    manage_passport_link_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Manage passport"]',
    )
    delete_passport_link_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Delete passport"]',
    )
    delete_passport_continue_btn_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="Continue"]',
    )
    delete_passport_data_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="Delete passport and its data"]',
    )
    delete_passport_message_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Passport deleted."]',
    )
    delete_passport_message_txt = "Passport deleted."
    passport_status_xpath = ""
    passport_status_initial_value_xpath = ""
    passport_status_initial_value_txt = ""
    passport_show_all_details_xpath = ""
    click_shared_review_cred_request_xpath = ""
    click_shared_review_accept_radio_button_xpath = ""
    click_shared_review_accept_continue_button_xpath = ""
    click_shared_review_accept_yes_confirm_radio_button_xpath = ""
    click_shared_review_accept_success_header_xpath = ""
    click_shared_review_accept_success_header_txt = ""
    pending_credentials_view_credentials_link_xpath = By.LINK_TEXT, "View credentials"
    dbs_supporting_information_credentials_expand_button = By.XPATH, "//span[contains(text(),'DBS supporting')]"
    pending_staff_passports_menu_link = By.XPATH, "//a[contains(text(),' Pending staff passports ')]"
    hr_portal_pending_staff_passport_back_link = By.LINK_TEXT, "Back"
    remind_user_to_review_link = By.XPATH, "//span[contains(text(),'Remind')]"
    identity_credentials_expand_button = By.XPATH, "//span[contains(text(),'Identity')]"
    rtw_credentials_expand_button = By.XPATH, "//span[contains(text(),'Right to work')]"
    """dbs credentials"""
    dbs_withdraw_link = (
        By.XPATH,
        "//div[contains(text(),'DBS supporting information')]/../details/summary/div/a[contains(text(),'Withdraw')]",
    )
    dbs_first_name = (
        By.XPATH,
        "//div[contains(text(),'DBS supporting information')]/..//dt[contains(text(),'First name')]/../dd",
    )
    dbs_last_name = (
        By.XPATH,
        "//div[contains(text(),'DBS')]/..//dt[contains(text(),'Last name')]/../dd",
    )
    dbs_dob = (
        By.XPATH,
        "//div[contains(text(),'DBS')]/..//dt[contains(text(),'Date of birth')]/../dd",
    )
    dbs_current_address_verified = (
        By.XPATH,
        "//div[contains(text(),'DBS')]/..//dt[contains(text(),'Current address verified')]/../dd",
    )
    dbs_current_address = (
        By.XPATH,
        "//div[contains(text(),'DBS')]/..//dt[text()='Current address']/../dd",
    )
    dbs_date_of_address_check = (
        By.XPATH,
        "//div[contains(text(),'DBS')]/..//dt[contains(text(),'Date of address check')]/../dd",
    )
    dbs_identity_verified = (
        By.XPATH,
        "//div[contains(text(),'DBS')]/..//dt[contains(text(),'Identity verified')]/../dd",
    )
    dbs_level_of_Assurance = (
        By.XPATH,
        "//div[contains(text(),'DBS')]/..//dt[contains(text(),'Level of Assurance')]/../dd",
    )
    dbs_policy = (
        By.XPATH,
        "//div[contains(text(),'DBS')]/..//dt[contains(text(),'Policy')]/../dd",
    )
    dbs_evidence_checked_by = (
        By.XPATH,
        "//div[contains(text(),'DBS')]/..//dt[contains(text(),'Evidence checked by')]/../dd",
    )
    dbs_passport_date_of_birth = (
        By.XPATH,
        "//div[contains(text(),'DBS')]/..//dt[contains(text(),'Date of birth')]/../dd",
    )
    dbs_evidence_profile = (
        By.XPATH,
        "//div[contains(text(),'DBS')]/..//dt[contains(text(),'Evidence Profile')]/../dd",
    )
    dbs_subject_id = (
        By.XPATH,
        "//div[contains(text(),'DBS')]/..//dt[contains(text(),'SubjectID')]/../dd",
    )
    dbs_origin = (
        By.XPATH,
        "//div[contains(text(),'DBS')]/..//dt[contains(text(),'Origin')]/../dd",
    )
    dbs_assurance_policy = (
        By.XPATH,
        "//div[contains(text(),'DBS')]/..//dt[contains(text(),'Assurance policy')]//../dd",
    )
    dbs_assurance_outcome = (
        By.XPATH,
        "//div[contains(text(),'DBS')]/..//dt[contains(text(),'Assurance outcome')]/../dd",
    )
    dbs_provider = (
        By.XPATH,
        "//div[contains(text(),'DBS')]/..//dt[contains(text(),'Provider')]/../dd",
    )
    dbs_verifier = (
        By.XPATH,
        "//div[contains(text(),'DBS')]/..//dt[contains(text(),'Verifier')]/../dd",
    )
    dbs_verification_method = (
        By.XPATH,
        "//div[contains(text(),'DBS')]/..//dt[contains(text(),'Verification method')]/../dd",
    )
    dbs_pedigree = (
        By.XPATH,
        "//div[contains(text(),'DBS')]/..//dt[contains(text(),'Pedigree')]/../dd",
    )
    dbs_last_refresh = (
        By.XPATH,
        "//div[contains(text(),'DBS')]/..//dt[contains(text(),'Last refresh')]/../dd",
    )

    """identity credentials"""
    id_withdraw_link = (
        By.XPATH,
        "//div[contains(text(),'Identity')]/../details/summary/div/a[contains(text(),'Withdraw')]",
    )
    id_first_name = (
        By.XPATH,
        "//span[contains(text(),'Identity')]/../../..//dt[contains(text(),'First name')]/../dd",
    )
    id_last_name = (
        By.XPATH,
        "//span[contains(text(),'Identity')]/../../..//dt[contains(text(),'Last name')]/../dd",
    )
    id_dob = (
        By.XPATH,
        "//span[contains(text(),'Identity')]/../../..//dt[contains(text(),'Date of birth')]/../dd",
    )
    id_current_address_verified = (
        By.XPATH,
        "//span[contains(text(),'Identity')]/../../..//dt[contains(text(),'Current address verified')]/../dd",
    )
    id_legal_gender = (
        By.XPATH,
        "//span[contains(text(),'Identity')]/../../..//dt[contains(text(),'Legal gender')]/../dd",
    )
    id_address = (
        By.XPATH,
        "//span[contains(text(),'Identity')]/../../..//dt[contains(text(),'Address')]/../dd",
    )
    id_origin = (
        By.XPATH,
        "//span[contains(text(),'Identity')]/../../..//dt[contains(text(),'Origin')]/../dd",
    )
    id_assurance_policy = (
        By.XPATH,
        "//span[contains(text(),'Identity')]/../../..//dt[contains(text(),'Assurance policy')]/../dd",
    )
    id_assurance_outcome = (
        By.XPATH,
        "//span[contains(text(),'Identity')]/../../..//dt[contains(text(),'Assurance outcome')]/../dd",
    )
    id_provider = (
        By.XPATH,
        "//span[contains(text(),'Identity')]/../../..//dt[contains(text(),'Provider')]/../dd",
    )
    id_verifier = (
        By.XPATH,
        "//span[contains(text(),'Identity')]/../../..//dt[contains(text(),'Verifier')]/../dd",
    )
    id_verification_method = (
        By.XPATH,
        "//span[contains(text(),'Identity')]/../../..//dt[contains(text(),'Verification method')]/../dd",
    )
    id_pedigree = (
        By.XPATH,
        "//span[contains(text(),'Identity')]/../../..//dt[contains(text(),'Pedigree')]/../dd",
    )
    id_last_refresh = (
        By.XPATH,
        "//span[contains(text(),'Identity')]/../../..//dt[contains(text(),'Last refresh')]/../dd",
    )

    """right to work credentials"""
    rtw_withdraw_link = (
        By.XPATH,
        "//div[contains(text(),'Right to work')]/../details/summary/div/a[contains(text(),'Withdraw')]",
    )
    rtw_legal_first_name = (
        By.XPATH,
        "//div[contains(text(),'Right to work')]/..//dt[contains(text(),'Legal first name')]/../dd",
    )
    rtw_legal_surname = (
        By.XPATH,
        "//div[contains(text(),'Right to work')]/..//dt[contains(text(),'Legal surname')]/../dd",
    )
    rtw_birth_date = (
        By.XPATH,
        "//div[contains(text(),'Right to work')]/..//dt[contains(text(),'Birth date')]/../dd",
    )
    rtw_identity_verified = (
        By.XPATH,
        "//div[contains(text(),'Right to work')]/..//dt[contains(text(),'Identity verified')]/../dd",
    )
    rtw_evidence_checked_by = (
        By.XPATH,
        "//div[contains(text(),'Right to work')]/..//dt[contains(text(),'Evidence checked by')]/../dd",
    )
    rtw_gpg45_profile = (
        By.XPATH,
        "//div[contains(text(),'Right to work')]/..//dt[contains(text(),'GPG45 Profile')]/../dd",
    )
    rtw_origin = (
        By.XPATH,
        "//div[contains(text(),'Right to work')]/..//dt[contains(text(),'Origin')]/../dd",
    )
    rtw_assurance_policy = (
        By.XPATH,
        "//div[contains(text(),'Right to work')]/..//dt[contains(text(),'Assurance policy')]/../dd",
    )
    rtw_assurance_outcome = (
        By.XPATH,
        "//div[contains(text(),'Right to work')]/..//dt[contains(text(),'Assurance outcome')]/../dd",
    )
    rtw_provider = (
        By.XPATH,
        "//div[contains(text(),'Right to work')]/..//dt[contains(text(),'Provider')]/../dd",
    )
    rtw_verifier = (
        By.XPATH,
        "//div[contains(text(),'Right to work')]/..//dt[contains(text(),'Verifier')]/../dd",
    )
    rtw_verification_method = (
        By.XPATH,
        "//div[contains(text(),'Right to work')]/..//dt[contains(text(),'Verification method')]/../dd",
    )
    rtw_pedigree = (
        By.XPATH,
        "//div[contains(text(),'Right to work')]/..//dt[contains(text(),'Pedigree')]/../dd",
    )
    rtw_last_refresh = (
        By.XPATH,
        "//div[contains(text(),'Right to work')]/..//dt[contains(text(),'Last refresh')]/../dd",
    )

    def hr_portal_pending_staff_passport_tab(self):
        """ Click on the Pending Staff Passport Tab within HR Portal"""
        self.click_element_with_wait(self.pending_staff_passports_menu_link, "pending staff passport menu link")
        self.user_defined_wait(3)

    def hr_portal_pending_search_username(self, value):
        """ Enter the DSP user details in the search box """
        # self.verify_element_displayed(self.pending_search_input_xpath)
        self.type_element(self.pending_search_input_xpath, value)

    def hr_portal_pending_search_submit_click(self):
        """ Click on the search button """
        self.click_element_with_wait(self.pending_search_submit_xpath, "pending search submit")

    def hr_portal_pending_search_result(self):
        """ Result should be displayed and user should click on the same"""
        self.click_element_with_wait(self.pending_search_result_xpath, "searched staff name link")

    def hr_portal_passport_page_initial_status_validation(self):
        """ Validate the passport status in the passport profile page"""
        if self.verify_element_displayed(self.passport_status_xpath):
            element = self.read_value_from_element(self.passport_status_initial_value_xpath)
            assert element in self.passport_status_initial_value_txt
            self.take_screenshot("PASS")

    def hr_portal_passport_page_click_on_show_details(self):
        """Function to click on show details link"""
        self.user_defined_wait(2)
        if self.verify_element_displayed(self.passport_show_all_details_xpath):
            self.click_element_with_wait(self.passport_show_all_details_xpath, "Click")
            self.user_defined_wait(2)

    def hr_portal_pending_click_review_credentials_request(self):
        """ Click on the Alert for reviewing the Credentials Requests"""
        if self.verify_element_displayed(self.click_review_cred_request_xpath):
            self.click_element_with_wait(self.click_review_cred_request_xpath, "Click")
            self.user_defined_wait(3)

    def hr_portal_pending_provide_credentials(self):
        """ Review the credentials request & select the provide radio button for the same"""
        # add scroll
        count = self.get_element_count("xpath", self.radio_button_elements)
        element_list = count // 2   # This will give you an integer result
        for i in range(1, element_list + 1, 1):
            provide_path = By.XPATH, self.provide_creds_count.format(position_number=i)
            cred_to_provide = self.verify_element_displayed(provide_path)
            cred_to_provide.click()

    def hr_portal_pending_provide_credentials_button(self):
        """ Click on the Provide Credential button"""
        if self.verify_element_displayed(self.provide_credentials_button_xpath):
            self.click_element_with_wait(self.provide_credentials_button_xpath, "Click")
            self.user_defined_wait(3)

    def hr_portal_pending_provide_credentials_continue(self):
        """ Click on Continue button , post selection of the request"""
        if self.verify_element_displayed(self.continue_btn_xpath):
            self.click_element_with_wait(self.continue_btn_xpath, "Click")
            self.user_defined_wait(3)

    def hr_portal_pending_provide_credentials_confirm_yes(self):
        """ Click on Yes radio button w.r.t credential request"""
        if self.verify_element_displayed(self.review_credentials_confirm_yes_xpath):
            self.click_element_with_wait(self.review_credentials_confirm_yes_xpath, "Click")
            self.user_defined_wait(3)

    def hr_portal_pending_provide_credentials_confirm_continue(self):
        """ Click on Continue button w.r.t credential request"""
        if self.verify_element_displayed(self.continue_btn_xpath):
            self.click_element_with_wait(self.continue_btn_xpath, "Click")
            self.user_defined_wait(3)

    def hr_portal_pending_provide_credentials_reviewed_success(self):
        """ Request reviewed successfully and message is displayed """
        self.user_defined_wait(3)
        if self.verify_element_displayed(self.review_credentials_success_xpath):
            message = self.read_value_from_element(self.review_credentials_success_xpath)
            assert message in self.review_credentials_success_txt
            self.take_screenshot("PASS")
            self.close_safari()

    def hr_portal_pending_connect_esr(self):
        """ Click on the Connect To ESR link button under Photo section"""
        if self.verify_element_displayed(self.connect_to_esr_xpath):
            self.click_element_with_wait(self.connect_to_esr_xpath, "Click")
            self.user_defined_wait(3)

    def hr_portal_pending_enter_esr_number(self, value):
        """ Enter valid ESR Number """
        if self.verify_element_displayed(self.enter_esr_number_xpath):
            self.type_element(self.enter_esr_number_xpath, value)
            self.user_defined_wait(3)

    def hr_portal_pending_confirm_esr_number(self):
        """ Click on the confirm button w.r.t ESR """
        if self.verify_element_displayed(self.confirm_esr_number_xpath):
            self.click_element_with_wait(self.confirm_esr_number_xpath, "Click")
            self.user_defined_wait(3)

    def hr_portal_pending_connect_to_passport(self):
        """ Click on the Connect to Passport Link"""
        if self.verify_element_displayed(self.connect_passport_to_esr_xpath):
            self.click_element_with_wait(self.connect_passport_to_esr_xpath, "Click")
            self.user_defined_wait(3)

    def hr_portal_pending_passport_connect_proceed(self):
        """ Click on Connect button"""
        if self.verify_element_displayed(self.connect_button_xpath):
            self.click_element_with_wait(self.connect_button_xpath, "Click")
            self.user_defined_wait(10)

    def hr_portal_pending_connect_to_passport_confirm_yes(self):
        """ Select the Yes radio button"""
        if self.verify_element_displayed(self.yes_radio_btn_xpath):
            self.click_element_with_wait(self.yes_radio_btn_xpath, "Click")
            self.user_defined_wait(3)

    def hr_portal_pending_connect_to_passport_confirm_no(self):
        """ Select the No radio button"""
        if self.verify_element_displayed(self.no_radio_btn_xpath):
            self.click_element_with_wait(self.no_radio_btn_xpath, "Click")
            self.user_defined_wait(3)

    def hr_portal_pending_connect_to_passport_confirm_continue(self):
        """ Click on the confirm button w.r.t Connect to Passport """
        if self.verify_element_displayed(self.continue_btn_xpath):
            self.click_element_with_wait(self.continue_btn_xpath, "Click")
            self.user_defined_wait(3)

    def hr_portal_pending_provide_credentials_link(self):
        """ Click on Provide Credentials Link"""
        if self.verify_element_displayed(self.provide_credentials_link_xpath):
            self.click_element_with_wait(self.provide_credentials_link_xpath, "Click")
            self.user_defined_wait(5)

    def hr_portal_pending_back_link_passport_page(self):
        """ Click on the back link to navigate back to passport page """
        if self.verify_element_displayed(self.back_link_pending_staff_xpath):
            self.click_element_with_wait(self.back_link_pending_staff_xpath, "Click")
            self.user_defined_wait(2)

    def hr_portal_pending_manage_passport_link(self):
        """ Click on Manage Passport Link"""
        if self.verify_element_displayed(self.manage_passport_link_xpath):
            self.click_element_with_wait(self.manage_passport_link_xpath, "Click")

    def hr_portal_pending_delete_passport_link(self):
        """ Click on Delete Passport Link"""
        if self.verify_element_displayed(self.delete_passport_link_xpath):
            self.click_element_with_wait(self.delete_passport_link_xpath, "Click")

    def hr_portal_pending_delete_passport_continue(self):
        """ Click on Continue button w.r.t delete passport"""
        if self.verify_element_displayed(self.delete_passport_continue_btn_xpath):
            self.click_element_with_wait(self.delete_passport_continue_btn_xpath, "Click")

    def hr_portal_pending_delete_passport_data(self):
        """ Click on delete passport data"""
        if self.verify_element_displayed(self.delete_passport_data_xpath):
            self.click_element_with_wait(self.delete_passport_data_xpath, "Click")

    def hr_portal_pending_delete_passport_message(self):
        """ Validate the message displayed in the screen"""
        if self.verify_element_displayed(self.delete_passport_message_xpath):
            message = self.read_value_from_element(self.delete_passport_message_xpath)
            assert message in self.delete_passport_message_txt
            self.take_screenshot("PASS")
            self.close_safari()

    def hr_portal_pending_click_shared_review_credentials_request(self):
        """ Click on the Alert for reviewing the Shared Credentials"""
        if self.verify_element_displayed(self.click_shared_review_cred_request_xpath):
            self.click_element_with_wait(self.click_shared_review_cred_request_xpath, "Click")
            self.user_defined_wait(3)

    def hr_portal_pending_click_shared_review_accept_radio_button(self):
        """ Click on the Accept radio button while reviewing Shared Credentials"""
        self.user_defined_wait(2)
        if self.verify_element_displayed(self.click_shared_review_accept_radio_button_xpath):
            self.click_element_with_wait(self.click_shared_review_accept_radio_button_xpath, "Click")
            self.user_defined_wait(2)

    def hr_portal_pending_click_shared_provide_credentials_confirm_continue(self):
        """ Click on Continue button w.r.t shared credentials review request"""
        if self.verify_element_displayed(self.click_shared_review_accept_continue_button_xpath):
            self.click_element_with_wait(self.click_shared_review_accept_continue_button_xpath, "Click")
            self.user_defined_wait(3)

    def hr_portal_pending_click_shared_provide_credentials_confirm_yes(self):
        """ Click on Yes radio button w.r.t to provide shared credential request"""
        self.user_defined_wait(2)
        if self.verify_element_displayed(self.click_shared_review_accept_yes_confirm_radio_button_xpath):
            self.click_element_with_wait(self.click_shared_review_accept_yes_confirm_radio_button_xpath, "Click")

    def hr_portal_pending_provide_shared_credentials_reviewed_success(self):
        """ Shared credentials request reviewed successfully and message is displayed """
        if self.verify_element_displayed(self.click_shared_review_accept_success_header_xpath):
            message = self.read_value_from_element(self.click_shared_review_accept_success_header_xpath)
            assert self.click_shared_review_accept_success_header_txt in message
            self.take_screenshot("PASS")
            self.complete_close_browser()

    def hr_portal_click_pending_view_credential(self):
        """Click on the View Credential button"""
        self.click_element_with_wait(
            self.pending_credentials_view_credentials_link_xpath,
            "pending credentials view credentials link",
        )

    def hr_portal_click_pending_view_credential_button(self):
        """Click on the View Credential button"""
        self.click_element_with_wait(
            self.dbs_supporting_information_credentials_expand_button,
            "dbs supporting information expand button",
        )

    def hr_portal_pending_back_link_displayed(self):
        """ Validate the back link displayed on the page"""
        return self.verify_element_displayed(self.hr_portal_pending_staff_passport_back_link, "back link ")

    def hr_portal_pending_remind_username_review_credential_link(self):
        """ verify the remind username link"""
        return self.verify_element_displayed(self.remind_user_to_review_link, "remind username link")

    def hr_portal_read_the_supplied_attribute(self, attribute):
        """ Read the supplied attribute from the page"""
        attribute_xpath = getattr(self, attribute)
        return self.read_value_from_element(attribute_xpath, attribute)

    def hr_portal_click_pending_view_credential_button_identity(self):
        """Click on the View Credential button"""
        self.click_element_with_wait(
            self.identity_credentials_expand_button,
            "dbs supporting information expand button",
        )

    def hr_portal_click_pending_view_credential_button_right_to_work(self):
        """ Click on the View Credential button"""
        self.click_element_with_wait(self.rtw_credentials_expand_button, "dbs supporting information expand button")

    def hr_portal_pending_withdraw_link_dbs_credentials(self):
        """ Click on the withdraw link for DBS credentials"""
        return self.verify_element_displayed(self.dbs_withdraw_link, "dbs withdraw link")

    def hr_portal_pending_withdraw_link_identity_credentials(self):
        """ Click on the withdraw link for Identity credentials"""
        return self.verify_element_displayed(self.id_withdraw_link, "identity withdraw link")

    def hr_portal_pending_withdraw_link_right_to_work_credentials(self):
        """ Click on the withdraw link for Right to work credentials"""
        return self.verify_element_displayed(self.rtw_withdraw_link, "right to work withdraw link")
