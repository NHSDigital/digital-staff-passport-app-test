"""this class contains methods for the page actions of ID rejected page"""
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class IdRejectedPage(BasePage):
    """ Methods for the DSP APP """

    Id_rejected_heading_xpath = AppiumBy.XPATH, ''
    question_mark_icon = AppiumBy.XPATH, ''
    hr_team_will_contact_txt = ("The organisation's HR team will contact you "
                                "to arrange an in-person identity checks")

    def verify_id_rejected_heading(self):
        """Function to verify id rejected heading"""
        self.verify_element_displayed(self.Id_rejected_heading_xpath)

    def verify_and_click_on_question_mark(self):
        """Function to question mark icon"""
        self.verify_element_displayed(self.question_mark_icon)
        self.click_element(self.question_mark_icon, "click")

    def verify_hr_team_will_contact_txt(self):
        """Function to verify hr team will contact text"""
        self.verify_element_displayed(self.hr_team_will_contact_txt)
