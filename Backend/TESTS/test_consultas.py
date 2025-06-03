import pytest

@pytest.mark.asyncio
async def test_consulta_datos_usuario(client):
    # Login primero para obtener token válido
    login_payload = {"Correo": "tomas@gmail.com", "password": "123456789"}
    login_res = await client.post("/auth/login", json=login_payload)
    assert login_res.status_code == 200
    token = login_res.json()["access_token"]

    # Usar token para la consulta
    headers = {"Authorization": f"Bearer {token}"}
    res = await client.get("/usuario/me", headers=headers)

    assert res.status_code == 200
    assert "email" in res.json()
