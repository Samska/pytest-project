from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    LOGIN_PATH = "/login"
    
    # Locators
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'password')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[data-testid=entrar]')
    ALERT_MESSAGE = (By.CLASS_NAME, 'alert')
    
    def __init__(self, browser):
        super().__init__(browser)
        
    def open_login_page(self):
        self.open_path(self.LOGIN_PATH)
        
    def login(self, email, password):
        self.input_text(self.EMAIL_INPUT, email)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click_element(self.SUBMIT_BUTTON)
    
    def get_alert_message(self):
        return self.wait_for_element(self.ALERT_MESSAGE)