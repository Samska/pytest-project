from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import WEB_BASE_URL

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def wait_for_element(self, locator):
        return WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    def input_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.send_keys(text)
        
    def get_page_text(self):
        return self.browser.page_source
    
    def wait_for_url_contains(self, path):
        return WebDriverWait(self.browser, 10).until(EC.url_contains(path))
    
    def open_url(self, url):
        self.browser.get(url)