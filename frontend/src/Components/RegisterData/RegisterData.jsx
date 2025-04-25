import React, { useState } from 'react';
import './RegisterData.css';

const RegisterData = () => {
  const [documento, setDocumento] = useState('');
  const [correo, setCorreo] = useState('');
  const [vrIngresos, setVrIngresos] = useState('');
  const [vrGastos, setVrGastos] = useState('');
  const [vrCredito, setVrCredito] = useState('');
  const [numCuotas, setNumCuotas] = useState('');
  const [nombre, setNombre] = useState(''); // Agregado para enviar "nombre"
  const [mensaje, setMensaje] = useState('');

  const handleSubmit = async () => {
    if (!nombre || !documento || !correo || !vrIngresos || !vrGastos || !vrCredito || !numCuotas) {
      setMensaje('⚠️ Por favor completa todos los campos.');
      return;
    }

    try {
      const res = await fetch('http://localhost:8003/guardarDatosFinac', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          nombre,
          documento: parseInt(documento),
          correo,
          vrIngresos: parseFloat(vrIngresos),
          vrGastos: parseFloat(vrGastos),
          vrCredito: parseFloat(vrCredito),
          numCuotas: parseInt(numCuotas)
        })
      });

      const data = await res.json();
      if (data.idResp === "0") {
        setMensaje('✅ ' + data.msg);
      } else {
        setMensaje('❌ Ocurrió un error: ' + (data.msg || data.error));
      }
    } catch (error) {
      console.error('Error al enviar los datos:', error);
      setMensaje('⚠️ Error de conexión con el servidor');
    }
  };

  return (
    <div className="container">
      <div className="welcome-message">
        <h3>Bienvenido, por favor ingrese los datos para realizar su gestión de riesgo</h3>
      </div>

      <div className="inputs">
        <div className="input">
          <input type="text" placeholder="Nombre completo" value={nombre} onChange={(e) => setNombre(e.target.value)} />
        </div>
        <div className="input">
          <input type="number" placeholder="Número de documento" value={documento} onChange={(e) => setDocumento(e.target.value)} />
        </div>
        <div className="input">
          <input type="email" placeholder="Correo electrónico" value={correo} onChange={(e) => setCorreo(e.target.value)} />
        </div>
        <div className="input">
          <input type="number" placeholder="Valor de los ingresos" value={vrIngresos} onChange={(e) => setVrIngresos(e.target.value)} />
        </div>
        <div className="input">
          <input type="number" placeholder="Valor de los gastos" value={vrGastos} onChange={(e) => setVrGastos(e.target.value)} />
        </div>
        <div className="input">
          <input type="number" placeholder="Valor del crédito a solicitar" value={vrCredito} onChange={(e) => setVrCredito(e.target.value)} />
        </div>
        <div className="input">
          <input type="number" placeholder="Número de cuotas" value={numCuotas} onChange={(e) => setNumCuotas(e.target.value)} />
        </div>
      </div>

      <div className="button-register">
        <button className="register" onClick={handleSubmit}>Registrar</button>
      </div>

      {mensaje && <div className="message">{mensaje}</div>}
    </div>
  );
};

export default RegisterData;
