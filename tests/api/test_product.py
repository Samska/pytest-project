import pytest
from tests.api.utils.login_utils import login
from tests.api.utils.product_utils import create_product, get_product_by_id, update_product
from fixtures.payloads.product_data import create_product_data

@pytest.fixture(scope="module")
def authorization_token():
    response, token = login("beltrano@qa.com.br", "teste")
    return token

@pytest.fixture(scope="module")
def create_product_fixture(authorization_token):
    product_data = create_product_data()
    response = create_product(product_data, authorization_token)

    assert response.status_code == 201
    response_json = response.json()
    assert response_json['message'] == "Cadastro realizado com sucesso"
    assert '_id' in response_json

    product_id = response_json['_id']
    return product_id

def test_get_product_by_id(authorization_token, create_product_fixture):
    product_id = create_product_fixture
    response = get_product_by_id(product_id, authorization_token)
    assert response.status_code == 200
    
def test_update_product(authorization_token, create_product_fixture):
    updated_product_data = create_product_data()
    product_id = create_product_fixture
    response = update_product(product_id, updated_product_data, authorization_token)
    assert response.status_code == 200
    assert response.json()['message'] == "Registro alterado com sucesso"