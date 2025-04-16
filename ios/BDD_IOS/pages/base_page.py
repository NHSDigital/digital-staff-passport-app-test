"""This module contains the BasePage class for the Page Object Model."""
# import configparser
# import glob
import os
import subprocess
import time
from datetime import datetime
from pathlib import Path

import yaml
from appium.options.common.base import AppiumOptions
from appium import webdriver as appium_webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import InvalidSelectorException
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver as selenium_webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from utilities import custom_logger
from utilities.read_config import ReadProperty

# Set up logging configuration
logger = custom_logger.get_logger()


class BasePage:
    """This Class contains all functions related to pages that are reusable"""

    def __init__(self, driver):
        self.driver = driver

    # Hardcoded configuration values
    package_name = "com.instagram.android"
    activity = "com.instagram.android.activity.MainTabActivity"

    def open_browser(self, headless_mode):
        """Open browser based on the browser type and headless option"""
        browser_test = 'chrome'
        if browser_test == 'chrome':
            options = selenium_webdriver.ChromeOptions()
            options.use_chromium = True
            options.add_argument("--no-sandbox")
            options.add_argument("--window-size=1920,1080")
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')
            options.add_argument('log-level=3')
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            options.add_argument("ignore-certificate-errors")
            if headless_mode == 'True':
                options.add_argument("--headless")
            # To avoid undesired logging on console
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            self.driver = selenium_webdriver.Chrome(options=options)
            self.driver.set_page_load_timeout(100)
            logger.info("Chrome Browser is open")
            return self.driver
        return

    def open_ios_app(self):
        """Open the ios app with below capabilities"""
        options = AppiumOptions()
        options.load_capabilities(
            {
                "platformName": "iOS",
                "appium:platformVersion": "18.3.2",
                "appium:deviceName": "iPhone SE",
                "appium:automationName": "XCUITest",
                "appium:udid": "00008110-00065C913402601E",
                "appium:bundleId": "uk.nhs.dsp",
            }
        )
        appium_server_url = "http://127.0.0.1:4723"
        self.driver = appium_webdriver.Remote(appium_server_url, options=options)
        logger.info("App is open")
        return self.driver

    def open_app_with_activity(self):
        """Attempt to open the app using a single activity entry point."""
        appium_server_url = "http://127.0.0.1:4723"
        # Define Load capabilities
        options = AppiumOptions()
        options.load_capabilities(
            {
                "platformName": "Android",
                "appium:deviceName": "Galaxy A14 5G",
                "appium:appPackage": self.package_name,
                "appium:automationName": "UIAutomator2",
                "appium:appActivity": self.activity,
                "appium:noReset": True,
            }
        )
        try:
            # Attempt to initialize the Appium session with the specified activity
            self.driver = appium_webdriver.Remote(appium_server_url, options=options)
        except Exception as error:
            logger.warning("Failed to launch with activity %s %s:", self.activity, error)
            if self.driver:
                self.driver.quit()  # Only quit if session initialization failed
            self.driver = None  # Ensure driver is reset if session creation failed
        else:
            logger.info("App launched successfully with activity %s:", self.activity)

    def open_browser_mobile(self):
        """Open browser based on the browser and run the appium server"""
        if ReadProperty.read_config("configuration", "browser_mobile") == "Safari":
            options = AppiumOptions()
            options.load_capabilities(
                {
                    "platformName": "iOS",
                    "appium:platformVersion": "18.3.2",
                    "appium:deviceName": "iPhone SE",
                    "appium:automationName": "XCUITest",
                    "appium:udid": "00008110-00065C913402601E",
                    "appium:app": "com.apple.mobilesafari",
                }
            )
            appium_server_url = "http://127.0.0.1:4723"
            self.driver = appium_webdriver.Remote(appium_server_url, options=options)
            logger.info("Browser is open")
            return self.driver
        return None

    def open_browser_mobile_simulator(self):
        """Open browser based on the browser and run the appium server"""
        if ReadProperty.read_config("configuration", "browser_mobile") == "Safari":
            options = AppiumOptions()
            options.load_capabilities(
                {
                    "platformName": "iOS",
                    "appium:platformVersion": "18.1",
                    "appium:deviceName": "iPhone 16 Pro",
                    "appium:automationName": "XCUITest",
                    "appium:udid": "8CC046FE-40B5-4658-A286-1E80D76133EB",
                    "appium:app": "com.apple.mobilesafari",
                }
            )
            appium_server_url = "http://127.0.0.1:4723"
            self.driver = appium_webdriver.Remote(appium_server_url, options=options)
            logger.info("Browser is open")
            return self.driver
        return None

    def open_dsp_hr_portal_application_url(self):
        """invoke the browser and open HR Portal URL."""
        try:
            self.driver.get(ReadProperty.environment_hr_url())
        except InvalidSelectorException:
            logger.error("DSP HR application URL is not open.")
            self.driver.close()
            assert False, "Test is failed in open login page section"
        else:
            logger.info("DSP HR application URL is open.")
            return self.driver

    def hr_portal_login_homepage(self):
        """Browser is open and user clicks on register link"""
        self.open_dsp_hr_portal_application_url()
        # self.user_defined_wait(5)

    def click_login_on_login_page(self):
        """click login page"""
        self.click_element_with_wait((By.XPATH, "//a[contains(text(),'Login')]"), "Login button")


    def is_app_installed(self):
        """Check if the app is installed on the device."""
        try:
            result = subprocess.run(
                ["adb", "shell", "pm", "list", "packages", self.package_name],
                check=True,
                capture_output=True,
                text=True,
            )
        except Exception as error:
            logger.error("Failed to check if app is installed:%s", error)
            return False
        return self.package_name in result.stdout

    def reset_app(self):
        """Force-stop the app to reset its state."""
        try:
            subprocess.run(
                ["adb", "shell", "am", "force-stop", self.package_name], check=True
            )
        except Exception as error:
            logger.warning("Failed to force-stop app: %s", error)
        else:
            logger.info("App has been force-stopped.")

    def uninstall_app(self):
        """Uninstall the app for test consistency if needed."""
        try:
            subprocess.run(["adb", "uninstall", self.package_name], check=True)
        except Exception as error:
            logger.error("Failed to uninstall app: %s", error)
        else:
            logger.info("App has been uninstalled.")

    @staticmethod
    def start_appium():
        """Start the Appium server."""
        # Initialize the AppiumService
        appium_service = AppiumService()
        # Start the Appium server on port 4723
        appium_service.start(args=["--port", "4723"])
        # Check if the server is running
        if appium_service.is_running:
            logger.info("Appium server started successfully!")
        else:
            logger.info("Failed to start Appium server.")

    @staticmethod
    def stop_appium():
        """Stops the Appium server if it was started by this script."""
        appium_service = AppiumService()
        if appium_service.is_running:
            appium_service.stop()
            logger.info("Appium server stopped.")
        else:
            logger.info("No Appium server is running.")

    def click_element_with_wait(self, by_locator, objname=None):
        """Click the element if displayed."""
        self.verify_element_displayed(by_locator, objname)
        element = self.find_element(by_locator)
        if element:
            element.click()
            logger.info("%s is clicked", objname)
        else:
            logger.error("Exception! Can't click on the element %s", objname)

    def read_value_from_element(self, by_locator, objname=None):
        """Returns the text of a web element."""
        element = self.find_element(by_locator)
        if element:
            logger.info("Element %s value is : %s", objname, element.text)
            return element.text
        logger.info("Exception! Can't read value from element")
        return "Can't read value from element"

    @staticmethod
    def user_defined_wait(sleep_seconds):
        """Wait for the specified number of seconds."""
        time.sleep(sleep_seconds)

    def find_element(self, by_locator, timeout=60):
        """Finds an element with the given locator and timeout."""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(by_locator)
            )
        except TimeoutException:
            logger.error("Element not found: %s", by_locator)
            return None
        return element

    def verify_element_displayed(self, by_locator, objname=None):
        """checks if the element is displayed"""
        try:
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located(by_locator)
            )
        except InvalidSelectorException:
            logger.error("Element not found")
            return False
        logger.info("Element found: %s", objname)
        return True

    def type_element(self, by_locator, text, objname=None):
        """types the passed text into the web element"""
        try:
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(by_locator)
            ).send_keys(text)
        except InvalidSelectorException:
            logger.error("Exception! Can't type on the element")
        else:
            logger.info("Value entered is: %s for field %s", text, objname)

    @staticmethod
    def get_test_data(page, field, filename):
        """to read test data"""
        file_path = os.path.join("data", filename)
        path = os.path.abspath(file_path)
        try:
            with open(path, "r", encoding="utf-8") as f_f:
                doc = yaml.safe_load(f_f)
        except yaml.YAMLError as exception:
            logger.warning(exception)
        return doc[page][field]

    def take_screenshot(self, status):
        """take screenshot and save"""
        file_path = str(Path("screenshots"))
        file_name = str(BasePage.file_name_generation(status))
        screenshots_file_path = os.path.join(file_path, file_name)
        self.driver.get_screenshot_as_file(screenshots_file_path)

    @staticmethod
    def file_name_generation(file_status):
        """returns format for filename"""
        date_time = datetime.now()
        year = date_time.year
        month = date_time.month
        day = date_time.day
        hour = date_time.hour
        minute = date_time.minute
        sec = date_time.second
        date_today = f"{year}-{month}-{day}-{hour}-{minute}-{sec}"
        if file_status == "PASS":
            file_name = str("Pass_" + date_today + ".png")
            return file_name
        if file_status == "FAIL":
            file_name = str("Fail_" + date_today + ".png")
            return file_name
        file_name = str("Unknown_" + date_today + ".png")
        return file_name

    def complete_close_browser(self):
        """close the instance of browser"""
        self.driver.quit()
        logger.info("Event is closed.")

    @staticmethod
    def kill_browser():
        """Function to kill browser process"""
        command = 'taskkill /F /IM "chrome.exe"'
        process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
        )
        process.communicate()

    def change_element_bg_color(self, by_bojtype, by_locator):
        """change the background color of the element"""
        element = self.driver.find_element(by_bojtype, by_locator)
        return self.driver.execute_script(
            "arguments[0].style.backgroundColor = 'lightgreen';", element
        )

    def verify_element_visible(self, by_obj_type, by_locator, objname=None):
        """verify the element"""
        time.sleep(3)
        try:
            self.driver.find_element(by_obj_type, by_locator).is_displayed()
        except NoSuchElementException:
            logger.info("Object is not visible: %s", objname)
            return False
        logger.info("Exception! Object is visible: %s", objname)
        return True

    def get_element_count(self, by_obj_type, by_locator):
        """to get the number of elements"""
        element_count = len(self.driver.find_elements(by_obj_type, by_locator))
        return element_count

    def read_text_from_element(self, by_obj_type, by_locator, objname=None):
        """returns the value of .text property of a web element"""
        try:
            text = self.driver.find_element(by_obj_type, by_locator).text
        except InvalidSelectorException:
            logger.info("Exception! Can't read value from element")
            return "Can't read value from element"
        logger.info("Element value is: %s, Name is: %s", text, objname)
        return text

    def navigate_url(self, value):
        """Navigate to the standalone URL as required"""
        self.driver.get(value)
        logger.info("URL is opened.")

    def close_safari(self):
        """Closes the Safari browser on iOS."""
        try:
            self.driver.quit()
        except Exception as error:
            print("Error closing Safari:%s", error)

    def close_app(self):
        """Closes the Safari browser on iOS."""
        try:
            self.driver.quit()
        except Exception as error:
            print("Error closing Safari:%s", error)

    def tap_on_coordinates(self, x, y):
        self.driver.execute_script("mobile: tap", {"x": x, "y": y})

    def open_notification(self):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(193, 11)
        actions.w3c_actions.pointer_action.move_to_location(187, 541)
        actions.perform()
