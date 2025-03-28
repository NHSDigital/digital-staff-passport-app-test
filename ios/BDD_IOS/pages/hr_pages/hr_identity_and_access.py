"""this class contains methods for the page actions
of HR portal Identity and Access page"""
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from selenium.webdriver.common.by import By



class HRIdentityAndAccessPage(BasePage):
    """Elements for the HR Portal for review of the request"""

    menu_toggle_id = By.ID, 'toggle-menu'
    identity_and_access_page_link_xpath = By.XPATH, "//*[contains(text(),' Identity and access ')]"

    invite_staff_to_DSP_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeStaticText[@name="Invite staff to Digital Staff Passport"]'
    )
    select_single_passport_radio_btn_id = AppiumBy.XPATH, (
        '//XCUIElementTypeStaticText[@name="A single passport using a form"]'
    )
    select_single_passport_continue_btn_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="Continue"]',
    )
    first_name_xpath = AppiumBy.XPATH, '//XCUIElementTypeTextField[@name="First name"]'
    last_name_xpath = AppiumBy.XPATH, '//XCUIElementTypeTextField[@name="Last name"]'
    date_of_birth_day_xpath = AppiumBy.XPATH, '//XCUIElementTypeTextField[@name="Day"]'
    date_of_birth_month_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeTextField[@name="Month"]',
    )
    date_of_birth_year_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeTextField[@name="Year"]',
    )
    email_address_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeTextField[@name="Email address"]',
    )
    phone_number_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeTextField[@name="Telephone number"]',
    )
    staff_group_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeOther[@value="Select an option"]',
    )
    staff_group_select_xpath_medical_dental = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="Medical and Dental"]',
    )
    employment_type_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeOther[@name="Employment type" and @value="Select an option"]'
    )
    emp_type_select_xpath_permanent_fixed_term = AppiumBy.XPATH, (
        '//XCUIElementTypeButton[@name="Permanent or fixed term"]'
    )
    employment_status_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeOther[@name="Employment status" and @value="Select '
        'an option"]'
    )
    employment_status_xpath_current_employer = AppiumBy.XPATH, (
        '//XCUIElementTypeButton[@name="Current employee or leaver"]'
    )
    personal_details_continue_btn_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="Continue"]',
    )
    create_passport_yes_radio_btn_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeStaticText[@name="Yes, create this passport"]'
    )
    create_passport_continue_btn_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="Continue"]',
    )
    create_passport_result_xpath = (
        AppiumBy.XPATH,
        '(//XCUIElementTypeStaticText[@name="Invitation Sent"])[1]',
    )
    status_invitation_sent_txt = ""
    create_passport_result_txt = "Invitation Sent"
    close_app_xpath = AppiumBy.XPATH, ""
    search_xpath = AppiumBy.CLASS_NAME, "XCUIElementTypeSearchField"

    search_submit_xpath = AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Search"]'
    search_result_xpath = AppiumBy.XPATH, (
        '(//XCUIElementTypeStaticText[@name="Full name"])['
        "2]/parent::XCUIElementTypeOther/XCUIElementTypeLink"
    )
    review_identity_details_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Review identity details"]',
    )
    employment_dropdown_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeOther[@name="Employment type" and @value="Select '
        'an option"]'
    )
    continue_button_xpath = AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Continue"]'
    confirm_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Yes, I want to confirm their identity"]',
    )
    confirm_identity_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Yes, I confirm this identity."]',
    )
    gender_dropdown_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeOther[@value="Select their gender"]',
    )
    gender_select_male_xpath = AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Male"]'
    nationality_dropdown_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeOther[@value="Select their nationality"]',
    )
    nationality_select_english_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="English"]',
    )
    address_1_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeTextField[@name="Address line 1"]',
    )
    address_2_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeTextField[@name="Address line 2 (optional)"]',
    )
    town_xpath = AppiumBy.XPATH, '//XCUIElementTypeTextField[@name="Town or city"]'
    postcode_xpath = AppiumBy.XPATH, '//XCUIElementTypeTextField[@name="Postcode"]'
    country_dropdown_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeOther[@name="Country" and @value="Select their country"]'
    )
    country_select_united_kingdom_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="United Kingdom"]',
    )
    yes_i_confirm_radio_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeStaticText[@name="Yes, I confirm their identity '
        'and I want to provide an NHS identity credential."]'
    )
    success_message_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Success"]',
    )
    success_text = "Success"
    delete_passport_link_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Delete passport from records."]',
    )
    no_delete_passport_radio_btn_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeStaticText[@name="No, go back and keep this record"]'
    )

    yes_delete_passport_radio_btn_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeStaticText[@name="Yes, delete staff '
        'passport from records"]'
    )
    delete_passport_continue_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="Continue"]',
    )
    user_profile_heading_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeOther[@name="Digital Staff Passport | '
        'Profile"]/XCUIElementTypeOther[4]/XCUIElementTypeOther['
        "2]/XCUIElementTypeStaticText"
    )
    identity_and_access_text = "Identity and access"
    Delete_passport_msg_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeStaticText[@name="You will no longer see the '
        'record on the Identity and access table."]'
    )
    Delete_passport_message_txt = (
        "You will no longer see the record on the Identity and access table"
    )

    def hr_portal_menu_click(self):
        """ Click on Identity & Access Tab from the menu """
        self.verify_element_displayed(self.menu_toggle_id, "Menu Toggle")
        self.click_element_with_wait(self.menu_toggle_id, "Menu Toggle")

    def hr_portal_menu_identity_and_access_click(self):
        """ Click on Identity & Access Tab from the menu """
        self.verify_element_displayed(self.identity_and_access_page_link_xpath)
        self.click_element_with_wait(self.identity_and_access_page_link_xpath, "Click")

    def hr_portal_identity_invitation_link(self):
        """ Click on invitation of Single Passport link """
        self.user_defined_wait(3)
        if self.verify_element_displayed(self.invite_staff_to_DSP_xpath):
            self.click_element_with_wait(self.invite_staff_to_DSP_xpath, "Click")

    def hr_portal_identity_single_passport_rdio_btn(self):
        """ Select the single passport form radio button """
        # self.user_defined_wait(2)
        if self.verify_element_displayed(self.select_single_passport_radio_btn_id):
            self.click_element_with_wait(self.select_single_passport_radio_btn_id, "Click")

    def hr_portal_identity_single_passport_continue(self):
        """ click on Continue button w.r.t single passport form"""
        # self.user_defined_wait(2)
        if self.verify_element_displayed(self.select_single_passport_continue_btn_xpath):
            self.click_element_with_wait(self.select_single_passport_continue_btn_xpath, "Click")

    def hr_portal_identity_single_passport_first_name(self, value):
        """ Enter First name w.r.t single passport form"""
        if self.verify_element_displayed(self.first_name_xpath):
            self.type_element(self.first_name_xpath, value)

    def hr_portal_identity_single_passport_last_name(self, value):
        """ Enter Last name w.r.t single passport form"""
        if self.verify_element_displayed(self.last_name_xpath):
            self.type_element(self.last_name_xpath, value)

    def hr_portal_identity_single_passport_dob_day(self, value):
        """ Enter Day - DOB w.r.t single passport form"""
        if self.verify_element_displayed(self.date_of_birth_day_xpath):
            self.type_element(self.date_of_birth_day_xpath, value)

    def hr_portal_identity_single_passport_dob_month(self, value):
        """ Enter Month - DOB w.r.t single passport form"""
        if self.verify_element_displayed(self.date_of_birth_month_xpath):
            self.type_element(self.date_of_birth_month_xpath, value)

    def hr_portal_identity_single_passport_dob_year(self, value):
        """ Enter Year - DOB w.r.t single passport form"""
        if self.verify_element_displayed(self.date_of_birth_year_xpath):
            self.type_element(self.date_of_birth_year_xpath, value)

    def hr_portal_identity_single_passport_email(self, value):
        """ Enter Email address w.r.t single passport form"""
        if self.verify_element_displayed(self.email_address_xpath):
            self.type_element(self.email_address_xpath, value)

    def hr_portal_identity_single_passport_phone(self, value):
        """ Enter Phone number w.r.t single passport form"""
        if self.verify_element_displayed(self.phone_number_xpath):
            self.type_element(self.phone_number_xpath, value)

    def hr_portal_identity_single_passport_staff_group(self):
        """ Select the Staff group dropdown w.r.t single passport form"""
        if self.verify_element_displayed(self.staff_group_xpath):
            self.click_element_with_wait(self.staff_group_xpath, "Click")
            self.user_defined_wait(2)
        if self.verify_element_displayed(self.staff_group_select_xpath_medical_dental):
            self.click_element_with_wait(self.staff_group_select_xpath_medical_dental, "Click")
            self.user_defined_wait(2)

    def hr_portal_identity_single_passport_emp_type(self):
        """ Select the Emp Type dropdown w.r.t single passport form"""
        if self.verify_element_displayed(self.employment_type_xpath):
            self.click_element_with_wait(self.employment_type_xpath, "Click")
            self.user_defined_wait(2)
        if self.verify_element_displayed(self.emp_type_select_xpath_permanent_fixed_term):
            self.click_element_with_wait(self.emp_type_select_xpath_permanent_fixed_term, "Click")
            self.user_defined_wait(2)

    def hr_portal_identity_single_passport_emp_status(self):
        """ Select the Emp Status dropdown w.r.t single passport form"""
        if self.verify_element_displayed(self.employment_status_xpath):
            self.click_element_with_wait(self.employment_status_xpath, "Click")
            self.user_defined_wait(2)
        if self.verify_element_displayed(self.employment_status_xpath_current_employer):
            self.click_element_with_wait(self.employment_status_xpath_current_employer, "Click")
            self.user_defined_wait(2)

    def hr_portal_identity_single_passport_details_continue_btn(self):
        """ Click on continue button w.r.t single passport form"""
        if self.verify_element_displayed(self.personal_details_continue_btn_xpath):
            self.click_element_with_wait(self.personal_details_continue_btn_xpath, "Click")

    def hr_portal_identity_single_passport_create_passport_radio_btn(self):
        """ Select create passport radio button w.r.t single passport form"""
        self.user_defined_wait(2)
        if self.verify_element_displayed(self.create_passport_yes_radio_btn_xpath):
            self.click_element_with_wait(self.create_passport_yes_radio_btn_xpath, "Click")

    def hr_portal_identity_single_passport_create_passport_continue_btn(self):
        """ Click continue button w.r.t create passport"""
        self.user_defined_wait(2)
        if self.verify_element_displayed(self.create_passport_continue_btn_xpath):
            self.click_element_with_wait(self.create_passport_continue_btn_xpath, "Click")
            self.user_defined_wait(2)

    def hr_portal_identity_single_passport_create_passport_message(self):
        """ Validate the status of the request under Identity & access search form"""
        self.user_defined_wait(2)
        if self.verify_element_displayed(self.create_passport_result_xpath):
            message = self.read_value_from_element(self.create_passport_result_xpath)
            assert self.create_passport_result_txt in message
            self.user_defined_wait(2)
            self.take_screenshot("PASS")
            self.close_safari()

    def hr_portal_identity_search_username(self, value):
        """ Enter the DSP user details in the search box """
        if self.verify_element_displayed(self.search_xpath):
            self.type_element(self.search_xpath, value)
            self.user_defined_wait(2)

    def hr_portal_identity_search_submit_click(self):
        """ Click on the search button """
        if self.verify_element_displayed(self.search_submit_xpath):
            self.click_element_with_wait(self.search_submit_xpath, "Click")
            self.user_defined_wait(2)

    def hr_portal_identity_search_result(self):
        """ Result should be displayed and user should click on the same"""
        if self.verify_element_displayed(self.search_result_xpath):
            self.click_element_with_wait(self.search_result_xpath, "Click")
            self.user_defined_wait(2)

    def hr_portal_identity_review_details(self):
        """ Click on the review Identity Details link to review the request """
        if self.verify_element_displayed(self.review_identity_details_xpath):
            self.click_element_with_wait(self.review_identity_details_xpath, "Click")
            self.user_defined_wait(2)

    def hr_portal_identity_select_employment_type_permanent(self):
        """ Select the Employment type details from the dropdown """
        if self.verify_element_displayed(self.employment_dropdown_xpath):
            self.click_element_with_wait(self.employment_dropdown_xpath, "Click")
            self.user_defined_wait(2)
        if self.verify_element_displayed(self.emp_type_select_xpath_permanent_fixed_term):
            self.click_element_with_wait(self.emp_type_select_xpath_permanent_fixed_term, "Click")
            self.user_defined_wait(2)

    def hr_portal_identity_continue_button(self):
        """ Click on the continue button"""
        self.user_defined_wait(2)
        if self.verify_element_displayed(self.continue_button_xpath):
            self.click_element_with_wait(self.continue_button_xpath, "Click")

    def hr_portal_identity_confirm_user_radiobutton(self):
        """ Click on the confirm Identity Button """
        # Add scroll as per the need
        if self.verify_element_displayed(self.confirm_identity_xpath):
            self.click_element_with_wait(self.confirm_identity_xpath, "Click")
            self.user_defined_wait(2)

    def hr_portal_identity_select_gender_dropdown_male(self):
        """ Select the gender details from the dropdown """
        # Add down scroll as per the need
        if self.verify_element_displayed(self.gender_dropdown_xpath):
            self.click_element_with_wait(self.gender_dropdown_xpath, "Click")
            self.user_defined_wait(2)
        if self.verify_element_displayed(self.gender_select_male_xpath):
            self.click_element_with_wait(self.gender_select_male_xpath, "Click")

    def hr_portal_identity_select_nationality_dropdown(self):
        """ Select the nationality details from the dropdown """
        if self.verify_element_displayed(self.nationality_dropdown_xpath):
            self.click_element_with_wait(self.nationality_dropdown_xpath, "Click")
            self.user_defined_wait(2)
        if self.verify_element_displayed(self.nationality_select_english_xpath):
            self.click_element_with_wait(self.nationality_select_english_xpath, "Click")

    def hr_portal_identity_enter_address_line_1_details(self, value):
        """ Enter the address details in Line 1 """
        # self.user_defined_wait(2)
        if self.verify_element_displayed(self.address_1_xpath):
            self.type_element(self.address_1_xpath, value)

    def hr_portal_identity_enter_address_line_2_details(self, value):
        """ Enter the address details in Line 2 """
        # self.user_defined_wait(2)
        if self.verify_element_displayed(self.address_2_xpath):
            self.type_element(self.address_2_xpath, value)

    def hr_portal_identity_enter_town_details(self, value):
        """ Enter the town details """
        # self.user_defined_wait(2)
        if self.verify_element_displayed(self.town_xpath):
            self.type_element(self.town_xpath, value)

    def hr_portal_identity_enter_postcode_details(self, value):
        """ Enter the postcode details """
        # self.user_defined_wait(2)
        if self.verify_element_displayed(self.postcode_xpath):
            self.type_element(self.postcode_xpath, value)

    def hr_portal_identity_country_dropdown(self):
        """ Enter the country details """
        # self.user_defined_wait(2)
        if self.verify_element_displayed(self.country_dropdown_xpath):
            self.click_element_with_wait(self.country_dropdown_xpath, "Click")
        if self.verify_element_displayed(self.country_select_united_kingdom_xpath):
            self.click_element_with_wait(self.country_select_united_kingdom_xpath, "Click")

    def hr_portal_identity_confirm_review_button(self):
        """ Click on the continue button"""
        # Add scroll to down as per requirement
        if self.verify_element_displayed(self.confirm_xpath):
            self.click_element_with_wait(self.confirm_xpath, "Click")
            self.user_defined_wait(5)

    def hr_portal_identity_yes_confirm_radio_xpath(self):
        """Click on the yes I confirm and provide identity"""
        if self.verify_element_displayed(self.confirm_identity_xpath):
            self.click_element_with_wait(self.confirm_identity_xpath, "Click")

    def hr_portal_identity_review_request_success_message(self):
        """ Once submitted, success message should be displayed """
        if self.verify_element_displayed(self.success_message_xpath):
            message = self.read_value_from_element(self.success_message_xpath)
            assert message in self.success_text
            self.take_screenshot("PASS")
            self.close_safari()

    def hr_portal_delete_passport_link(self):
        """User selects the option to delete staff passport"""
        self.user_defined_wait(2)
        if self.verify_element_displayed(self.delete_passport_link_xpath):
            self.click_element_with_wait(self.delete_passport_link_xpath, "Click")
            # self.user_defined_wait(3)

    def hr_portal_no_delete_passport_radio_btn(self):
        """User not delete staff passport from records"""
        if self.verify_element_displayed(self.no_delete_passport_radio_btn_xpath):
            self.click_element_with_wait(self.no_delete_passport_radio_btn_xpath, "Click")

    def hr_portal_yes_delete_passport_radio_btn(self):
        """User confirms to delete the staff passport"""
        if self.verify_element_displayed(self.yes_delete_passport_radio_btn_xpath):
            self.click_element_with_wait(self.yes_delete_passport_radio_btn_xpath, "Click")

    def hr_portal_continue_btn_delete_passport(self):
        """User clicks on continue button w.r.t delete the staff passport"""
        if self.verify_element_displayed(self.delete_passport_continue_xpath):
            self.click_element_with_wait(self.delete_passport_continue_xpath, "Click")

    def hr_portal_user_profile_validation(self):
        """Validate the user profile is visible"""
        self.user_defined_wait(2)
        if self.verify_element_displayed(self.user_profile_heading_xpath):
            message = self.read_value_from_element(self.user_profile_heading_xpath)
            assert self.identity_and_access_text in message
            self.take_screenshot("PASS")
            self.complete_close_browser()

    def hr_portal_delete_passport_message(self):
        """validating the message displayed post deleting staff passport"""
        if self.verify_element_displayed(self.Delete_passport_msg_xpath):
            message = self.read_value_from_element(self.Delete_passport_msg_xpath)
            assert message in self.Delete_passport_message_txt
            self.take_screenshot("PASS")
