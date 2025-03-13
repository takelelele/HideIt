import re

from fastapi.testclient import TestClient
from pytest import fixture
from main import app

client = TestClient(app)
@fixture
def test_create_secret_without_passphrase():
    response = client.post("/generate", json={
        "secret": "Pytest"
    })
    pattern = re.compile(r"^[0-9a-f]{32}$")
    assert response.status_code == 200
    assert re.match(pattern, response.json())
    return response.json()

@fixture
def test_create_secret_with_passphrase():
    response = client.post("/generate", json={
        "secret": "Pytest2",
        "passphrase": "Apelsin"
    })
    pattern = re.compile(r"^[0-9a-f]{32}$")
    assert response.status_code == 200
    assert re.match(pattern, response.json())
    return response.json()

def test_create_secret_with_empty_body():
    response = client.post("/generate", json={})
    assert response.status_code == 422

def test_get_secret_without_passphrase_by_null_token():
    response = client.post("/secrets/00000000000000000000000000000000")
    assert response.json() == "Нет секретов"

def test_get_secret_without_passphrase_by_token(test_create_secret_without_passphrase):
    response = client.post(f"/secrets/{test_create_secret_without_passphrase}")
    assert response.status_code == 200
    assert response.json() == "Pytest"

def test_get_secret_with_passphrase_by_token_with_empty_passphrase(test_create_secret_with_passphrase):
    response = client.post(f"/secrets/{test_create_secret_with_passphrase}", json={ })
    assert response.status_code == 200
    assert response.json() == "Нет секретов"

def test_get_secret_with_passphrase_by_token_with_wrong_passphrase(test_create_secret_with_passphrase):
    response = client.post(f"/secrets/{test_create_secret_with_passphrase}", json={
        "passphrase": "Apelsin1"
    })
    assert response.status_code == 200
    assert response.json() == "Нет секретов"

def test_get_secret_with_passphrase_by_token_with_passphrase(test_create_secret_with_passphrase):
    response = client.post(f"/secrets/{test_create_secret_with_passphrase}", json={
        "passphrase": "Apelsin"
    })
    assert response.status_code == 200
    assert response.json() == "Pytest2"