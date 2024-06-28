from tests.api.utils.login_utils import login

def test_login_successful():
    response, authorization_token = login("beltrano@qa.com.br", "teste")
    
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["message"] == "Login realizado com sucesso"
    assert "authorization" in response_json
    
def test_login_invalid_credentials():
    response, authorization_token = login("invaliduser@example.com", "invalidpassword")

    assert response.status_code == 401
    response_json = response.json()
    assert response_json["message"] == "Email e/ou senha inválidos"