import pytest
from tests.api.utils.user_utils import create_user, get_user, get_users, update_user, delete_user
from tests.data.user_data import create_user_data

@pytest.fixture(scope="module")
def create_user_fixture():
    user_data = create_user_data()
    response = create_user(user_data)
    assert response.status_code == 201
    user_id = response.json().get('_id')
    return user_id
    
def test_get_users():
    response = get_users()
    assert response.status_code == 200
    response_json = response.json()
    assert "quantidade" in response_json
    assert "usuarios" in response_json
    assert isinstance(response_json["usuarios"], list)

def test_get_user_details(create_user_fixture):
    user_id = create_user_fixture
    response = get_user(user_id)
    assert response.status_code == 200
    user_details = response.json()
    assert user_details.get('_id') == user_id

def test_update_user(create_user_fixture):
    user_id = create_user_fixture
    updated_user_data = create_user_data()
    response = update_user(user_id, updated_user_data)
    assert response.status_code == 200
    assert response.json()['message'] == "Registro alterado com sucesso"

def test_delete_user(create_user_fixture):
    user_id = create_user_fixture
    response = delete_user(user_id)
    assert response.status_code == 200
    assert "Registro excluído com sucesso" in response.json()['message']