"""this class contains methods for the page actions of HR portal Reviewed Staff Passport page"""
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities import custom_logger
logger = custom_logger.get_logger()


class HRReviewedStaffPassportPage(BasePage):
    """ Elements for the HR Portal-Reviewed staff passport to provide credentials"""
    menu_toggle_xpath = AppiumBy.XPATH, "//XCUIElementTypeButton[@name=\"Open menu\"]"
    reviewed_staff_passport_tab_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"Reviewed staff passports\"]"

    reviewed_search_input_xpath = AppiumBy.CLASS_NAME, "XCUIElementTypeSearchField"
    reviewed_search_submit_xpath = AppiumBy.XPATH, "//XCUIElementTypeButton[@name=\"Search\"]"
    create_passport_result_xpath = AppiumBy.XPATH, "//tbody/tr[1]/td[7]/span[2]/span[1]"
    reviewed_passport_status_xpath = AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"Active\"]"
    reviewed_passport_status_txt = "Active"
    reviewed_search_result_xpath = AppiumBy.XPATH, ("(//XCUIElementTypeStaticText[@name=\"Full name\"])["
                                                   "2]/parent::XCUIElementTypeOther/XCUIElementTypeLink")


    def hr_portal_reviewed_staff_passport_tab(self):
        """ Click on the Reviewed Staff Passport Tab within HR Portal"""
        if self.verify_element_displayed(self.menu_toggle_xpath):
            self.click_element(self.menu_toggle_xpath, "Click")
        if self.verify_element_displayed(self.reviewed_staff_passport_tab_xpath):
            self.click_element(self.reviewed_staff_passport_tab_xpath, "Click")
            self.user_defined_wait(5)

    def hr_portal_reviewed_search_username(self, value):
        """ Enter the DSP user details in the search box """
        self.user_defined_wait(2)
        if self.verify_element_displayed(self.reviewed_search_input_xpath):
            self.type_element(self.reviewed_search_input_xpath, value)
            self.user_defined_wait(3)

    def hr_portal_reviewed_search_submit_click(self):
        """ Click on the search button """
        if self.verify_element_displayed(self.reviewed_search_submit_xpath):
            self.click_element(self.reviewed_search_submit_xpath, "Click")
            self.user_defined_wait(3)

    def hr_portal_reviewed_validate_search_result(self):
        """ Result should be displayed and user validate the status of the passport"""
        self.user_defined_wait(2)
        if self.verify_element_displayed(self.reviewed_passport_status_xpath):
            message = self.read_value_from_element(self.reviewed_passport_status_xpath)
            assert message in self.reviewed_passport_status_txt
            self.take_screenshot("PASS")

    def hr_portal_reviewed_click_search_result(self):
        """ Result should be displayed and user click on the result"""
        if self.verify_element_displayed(self.reviewed_search_result_xpath):
            self.click_element(self.reviewed_search_result_xpath, "click")
            self.user_defined_wait(2)