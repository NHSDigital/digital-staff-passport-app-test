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
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import InvalidSelectorException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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

    def open_ios_app(self):
        """Open the ios app with below capabilities"""
        options = AppiumOptions()
        options.load_capabilities({
            "platformName": "iOS",
            "appium:platformVersion": "18.1.1",
            "appium:deviceName": "iPhone SE",
            "appium:automationName": "XCUITest",
            "appium:udid": "00008110-00065C913402601E",
            "appium:bundleId": "uk.nhs.dsp"
        })
        appium_server_url = 'http://127.0.0.1:4723'
        self.driver = appium_webdriver.Remote(appium_server_url, options=options)
        logger.info("App is open")
        return self.driver


    def open_app_with_activity(self):
        """Attempt to open the app using a single activity entry point."""

        # Define Load capabilities
        options = AppiumOptions()
        options.load_capabilities({
            "platformName": "Android",
            "appium:deviceName": "Galaxy A14 5G",
            "appium:appPackage": self.package_name,
            "appium:automationName": "UIAutomator2",
            "appium:appActivity": self.activity,
            "appium:noReset": True
        })

        try:
            # Attempt to initialize the Appium session with the specified activity
            appium_server_url = 'http://127.0.0.1:4723'
            self.driver = appium_webdriver.Remote(appium_server_url, options=options)
            logger.info(f"App launched successfully with activity: {self.activity}")
        except Exception as e:
            logger.warning(f"Failed to launch with activity {self.activity}: {e}")
            if self.driver:
                self.driver.quit()  # Only quit if session initialization failed
            self.driver = None  # Ensure driver is reset if session creation failed

    def open_browser_mobile(self):
        """Open browser based on the browser and run the appium server"""
        if ReadProperty.read_config("configuration", "browser_mobile") == 'Safari':
            options = AppiumOptions()
            options.load_capabilities({
                "platformName": "iOS",
                "appium:platformVersion": "18.1.1",
                "appium:deviceName": "iPhone SE",
                "appium:automationName": "XCUITest",
                "appium:udid": "00008110-00065C913402601E",
                "appium:app": "com.apple.mobilesafari"
            })
            appium_server_url = 'http://127.0.0.1:4723'
            self.driver = appium_webdriver.Remote(appium_server_url, options=options)
            logger.info("Browser is open")
            return self.driver


    def open_browser_mobile_simulator(self):
        """Open browser based on the browser and run the appium server"""
        if ReadProperty.read_config("configuration", "browser_mobile") == 'Safari':
            options = AppiumOptions()
            options.load_capabilities({
                "platformName": "iOS",
                "appium:platformVersion": "18.1",
                "appium:deviceName": "iPhone 16 Pro",
                "appium:automationName": "XCUITest",
                "appium:udid": "8CC046FE-40B5-4658-A286-1E80D76133EB",
                "appium:app": "com.apple.mobilesafari"
            })
            appium_server_url = 'http://127.0.0.1:4723'
            self.driver = appium_webdriver.Remote(appium_server_url, options=options)
            logger.info("Browser is open")
            return self.driver


    def open_dsp_hr_portal_application_url(self):
        """invoke the browser and open HR Portal URL."""
        try:
            self.driver.get(ReadProperty.environment_hr_url())
            logger.info("DSP HR application URL is open.")
            return self.driver
        except InvalidSelectorException:
            logger.error("DSP HR application URL is not open.")
            self.driver.close()
            assert False, "Test is failed in open login page section"


    def is_app_installed(self):
        """Check if the app is installed on the device."""

        try:
            result = subprocess.run(["adb", "shell", "pm", "list", "packages", self.package_name],
                                    capture_output=True, text=True)
            return self.package_name in result.stdout
        except Exception as e:
            logger.error(f"Failed to check if app is installed: {e}")
            return False

    def reset_app(self):
        """Force-stop the app to reset its state."""
        try:
            subprocess.run(["adb", "shell", "am", "force-stop", self.package_name], check=True)
            logger.info("App has been force-stopped.")
        except Exception as e:
            logger.warning(f"Failed to force-stop app: {e}")

    def uninstall_app(self):
        """Uninstall the app for test consistency if needed."""
        try:
            subprocess.run(["adb", "uninstall", self.package_name], check=True)
            logger.info("App has been uninstalled.")
        except Exception as e:
            logger.error(f"Failed to uninstall app: {e}")

    @staticmethod
    def start_appium():
        # Initialize the AppiumService
        appium_service = AppiumService()
        # Start the Appium server on port 4723
        appium_service.start(args=['--port', '4723'])
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


    def click_element(self, by_locator, objname=None):
        """Click the element if displayed."""
        element = self.find_element(by_locator)
        if element:
            element.click()
            logger.info("%s is clicked", objname)
        else:
            logger.error("Exception! Can't click on the element %s", objname)

    def read_value_from_element(self, by_locator):
        """Returns the text of a web element."""
        element = self.find_element(by_locator)
        if element:
            logger.info("Element value is : %s", element.text)
            return element.text
        else:
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
            return element
        except TimeoutException:
            logger.error("Element not found: %s", by_locator)
            return None

    def verify_element_displayed(self, by_locator):
        """checks if the element is displayed"""
        try:
            WebDriverWait(self.driver,
                                    60).until(EC.presence_of_element_located(by_locator))
            return True
        except InvalidSelectorException:
            logger.error("Element not found")
            return False

    def type_element(self, by_locator, text, objname=None):
        """types the passed text into the web element"""
        try:
            WebDriverWait(self.driver,
                          30).until(EC.presence_of_element_located(by_locator)).send_keys(text)
            logger.info("Value entered is: %s for field.", text)
            logger.info("Value entered is: %s for field.", objname)
        except InvalidSelectorException:
            logger.error("Exception! Can't type on the element")

    @staticmethod
    def get_test_data(page, field, filename):
        """to read test data"""
        try:
            file_path = os.path.join("data", filename)
            path = os.path.abspath(file_path)
            with open(path, 'r', encoding="utf-8") as f_f:
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
        """ Function to kill browser process"""
        command = 'taskkill /F /IM "chrome.exe"'
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   shell=True)
        process.communicate()


    def change_element_bg_color(self, by_bojtype, by_locator):
        element = self.driver.find_element(by_bojtype, by_locator)
        return self.driver.execute_script("arguments[0].style.backgroundColor = 'lightgreen';", element)


    def verify_element_visible(self, by_obj_type, by_locator, objname=None):
        """verify the element"""
        time.sleep(3)
        try:
            self.driver.find_element(by_obj_type, by_locator).is_displayed()
            logger.info("Exception! Object is visible: %s", objname)
            return True
        except NoSuchElementException:
            logger.info("Object is not visible: %s", objname)
            return False


    def click_element_wait(self, by_bojtype, by_locator, objname=None):
        """clicks the element passed as by_locator"""
        try:
            element = self.driver.find_element(by_bojtype, by_locator)
            element.click()
            logger.info("%s is clicked", objname)
        except InvalidSelectorException:
            logger.error("Exception! Can't click on the element %s", objname)


    def get_element_count(self, by_obj_type, by_locator):
        """to get the number of elements """
        element_count = len(self.driver.find_elements(by_obj_type, by_locator))
        return element_count


    def read_text_from_element(self, by_obj_type, by_locator):
        """returns the value of .text property of a web element"""
        try:
            text = self.driver.find_element(by_obj_type, by_locator).text
            logger.info("Element value is : %s", text)
            return text
        except InvalidSelectorException:
            logger.info("Exception! Can't read value from element")
            return "Can't read value from element"


    def navigate_url(self, value):
        """ Navigate to the standalone URL as required"""
        self.driver.get(value)
        logger.info("URL is opened.")


    def close_safari(self):
        """Closes the Safari browser on iOS."""
        try:
            self.driver.quit()
        except Exception as e:
            print(f"Error closing Safari: {e}")
