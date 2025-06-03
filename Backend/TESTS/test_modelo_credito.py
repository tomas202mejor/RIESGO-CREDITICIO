import pytest

@pytest.mark.asyncio
async def test_evaluar_credito(client):
    login_payload = {"Correo": "tomas@gmail.com", "password": "123456789"}
    login_res = await client.post("/auth/login", json=login_payload)
    token = login_res.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "idCredito": 1,
        "ingresos": 1500000,
        "gastos": 500000,
        "credito": 3000000,
        "cuotas": 6
    }
    res = await client.post("/Modelo/evaluarCredito", headers=headers, json=data)
    assert res.status_code == 200
    assert "decision" in res.json()
