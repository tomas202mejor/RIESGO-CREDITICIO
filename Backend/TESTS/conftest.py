import sys
import os
import pytest_asyncio
from httpx import AsyncClient
from httpx._transports.asgi import ASGITransport

# Añadir el path del proyecto para encontrar Servicios.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Servicios import app

@pytest_asyncio.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
