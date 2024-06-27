import requests

def test_get_endpoint():
    response = requests.get('https://serverest.dev/usuarios')
    assert response.status_code == 200