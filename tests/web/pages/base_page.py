from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config import WEB_BASE_URL

class BasePage:
    LOGIN_URL = f"{WEB_BASE_URL}/login"
    
    # Locators
    NAV_ITEM_HOME = (By.CSS_SELECTOR, '[data-testid=home]')
    NAV_ITEM_CREATE_USER = (By.CSS_SELECTOR, '[data-testid=cadastrar-usuarios]')
    NAV_ITEM_LIST_USERS = (By.CSS_SELECTOR, '[data-testid=listar-usuarios]')
    NAV_ITEM_CREATE_PRODUCT = (By.CSS_SELECTOR, '[data-testid=cadastrar-produtos]')
    NAV_ITEM_LIST_PRODUCTS = (By.CSS_SELECTOR, '[data-testid=listar-produtos]')
    NAV_ITEM_LOGOUT = (By.CSS_SELECTOR, '[data-testid=logout]')
    
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
        
    def login(self, email, password):
        self.open_url(self.LOGIN_URL)
        self.input_text((By.ID, 'email'), email)
        self.input_text((By.ID, 'password'), password)
        self.click_element((By.CSS_SELECTOR, '[data-testid=entrar]'))
        self.wait_for_url_contains('/admin/home')