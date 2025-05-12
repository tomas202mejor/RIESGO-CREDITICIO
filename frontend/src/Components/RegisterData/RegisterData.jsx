import React, { useState } from 'react';
import './RegisterData.css';

const RegisterData = () => {
  const [form, setForm] = useState({
    nombre: '',
    documento: '',
    correo: '',
    vrIngresos: '',
    vrGastos: '',
    vrCredito: '',
    numCuotas: ''
  });

  const [mensaje, setMensaje] = useState('');

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async () => {
    const { nombre, documento, correo, vrIngresos, vrGastos, vrCredito, numCuotas } = form;

    if (!nombre || !documento || !correo || !vrIngresos || !vrGastos || !vrCredito || !numCuotas) {
      setMensaje('⚠️ Por favor completa todos los campos.');
      return;
    }

    const token = localStorage.getItem('token');
    if (!token) {
      setMensaje('⚠️ No se encontró el token de autenticación.');
      return;
    }

    try {
      const body = {
        nombre,
        documento,  // Enviar como cadena, sin convertir a número
        correo,
        vrIngresos: parseFloat(vrIngresos),
        vrGastos: parseFloat(vrGastos),
        vrCredito: parseFloat(vrCredito),
        numCuotas: parseInt(numCuotas)
      };

      const res = await fetch('http://localhost:8000/finanzas/guardarDatosFinac', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify(body)
      });

      const data = await res.json();

      if (res.ok && data.idResp === "0") {
        setMensaje('✅ ' + data.msg);
      } else {
        setMensaje('❌ Ocurrió un error: ' + (data.msg || data.detail || 'Error desconocido.'));
        console.log(data);  // Aquí puedes ver más detalles del error
      }

    } catch (error) {
      console.error('Error al enviar los datos:', error);
      setMensaje('⚠️ Error de conexión con el servidor o formato incorrecto');
    }
  };

  return (
    <div className="form-container">
      <h2>Registrar Datos Financieros</h2>
      <input name="nombre" placeholder="Nombre" value={form.nombre} onChange={handleChange} />
      <input name="documento" placeholder="Documento" type="number" value={form.documento} onChange={handleChange} />
      <input name="correo" placeholder="Correo" type="email" value={form.correo} onChange={handleChange} />
      <input name="vrIngresos" placeholder="Ingresos" type="number" step="0.01" value={form.vrIngresos} onChange={handleChange} />
      <input name="vrGastos" placeholder="Gastos" type="number" step="0.01" value={form.vrGastos} onChange={handleChange} />
      <input name="vrCredito" placeholder="Crédito Solicitado" type="number" step="0.01" value={form.vrCredito} onChange={handleChange} />
      <input name="numCuotas" placeholder="Número de Cuotas" type="number" value={form.numCuotas} onChange={handleChange} />
      <button onClick={handleSubmit}>Registrar</button>
      {mensaje && <p className="mensaje">{mensaje}</p>}
    </div>
  );
};

export default RegisterData;  // Asegúrate de tener esta línea al final
