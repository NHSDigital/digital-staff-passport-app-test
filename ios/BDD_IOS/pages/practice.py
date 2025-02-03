import time

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = AppiumOptions()
options.load_capabilities({
    "platformName": "iOS",
    "appium:platformVersion": "18.1.1",
    "appium:deviceName": "iPhone SE",
    "appium:automationName": "XCUITest",
    "appium:udid": "00008110-00065C913402601E",
    "browserName": "safari"  # Specify the browser to launch (Safari),

})

appium_server_url = 'http://127.0.0.1:4723'
driver = webdriver.Remote(appium_server_url, options=options)
wait = WebDriverWait(driver, 20)
time.sleep(4)

driver.get("https://hr-uhcwuat.staffpassports.nhs.uk/")
# sms_body = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Login"]')))
# time.sleep(3)
# sms_body.click()
time.sleep(2)
driver.close()
driver.quit()
