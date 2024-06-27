import pytest
from tests.api.utils.user_utils import create_user, get_user, get_users, update_user, delete_user
from tests.data.user_data import create_user_data

@pytest.fixture(scope="module")
def create_user_fixture():
    user_data = create_user_data()
    response = create_user(user_data)
    assert response.status_code == 201, f"Failed to create user: {response.text}"
    user_id = response.json().get('_id')
    yield user_id
    
def test_get_users():
    response = get_users()
    assert response.status_code == 200, f"Failed to retrieve users: {response.text}"
    response_json = response.json()
    assert "quantidade" in response_json, "Response does not contain 'quantidade'"
    assert "usuarios" in response_json, "Response does not contain 'usuarios'"
    assert isinstance(response_json["usuarios"], list), "'usuarios' field is not a list"

def test_get_user_details(create_user_fixture):
    user_id = create_user_fixture
    response = get_user(user_id)
    assert response.status_code == 200, f"Failed to retrieve user details: {response.text}"
    user_details = response.json()
    assert user_details.get('_id') == user_id, f"Returned user ID {user_details.get('_id')} does not match expected {user_id}"

def test_update_user(create_user_fixture):
    user_id = create_user_fixture
    updated_user_data = create_user_data()
    response = update_user(user_id, updated_user_data)
    assert response.status_code == 200, f"Failed to update user: {response.text}"
    assert response.json()['message'] == "Registro alterado com sucesso", f"Unexpected message: {response.json()['message']}"

def test_delete_user(create_user_fixture):
    user_id = create_user_fixture
    response = delete_user(user_id)
    assert response.status_code == 200, f"Failed to delete user: {response.text}"
    assert "Registro excluído com sucesso" in response.json()['message'], f"Unexpected message: {response.json()['message']}"