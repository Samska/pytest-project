import pytest
from pages.product_page import ProductPage
from tests.data.product_data import create_product_data

@pytest.fixture(scope="module")
def product_page(browser):
    page = ProductPage(browser)
    page.login('beltrano@qa.com.br', 'teste')
    return page

def test_create_product_success(product_page):
    product_page.click_element(product_page.NAV_ITEM_CREATE_PRODUCT)
    
    product_data = create_product_data()
        
    product_page.create_product(product_data['nome'], product_data['preco'], product_data['descricao'], product_data['quantidade'])
    product_page.wait_for_url_contains('/admin/listarprodutos')    
    assert '/admin/listarprodutos' in product_page.browser.current_url
    
def test_create_product_empty_fields(product_page):
    product_page.click_element(product_page.NAV_ITEM_CREATE_PRODUCT)    
    product_page.create_product('', '', '', '')
    product_page.wait_for_element(product_page.ALERT_MESSAGE)    
    expected_messages = ["Nome é obrigatório", "Preco é obrigatório", "Descricao é obrigatório", "Quantidade é obrigatório"]
    page_text = product_page.get_page_text()    
    for expected_text in expected_messages:
        assert expected_text in page_text