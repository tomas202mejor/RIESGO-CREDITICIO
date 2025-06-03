import React, { useState, useEffect } from 'react';
import axios from 'axios';
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
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      setMensaje('No autenticado, inicia sesión.');
      return;
    }

    axios.get('http://localhost:8000/usuario/me', {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
    .then(response => {
      const data = response.data;
      setForm(prevForm => ({
        ...prevForm,
        nombre: data.nombre || '',
        documento: data.Ndocumento || '',
        correo: data.email || ''
      }));
      setMensaje('');
    })
    .catch(error => {
      console.error('Error al obtener datos del usuario:', error);
      setMensaje('Error al obtener datos del usuario.');
    });
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;

    // No permitir editar estos campos
    if (['nombre', 'documento', 'correo'].includes(name)) return;

    setForm(prevForm => ({
      ...prevForm,
      [name]: value
    }));
  };

  const handleSubmit = async () => {
    const { nombre, documento, correo, vrIngresos, vrGastos, vrCredito, numCuotas } = form;

    if (!nombre || !documento || !correo || !vrIngresos || !vrGastos || !vrCredito || !numCuotas) {
      setMensaje('Por favor completa todos los campos.');
      return;
    }

        // Validación para evitar números negativos
    if (
      parseFloat(vrIngresos) < 0 ||
      parseFloat(vrGastos) < 0 ||
      parseFloat(vrCredito) < 0 ||
      parseInt(numCuotas) < 0
    ) {
      setMensaje('⚠️ Los valores numéricos no pueden ser negativos.');
      return;
    }

    const token = localStorage.getItem('token');
    if (!token) {
      setMensaje('No se encontró el token de autenticación.');
      return;
    }

    setLoading(true);
    setMensaje('');

    try {
      const body = {
        nombre,
        documento,
        correo,
        vrIngresos: parseFloat(vrIngresos),
        vrGastos: parseFloat(vrGastos),
        vrCredito: parseFloat(vrCredito),
        numCuotas: parseInt(numCuotas)
      };

      const res = await axios.post('http://localhost:8000/finanzas/guardarDatosFinac', body, {
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`
        }
      });

      if (res.status === 200 && res.data.idResp === "0") {
        setMensaje('✅ ' + res.data.msg);
      } else {
        setMensaje('Ocurrió un error: ' + (res.data.msg || res.data.detail || 'Error desconocido.'));
      }
    } catch (error) {
      console.error('Error al enviar los datos:', error);
      setMensaje('⚠️ Error de conexión con el servidor o formato incorrecto');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="form-container">
      <h2>Registrar Datos Financieros</h2>
      

      <div className="inputs">
        <input name="nombre" placeholder="Nombre" value={form.nombre} readOnly />
        <input name="documento" placeholder="Documento" type="text" value={form.documento} readOnly />
        <input name="correo" placeholder="Correo" type="email" value={form.correo} readOnly />

        <input name="vrIngresos" placeholder="Ingresos" type="number" step="0.01" value={form.vrIngresos} onChange={handleChange} />
        <input name="vrGastos" placeholder="Gastos" type="number" step="0.01" value={form.vrGastos} onChange={handleChange} />
        <input name="vrCredito" placeholder="Crédito Solicitado" type="number" step="0.01" value={form.vrCredito} onChange={handleChange} />
        <input name="numCuotas" placeholder="Número de Cuotas" type="number" value={form.numCuotas} onChange={handleChange} />
      </div>

      <div className="button-register">
        <button className="register" onClick={handleSubmit} disabled={loading}>
          {loading ? 'Registrando...' : 'Registrar'}
        </button>
      </div>

      {mensaje && <p className="mensaje">{mensaje}</p>}
    </div>
  );
};

export default RegisterData;
