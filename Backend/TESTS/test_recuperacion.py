
import pytest

@pytest.mark.asyncio
async def test_enviar_codigo_recuperacion(client):
    data = {"email": "test@mail.com"}
    res = await client.post("/auth/recuperar", json=data)
    assert res.status_code == 200
