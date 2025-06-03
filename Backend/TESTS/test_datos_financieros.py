import pytest

@pytest.mark.asyncio
async def test_guardar_datos_financieros(client):
    login_payload = {"Correo": "tomas@gmail.com", "password": "123456789"}
    login_res = await client.post("/auth/login", json=login_payload)
    token = login_res.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "nombre": "tomas",
        "documento": "123456789",
        "correo": "tomas@gmail.com",
        "vrIngresos": 2000000,
        "vrGastos": 500000,
        "vrCredito": 1000000,
        "numCuotas": 5
    }
    res = await client.post("/finanzas/guardarDatosFinac", headers=headers, json=data)
    assert res.status_code == 200
