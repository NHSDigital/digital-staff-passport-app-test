"""
Steps definition w.r.t share cred with different org
"""
from behave import given, when, then
from pages.base_page import BasePage
from pages.hr_pages.ssp_share_credential_with_diff_org import SsPortalShareCredWithDiffOrg



@then('Review shared credential and click accept all checkbox')
def ss_portal_share_cred_with_different_org(context):
    context.ss_portal_share_with_diff = SsPortalShareCredWithDiffOrg(context.driver)
    context.ss_portal_share_with_diff.hr_portal_review_credential_link()

@then('HR selects continue button on review shared credential page')
def ss_portal_share_cred_with_different_org(context):
    context.ss_portal_share_with_diff.hr_portal_select_continue_button()

@then('HR review heading and select Yes confirm radio button')
def ss_portal_share_cred_with_different_org(context):
    context.ss_portal_share_with_diff.hr_portal_yes_confirm_radio_button()

@then('HR validates success message for shared credential')
def ss_portal_share_cred_with_different_org(context):
    context.ss_portal_share_with_diff.hr_portal_status_confirmed_message()

@then('HR user verifies the identity credentials')
def hr_portal_share_cred_with_different_org(context):
    context.ss_portal_share_with_diff = SsPortalShareCredWithDiffOrg(context.driver)
    context.ss_portal_share_with_diff.hr_portal_identity_creds_check()


@then('HR user verifies the employment checks credentials')
def hr_portal_share_cred_with_different_org(context):
    context.ss_portal_share_with_diff.hr_portal_dbs_creds_check()
    context.ss_portal_share_with_diff.hr_portal_occupation_health_creds_check()
    context.ss_portal_share_with_diff.hr_portal_profession_registration_creds_check()


@then('HR user verifies the Core skills training information')
def hr_portal_share_cred_with_different_org(context):
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
def hr_portal_share_cred_with_different_org(context):
    context.ss_portal_share_with_diff = SsPortalShareCredWithDiffOrg(context.driver)
    context.ss_portal_share_with_diff.hr_portal_conflict_resolution_creds_click()

@then('HR user verifies that the conflict resolution should have Reject shared credentials link')
def hr_portal_share_cred_with_different_org(context):
    context.ss_portal_share_with_diff.hr_portal_occupation_health_creds_reject_shared_credentials_check()
