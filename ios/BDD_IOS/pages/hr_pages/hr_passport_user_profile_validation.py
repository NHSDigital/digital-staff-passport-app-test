"""this class contains methods for the page actions
of HR portal - USer Management page"""
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from utilities import custom_logger

logger = custom_logger.get_logger()


class HrPortalPassportUserProfileValidation(BasePage):
    """ Elements of the User Management tab within HR Portal: Validating user data"""

    passport_status_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"Passport status:\"]"
    passport_status_initial_value_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"Credentials Pending\"]"
    passport_status_initial_value_txt = "Credentials Pending"
    passport_show_all_details_xpath = AppiumBy.XPATH, "//XCUIElementTypeButton[@value=\"Show all details\"]"
    passport_first_name_value_xpath = AppiumBy.XPATH, ("//XCUIElementTypeOther[@name=\"main\"]/XCUIElementTypeOther"
                                                       "/XCUIElementTypeOther[2]/XCUIElementTypeStaticText")
    passport_last_name_value_xpath = AppiumBy.XPATH, ("//XCUIElementTypeOther[@name=\"main\"]/XCUIElementTypeOther"
                                                       "/XCUIElementTypeOther[4]/XCUIElementTypeStaticText")
    passport_dob_xpath = AppiumBy.XPATH, ("//XCUIElementTypeOther[@name=\"main\"]/XCUIElementTypeOther"
                                                       "/XCUIElementTypeOther[8]/XCUIElementTypeStaticText")
    passport_telephone_value_xpath = AppiumBy.XPATH, ("//XCUIElementTypeOther[@name=\"main\"]/XCUIElementTypeOther"
                                                       "/XCUIElementTypeOther[1]/XCUIElementTypeOther["
                                                      "2]/XCUIElementTypeLink")
    passport_email_id_value_xpath = AppiumBy.XPATH, ("//XCUIElementTypeOther[@name=\"main\"]/XCUIElementTypeOther"
                                                       "/XCUIElementTypeOther[1]/XCUIElementTypeOther["
                                                     "4]/XCUIElementTypeStaticText")
    passport_staff_group_value_xpath = AppiumBy.XPATH, ("//XCUIElementTypeOther[@name=\"main\"]/XCUIElementTypeOther"
                                                       "/XCUIElementTypeOther[1]/XCUIElementTypeOther["
                                                        "10]/XCUIElementTypeStaticText")
    passport_employment_type_value_xpath = AppiumBy.XPATH, ("//XCUIElementTypeOther["
                                                            "@name=\"main\"]/XCUIElementTypeOther"
                                                       "/XCUIElementTypeOther[1]/XCUIElementTypeOther["
                                                            "14]/XCUIElementTypeStaticText")
    passport_employment_status_value_xpath = AppiumBy.XPATH, ("//XCUIElementTypeOther["
                                                              "@name=\"main\"]/XCUIElementTypeOther"
                                                       "/XCUIElementTypeOther[1]/XCUIElementTypeOther["
                                                              "16]/XCUIElementTypeStaticText")
    complete_creds_required_xpath = AppiumBy.XPATH, "//XCUIElementTypeButton[@name=\"Complete credentials required\"]"
    complete_creds_confirm_xpath = AppiumBy.XPATH, "//XCUIElementTypeButton[@name=\"Complete credentials required\"]"
    complete_success_message_xpath = AppiumBy.XPATH, ("//XCUIElementTypeStaticText[@name=\"Credentials required "
                                                      "request completed\"]")
    complete_success_message_txt = "Credentials required request completed"
    passport_status_complete_value_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"Active\"]"
    passport_status_complete_value_txt = "Active"

    def hr_portal_passport_page_initial_status_validation(self):
        """ Validate the passport status in the passport profile page"""
        if self.verify_element_displayed(self.passport_status_xpath):
            element = self.read_value_from_element(self.passport_status_initial_value_xpath)
            assert element in self.passport_status_initial_value_txt
            self.take_screenshot("PASS")

    def hr_portal_passport_page_click_on_show_details(self):
        """Function to click on show details link"""
        if self.verify_element_displayed(self.passport_show_all_details_xpath):
            self.click_element(self.passport_show_all_details_xpath, "Click")
            self.user_defined_wait(2)

    def hr_portal_passport_page_firstname(self, value):
        """Function to verify the user first name"""
        if self.verify_element_displayed(self.passport_first_name_value_xpath):
            element = self.read_value_from_element(self.passport_first_name_value_xpath)
            assert element in value
            self.take_screenshot("PASS")

    def hr_portal_passport_page_lastname(self, value):
        """Function to verify the user last name"""
        if self.verify_element_displayed(self.passport_last_name_value_xpath):
            element = self.read_value_from_element(self.passport_last_name_value_xpath)
            assert element in value


    def hr_portal_passport_page_dob(self, value):
        """Function to verify the user dob"""
        if self.verify_element_displayed(self.passport_dob_xpath):
            element = self.read_value_from_element(self.passport_dob_xpath)
            assert element in value


    def hr_portal_passport_page_telephone(self, value):
        """Function to verify the user telephone number"""
        if self.verify_element_displayed(self.passport_telephone_value_xpath):
            element = self.read_value_from_element(self.passport_telephone_value_xpath)
            assert element in value

    def hr_portal_passport_page_email_address(self, value):
        """Function to verify the user email address"""
        if self.verify_element_displayed(self.passport_email_id_value_xpath):
            element = self.read_value_from_element(self.passport_email_id_value_xpath)
            assert element in value

    def hr_portal_passport_page_staff_group(self, value):
        """Function to verify the staff group validation"""
        if self.verify_element_displayed(self.passport_staff_group_value_xpath):
            element = self.read_value_from_element(self.passport_staff_group_value_xpath)
            assert element in value


    def hr_portal_passport_page_emp_type(self, value):
        """Function to verify the user employment type"""
        if self.verify_element_displayed(self.passport_employment_type_value_xpath):
            element = self.read_value_from_element(self.passport_employment_type_value_xpath)
            assert element in value

    def hr_portal_passport_page_emp_stat(self, value):
        """Function to verify the user employment stat"""
        if self.verify_element_displayed(self.passport_employment_status_value_xpath):
            element = self.read_value_from_element(self.passport_employment_status_value_xpath)
            assert element in value
            self.close_safari()

    def hr_portal_passport_page_complete_creds_required(self):
        """ Click on complete credentials required in the passport profile page"""
        if self.verify_element_displayed(self.complete_creds_required_xpath):
            self.click_element(self.complete_creds_required_xpath, "click")
            self.click_element(self.complete_creds_confirm_xpath, "click")
        if self.verify_element_displayed(self.complete_success_message_xpath):
            element = self.read_value_from_element(self.complete_success_message_xpath)
            assert element in self.complete_success_message_txt
            self.take_screenshot("PASS")

    def hr_portal_passport_page_complete_status_validation(self):
        """ Validate the passport status in the passport profile page"""
        if self.verify_element_displayed(self.passport_status_xpath):
            element = self.read_value_from_element(self.passport_status_complete_value_xpath)
            assert element in self.passport_status_complete_value_txt
            self.take_screenshot("PASS")
            self.close_safari()
