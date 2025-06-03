
from jose import jwt
from auth import crear_token_acceso, verificar_token

def test_crear_y_verificar_token():
    datos = {"email": "test@mail.com", "id_usuario": 1}
    token = crear_token_acceso(datos)
    decoded = verificar_token(token)
    assert decoded["email"] == datos["email"]
    assert decoded["id_usuario"] == datos["id_usuario"]
