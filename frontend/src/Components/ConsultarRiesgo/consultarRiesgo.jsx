import React, { useState, useEffect } from 'react';
import axios from "axios";
import { useNavigate } from 'react-router-dom';
import './ConsultarRiesgo.css';

const CreditRiskDashboard = () => {
  const navigate = useNavigate();
  const handleLogout = () => {
    // Aquí puedes agregar cualquier lógica adicional de cierre de sesión (como limpiar el estado, cookies, etc.)
    navigate('/'); // Redirige al login
  };
  const [userData, setUserData] = useState(null);
  const [data, setData] = useState([]);
  const [mensaje, setMensaje] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem("token");

    // Obtener datos del usuario
    axios.get("http://localhost:8000/usuario/me", {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
      .then(response => {
        setUserData(response.data);
      })
      .catch(error => {
        console.error("Error al obtener datos del usuario:", error);
      });

    // Función para hacer la consulta automáticamente
    const fetchData = async () => {
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

    fetchData();
  }, []);

  const formatCurrency = (value) => {
    return new Intl.NumberFormat('es-CO', {
      style: 'currency',
      currency: 'COP',
      minimumFractionDigits: 0
    }).format(value);
  };

  return (

    <div className="credit-risk-dashboard">
      <nav className="navbar">
        <div className="navbar-logo" onClick={() => navigate('/Menu')}>Gestión de Riesgos</div>
        <ul className="navbar-menu">
          <li><a href="#">Perfil</a></li>
          <li className="logout"><a href="#" onClick={handleLogout}>Cerrar sesión</a></li>
        </ul>
      </nav>

      <div className="dashboard-content">
        <div className="client-section">
          <h2>Datos del Cliente</h2>
          <div className="info-card">
            <h3>Información Básica</h3>
            <div className="info-grid">
              {userData && (
                <><div>
                  <label>Usuario:</label>
                  <span>{userData.username}</span>
                </div><div>
                    <label>Nombre:</label>
                    <span>{userData.nombre}</span>
                  </div><div>
                    <label>Identificación:</label>
                    <span>{userData.Ndocumento}</span>
                  </div><div>
                    <label>Contacto:</label>
                    <span>{userData.email} | {userData.telefono}</span>
                  </div></>
              )}
            </div>
          </div>

          <div className="info-card">
            <h3>Historial Crediticio</h3>
            <div className="info-grid">
              {data.map((item) => (
                <>
                  <div>
                    <label>Ingresos:</label>
                    <span>{formatCurrency(item.vrIngresos)}</span>
                  </div>
                  <div>
                    <label>Gastos:</label>
                    <span>{formatCurrency(item.vrGastos)}</span>
                  </div>
                  <div>
                    <label>Crédito:</label>
                    <span>{formatCurrency(item.vrCredito)}</span>
                  </div>
                  <div>
                    <label>Cuotas:</label>
                    <span>{item.numCuotas}</span>
                  </div></>
              ))}
            </div>
          </div>
        </div>

        <div className="recommendation-section">
          <h2>Recomendación Automatizada</h2>
          <div className="recommendation-card">
            <h3>Decisión: APROBADO</h3>
            <div className="ml-metrics">
              <div>
                <label>Límite de Crédito:</label>
                <span>$</span>
              </div>
              <div>
                <label>Tasa de Interés:</label>
                <span>%</span>
              </div>
              <div>
                <label>Confianza del Modelo:</label>
                <span>%</span>
              </div>
            </div>
            <div className="ml-connection">
              <button onClick={() => connectToMLModel(clientData)}>
                Evaluar con ML
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CreditRiskDashboard;