from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config import WEB_BASE_URL

class SignupPage(BasePage):
    SIGNUP_URL = f"{WEB_BASE_URL}/cadastrarusuarios"

    # Locators
    NAME_INPUT = (By.ID, 'nome')
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'password')
    ADMIN_CHECKBOX = (By.ID, 'administrador')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[data-testid=cadastrar]')
    ALERT_MESSAGE = (By.CLASS_NAME, 'alert')

    def __init__(self, browser):
        super().__init__(browser)

    def signup(self, nome, email, password, is_admin):
        self.input_text(self.NAME_INPUT, nome)
        self.input_text(self.EMAIL_INPUT, email)
        self.input_text(self.PASSWORD_INPUT, password)
        if is_admin:
            self.click_element(self.ADMIN_CHECKBOX)
        self.click_element(self.SUBMIT_BUTTON)

    def get_alert_message(self):
        return self.wait_for_element(self.ALERT_MESSAGE)