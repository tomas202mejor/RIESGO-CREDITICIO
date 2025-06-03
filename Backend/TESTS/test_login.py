import pytest

@pytest.mark.asyncio
async def test_login_correcto(client):
    payload = {
        "Correo": "tomas@gmail.com",
        "password": "123456789"
    }
    response = await client.post("/auth/login", json=payload)
    assert response.status_code == 200
    assert "access_token" in response.json()

@pytest.mark.asyncio
async def test_login_incorrecto(client):
    payload = {
        "Correo": "invalido@mail.com",
        "password": "wrong"
    }
    response = await client.post("/auth/login", json=payload)
    assert response.status_code == 401
