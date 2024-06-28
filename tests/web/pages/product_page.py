from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    CREATE_PRODUCT_PATH = "/admin/cadastrarprodutos"
    
    # Locators
    NAME_INPUT = (By.ID, 'nome')
    PRICE_INPUT = (By.ID, 'price')
    DESCRIPTION_TEXTAREA = (By.ID, 'description')
    QTY_INPUT = (By.ID, 'quantity')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[data-testid=cadastarProdutos]')
    ALERT_MESSAGE = (By.CLASS_NAME, 'alert')
    
    def __init__(self, browser):
        super().__init__(browser)
        
    def create_product(self, name, price, description, quantity):
        self.input_text(self.NAME_INPUT, name)
        self.input_text(self.PRICE_INPUT, price)
        self.input_text(self.DESCRIPTION_TEXTAREA, description)
        self.input_text(self.QTY_INPUT, quantity)
        self.click_element(self.SUBMIT_BUTTON)
        
    def get_alert_message(self):
        return self.wait_for_element(self.ALERT_MESSAGE)