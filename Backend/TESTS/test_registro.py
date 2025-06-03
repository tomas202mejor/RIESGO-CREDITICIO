
import random
import pytest

@pytest.mark.asyncio
async def test_registro_usuario(client):
    numero = random.randint(10000, 99999)
    user = {
        "nombre": "Juan",
        "apellido": "Pérez",
        "Nusuario": f"user{numero}",
        "Ndocumento": f"{numero}123",
        "email": f"user{numero}@mail.com",
        "telefono": f"321{numero}",
        "password": "test1234"
    }
    response = await client.post("/users/registro", json=user)
    assert response.status_code == 200
    assert "id" in response.json()
