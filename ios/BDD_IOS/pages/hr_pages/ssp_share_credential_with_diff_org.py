"""this class contains methods for the page actions
of Share credential with different organisation page ,and is called in the step definition file
"""
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from utilities import custom_logger
logger = custom_logger.get_logger()


class SsPortalShareCredWithDiffOrg(BasePage):
    """contains the page actions of ss portal -Share credential with different organisation"""

    Review_credential_link_xpath = AppiumBy.XPATH, (
        "//XCUIElementTypeStaticText[@name=\"Review credentials\"]"
    )

    Accept_all_checkbox_xpath = AppiumBy.XPATH, (
        "//XCUIElementTypeStaticText[@name=\"Accept all (28)\"]"
    )

    Continue_button_xpath = AppiumBy.XPATH, (
        "//XCUIElementTypeButton[@name=\"Continue\"]"
    )

    Review_shared_credentials_heading_xpath = AppiumBy.XPATH, (
        "//XCUIElementTypeStaticText[@name=\"Review shared credentials\"]"
    )

    Yes_confirm_button_id = AppiumBy.XPATH, (
        "//XCUIElementTypeStaticText[@name=\"Yes, confirm\"]"
    )

    Status_confirmed_heading_xpath = AppiumBy.XPATH, (
        "//XCUIElementTypeStaticText[@name=\"Status confirmed\"]"
    )
    Status_confirmed_txt = "Status confirmed"

    hr_conflict_resolution_value_xpath = AppiumBy.XPATH, (
        "(//XCUIElementTypeStaticText[@name=\"Conflict resolution\"])[1]"
    )

    hr_portal_provided_by_xpath = AppiumBy.XPATH, (
        "//XCUIElementTypeStaticText[@name=\"Provided by: University Hospitals Cov and Warwickshire\"]"
    )

    hr_portal_reject_shared_creds_xpath = AppiumBy.XPATH, (
        "//XCUIElementTypeStaticText[@name=\"Reject shared credential\"]"
    )
    hr_portal_reject_shared_creds_text = "Reject shared credential"

    hr_portal_creds_value = (
        '//XCUIElementTypeStaticText[@name="{dynamic_value}"]'
    )

    def hr_portal_review_credential_link(self):
        """ function to click on Review credential link and select accept all checkbox """
        self.click_element_with_wait(self.Review_credential_link_xpath, "Click on review credential link")
        self.click_element_with_wait(self.Accept_all_checkbox_xpath, "Click on accept all checkbox")

    def hr_portal_select_continue_button(self):
        """ Function to click on continue button on review shared credential page"""
        self.click_element_with_wait(self.Continue_button_xpath, "click on continue button")

    def hr_portal_yes_confirm_radio_button(self):
        """Verify Review shared credential heading and select yes confirm button"""
        self.verify_element_displayed(self.Review_shared_credentials_heading_xpath)
        self.take_screenshot("PASS")
        self.click_element_with_wait(self.Yes_confirm_button_id, "Click on yes confirm button")

    def hr_portal_status_confirmed_message(self):
        """Function to confirm success message"""
        self.verify_element_displayed(self.Status_confirmed_heading_xpath)
        message = self.read_value_from_element(self.Status_confirmed_heading_xpath)
        assert message in self.Status_confirmed_txt
        self.take_screenshot("PASS")
        self.close_safari()

    def hr_portal_creds_check(self, creds_value):
        """Common function to verify the credentials"""
        dynamic_value = creds_value
        self.verify_element_visible("xpath", self.hr_portal_creds_value.format(dynamic_value=dynamic_value))
        self.user_defined_wait(2)
        message = self.read_text_from_element("xpath",
                                                  self.hr_portal_creds_value.format(dynamic_value=dynamic_value))
        assert dynamic_value in message
        self.user_defined_wait(2)

    def hr_portal_identity_creds_check(self):
        """Verify if the identity credentials are shared and visible"""
        dynamic_value = "Identity"
        self.hr_portal_creds_check(dynamic_value)

    def hr_portal_dbs_creds_check(self):
        """Verify if the dbs credentials are shared and visible"""
        dynamic_value = "Disclosure and Barring Service (DBS)"
        self.hr_portal_creds_check(dynamic_value)

    def hr_portal_occupation_health_creds_check(self):
        """Verify if the occupation health credentials are shared and visible"""
        dynamic_value = "Occupational health"
        self.hr_portal_creds_check(dynamic_value)

    def hr_portal_profession_registration_creds_check(self):
        """Verify if the profession registration are shared and visible"""
        dynamic_value = "Professional registration"
        self.hr_portal_creds_check(dynamic_value)

    def hr_portal_conflict_resolution_creds_check(self):
        """Verify if conflict resolution are shared and visible"""
        dynamic_value = "Conflict resolution"
        self.hr_portal_creds_check(dynamic_value)

    def hr_portal_equality_diversity_human_rights_creds_check(self):
        """Verify if Equality diversity and human rights are shared and visible"""
        dynamic_value = "Equality diversity and human rights"
        self.hr_portal_creds_check(dynamic_value)

    def hr_portal_fire_safety_creds_check(self):
        """Verify if fire safety are shared and visible"""
        dynamic_value = "Fire safety"
        self.hr_portal_creds_check(dynamic_value)

    def hr_portal_health_safety_welfare_creds_check(self):
        """Verify if health safety and welfare are shared and visible"""
        dynamic_value = "Health safety and welfare"
        self.hr_portal_creds_check(dynamic_value)

    def hr_portal_infection_prevention_control_level1_creds_check(self):
        """Verify if infection prevention and control level1 are shared and visible"""
        dynamic_value = "Infection prevention and control (Level 1)"
        self.hr_portal_creds_check(dynamic_value)

    def hr_portal_infection_prevention_control_level2_creds_check(self):
        """Verify if infection prevention and control level2 are shared and visible"""
        dynamic_value = "Infection prevention and control (Level 2)"
        self.hr_portal_creds_check(dynamic_value)

    def hr_portal_information_governance_data_security_creds_check(self):
        """Verify if Information governance and data security are shared and visible"""
        dynamic_value = "Information governance and data security"
        self.hr_portal_creds_check(dynamic_value)

    def hr_portal_moving_and_handling_level1_creds_check(self):
        """Verify if Moving and handling (Level 1) are shared and visible"""
        dynamic_value = "Moving and handling (Level 1)"
        self.hr_portal_creds_check(dynamic_value)

    def hr_portal_moving_and_handling_level2_creds_check(self):
        """Verify if Moving and handling (Level 2) are shared and visible"""
        dynamic_value = "Moving and handling (Level 2)"
        self.hr_portal_creds_check(dynamic_value)

    def hr_portal_preventing_radicalisation_basic_prevent_awareness_creds_check(self):
        """Verify if Preventing radicalisation basic prevent awareness are shared and visible"""
        dynamic_value = "Preventing radicalisation basic prevent awareness"
        self.hr_portal_creds_check(dynamic_value)
        self.take_screenshot("PASS")

    def hr_portal_preventing_radicalisation_prevent_awareness_creds_check(self):
        """Verify if Preventing radicalisation prevent awareness are shared and visible"""
        dynamic_value = "Preventing radicalisation prevent awareness"
        self.hr_portal_creds_check(dynamic_value)

    def hr_portal_resuscitation_creds_check(self):
        """Verify if resuscitation are shared and visible"""
        dynamic_value = "Resuscitation"
        self.hr_portal_creds_check(dynamic_value)

    def hr_portal_resuscitation_adult_basic_life_support_creds_check(self):
        """Verify if resuscitation adult basic life support are shared and visible"""
        dynamic_value = "Resuscitation adult basic life support"
        self.hr_portal_creds_check(dynamic_value)

    def hr_portal_resuscitation_adult_immediate_life_support_creds_check(self):
        """Verify if resuscitation adult immediate life support are shared and visible"""
        dynamic_value = "Resuscitation adult immediate life support"
        self.hr_portal_creds_check(dynamic_value)

    def hr_portal_resuscitation_newborn_basic_life_support_creds_check(self):
        """Verify if resuscitation newborn basic life support are shared and visible"""
        dynamic_value = "Resuscitation newborn basic life support"
        self.hr_portal_creds_check(dynamic_value)

    def hr_portal_resuscitation_newborn_immediate_life_support_creds_check(self):
        """Verify if resuscitation newborn immediate life support are shared and visible"""
        dynamic_value = "Resuscitation newborn immediate life support"
        self.hr_portal_creds_check(dynamic_value)

    def hr_portal_resuscitation_paediatric_basic_life_support_creds_check(self):
        """Verify if resuscitation paediatric basic life support are shared and visible"""
        dynamic_value = "Resuscitation paediatric basic life support"
        self.hr_portal_creds_check(dynamic_value)

    def hr_portal_resuscitation_paediatric_immediate_life_support_creds_check(self):
        """Verify if resuscitation paediatric immediate life support are shared and visible"""
        dynamic_value = "Resuscitation paediatric immediate life support"
        self.hr_portal_creds_check(dynamic_value)

    def hr_portal_safeguarding_adults_level1_creds_check(self):
        """Verify if Safeguarding adults (Level 1) are shared and visible"""
        dynamic_value = "Safeguarding adults (Level 1)"
        self.hr_portal_creds_check(dynamic_value)

    def hr_portal_safeguarding_adults_level2_creds_check(self):
        """Verify if Safeguarding adults (Level 2) are shared and visible"""
        dynamic_value = "Safeguarding adults (Level 2)"
        self.hr_portal_creds_check(dynamic_value)

    def hr_portal_safeguarding_adults_level3_creds_check(self):
        """Verify if Safeguarding adults (Level 3) are shared and visible"""
        dynamic_value = "Safeguarding adults (Level 3)"
        self.hr_portal_creds_check(dynamic_value)

    def hr_portal_safeguarding_children_level1_creds_check(self):
        """Verify if Safeguarding children (Level 1) are shared and visible"""
        dynamic_value = "Safeguarding children (Level 1)"
        self.hr_portal_creds_check(dynamic_value)

    def hr_portal_safeguarding_children_level2_creds_check(self):
        """Verify if Safeguarding children (Level 2) are shared and visible"""
        dynamic_value = "Safeguarding children (Level 2)"
        self.hr_portal_creds_check(dynamic_value)

    def hr_portal_safeguarding_children_level3_creds_check(self):
        """Verify if Safeguarding children (Level 3) are shared and visible"""
        dynamic_value = "Safeguarding children (Level 3)"
        self.hr_portal_creds_check(dynamic_value)
        self.take_screenshot("PASS")
        self.close_safari()

    def hr_portal_conflict_resolution_creds_click(self):
        """Function to click on the occupation health credentials"""
        self.click_element_with_wait(self.hr_conflict_resolution_value_xpath, "click on conflict resolution")

    def hr_portal_occupation_health_creds_reject_shared_credentials_check(self):
        """Verify if shared credentials with different org have reject shared credentials"""
        self.verify_element_displayed(self.hr_portal_provided_by_xpath)
        self.verify_element_displayed(self.hr_portal_reject_shared_creds_xpath)
        message = self.read_value_from_element(self.hr_portal_reject_shared_creds_xpath)
        assert self.hr_portal_reject_shared_creds_text in message
        self.close_safari()
