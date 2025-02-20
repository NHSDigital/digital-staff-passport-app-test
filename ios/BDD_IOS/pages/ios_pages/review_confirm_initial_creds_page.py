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
