"""this class contains methods for the page actions
of HR portal Pending Staff Passport page"""
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from ios.BDD_IOS.pages.base_page import BasePage
from ios.BDD_IOS.pages.hr_identity_and_access import HRIdentityAndAccessPage
from ios.BDD_IOS.utilities import custom_logger

logger = custom_logger.get_logger()


class HRPendingStaffPassportPage(BasePage):
    """ Elements for the HR Portal-Pending staff passport to provide credentials"""
    menu_toggle_xpath = HRIdentityAndAccessPage.menu_toggle_xpath
    pending_staff_passport_page_link_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"Pending staff passports\"]"
    click_review_cred_request_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"Review credential requests\"]"
    provide_credentials_button_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"Provide Credentials\"]"
    radio_button_elements = "(//XCUIElementTypeOther[@value=\"0\"])"
    pending_search_input_xpath = AppiumBy.CLASS_NAME, "XCUIElementTypeSearchField"
    pending_search_submit_xpath = AppiumBy.ACCESSIBILITY_ID, "Search"
    pending_search_result_xpath = AppiumBy.XPATH, ("(//XCUIElementTypeStaticText[@name=\"Full name\"])["
                                                   "2]/parent::XCUIElementTypeOther/XCUIElementTypeLink")
    connect_to_esr_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"Connect to ESR\"]"
    enter_esr_number_xpath = AppiumBy.XPATH, "//XCUIElementTypeTextField[@name=\"ESR assignment number\"]"
    confirm_esr_number_xpath = AppiumBy.XPATH, "//XCUIElementTypeButton[@name=\"Confirm\"]"
    connect_passport_to_esr_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"Connect passport to ESR\"]"
    connect_button_xpath = AppiumBy.XPATH, "//XCUIElementTypeButton[@name=\"Connect\"]"
    yes_radio_btn_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"Yes, this is the correct staff member\"]"
    no_radio_btn_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"No, edit the ESR assignment number\"]"
    continue_btn_xpath = AppiumBy.XPATH, "//XCUIElementTypeButton[@name=\"Continue\"]"
    provide_credentials_link_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"Provide Credentials\"]"
    back_link_pending_staff_xpath = AppiumBy.XPATH, ("//XCUIElementTypeStaticText[@name=\"Not now - go back to "
                                                     "AutomationTwo User's passport\"]")
    provide_creds_count = "(//XCUIElementTypeOther[@value=\"0\"])[{position_number}]"
    review_credentials_confirm_yes_xpath = AppiumBy.XPATH, ("//XCUIElementTypeStaticText[@name=\"Yes, continue with "
                                                            "this selection\"]")
    review_credentials_success_xpath = AppiumBy.XPATH, ("//XCUIElementTypeStaticText[@name=\"Credential requests "
                                                        "reviewed\"]")
    review_credentials_success_txt = "Credential requests reviewed"
    manage_passport_link_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"Manage passport\"]"
    delete_passport_link_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"Delete passport\"]"
    delete_passport_continue_btn_xpath = AppiumBy.XPATH, "//XCUIElementTypeButton[@name=\"Continue\"]"
    delete_passport_data_xpath = AppiumBy.XPATH, "//XCUIElementTypeButton[@name=\"Delete passport and its data\"]"
    delete_passport_message_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"Passport deleted.\"]"
    delete_passport_message_txt = "Passport deleted."


    def hr_portal_pending_staff_passport_tab(self):
        """ Click on the Pending Staff Passport Tab within HR Portal"""
        if self.verify_element_displayed(self.menu_toggle_xpath):
            self.click_element(self.menu_toggle_xpath, "Click")
        if self.verify_element_displayed(self.pending_staff_passport_page_link_xpath):
            self.click_element(self.pending_staff_passport_page_link_xpath, "Click")

    def hr_portal_pending_search_username(self, value):
        """ Enter the DSP user details in the search box """
        if self.verify_element_displayed(self.pending_search_input_xpath):
            self.type_element(self.pending_search_input_xpath, value)

    def hr_portal_pending_search_submit_click(self):
        """ Click on the search button """
        if self.verify_element_displayed(self.pending_search_submit_xpath):
            self.click_element(self.pending_search_submit_xpath, "Click")

    def hr_portal_pending_search_result(self):
        """ Result should be displayed and user should click on the same"""
        if self.verify_element_displayed(self.pending_search_result_xpath):
            self.click_element(self.pending_search_result_xpath, "Click")
            self.user_defined_wait(3)
            # self.close_safari()

    def hr_portal_passport_page_initial_status_validation(self):
        """ Validate the passport status in the passport profile page"""
        if self.verify_element_displayed(self.passport_status_xpath):
            element = self.read_value_from_element(self.passport_status_initial_value_xpath)
            assert element in self.passport_status_initial_value_txt
            self.take_screenshot("PASS")

    def hr_portal_passport_page_click_on_show_details(self):
        """Function to click on show details link"""
        self.scroll_page_to_middle()
        self.user_defined_wait(2)
        if self.verify_element_displayed(self.passport_show_all_details_xpath):
            self.click_element(self.passport_show_all_details_xpath, "Click")
            self.user_defined_wait(2)


    def hr_portal_pending_click_review_credentials_request(self):
        """ Click on the Alert for reviewing the Credentials Requests"""
        if self.verify_element_displayed(self.click_review_cred_request_xpath):
            self.click_element(self.click_review_cred_request_xpath, "Click")
            self.user_defined_wait(3)


    def hr_portal_pending_provide_credentials(self):
        """ Review the credentials request & select the provide radio button for the same"""
        # add scroll
        count = self.get_element_count("xpath", self.radio_button_elements)
        element_list = count // 2 # This will give you an integer result
        for i in range(1, element_list + 1, 1):
            print(i)
            provide_path = By.XPATH, self.provide_creds_count.format(position_number=i)
            cred_to_provide = self.verify_element_displayed(provide_path)
            cred_to_provide.click()


    def hr_portal_pending_provide_credentials_button(self):
        """ Click on the Provide Credential button"""
        if self.verify_element_displayed(self.provide_credentials_button_xpath):
            self.click_element(self.provide_credentials_button_xpath, "Click")
            self.user_defined_wait(3)


    def hr_portal_pending_provide_credentials_continue(self):
        """ Click on Continue button , post selection of the request"""
        if self.verify_element_displayed(self.continue_btn_xpath):
            self.click_element(self.continue_btn_xpath, "Click")
            self.user_defined_wait(3)


    def hr_portal_pending_provide_credentials_confirm_yes(self):
        """ Click on Yes radio button w.r.t credential request"""
        if self.verify_element_displayed(self.review_credentials_confirm_yes_xpath):
            self.click_element(self.review_credentials_confirm_yes_xpath, "Click")
            self.user_defined_wait(3)


    def hr_portal_pending_provide_credentials_confirm_continue(self):
        """ Click on Continue button w.r.t credential request"""
        if self.verify_element_displayed(self.continue_btn_xpath):
            self.click_element(self.continue_btn_xpath, "Click")
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
            self.click_element(self.connect_to_esr_xpath, "Click")
            self.user_defined_wait(3)

    def hr_portal_pending_enter_esr_number(self, value):
        """ Enter valid ESR Number """
        if self.verify_element_displayed(self.enter_esr_number_xpath):
            self.type_element(self.enter_esr_number_xpath, value)
            self.user_defined_wait(3)

    def hr_portal_pending_confirm_esr_number(self):
        """ Click on the confirm button w.r.t ESR """
        if self.verify_element_displayed(self.confirm_esr_number_xpath):
            self.click_element(self.confirm_esr_number_xpath, "Click")
            self.user_defined_wait(3)

    def hr_portal_pending_connect_to_passport(self):
        """ Click on the Connect to Passport Link"""
        if self.verify_element_displayed(self.connect_passport_to_esr_xpath):
            self.click_element(self.connect_passport_to_esr_xpath, "Click")
            self.user_defined_wait(3)

    def hr_portal_pending_passport_connect_proceed(self):
        """ Click on Connect button"""
        if self.verify_element_displayed(self.connect_button_xpath):
            self.click_element(self.connect_button_xpath, "Click")
            self.user_defined_wait(10)

    def hr_portal_pending_connect_to_passport_confirm_yes(self):
        """ Select the Yes radio button"""
        if self.verify_element_displayed(self.yes_radio_btn_xpath):
            self.click_element(self.yes_radio_btn_xpath, "Click")
            self.user_defined_wait(3)

    def hr_portal_pending_connect_to_passport_confirm_no(self):
        """ Select the No radio button"""
        if self.verify_element_displayed(self.no_radio_btn_xpath):
            self.click_element(self.no_radio_btn_xpath, "Click")
            self.user_defined_wait(3)

    def hr_portal_pending_connect_to_passport_confirm_continue(self):
        """ Click on the confirm button w.r.t Connect to Passport """
        if self.verify_element_displayed(self.continue_btn_xpath):
            self.click_element(self.continue_btn_xpath, "Click")
            self.user_defined_wait(3)

    def hr_portal_pending_provide_credentials_link(self):
        """ Click on Provide Credentials Link"""
        if self.verify_element_displayed(self.provide_credentials_link_xpath):
            self.click_element(self.provide_credentials_link_xpath, "Click")
            self.user_defined_wait(5)

    def hr_portal_pending_back_link_passport_page(self):
        """ Click on the back link to navigate back to passport page """
        if self.verify_element_displayed(self.back_link_pending_staff_xpath):
            self.click_element(self.back_link_pending_staff_xpath, "Click")
            self.user_defined_wait(2)

    def hr_portal_pending_manage_passport_link(self):
        """ Click on Manage Passport Link"""
        if self.verify_element_displayed(self.manage_passport_link_xpath):
            self.click_element(self.manage_passport_link_xpath, "Click")

    def hr_portal_pending_delete_passport_link(self):
        """ Click on Delete Passport Link"""
        if self.verify_element_displayed(self.delete_passport_link_xpath):
            self.click_element(self.delete_passport_link_xpath, "Click")


    def hr_portal_pending_delete_passport_continue(self):
        """ Click on Continue button w.r.t delete passport"""
        if self.verify_element_displayed(self.delete_passport_continue_btn_xpath):
            self.click_element(self.delete_passport_continue_btn_xpath, "Click")

    def hr_portal_pending_delete_passport_data(self):
        """ Click on delete passport data"""
        if self.verify_element_displayed(self.delete_passport_data_xpath):
            self.click_element(self.delete_passport_data_xpath, "Click")

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
            self.click_element(self.click_shared_review_cred_request_xpath, "Click")
            self.user_defined_wait(3)

    def hr_portal_pending_click_shared_review_accept_radio_button(self):
        """ Click on the Accept radio button while reviewing Shared Credentials"""
        self.scroll_page_to_bottom()
        self.user_defined_wait(2)
        if self.verify_element_displayed(self.click_shared_review_accept_radio_button_xpath):
            self.click_element(self.click_shared_review_accept_radio_button_xpath, "Click")
            self.user_defined_wait(2)

    def hr_portal_pending_click_shared_provide_credentials_confirm_continue(self):
        """ Click on Continue button w.r.t shared credentials review request"""
        if self.verify_element_displayed(self.click_shared_review_accept_continue_button_xpath):
            self.click_element(self.click_shared_review_accept_continue_button_xpath, "Click")
            self.user_defined_wait(3)

    def hr_portal_pending_click_shared_provide_credentials_confirm_yes(self):
        """ Click on Yes radio button w.r.t to provide shared credential request"""
        self.scroll_page_to_bottom()
        self.user_defined_wait(2)
        if self.verify_element_displayed(self.click_shared_review_accept_yes_confirm_radio_button_xpath):
            self.click_element(self.click_shared_review_accept_yes_confirm_radio_button_xpath, "Click")

    def hr_portal_pending_provide_shared_credentials_reviewed_success(self):
        """ Shared credentials request reviewed successfully and message is displayed """
        if self.verify_element_displayed(self.click_shared_review_accept_success_header_xpath):
            message = self.read_value_from_element(self.click_shared_review_accept_success_header_xpath)
            assert self.click_shared_review_accept_success_header_txt in message
            self.take_screenshot("PASS")
            self.complete_close_browser()
