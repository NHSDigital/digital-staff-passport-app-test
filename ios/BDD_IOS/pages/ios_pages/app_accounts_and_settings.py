"""this class contains methods for the page actions of dsp app accounts and settings page"""
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class AppAccountsandSettings(BasePage):
    """ Methods for the DSP APP account and settings page """

    Accounts_and_settings_tab_xpath = AppiumBy.XPATH, ''
    Accounts_and_settings_heading_xpath = AppiumBy.XPATH, ''
    delete_your_nhs_digital_staff_passport_xpath = AppiumBy.XPATH, ''
    back_link_xpath = AppiumBy.XPATH, ''
    question_mark_xpath = AppiumBy.XPATH, ''
    terms_of_use_and_other_policies_link_xpath = AppiumBy.XPATH, ''
    to_delete_your_information_xpath = AppiumBy.XPATH, ''
    to_delete_your_information_text = "To delete your information held by an organisation."


    def click_account_and_settings_tab(self):
        """Function to click on account and settings tab"""
        if self.verify_element_displayed(self.Accounts_and_settings_tab_xpath):
            self.click_element(self.Accounts_and_settings_tab_xpath, "Click")


    def verify_account_and_settings_heading(self):
        """Function to verify account and settings heading"""
        self.verify_element_displayed(self.Accounts_and_settings_heading_xpath)


    def verify_and_click_question_mark_icon(self):
        """Function to validate the welcome message on home page"""
        if self.verify_element_displayed(self.question_mark_xpath):
            self.click_element(self.question_mark_xpath, "click")


    def click_on_back_link(self):
        """Function click on back link and then again on account and settings tab"""
        if self.verify_element_displayed(self.back_link_xpath):
            self.click_element(self.back_link_xpath, "click")
            self.click_element(self.Accounts_and_settings_tab_xpath, "click")


    def verify_delete_your_staff_passport_page(self):
        """Function to validate delete your staff passport page"""
        self.verify_element_displayed(self.delete_your_nhs_digital_staff_passport_xpath)


    def click_on_terms_of_use_and_other_policies(self):
        """Function to validate the action on home page"""
        if self.verify_element_displayed(self.terms_of_use_and_other_policies_link_xpath):
            self.click_element(self.terms_of_use_and_other_policies_link_xpath, "click")

