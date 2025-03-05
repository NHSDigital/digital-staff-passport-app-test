# pylint: disable=too-many-public-methods

"""this class contains methods for the page actions of review and confirm two creds"""

from pages.base_page import BasePage


class ReviewAndConfirmTwoCredsPage(BasePage):
    """this class contains methods for the page actions of review and confirm two creds"""

    # 2 creds home page elements
    two_creds_home_page_header_xpath = ''
    two_creds_home_page_header_text = ''
    two_creds_home_page_2creds_ready_review_xpath = ''
    # Credentials page elements
    creds_page_header_xpath = ''
    creds_to_confirm_header_xpath = ''
    prof_reg_cred_action_required_xpath = ''
    employ_assign_acton_required_xpath = ''
    confirmed_creds_header_xpath = ''
    dbs_support_info_confirmed_cred_xpath = ''
    right_to_work_confirmed_cred_xpath = ''
    identity_confirmed_cred_xpath = ''
    prof_reg_confirmed_cred_xpath = ''
    employ_assign_confirmed_cred_xpath = ''
    # Prof reg cred page elements
    prof_reg_cred_page_header_xpath = ''
    prof_reg_details_header_xpath = ''
    prof_reg_body_header_xpath = ''
    prof_reg_staff_member_header_xpath = ''
    prof_reg_expiry_date_header_xpath = ''
    prof_reg_status_header_xpath = ''
    prof_reg_date_header_xpath = ''
    # Employment assignment cred page elements
    employment_assignment_cred_page_header_xpath = ''
    emp_assign_details_header_xpath = ''
    emp_assign_employer_header_xpath = ''
    emp_assign_department_header_xpath = ''
    emp_assign_job_title_header_xpath = ''
    emp_assign_category_header_xpath = ''
    emp_assign_status_header_xpath = ''
    emp_assign_effective_start_date_header_xpath = ''
    emp_assign_number_header_xpath = ''

    def read_two_creds_home_page_heading(self):
        """method to read the two creds home page heading"""
        return self.read_value_from_element(
            self.two_creds_home_page_header_xpath, "two creds home page heading"
        )

    def click_two_creds_ready_review(self):
        """method to click two credentials ready to review"""
        return self.click_element(
            self.two_creds_home_page_2creds_ready_review_xpath, "click 2 creds review"
        )

    def read_creds_page_heading(self):
        """method to read the credentials page heading"""
        return self.read_value_from_element(
            self.creds_page_header_xpath, "credentials page heading"
        )

    def read_creds_page_creds_to_confirm_heading(self):
        """method to read the credentials page creds to confirm heading"""
        return self.read_value_from_element(
            self.creds_to_confirm_header_xpath, "creds to confirm heading"
        )

    def verify_prof_registration_cred(self):
        """method to verify if the prof registration cred is listed with action required"""
        return self.verify_element_displayed(
            self.prof_reg_cred_action_required_xpath, "prof reg cred action required"
        )

    def verify_employment_assign_cred(self):
        """method to verify if the employment assignment cred is listed with action required"""
        return self.verify_element_displayed(
            self.employ_assign_acton_required_xpath,
            "employment assign cred action required",
        )

    def read_creds_page_confirmed_creds_heading(self):
        """method to read the credentials page confirmed creds heading"""
        return self.read_value_from_element(
            self.confirmed_creds_header_xpath, "confirmed creds heading"
        )

    def verify_dbs_support_info_cred(self):
        """method to verify if the dbs info cred is listed in confirmed creds"""
        return self.verify_element_displayed(
            self.dbs_support_info_confirmed_cred_xpath, "dbs support info confirmed cred"
        )

    def verify_right_to_work_cred(self):
        """method to verify if the right to work cred is listed in confirmed creds"""
        return self.verify_element_displayed(
            self.right_to_work_confirmed_cred_xpath, "right to work confirmed cred"
        )

    def verify_identity_cred(self):
        """method to verify if the identity cred is listed in confirmed creds"""
        return self.verify_element_displayed(
            self.identity_confirmed_cred_xpath, "identity confirmed cred"
        )

    def click_prof_reg_cred_to_review(self):
        """method to click prof reg cred to review"""
        return self.click_element(
            self.prof_reg_cred_action_required_xpath, "click prof reg to review"
        )

    def read_prof_reg_creds_page_heading(self):
        """method to read the prof reg credential page heading"""
        return self.read_value_from_element(
            self.prof_reg_cred_page_header_xpath, "prof reg page heading"
        )

    def read_prof_reg_details_heading(self):
        """method to read the prof reg credential page details heading"""
        return self.read_value_from_element(
            self.prof_reg_details_header_xpath, "prof reg page details heading"
        )

    def read_prof_reg_body_heading(self):
        """method to read the prof reg credential page body heading"""
        return self.read_value_from_element(
            self.prof_reg_body_header_xpath, "prof reg page body heading"
        )

    def read_prof_reg_staff_member_heading(self):
        """method to read the prof reg credential page staff member heading"""
        return self.read_value_from_element(
            self.prof_reg_staff_member_header_xpath, "prof reg page staff member heading"
        )

    def read_prof_reg_expiry_date_heading(self):
        """method to read the prof reg credential page expiry date heading"""
        return self.read_value_from_element(
            self.prof_reg_expiry_date_header_xpath, "prof reg page expiry date heading"
        )

    def read_prof_reg_status_heading(self):
        """method to read the prof reg credential page status heading"""
        return self.read_value_from_element(
            self.prof_reg_status_header_xpath, "prof reg page status heading"
        )

    def read_prof_reg_date_heading(self):
        """method to read the prof reg credential page registration date heading"""
        return self.read_value_from_element(
            self.prof_reg_date_header_xpath, "prof reg page date heading"
        )

    def verify_prof_reg_cred_review_removed(self):
        """method to verify the prof reg credential removed from review status"""
        return self.verify_element_displayed(
            self.prof_reg_cred_action_required_xpath, "prof reg creds to review"
        )

    def verify_prof_reg_cred_confirmed_listed(self):
        """method to verify the prof reg cred listed with confirmed status"""
        return self.verify_element_displayed(
            self.prof_reg_confirmed_cred_xpath, "prof reg creds confirmed"
        )

    def click_emp_assign_cred_to_review(self):
        """method to click employment assignment cred to review"""
        return self.click_element(
            self.employ_assign_acton_required_xpath, "click emp assignment to review"
        )

    def read_emp_assign_creds_page_heading(self):
        """method to read the emp assignment credential page heading"""
        return self.read_value_from_element(
            self.employment_assignment_cred_page_header_xpath, "emp assign page heading"
        )

    def read_emp_assign_details_heading(self):
        """method to read the emp assign credential page details heading"""
        return self.read_value_from_element(
            self.emp_assign_details_header_xpath, "emp assign page details heading"
        )

    def read_emp_assign_employer_heading(self):
        """method to read the emp assign credential page employer heading"""
        return self.read_value_from_element(
            self.emp_assign_employer_header_xpath, "emp assign page employer heading"
        )

    def read_emp_assign_department_heading(self):
        """method to read the emp assign credential page department heading"""
        return self.read_value_from_element(
            self.emp_assign_department_header_xpath, "emp assign page department heading"
        )

    def read_emp_assign_job_title_heading(self):
        """method to read the emp assign credential page job title heading"""
        return self.read_value_from_element(
            self.emp_assign_job_title_header_xpath, "emp assign page job title heading"
        )

    def read_emp_assign_category_heading(self):
        """method to read the emp assign credential page category heading"""
        return self.read_value_from_element(
            self.emp_assign_category_header_xpath, "emp assign page category heading"
        )

    def read_emp_assign_status_heading(self):
        """method to read the emp assign credential page status heading"""
        return self.read_value_from_element(
            self.emp_assign_status_header_xpath, "emp assign page status heading"
        )

    def read_emp_assign_effective_date_heading(self):
        """method to read the emp assign credential page effective start date heading"""
        return self.read_value_from_element(
            self.emp_assign_effective_start_date_header_xpath,
            "emp assign page effective date heading",
        )

    def read_emp_assignment_num_heading(self):
        """method to read the emp assign credential page assignment number heading"""
        return self.read_value_from_element(
            self.emp_assign_number_header_xpath, "emp assignment number heading"
        )

    def verify_emp_assign_cred_review_removed(self):
        """method to verify the employment assignment credential removed from review status"""
        return self.verify_element_displayed(
            self.employ_assign_acton_required_xpath, "emp assign creds to review"
        )

    def verify_emp_assign_cred_confirmed_listed(self):
        """method to verify the employment assignment credential listed with confirmed status"""
        return self.verify_element_displayed(
            self.employ_assign_confirmed_cred_xpath, "emp assign creds confirmed"
        )
