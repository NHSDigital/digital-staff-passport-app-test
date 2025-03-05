"""steps for review and confirm two credentials"""
from behave import then, when
from pages.ios_pages.review_confirm_two_creds_page import ReviewAndConfirmTwoCredsPage


@then("user navigate back to home page with 2 credentials ready to review")
def verify_navigation_back_to_home_page(context):
    """step to call read page heading and assert the expected value"""
    context.review_two_creds = ReviewAndConfirmTwoCredsPage(context.driver)
    assert "Welcome " in context.review_two_creds.read_two_creds_home_page_heading(), "Page heading is not displayed"


@then("user clicks on 2 credentials ready to review")
def click_two_creds_home_page(context):
    """step to click two creds to review"""
    context.review_two_creds.click_two_creds_ready_review()


@then("user navigates to credentials page")
def verify_my_credentials_page(context):
    """step to call read page heading and assert the expected value"""
    assert "My Credentials " in context.review_two_creds.read_creds_page_heading(), "Page heading is not displayed"


@then("user verifies credentials to confirm heading")
def verify_creds_to_confirm_header(context):
    """step to call read heading and assert the expected value"""
    context.review_two_creds = ReviewAndConfirmTwoCredsPage(context.driver)
    assert (
        "Credentials to confirm"
        in context.review_two_creds.read_creds_page_creds_to_confirm_heading()
    ), "creds to confirm heading is not displayed"


@then("user verifies credentials to confirm has Professional registration credential listed with action required")
def verify_prof_reg_cred(context):
    """step to verify prof reg creds listed with action required status"""
    assert context.review_two_creds.verify_prof_registration_cred(), "prof reg creds is not displayed"


@then("user verifies credentials to confirm has Employment assignment credential listed with action required")
def verify_emp_assignment_cred(context):
    """step to verify employment assignment cred listed with action required status"""
    assert context.review_two_creds.verify_employment_assign_cred, "emp assignment creds is not displayed"


@then("user verifies confirmed credentials heading")
def verify_confirmed_creds_header(context):
    """step to call read heading and assert the expected value"""
    assert "Confirmed credentials" in context.review_two_creds.read_creds_page_confirmed_creds_heading(), ("confirmed "
                                                                                                           "cred "
                                                                                                           "heading "
                                                                                                           "is not "
                                                                                                           "displayed")


@then("user verifies confirmed credentials has DBS supporting information credential listed in confirmed creds")
def verify_dbs_supporting_info(context):
    """step to verify dbs supporting info cred listed in confirmed creds"""
    assert context.review_two_creds.verify_dbs_support_info_cred(), "dbs support info cred is not displayed"


@then("user verifies confirmed credentials has Right to work credential listed in confirmed creds")
def verify_right_to_work_creds(context):
    """step to verify right to work cred listed in confirmed creds"""
    assert context.review_two_creds.verify_right_to_work_cred(), "right to work cred is not displayed"


@then("user verifies confirmed credentials has identity credential listed in confirmed creds")
def verify_identity_creds(context):
    """step to verify identity cred listed in confirmed creds"""
    assert context.review_two_creds.verify_identity_cred(), "identity cred is not displayed"


@when("user clicks on Professional registration credential to confirm")
def click_prof_reg_creds(context):
    """step to click prof reg credential to review"""
    context.review_two_creds.click_prof_reg_cred_to_review()


@then("user verifies professional registration heading")
def verify_prof_reg_cred_header(context):
    """step to verify professional registration heading"""
    assert "Professional registration" in context.review_two_creds.read_prof_reg_creds_page_heading(), ("professional "
                                                                                                        "registration")


@then("user verifies details heading")
def verify_details_section(context):
    """step to verify prof reg page section heading"""
    assert "Details" in context.review_two_creds.read_prof_reg_details_heading(), "details section is not displayed"


@then("user verifies details body section")
def verify_details_body_section(context):
    """step to verify prof reg page section heading"""
    assert "Body" in context.review_two_creds.read_prof_reg_body_heading(), "body section is not displayed"


@then("user verifies staff member section")
def verify_staff_member_section(context):
    """step to verify prof reg page section heading"""
    assert (
        "Staff member" in context.review_two_creds.read_prof_reg_staff_member_heading()
    ), "staff member section is not displayed"


@then("user verifies expiry date section")
def verify_expiry_date_section(context):
    """step to verify prof reg page section heading"""
    assert (
        "Expiry dater" in context.review_two_creds.read_prof_reg_expiry_date_heading()
    ), "expiry date section is not displayed"


@then("user verifies status section")
def verify_status_section(context):
    """step to verify prof reg page section heading"""
    assert "Status" in context.review_two_creds.read_prof_reg_status_heading(), "Status section is not displayed"


@then("user verifies registration date section")
def verify_reg_date_section(context):
    """step to verify prof reg page section heading"""
    assert "Registration date" in context.review_two_creds.read_prof_reg_date_heading(), ("reg date section is not "
                                                                                          "displayed")


@then("user verifies professional registration cred is removed from credentials to confirm")
def verify_prof_reg_cred_removed_from_confirm_section(context):
    """step to verify the prof reg credential removed from review"""
    context.review_two_creds = ReviewAndConfirmTwoCredsPage(context.driver)
    assert not context.review_creds.verify_prof_reg_cred_review_removed(), "prof reg credential is not removed"


@then("user verifies professional registration cred is listed under confirmed credentials")
def verify_prof_reg_cred_listed_confirmed_section(context):
    """step to verify the prof reg credential listed as confirmed"""
    assert context.review_creds.verify_prof_reg_cred_confirmed_listed(), "prof reg credential confirmed"


@when("user clicks on employment assignment credential to confirm")
def click_employment_assignment_creds(context):
    """step to click employment assignment cred to review"""
    context.review_two_creds.click_emp_assign_cred_to_review()


@then("user verifies employment assignment heading")
def verify_employment_assignment_page_header(context):
    """step to verify employment assignment heading"""
    assert "Employment assignment" in context.review_two_creds.read_emp_assign_creds_page_heading(), ("employment "
                                                                                                      "assignment")


@then("user verifies emp assign details heading")
def verify_emp_assign_details_heading(context):
    """step to verify emp assign page section heading"""
    assert "Details" in context.review_two_creds.read_emp_assign_details_heading(), ("emp assign details section is "
                                                                                     "not displayed")


@then("user verifies employer section")
def verify_employer_section(context):
    """step to verify emp assignment page section heading"""
    assert (
        "Employer" in context.review_two_creds.read_emp_assign_employer_heading()
    ), "employer section is not displayed"


@then("user verifies department section")
def verify_department_section(context):
    """step to verify emp assignment page section heading"""
    assert "Department" in context.review_two_creds.read_emp_assign_department_heading(), ("department section is not "
                                                                                           "displayed")


@then("user verifies job title section")
def verify_job_title_section(context):
    """step to verify emp assignment page section heading"""
    assert "Job title" in context.review_two_creds.read_emp_assign_job_title_heading(), ("job title section is not "
                                                                                         "displayed")


@then("user verifies assignment category section")
def verify_assignment_category_section(context):
    """step to verify emp assignment page section heading"""
    assert "Assignment category" in context.review_two_creds.read_emp_assign_category_heading(), ("assign category "
                                                                                                  "section is not "
                                                                                                  "displayed")


@then("user verifies assignment status section")
def verify_assignment_status_section(context):
    """step to verify emp assignment page section heading"""
    assert "Assignment status" in context.review_two_creds.read_emp_assign_status_heading(), ("assign status section "
                                                                                              "is not displayed")


@then("user verifies assignment effective start date section")
def verify_assign_start_date_section(context):
    """step to verify emp assignment page section heading"""
    assert (
        "Assignment effective start date"
        in context.review_two_creds.read_emp_assign_effective_date_heading()
    ), "assign effective start date section is not displayed"


@then("user verifies employment assignment number section")
def verify_assignment_num_section(context):
    """step to verify emp assignment page section heading"""
    assert "Employment assignment number" in context.review_two_creds.read_emp_assignment_num_heading(), ("emp assign "
                                                                                                          "num "
                                                                                                          "section is "
                                                                                                          "not "
                                                                                                          "displayed")


@then("user verifies employment assignment cred is removed from credentials to confirm")
def verify_employ_assign_cred_removed_cred_confirm_section(context):
    """step to verify the employment assignment credential removed from review"""
    context.review_two_creds = ReviewAndConfirmTwoCredsPage(context.driver)
    assert not context.review_creds.verify_emp_assign_cred_review_removed(), "emp assignment credential is not removed"


@then("user verifies employment assignment cred is listed under confirmed credentials")
def verify_employ_assign_cred_listed_in_confirmed_section(context):
    """step to verify the employment assignment credential listed as confirmed"""
    assert context.review_creds.verify_emp_assign_cred_confirmed_listed(), "emp assign credential confirmed"
