#WEB
WEB_BASE_URL = "https://front.serverest.dev"
#API
API_BASE_URL = "https://serverest.dev"
#MOBILE
import os

# Get the current directory of the config file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to the APK and IPA files relative to the config file location
ANDROID_APP_PATH = os.path.join(current_dir, 'app', 'android', 'demo-saucelabs.apk')
IOS_APP_PATH = os.path.join(current_dir, 'app', 'ios', 'demo-saucelabs.ipa')

APPIUM_SERVER_URL = "http://localhost:4723/wd/hub"

ANDROID_CAPS = {
    "platformName": "Android",
    "deviceName": "Android Simulator",
    "app": ANDROID_APP_PATH,
    "automationName": "UiAutomator2"
}

IOS_CAPS = {
    "platformName": "iOS",
    "deviceName": "iPhone Simulator",
    "app": IOS_APP_PATH,
    "automationName": "XCUITest"
}