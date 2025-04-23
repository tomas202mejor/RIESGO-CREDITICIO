import React, { useState } from 'react';

function App() {
  const [user, setUser] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleLogin = async () => {
    try {
      // Enviar la petición al servidor FastAPI
      const res = await fetch('http://localhost:8000/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ Correo: user, password: password })
      });

      const data = await res.json();

      // Verificar si el login fue exitoso
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

  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial' }}>
      <h2>Login</h2>
      <input
        type="email"
        placeholder="Correo electrónico"
        value={user}
        onChange={e => setUser(e.target.value)}
      /><br /><br />
      <input
        type="password"
        placeholder="Contraseña"
        value={password}
        onChange={e => setPassword(e.target.value)}
      /><br /><br />
      <button onClick={handleLogin}>Iniciar sesión</button>
      {message && <p>{message}</p>}
    </div>
  );
}

export default App;
