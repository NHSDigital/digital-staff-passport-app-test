"""this class contains methods for the page actions
of HR portal temporary placement credential creation page"""
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from utilities import custom_logger
logger = custom_logger.get_logger()


class HRTemporaryPlacementCredentialPage(BasePage):
    """Elements for the HR Portal-temporary placement credential creation"""

    Create_temporary_placement_cred_link_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeStaticText[@name="Create temporary placement credential"]'
    )
    When_should_you_issue_temp_cred_heading_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeStaticText[@name="When should '
        'you issue a temporary placement credential?"]'
    )
    Continue_button_1st_page_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Continue"]',
    )
    Position_title_field_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeTextField[@name="Position title"]',
    )
    Position_number_field_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeTextField[@name="Position number"]',
    )
    Brief_description_textbox_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeTextView[@name="Brief description of work pattern"]'
    )
    Start_day_xpath = AppiumBy.XPATH, '(//XCUIElementTypeTextField[@name="Day"])[1]'
    start_month_xpath = AppiumBy.XPATH, '(//XCUIElementTypeTextField[@name="Month"])[1]'
    start_Year_xpath = AppiumBy.XPATH, '(//XCUIElementTypeTextField[@name="Year"])[1]'
    end_day_xpath = AppiumBy.XPATH, '(//XCUIElementTypeTextField[@name="Day"])[2]'
    end_month_xpath = AppiumBy.XPATH, '(//XCUIElementTypeTextField[@name="Month"])[2]'
    end_year_xpath = AppiumBy.XPATH, '(//XCUIElementTypeTextField[@name="Year"])[2]'
    Continue_button_2nd_page = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="Continue"]',
    )
    permanent_employer_dropdown_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeOther[@name="Permanent Employer"]',
    )
    coventry_option_select_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeButton[@name="University Hospitals Coventry and '
        'Warwickshire NHS Trust"]'
    )
    Enter_your_employer_in_text_box_xpath = AppiumBy.XPATH, ""
    Department_field_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeTextField[@name="Department"]',
    )
    Depart_contact_email_address_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeTextField[@name="Department contact email address"]'
    )
    HR_contact_field_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeTextField[@name="HR contact"]',
    )
    Depart_Contact_name_field_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeTextField[@name="Department Contact name"]',
    )
    Approved_by_field_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeTextField[@name="Approved by"]',
    )
    Licence_to_attend_heading_xpath = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Licence to attend"]',
    )
    Yes_confirm_licence_requirement_radio_btn_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeStaticText[@name="Yes, confirm licence requirement"]'
    )
    No_dont_include_licence_radio_btn_xpath = AppiumBy.XPATH, ""
    Confirm_dtls_provide_credential_heading_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeStaticText[@name="Confirm details and provide credential"]'
    )
    Yes_confirm_and_provide_credential_radio_btn_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeStaticText[@name="Yes, confirm and provide credential"]'
    )
    No_return_to_staff_profile_radio_btn_xpath = AppiumBy.XPATH, ""
    Temporary_placement_cred_provided_heading_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeStaticText[@name="Temporary placement credential provided"]'
    )
    Temporary_placement_cred_provided_heading_txt = (
        "Temporary placement credential provided"
    )
    Temp_placement_back_to_user_passport_link_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeStaticText[@name="Back to ' "AutomationTwo User's passport\"]"
    )
    Temp_placement_Passport_history_link_xpath = AppiumBy.XPATH, (
        '//XCUIElementTypeStaticText[@name="Passport history"]'
    )
    Passport_history_page_heading_temp_creds_xpath = AppiumBy.XPATH, (
        "//XCUIElementTypeOther["
        '@name="main"]/XCUIElementTypeOther['
        "2]/XCUIElementTypeStaticText"
    )
    Passport_history_event_txt_temp_creds_xpath = AppiumBy.XPATH, (
        "//XCUIElementTypeOther["
        '@name="main"]/XCUIElementTypeOther['
        "3]/XCUIElementTypeOther["
        "2]/XCUIElementTypeOther"
        "/XCUIElementTypeStaticText[2]"
    )
    Passport_history_event_temp_creds_txt = "Temporary placement credential"
    I_do_not_know_the_position_number_xpath = AppiumBy.XPATH, ""

    def hr_portal_click_create_temporary_placement_credential_link(self):
        """click on Create temporary placement credential"""
        self.click_element_with_wait(self.Create_temporary_placement_cred_link_xpath, "Click on create temporary placement credential")

    def hr_portal_verify_heading_and_click_continue(self):
        """Verify temporary placement credential & click continue"""
        self.click_element_with_wait(self.Continue_button_1st_page_xpath, "Click continue")

    def hr_portal_add_details_in_position_title_field(self, value):
        """Function to add details in position title field"""
        self.verify_element_displayed(self.Position_title_field_xpath)
        self.type_element(self.Position_title_field_xpath, value)

    def hr_portal_add_details_in_position_number(self, value):
        """function to add details in position number field"""
        self.verify_element_displayed(self.Position_number_field_xpath)
        self.type_element(self.Position_number_field_xpath, value)

    def hr_portal_select_checkbox_i_do_not_know_the_position_number(self):
        """function to select I do not know the position number checkbox"""
        self.click_element_with_wait(self.I_do_not_know_the_position_number_xpath, "click hr checkbox")

    def hr_portal_add_details_in_brief_description_textbox(self, value):
        """Function to add details in Brief description of work pattern field """
        if self.verify_element_displayed(self.Brief_description_textbox_xpath):
            self.type_element(self.Brief_description_textbox_xpath, value)

    def hr_portal_add_temporary_placement_start_day(self, value):
        """Function to add temporary placement start date"""
        self.verify_element_displayed(self.Start_day_xpath)
        self.type_element(self.Start_day_xpath, value)

    def hr_portal_add_temporary_placement_start_month(self, value):
        """Function to add temporary placement start month"""
        self.verify_element_displayed(self.start_month_xpath)
        self.type_element(self.start_month_xpath, value)

    def hr_portal_add_temporary_placement_start_year(self, value):
        """Function to add temporary placement start year"""
        self.verify_element_displayed(self.start_Year_xpath)
        self.type_element(self.start_Year_xpath, value)

    def hr_portal_add_temporary_placement_end_day(self, value):
        """Function to add temporary placement end date"""
        self.verify_element_displayed(self.end_day_xpath)
        self.type_element(self.end_day_xpath, value)

    def hr_portal_add_temporary_placement_end_month(self, value):
        """Function to add temporary placement end month"""
        self.verify_element_displayed(self.end_month_xpath)
        self.type_element(self.end_month_xpath, value)

    def hr_portal_add_temporary_placement_end_year(self, value):
        """Function to add temporary placement end year"""
        self.verify_element_displayed(self.end_year_xpath)
        self.type_element(self.end_year_xpath, value)

    def hr_portal_click_on_continue_button_on_page(self):
        """Function to click on continue button"""
        self.click_element_with_wait(self.Continue_button_2nd_page, "click continue button")

    def hr_portal_select_permanent_employer_detail_from_dropdown(self):
        """Function to select permanent employment details from dropdown"""
        self.click_element_with_wait(self.permanent_employer_dropdown_xpath)
        self.click_element_with_wait(self.coventry_option_select_xpath)

    def hr_portal_to_enter_employer_details_in_the_text_box(self, value):
        """function to enter your employer in the text box below field"""
        self.verify_element_displayed(self.Enter_your_employer_in_text_box_xpath)
        self.type_element(self.Enter_your_employer_in_text_box_xpath, value)

    def hr_portal_add_details_in_department_field(self, value):
        """Function to add details in department field"""
        self.verify_element_displayed(self.Department_field_xpath)
        self.type_element(self.Department_field_xpath, value)

    def hr_portal_add_details_in_department_contact_name_field(self, value):
        """Function to add details in department field"""
        self.verify_element_displayed(self.Depart_Contact_name_field_xpath)
        self.type_element(self.Depart_Contact_name_field_xpath, value)

    def hr_portal_add_details_in_department_contact_email_address_field(self, value):
        """Function to add details in department field"""
        self.verify_element_displayed(self.Depart_contact_email_address_xpath)
        self.type_element(self.Depart_contact_email_address_xpath, value)

    def hr_portal_add_details_in_hr_contact_field(self, value):
        """Function to add details in HR contact field"""
        self.verify_element_displayed(self.HR_contact_field_xpath)
        self.type_element(self.HR_contact_field_xpath, value)

    def hr_portal_add_details_in_approved_by_field(self, value):
        """Function to add details in Approved by field"""
        self.verify_element_displayed(self.Approved_by_field_xpath)
        self.type_element(self.Approved_by_field_xpath, value)

    def hr_portal_select_licence_to_attend_yes_radio_btn(self):
        """Function to select Yes, confirm licence requirement radio button option"""
        self.click_element_with_wait(
            self.Yes_confirm_licence_requirement_radio_btn_xpath,
            "click on yes radio button",
        )

    def hr_portal_select_licence_to_attend_no_radio_btn(self):
        """Function to select No, don't include licence option"""
        self.click_element_with_wait(self.No_dont_include_licence_radio_btn_xpath, "click on no radio button")

    def hr_portal_confirm_details_page_and_select_yes_radio_button(self):
        """Validates Confirm details and provide credential heading and select yes radio button"""
        self.click_element_with_wait(
            self.Yes_confirm_and_provide_credential_radio_btn_xpath,
            "click on yes radio button",
        )

    def hr_portal_confirm_details_page_and_select_no_radio_button(self):
        """Validates Confirm details and provide credential heading and select No radio button"""
        self.click_element_with_wait(self.No_return_to_staff_profile_radio_btn_xpath, "click on no radio button")

    def hr_portal_temp_placement_provided_success_message(self):
        """Validate Temporary placement credential provided success message"""
        self.verify_element_displayed(self.Temporary_placement_cred_provided_heading_xpath)
        message = self.read_value_from_element(self.Temporary_placement_cred_provided_heading_xpath)
        assert message in self.Temporary_placement_cred_provided_heading_txt
        self.take_screenshot("PASS")

    def hr_portal_temp_placement_passport_history_event_details(self):
        """Function verifies passport history heading and event"""
        self.click_element_with_wait(
            self.Temp_placement_back_to_user_passport_link_xpath,
            "click on back to user passport",
        )
        self.click_element_with_wait(
            self.Temp_placement_Passport_history_link_xpath, "click on passport history"
        )
        self.verify_element_displayed(self.Passport_history_page_heading_temp_creds_xpath)
        message = self.read_value_from_element(
            self.Passport_history_event_txt_temp_creds_xpath
        )
        assert self.Passport_history_event_temp_creds_txt in message
        self.take_screenshot("PASS")
        self.close_safari()

