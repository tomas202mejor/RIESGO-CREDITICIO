import React, { useState } from 'react';
import './LoginSignup.css';

const LoginSignup = () => {
  const [isLogin, setIsLogin] = useState(true);
  const [user, setUser] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  // Estados para el registro
  const [nusuario, setNusuario] = useState('');
  const [nombres, setNombres] = useState('');
  const [apellidos, setApellidos] = useState('');
  const [ndocumento, setNdocumento] = useState('');
  const [correo, setCorreo] = useState('');
  const [telefono, setTelefono] = useState('');
  const [regPassword, setRegPassword] = useState('');

  const handleLogin = async () => {
    if (!user || !password) {
      setMessage('⚠️ Por favor completa todos los campos.');
      return;
    }
  
    try {
      const res = await fetch('http://localhost:8000/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ Correo: user, password: password })
      });
  
      const data = await res.json();
  
      if (data.ok) {
        setMessage('✅ Inicio de sesión correcto');
      } else {
        setMessage('❌ Usuario o contraseña incorrectos');
      }
    } catch (error) {
      console.error('Error al conectarse con el backend:', error);
      setMessage('⚠️ Error de conexión con el servidor');
    }
  };
  
  const handleRegister = async () => {
    if (
      !nusuario || !nombres || !apellidos || !ndocumento ||
      !correo || !telefono || !regPassword
    ) {
      setMessage('⚠️ Por favor completa todos los campos del formulario de registro.');
      return;
    }
  
    try {
      const res = await fetch('http://localhost:8002/registro', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          Nusuario: nusuario,
          nombre: nombres,
          apellido: apellidos,
          Ndocumento: ndocumento,
          email: correo,
          telefono: telefono,
          password: regPassword
        })
      });
  
      const data = await res.json();
  
      if (data.ok) {
        setMessage('✅ Registro exitoso');
        setIsLogin(true); // Cambia a login después del registro
      } else {
        setMessage('❌ ' + data.mensaje);
      }
    } catch (error) {
      console.error('Error en el registro:', error);
      setMessage('⚠️ Error de conexión con el servidor');
    }
  };

  return (
    <div className="container">

      <div className="header">
        <div className="text">{isLogin ? 'Ingresar' : 'Registrarse'}</div>
        <div className="underline"></div>
      </div>

      <div className="inputs">
        {isLogin ? (
          <>
            <div className="input">
              <input
                type="email"
                placeholder="Correo electrónico"
                value={user}
                onChange={(e) => setUser(e.target.value)}
              />
            </div>
            <div className="input">
              <input
                type="password"
                placeholder="Contraseña"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
          </>
        ) : (
          <>
            <div className="input">
              <input
                type="text"
                placeholder="Nombre de usuario"
                value={nusuario}
                onChange={(e) => setNusuario(e.target.value)}
              />
            </div>
            <div className="input">
              <input
                type="text"
                placeholder="Nombres"
                value={nombres}
                onChange={(e) => setNombres(e.target.value)}
              />
            </div>
            <div className="input">
              <input
                type="text"
                placeholder="Apellidos"
                value={apellidos}
                onChange={(e) => setApellidos(e.target.value)}
              />
            </div>
            <div className="input">
              <input
                type="text"
                placeholder="Número de documento"
                value={ndocumento}
                onChange={(e) => setNdocumento(e.target.value)}
              />
            </div>
            <div className="input">
              <input
                type="email"
                placeholder="Correo electrónico"
                value={correo}
                onChange={(e) => setCorreo(e.target.value)}
              />
            </div>
            <div className="input">
              <input
                type="tel"
                placeholder="Teléfono"
                value={telefono}
                onChange={(e) => setTelefono(e.target.value)}
              />
            </div>
            <div className="input">
              <input
                type="password"
                placeholder="Contraseña"
                value={regPassword}
                onChange={(e) => setRegPassword(e.target.value)}
              />
            </div>
          </>
        )}
      </div>

      {isLogin && (
        <div className="forgot-password">
          ¿Olvidaste tu contraseña?<span> Click aquí</span>
        </div>
      )}

      <div className="submit-container">
        <div
          className="submit"
          onClick={() => {
            if (!isLogin) {
              handleRegister();
            } else {
              setIsLogin(false);
            }
          }}
        >
          Registrarse
        </div>
        <div
          className="submit"
          onClick={() => {
            if (isLogin) {
              handleLogin();
            } else {
              setIsLogin(true);
            }
          }}
        >
          Ingresar
        </div>
      </div>

      {message && <div className="message">{message}</div>}
    </div>
  );
};

export default LoginSignup;
