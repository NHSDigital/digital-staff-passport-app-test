"""this module to be used to call in the steps
    definition for the review initial 3 creds page
"""
from pages.base_page import BasePage


class ReviewAndConfirmInitialCredentialsPage(BasePage):
    """credentials page with dates locators"""
    credentials_page_heading = ""
    credentials_to_confirm = ""
    identity_credentials = ""
    right_to_work_credentials = ""
    dbs_supporting_information = ""
    action_required = ""
    confirmed_credentials = ""
    no_credentials_yet = ""
    home_icon = ""
    credentials_icon = ""
    question_icon = ''
    account_icon = ''
    """identity credentials page locators"""
    identity_page_heading = ""
    provided_by_trust = ""
    photo_of_your_face = ''
    name_title = ''
    name_value = ''
    dob_title = ''
    dob_value = ''
    legal_gender_title = ''
    legal_gender_value = ''
    nationality_title = ''
    nationality_value = ''
    origin_title = ''
    origin_value = ''
    issued_on_title = ''
    issued_on_value = ''
    something_is_not_right_link = ''
    confirm_credential_button = ''
    """confirming credential1 page locators"""
    confirming_credentials_spinner = ''
    """credentials confirmed page locators"""
    credential_confirmed_title = ''
    credentials_confirmed_message = ''
    back_to_my_credentials_button = ''
    """right to work page locators"""
    right_to_work_heading = ''
    rtw_name_title = ''
    rtw_name_value = ''
    rtw_dob_title = ''
    rtw_dob_value = ''
    rtw_biometric_page_title = ''
    rtw_passport_expiry_date_title = ''
    rtw_something_is_not_right_link = ''
    rtw_confirm_credential_button = ''
    """dbs supporting information"""
    dbs_supporting_info_heading = ''
    dbs_name_title = ''
    dbs_name_value = ''
    dbs_dob_title = ''
    dbs_dob_value = ''
    dbs_verified_current_address_title = ''
    dbs_verified_current_address_value = ''
    dbs_resident_form_title = ''
    dbs_resident_from_value = ''
    dbs_passport_number_title = ''
    dbs_passport_number_value = ''
    dbs_passport_nationality_title = ''
    dbs_passport_nationality_value = ''
    dbs_passport_issue_date_title = ''
    dbs_passport_issue_date_value = ''
    dbs_some_thing_is_not_right_link = ''
    dbs_confirm_credential_button = ''
    email_content = ''
    user_name_in_email_content = ''
    splash_screen_text_content = ''
    email_subject = ''
    version_number = ''
    nhs_logo = ''
    """account and setting page"""
    account_and_settings_page_heading = ""
    account_and_settings_delete_your_nhs_digital_staff_pp = ''
    security_and_privacy_section_heading = ''
    back_link = ""
    def read_identity_page_heading(self):
        """method to read the page heading"""
        return self.read_value_from_element(self.identity_page_heading, "identity page heading")

    def verify_question_mark_icon(self):
        """method to verify the question mark icon"""
        return self.verify_element_displayed(self.question_icon, "question mark icon")

    def verify_user_account_icon(self):
        """method to verify the account icon"""
        return self.verify_element_displayed(self.account_icon, "account icon")

    def verify_home_button(self):
        """method to verify the home button"""
        return self.verify_element_displayed(self.home_icon, "home icon")

    def verify_credentials_button(self):
        """method to verify the credentials icon"""
        return self.verify_element_displayed(self.credentials_icon, "credentials icon")

    def verify_identity_credential(self):
        """method to verify the identity credential"""
        return self.verify_element_displayed(self.identity_credentials, "identity credentials")

    def verify_right_to_work_credentials(self):
        """method to verify the right to work credentials"""
        return self.verify_element_displayed(self.right_to_work_credentials, "right to work credentials")

    def verify_dbs_supporting_documents(self):
        """method to verify the dbs supporting documents"""
        return self.verify_element_displayed(self.dbs_supporting_information, "dbs supporting documents")

    def verify_no_credentials_yet(self):
        """method to verify the no credentials yet message"""
        return self.verify_element_displayed(self.no_credentials_yet, "no credentials yet")

    def click_identity_credential(self):
        """method to click on identity credential"""
        self.click_element(self.identity_credentials, "identity credentials")

    def verify_provided_by_trust(self):
        """method to verify provided by trust"""
        return self.verify_element_displayed(self.provided_by_trust, "provided by trust")

    def verify_identity_credential_details(self):
        """method to verify the identity credential details"""
        return self.verify_element_displayed(self.photo_of_your_face)

    def verify_something_not_right_link(self):
        """method to verify the something not right link"""
        return self.verify_element_displayed(self.something_is_not_right_link, "something is not right link")

    def click_confirm_credential_button(self):
        """method to click on confirm credential button"""
        self.click_element(self.confirm_credential_button, "confirm credential button")

    def verify_confirming_credential_spinner(self):
        """method to verify the confirming credential spinner"""
        return self.verify_element_displayed(self.confirming_credentials_spinner, "confirming credentials spinner")

    def verify_credentials_confirmed_page(self):
        """method to verify the credentials confirmed page"""
        return self.verify_element_displayed(self.credential_confirmed_title, "credential confirmed title")

    def verify_text_on_page(self):
        """method to verify the text on the page"""
        return self.verify_element_displayed(self.credentials_confirmed_message, "credentials confirmed message")

    def click_back_to_my_credentials_button(self):
        """method to click back to my credentials button"""
        self.click_element(self.back_to_my_credentials_button, "back to my credentials button")

    def verify_credentials_page(self):
        """method to verify the credentials page"""
        return self.verify_element_displayed(self.credentials_page_heading, "credentials page heading")

    def verify_identity_credential_removed(self):
        """method to verify the identity credential removed"""
        return self.verify_element_displayed(self.identity_credentials, "identity credentials")

    def verify_identity_listed(self):
        """method to verify the identity listed"""
        return self.verify_element_displayed(self.identity_credentials, "identity credentials")

    def click_right_to_work_credentials(self):
        """method to click on right to work credentials"""
        self.click_element(self.right_to_work_credentials, "right to work credentials")

    def verify_right_to_work_credential_details(self):
        """method to verify the right to work credential details"""
        return self.verify_element_displayed(self.rtw_name_title, "right to work name title")

    def verify_something_went_wrong_link(self):
        """method to verify the something went wrong link"""
        return self.verify_element_displayed(self.rtw_something_is_not_right_link, "something is not right link")

    def verify_spinner_page_with_confirming_credential(self):
        """method to verify the spinner page with confirming credential"""
        return self.verify_element_displayed(self.confirming_credentials_spinner, "confirming credentials spinner")

    def verify_right_to_work_credential_removed(self):
        """method to verify the right to work credential removed"""
        return self.verify_element_displayed(self.right_to_work_credentials, "right to work credentials")

    def verify_right_to_work_listed(self):
        """method to verify the right to work listed"""
        return self.verify_element_displayed(self.right_to_work_credentials, "right to work credentials")

    def click_dbs_supporting_documents(self):
        """method to click on dbs supporting documents"""
        self.click_element(self.dbs_supporting_information, "dbs supporting information")

    def verify_dbs_supporting_documents_details(self):
        """method to verify the dbs supporting documents details"""
        return self.verify_element_displayed(self.dbs_name_title, "dbs name title")

    def verify_dbs_supporting_documents_removed(self):
        """method for dbs supporting documents removed"""
        return self.verify_element_displayed(self.dbs_supporting_information, "dbs supporting information")

    def verify_dbs_supporting_documents_listed(self):
        """method to verify the dbs supporting documents listed"""
        return self.verify_element_displayed(self.dbs_supporting_information, "dbs supporting information")

    def verify_email_content(self):
        """method to verify email content"""
        return self.read_value_from_element(self.email_content)

    def verify_user_name_in_email(self):
        """method to verify user name in email"""
        return self.read_value_from_element(self.user_name_in_email_content)

    def verify_splash_screen_content(self):
        """method to verify splash screen content"""
        return self.read_value_from_element(self.splash_screen_text_content)

    def provide_wrong_face(self):
        """method to provide wrong face"""
        pass

    def wrong_face_error_message(self):
        """method to get error message"""
        pass

    def verify_email_subject(self):
        """method to verify email subject"""
        return self.read_value_from_element(self.email_subject)

    def verify_nhs_logo(self):
        """method to verify nhs logo"""
        return self.verify_element_displayed(self.nhs_logo, "nhs logo")

    def verify_version_number(self):
        """method to verify version number"""
        return self.read_value_from_element(self.version_number)

    def verify_home_page(self):
        """method to verify home page"""
        return self.verify_element_displayed(self.home_icon, "home icon")

    def read_name_on_identity_credentials_page(self):
        """method to read the name on identity credentials page"""
        return self.read_value_from_element(self.name_value, "name value")

    def read_dob_on_identity_credentials_page(self):
        """method to read the dob on identity credentials page"""
        return self.read_value_from_element(self.dob_value, "dob value")

    def read_legal_gender_on_identity_credentials_page(self):
        """method to read the gender value on identity credentials page"""
        return self.read_value_from_element(self.legal_gender_value)

    def read_nationality_on_identity_credentials_page(self):
        """method to read the nationality value on identity credentials page"""
        return self.read_value_from_element(self.nationality_value)

    def read_issued_on_value_on_identity_credentials_page(self):
        """method to read the issued on value on identity credentials page"""
        return self.read_value_from_element(self.issued_on_value)

    def read_name_on_right_to_work_page(self):
        """method to read the name on right to work page"""
        return self.read_value_from_element(self.rtw_name_value, "right to work name value")

    def read_dob_on_right_to_work_page(self):
        """method to read the dob on right to work page"""
        return self.read_value_from_element(self.rtw_dob_value, "right to work dob value")

    def read_passport_expiry_date_on_right_to_work_page(self):
        """method to read the passport expiry date on right to work page"""
        return self.read_value_from_element(self.rtw_passport_expiry_date_title)

    def read_name_on_dbs_supporting_documents_page(self):
        """method to read the name on dbs supporting documents page"""
        return self.read_value_from_element(self.dbs_name_value, "dbs name value")

    def read_dob_on_dbs_supporting_documents_page(self):
        """method to read the dob on dbs supporting documents page"""
        return self.read_value_from_element(self.dbs_dob_value, "dbs dob value")

    def read_verified_current_address_on_dbs_supporting_documents_page(self):
        """method to read the verified current address on dbs supporting documents page"""
        return self.read_value_from_element(self.dbs_verified_current_address_value)

    def read_resident_from_on_dbs_supporting_documents_page(self):
        """method to read the resident from on dbs supporting documents page"""
        return self.read_value_from_element(self.dbs_resident_from_value)

    def read_passport_number_on_dbs_supporting_documents_page(self):
        """method to read the passport number on dbs supporting documents page"""
        return self.read_value_from_element(self.dbs_passport_number_value)

    def read_passport_nationality_on_dbs_supporting_documents_page(self):
        """method to read the passport nationality on dbs supporting information page"""
        return self.read_value_from_element(self.dbs_passport_nationality_value)

    def read_passport_issue_date_on_dbs_supporting_documents_page(self):
        """method to read the passport issue date on dbs supporting documents page"""
        return self.read_value_from_element(self.dbs_passport_issue_date_value)

    def click_account_icon(self):
        """click account icon with click element"""
        self.click_element(self.account_icon)

    def verify_back_link(self):
        """verify back link is displayed"""
        return self.verify_element_displayed(self.back_link)


    def verify_account_and_settings_page(self):
        """verify is there is account and setting page displayed"""
        return self.verify_element_displayed(self.account_and_settings_page_heading)

    def verify_delete_nhs_digital_staff_passport_section(self):
        """verify is element is present"""
        return self.verify_element_displayed(self.account_and_settings_delete_your_nhs_digital_staff_pp)

    def verify_security_and_privacy_section(self):
        """verify is element is present"""
        return self.verify_element_displayed(self.security_and_privacy_section_heading)

    def click_back_link(self):
        """call click element from base page & click back link"""
        self.click_element(self.back_link, "back link")


    def verify_no_credentials(self):
        """verify no credentials message"""
        return self.verify_element_displayed(self.no_credentials_yet)
