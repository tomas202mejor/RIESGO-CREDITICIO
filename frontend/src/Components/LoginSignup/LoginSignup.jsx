import React, { useState } from 'react';
import './LoginSignup.css';
import { useNavigate } from 'react-router-dom';

const LoginSignup = () => {
  const navigate = useNavigate();
  const [isLogin, setIsLogin] = useState(true);
  const [message, setMessage] = useState('');

  const [user, setUser] = useState('');
  const [password, setPassword] = useState('');

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
      const res = await fetch('http://localhost:8000/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ Correo: user, password })
      });

      const data = await res.json();

      if (res.ok) {
        localStorage.setItem('token', data.access_token); // Guardar token
        setMessage('✅ Inicio de sesión correcto');
        navigate('/Menu'); // Ir al menú principal
      } else {
        setMessage('❌ Usuario o contraseña incorrectos');
      }
    } catch (error) {
      console.error('Error de conexión:', error);
      setMessage('⚠️ Error de conexión con el servidor');
    }
  };

  const handleRegister = async () => {
    if (!nusuario || !nombres || !apellidos || !ndocumento || !correo || !telefono || !regPassword) {
      setMessage('⚠️ Por favor completa todos los campos del formulario de registro.');
      return;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(correo)) {
      setMessage('⚠️ Por favor ingresa un correo electrónico válido.');
      return;
    }

    try {
      const res = await fetch('http://localhost:8000/users/registro', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          Nusuario: nusuario,
          nombre: nombres,
          apellido: apellidos,
          Ndocumento: ndocumento,
          email: correo,
          telefono,
          password: regPassword
        })
      });

      const data = await res.json();

      if (res.ok && data && data.id) {
        setMessage('✅ Registro exitoso');
        setIsLogin(true);
      } else {
        setMessage('❌ Error desconocido');
      }
    } catch (error) {
      console.error('Error en el registro:', error);
      setMessage('⚠️ Error de conexión con el servidor');
    }
  };

  const handleSubmit = () => {
    isLogin ? handleLogin() : handleRegister();
  };

  const handleModeSwitch = () => {
    setIsLogin(!isLogin);
    setMessage('');
    setUser('');
    setPassword('');
    setNusuario('');
    setNombres('');
    setApellidos('');
    setNdocumento('');
    setCorreo('');
    setTelefono('');
    setRegPassword('');
  };

  return (
    <div className="container">
      <div className="header">
        <div className="text">{isLogin ? 'Ingresar' : 'Registrarse'}</div>
        <div className="underline"></div>
      </div>

      <div className="inputs">
        {!isLogin && (
          <>
            <div className="input"><input type="text" placeholder="Usuario" value={nusuario} onChange={(e) => setNusuario(e.target.value)} /></div>
            <div className="input"><input type="text" placeholder="Nombres" value={nombres} onChange={(e) => setNombres(e.target.value)} /></div>
            <div className="input"><input type="text" placeholder="Apellidos" value={apellidos} onChange={(e) => setApellidos(e.target.value)} /></div>
            <div className="input"><input type="text" placeholder="Documento" value={ndocumento} onChange={(e) => setNdocumento(e.target.value)} /></div>
            <div className="input"><input type="email" placeholder="Correo" value={correo} onChange={(e) => setCorreo(e.target.value)} /></div>
            <div className="input"><input type="tel" placeholder="Teléfono" value={telefono} onChange={(e) => setTelefono(e.target.value)} /></div>
            <div className="input"><input type="password" placeholder="Contraseña" value={regPassword} onChange={(e) => setRegPassword(e.target.value)} /></div>
          </>
        )}

        {isLogin && (
          <>
            <div className="input"><input type="email" placeholder="Correo" value={user} onChange={(e) => setUser(e.target.value)} /></div>
            <div className="input"><input type="password" placeholder="Contraseña" value={password} onChange={(e) => setPassword(e.target.value)} /></div>
          </>
        )}
      </div>

      <div className="submit-container">
        <div className="submit" onClick={handleSubmit}>{isLogin ? 'Ingresar' : 'Registrar'}</div>
        <div className="toggle-mode" onClick={handleModeSwitch}>
          {isLogin ? '¿No tienes cuenta? Regístrate' : '¿Ya tienes cuenta? Inicia sesión'}
        </div>
      </div>

      {message && <div className="message">{message}</div>}
    </div>
  );
};

export default LoginSignup;
