import React, { useState } from 'react';
import './ConsultaFinanciera.css';

const ConsultaFinanciera = () => {
  const [data, setData] = useState([]);
  const [mensaje, setMensaje] = useState('');
  const [loading, setLoading] = useState(false);

  const handleConsulta = async () => {
    const token = localStorage.getItem('token');

    if (!token) {
      setMensaje('❌ No estás autenticado. Inicia sesión.');
      setData([]);
      return;
    }

    setLoading(true);
    setMensaje('');
    setData([]);

    try {
      const res = await fetch('http://localhost:8000/Consulta/Consulta', {
        headers: {
          Authorization: `Bearer ${token}`
        }
      });

      const result = await res.json();

      if (res.ok) {
        setData(result);
      } else {
        setMensaje(result.detail || '❌ No se encontró información financiera.');
      }
    } catch (error) {
      console.error('Error al consultar datos:', error);
      setMensaje('⚠️ Error de conexión con el servidor');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="form-container">
      <h2>Consulta Financiera</h2>

      <button onClick={handleConsulta} disabled={loading} className="consulta-btn">
        {loading ? 'Consultando...' : 'Consultar Mis Datos'}
      </button>

      {mensaje && <div className="mensaje">{mensaje}</div>}

      {data.length > 0 && (
        <div className="resultado scrollable">
          <h3>Resumen Financiero</h3>
          {data.map((item, index) => (
            <div key={index} className="registro">
              <p><strong>Nombre:</strong> {item.nombre}</p>
              <p><strong>Documento:</strong> {item.documento}</p>
              <p><strong>Ingresos:</strong> ${item.vrIngresos}</p>
              <p><strong>Gastos:</strong> ${item.vrGastos}</p>
              <p><strong>Créditos:</strong> ${item.vrCredito}</p>
              <p><strong>Cuotas:</strong> {item.numCuotas}</p>
              <p><strong>Balance:</strong> ${item.balance}</p>
              <hr />
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default ConsultaFinanciera;
