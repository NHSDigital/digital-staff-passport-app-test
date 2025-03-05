"""
Steps definition w.r.t share cred with different org
"""
from behave import then
from pages.hr_pages.ssp_share_credential_with_diff_org import SsPortalShareCredWithDiffOrg


@then('Review shared credential and click accept all checkbox')
def review_shared_cred_click_accept_all_checkbox(context):
    """Review shared credential and click accept all checkbox"""
    context.ss_portal_share_with_diff = SsPortalShareCredWithDiffOrg(context.driver)
    context.ss_portal_share_with_diff.hr_portal_review_credential_link()


@then('HR selects continue button on review shared credential page')
def hr_select_continue_button_on_review_shared_cred(context):
    """HR selects continue button on review shared credential page"""
    context.ss_portal_share_with_diff.hr_portal_select_continue_button()


@then('HR review heading and select Yes confirm radio button')
def ss_portal_share_cred_with_different_org(context):
    """HR review heading and select Yes confirm radio button"""
    context.ss_portal_share_with_diff.hr_portal_yes_confirm_radio_button()


@then('HR validates success message for shared credential')
def hr_validate_success_for_cred(context):
    """HR validates success message for shared credential"""
    context.ss_portal_share_with_diff.hr_portal_status_confirmed_message()


@then('HR user verifies the identity credentials')
def hr_portal_share_cred_with_different_org(context):
    """HR user verifies the identity credentials"""
    context.ss_portal_share_with_diff = SsPortalShareCredWithDiffOrg(context.driver)
    context.ss_portal_share_with_diff.hr_portal_identity_creds_check()


@then('HR user verifies the employment checks credentials')
def hr_verifies_the_employment_checks_creds(context):
    """HR user verifies the employment checks credentials"""
    context.ss_portal_share_with_diff.hr_portal_dbs_creds_check()
    context.ss_portal_share_with_diff.hr_portal_occupation_health_creds_check()
    context.ss_portal_share_with_diff.hr_portal_profession_registration_creds_check()


@then('HR user verifies the Core skills training information')
def hr_user_verifies_the_core_skill_training_info(context):
    """HR user verifies the Core skills training information"""
    context.ss_portal_share_with_diff.hr_portal_conflict_resolution_creds_check()

    context.ss_portal_share_with_diff.hr_portal_equality_diversity_human_rights_creds_check()

    context.ss_portal_share_with_diff.hr_portal_fire_safety_creds_check()

    context.ss_portal_share_with_diff.hr_portal_health_safety_welfare_creds_check()

    context.ss_portal_share_with_diff.hr_portal_infection_prevention_control_level1_creds_check()

    context.ss_portal_share_with_diff.hr_portal_infection_prevention_control_level2_creds_check()

    context.ss_portal_share_with_diff.hr_portal_information_governance_data_security_creds_check()

    context.ss_portal_share_with_diff.hr_portal_moving_and_handling_level1_creds_check()

    context.ss_portal_share_with_diff.hr_portal_moving_and_handling_level2_creds_check()

    context.ss_portal_share_with_diff.hr_portal_preventing_radicalisation_basic_prevent_awareness_creds_check()

    context.ss_portal_share_with_diff.hr_portal_preventing_radicalisation_prevent_awareness_creds_check()

    context.ss_portal_share_with_diff.hr_portal_resuscitation_creds_check()

    context.ss_portal_share_with_diff.hr_portal_resuscitation_adult_basic_life_support_creds_check()

    context.ss_portal_share_with_diff.hr_portal_resuscitation_adult_immediate_life_support_creds_check()

    context.ss_portal_share_with_diff.hr_portal_resuscitation_newborn_basic_life_support_creds_check()

    context.ss_portal_share_with_diff.hr_portal_resuscitation_newborn_immediate_life_support_creds_check()

    context.ss_portal_share_with_diff.hr_portal_resuscitation_paediatric_basic_life_support_creds_check()

    context.ss_portal_share_with_diff.hr_portal_resuscitation_paediatric_immediate_life_support_creds_check()

    context.ss_portal_share_with_diff.hr_portal_safeguarding_adults_level1_creds_check()

    context.ss_portal_share_with_diff.hr_portal_safeguarding_adults_level2_creds_check()

    context.ss_portal_share_with_diff.hr_portal_safeguarding_adults_level3_creds_check()

    context.ss_portal_share_with_diff.hr_portal_safeguarding_children_level1_creds_check()

    context.ss_portal_share_with_diff.hr_portal_safeguarding_children_level2_creds_check()

    context.ss_portal_share_with_diff.hr_portal_safeguarding_children_level3_creds_check()


@then('HR User clicks conflict resolution credential')
def hr_clicks_conflict_resolution_cred(context):
    """HR User clicks conflict resolution credential"""
    context.ss_portal_share_with_diff = SsPortalShareCredWithDiffOrg(context.driver)
    context.ss_portal_share_with_diff.hr_portal_conflict_resolution_creds_click()


@then('HR user verifies that the conflict resolution should have Reject shared credentials link')
def verify_conflict_resolution_reject_shared_cred_link(context):
    """HR user verifies that the conflict resolution should Reject shared credentials link"""
    context.ss_portal_share_with_diff.hr_portal_occupation_health_creds_reject_shared_credentials_check()
