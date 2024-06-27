import pytest
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def login_page(browser):
    page = LoginPage(browser)
    page.open_url(LoginPage.URL)
    return page

def test_login_success(login_page):
    login_page.login('beltrano@qa.com.br', 'teste')
    login_page.wait_for_url_contains('/admin/home')
    assert '/admin/home' in login_page.browser.current_url
    
def test_login_empty_fields(login_page):
    login_page.login('', '')
    login_page.wait_for_element(login_page.ALERT_MESSAGE)
    expected_messages = ["Email é obrigatório", "Password é obrigatório"]
    page_text = login_page.get_page_text()
    for expected_text in expected_messages:
        assert expected_text in page_text