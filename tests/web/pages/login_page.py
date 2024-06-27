from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config import WEB_BASE_URL

class LoginPage(BasePage):
    URL = f"{WEB_BASE_URL}/login"
    
    # Locators
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'password')
    ENTRAR_BUTTON = (By.CSS_SELECTOR, '[data-testid=entrar]')
    ALERT_MESSAGE = (By.CLASS_NAME, 'alert')
    
    def __init__(self, browser):
        super().__init__(browser)
        
    def login(self, email, password):
        self.input_text(self.EMAIL_INPUT, email)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click_element(self.ENTRAR_BUTTON)
    
    def get_alert_message(self):
        return self.wait_for_element(self.ALERT_MESSAGE)