import pytest
from pages.signup_page import SignupPage
from tests.data.user_data import create_user_data

@pytest.fixture(scope="function")
def signup_page(browser):
    page = SignupPage(browser)
    page.open_url(SignupPage.SIGNUP_URL)
    return page

def test_signup_success(signup_page):
    user_data = create_user_data()
    signup_page.signup(user_data['nome'], user_data['email'], user_data['password'], True)    
    signup_page.wait_for_element(signup_page.ALERT_MESSAGE)    
    page_text = signup_page.get_page_text()
    assert "Cadastro realizado com sucesso" in page_text

def test_signup_existing_email(signup_page):
    signup_page.signup('Fulano da Silva', 'beltrano@qa.com.br', 'teste!', False)
    signup_page.wait_for_element(signup_page.ALERT_MESSAGE)
    page_text = signup_page.get_page_text()
    assert "Este email já está sendo usado" in page_text

def test_signup_empty_fields(signup_page):
    signup_page.signup('', '', '', False)
    signup_page.wait_for_element(signup_page.ALERT_MESSAGE)
    expected_messages = ["Nome é obrigatório", "Email é obrigatório", "Password é obrigatório"]
    page_text = signup_page.get_page_text()
    for expected_text in expected_messages:
        assert expected_text in page_text