import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; 
import './OlvidoContraseña.css';

const ResetPasswordPopup = ({ onClose }) => {
  const [codigo, setCodigo] = useState('');
  const [nuevaClave, setNuevaClave] = useState('');
  const [message, setMessage] = useState('');
  const navigate = useNavigate();  // <--- Aquí faltaba definir navigate

  const handleSubmit = async () => {
    if (!codigo || !nuevaClave) {
      setMessage('⚠️ Completa todos los campos.');
      return;
    }

    try {
      const res = await fetch('http://localhost:8000/auth/reset', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ codigo, nueva_password: nuevaClave }),
      });

      if (res.ok) {
        setMessage('✅ Contraseña cambiada con éxito.');
        setTimeout(() => {
          setMessage('');
          onClose();
        }, 2000);
      } else {
        const data = await res.json();
        setMessage(`❌ Error: ${data.detail || 'No se pudo cambiar la contraseña.'}`);
      }
    } catch (error) {
      setMessage('⚠️ Error de conexión con el servidor.');
    }
  };

  return (
    <div className="popup-overlay">
      <div className="popup">
        <h2>Restablecer Contraseña</h2>
        <input
          type="text"
          placeholder="Código de verificación"
          value={codigo}
          onChange={(e) => setCodigo(e.target.value)}
        />
        <input
          type="password"
          placeholder="Nueva contraseña"
          value={nuevaClave}
          onChange={(e) => setNuevaClave(e.target.value)}
        />
        <button className="register" onClick={handleSubmit}>
          Cambiar contraseña
        </button>
        <button
          className="register"
          style={{ marginLeft: '10px' }}
          onClick={() => navigate('/')}
        >
          ← Regresar
        </button>

        {message && <p>{message}</p>}
      </div>
    </div>
  );
};

const OlvidoContraseña = () => {
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');
  const [showResetPopup, setShowResetPopup] = useState(false);
  const navigate = useNavigate();

  const handleReset = async () => {
    if (!email) {
      setMessage('⚠️ Por favor ingresa tu correo.');
      return;
    }

    try {
      const res = await fetch('http://localhost:8000/auth/recuperar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email }),
      });

      if (res.ok) {
        setMessage('✅ Si el correo existe, se enviará un enlace o código de recuperación.');
        setShowResetPopup(true);
      } else {
        setMessage('❌ No se pudo procesar la solicitud.');
      }
    } catch (error) {
      console.error('Error:', error);
      setMessage('⚠️ Error de conexión con el servidor.');
    }
  };

  return (
    <div className="container">
      <div className="header">
        <div className="text">Recuperar contraseña</div>
        <div className="underline"></div>
      </div>

      <div className="inputs">
        <div className="input">
          <input
            type="email"
            placeholder="Ingresa tu correo registrado"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            disabled={showResetPopup}
          />
        </div>
      </div>

      <div className="submit-container">
        <div
          className="submit"
          onClick={handleReset}
          style={{ pointerEvents: showResetPopup ? 'none' : 'auto' }}
        >
          Enviar
        </div>
        <button
          className="register"
          style={{ marginLeft: '15px' }}
          onClick={() => navigate('/')}
        >
          ← Regresar
        </button>
      </div>

      {message && <div className="message">{message}</div>}

      {showResetPopup && (
        <ResetPasswordPopup onClose={() => setShowResetPopup(false)} />
      )}
    </div>
  );
};

export default OlvidoContraseña;