import pytest
from appium import webdriver
from config import APPIUM_SERVER_URL, ANDROID_CAPS, IOS_CAPS

@pytest.fixture(scope="module")
def android_driver():
    driver = webdriver.Remote(command_executor=APPIUM_SERVER_URL, desired_capabilities=ANDROID_CAPS)
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def ios_driver():
    driver = webdriver.Remote(command_executor=APPIUM_SERVER_URL, desired_capabilities=IOS_CAPS)
    yield driver
    driver.quit()