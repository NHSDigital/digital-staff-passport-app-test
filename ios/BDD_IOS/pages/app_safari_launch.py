"""page object file for app logon"""
from selenium.common import TimeoutException
from ios.BDD_IOS.pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from ios.BDD_IOS.utilities import custom_logger

# Set up logging configuration
logger = custom_logger.get_logger()


class SafariAppAutomation(BasePage):
    """Methods to launch android app"""
    aos_app_login_username_xpath = AppiumBy.XPATH, ('//android.widget.FrameLayout['
                                                    '@resource-id="com.instagram.android:id/layout_container_main"]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText')
    aos_app_login_password_xpath = AppiumBy.XPATH, ('//android.widget.FrameLayout['
                                                    '@resource-id="com.instagram.android:id/layout_container_main"]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.EditText')
    aos_app_login_button_xpath = AppiumBy.XPATH, '//android.view.View[@content-desc="Log in"]'
    aos_app_save_login_info_not_now_xpath = AppiumBy.XPATH, '//android.view.View[@content-desc="Not now"]'
    aos_app_deny_option_xpath = (AppiumBy.XPATH, '//android.widget.Button['
                                                 '@resource-id="com.android.permissioncontroller:id/permission_deny_button"]')
    aos_app_skip_xpath = (AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.instagram.android:id/skip_button"]')
    aos_app_primary_option_click_xpath = (AppiumBy.XPATH, '//android.widget.Button['
                                                          '@resource-id="com.instagram.android:id/primary_button"]')
    aos_app_negative_option_click_xpath = (AppiumBy.XPATH, '//android.widget.Button['
                                                           '@resource-id="com.instagram.android:id/negative_button"]')
    aos_app_discover_ppl_click_xpath = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Next"]')
    aos_app_home_button_xpath = AppiumBy.XPATH, ('(//android.widget.ImageView['
                                                 '@resource-id="com.instagram.android:id/tab_icon"])[2]')
    aos_app_profile_tab_button_xpath = AppiumBy.XPATH, ('//android.widget.ImageView['
                                                        '@resource-id="com.instagram.android:id/tab_avatar"]')
    aos_app_options_profile_tab_xpath = AppiumBy.XPATH, '//android.widget.Button[@content-desc="Options"]'
    aos_app_options_logout_xpath = AppiumBy.XPATH, '//android.widget.TextView[@text="Log out"]'
    aos_app_save_login_negative_xpath = AppiumBy.XPATH, ('//android.widget.Button['
                                                         '@resource-id="com.instagram.android:id/negative_button"]')
    aos_app_logout_confirm_yes_xpath = AppiumBy.XPATH, ('//android.widget.Button['
                                                        '@resource-id="com.instagram.android:id/primary_button"]')
    aos_app_search_tab_xpath = AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Search and explore"]'
    aos_app_profile_search_text_xpath = AppiumBy.XPATH, ('//android.widget.EditText['
                                                         '@resource-id="com.instagram.android:id/action_bar_search_edit_text"]')
    aos_app_search_result_xpath = AppiumBy.XPATH, ('//android.widget.TextView['
                                                   '@resource-id="com.instagram.android:id/row_search_user_username" '
                                                   'and @text="nhs"]')

    def check_app_not_installed(self):
        # self.start_appium()
        if self.is_app_installed():
            self.reset_app()
            self.uninstall_app()  # Optional: Uninstall if it’s needed for test consistency
        assert not self.is_app_installed(), "Expected app to be uninstalled"

    def check_app_installed(self):
        # self.start_appium()
        if not self.is_app_installed():
            self.install_aos_app()
        assert self.is_app_installed(), "Expected app to be installed"

    def app_username(self, value):
        """Enter app login username"""
        self.user_defined_wait(5)
        if self.verify_element_displayed(self.aos_app_login_username_xpath):
            self.type_element(self.aos_app_login_username_xpath, value)

    def app_password(self, value):
        """Enter app login password"""
        if self.verify_element_displayed(self.aos_app_login_password_xpath):
            self.type_element(self.aos_app_login_password_xpath, value)

    def app_login_click(self):
        """User clicks on login"""
        if self.verify_element_displayed(self.aos_app_login_button_xpath):
            self.click_element(self.aos_app_login_button_xpath, "Click")

    def app_search_tab_click(self):
        """User navigate to search tab"""
        if self.verify_element_displayed(self.aos_app_search_tab_xpath):
            self.click_element(self.aos_app_search_tab_xpath, "Click")

    def profile_search_text_enter(self, value):
        """User enters profile name to search"""
        self.user_defined_wait(2)
        if self.verify_element_displayed(self.aos_app_profile_search_text_xpath):
            self.type_element(self.aos_app_profile_search_text_xpath, value)

    def profile_search_result_click(self):
        """User select search result"""
        if self.verify_element_displayed(self.aos_app_search_result_xpath):
            self.click_element(self.aos_app_search_result_xpath, "Click")

    def app_navigate_to_home_screen(self):
        """Navigates through any intermediate screens to reach the home screen."""
        self.user_defined_wait(2)
        # List of elements to click in sequence to reach the home screen
        navigation_steps = [
            self.aos_app_save_login_info_not_now_xpath,
            self.aos_app_deny_option_xpath
        ]
        for element_xpath in navigation_steps:
            try:
                if self.verify_element_displayed(element_xpath):
                    self.click_element(element_xpath, "Click")
                    self.user_defined_wait(1)
            except TimeoutException:
                # If the element is not found, skip to the next one in the list
                continue
        logger.info("Navigated to the home screen.")

    def close_app(self):
        """Closes the app gracefully using adb if it is active."""
        # self.stop_appium()
        self.user_defined_wait(2)
        self.reset_app()

