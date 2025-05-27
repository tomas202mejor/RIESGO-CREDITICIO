import React, { useState, useEffect } from 'react';
import axios from "axios";
import Grafico from "../GraficoRiesgo/Grafico.jsx";
import { useNavigate } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import './ConsultarRiesgo.css';


const CreditRiskDashboard = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const handleLogout = () => {
    navigate('/'); 
  };
  const [userData, setUserData] = useState(null);
  const [data, setData] = useState([]);
  const [creditoData, setCreditoData] = useState([]);
  const [modeloData, setModeloData] = useState([]);
  const [correoData, setCorreoData] = useState({});
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
        setMensaje('No estás autenticado. Inicia sesión.');
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
          setMensaje(result.detail || 'No se encontró información financiera.');
        }
      } catch (error) {
        console.error('Error al consultar datos:', error);
        setMensaje('Error de conexión con el servidor');
      } finally {
        setLoading(false);
      }
    };

    const datosFinancieros = async () => {
      if (!token) {
        setMensaje('No estás autenticado. Inicia sesión.');
        setCreditoData([]);
        return;
      }

      setLoading(true);
      setMensaje('');
      setCreditoData([]);

      try {
        const res = await fetch(`http://localhost:8000/Consulta/ConsultaCredito/${id}`, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });


        const result = await res.json();

        if (res.ok) {
          setCreditoData(result);
        } else {
          setMensaje(result.detail || 'No se encontró información financiera.');
        }
      } catch (error) {
        console.error('Error al consultar datos:', error);
        setMensaje('Error de conexión con el servidor');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
    datosFinancieros();
  }, []);

  const formatCurrency = (value) => {
    return new Intl.NumberFormat('es-CO', {
      style: 'currency',
      currency: 'COP',
      minimumFractionDigits: 0
    }).format(value);
  };

  const evaluarCredito = async (item) => {
    const token = localStorage.getItem("token");

    try {
      const response = await fetch("http://localhost:8000/Modelo/evaluarCredito", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`
        },
        body: JSON.stringify({
          idCredito: item.id,
          ingresos: item.vrIngresos,
          gastos: item.vrGastos,
          credito: item.vrCredito,
          cuotas: item.numCuotas
        })
      });

      const result = await response.json();

      if (response.ok) {
        console.log("Respuesta del modelo:", result);
        setModeloData(result)
        setCreditoData((prevData) =>
        prevData.map((el) =>
          el.id === item.id
            ? {
                ...el,
                rentable: result.rentable,
                porcentAprobado: result.aprobado.toFixed(0),
                porcentRechazo: result.rechazado.toFixed(0),
                estado: 1
              }
            : el
        )
      );
      } else {
        console.error("Error:", result.detail || "No se pudo evaluar");
      }
    } catch (error) {
      console.error("Error al enviar datos al modelo:", error);
    }
  };

  const enviarResultado = async (item) => {
    const token = localStorage.getItem("token");
    try {
      const response = await fetch("http://localhost:8000/send/sendScoring", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`
        },
        body: JSON.stringify({
          nombre: item.nombre,
          documento: item.documento,
          correo: userData.email,
          credito: item.vrCredito,
          cuotas: item.numCuotas,
          resultado: item.rentable,
          porcentajeAprobado: item.porcentAprobado,
          porcentajeRechazo: item.porcentRechazo
        })
      });

      const result = await response.json();

      if (response.ok) {
        setCorreoData(prev => ({
          ...prev,
          [item.id]: result.message
        }));
        console.log("Respuesta del correo:", result);
      } else {
        console.error("Error:", result.detail || "No se pudo enviar correo");
      }
    } catch (error) {
      console.error("Error al enviar datos para correo:", error);
    }
  };
  

  return (

    <div className="credit-risk-dashboard">
      <nav className="navbar">
        
        <ul className="navbar-menu"> </ul>
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
            <h3>Datos Crediticios</h3>
            <div className="info-grid">
            {creditoData.map((item, index) => (
              <React.Fragment key={index}>
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
                </div>
              </React.Fragment>
            ))}
          </div>
          </div>
        </div>

        <div className="recommendation-section">
          <h2>Procesamiento del Crédito</h2>
          <div className="recommendation-card">
            {creditoData.map((item, index) => (
                <React.Fragment key={index}>
                  <div>
                    <h3>Estado: {item.estado == 0?'Pendiente':'Procesado'}</h3>
                    {item.rentable != null ? (
                      <h3>Decisión: {item.rentable == 1?'APROBADO':'RECHAZADO'}</h3>
                    ) : (
                      <h3>Decisión: Sin Procesar</h3>
                    )}
                    {item.porcentAprobado != null && item.porcentRechazo != null && (
                        <Grafico
                          aprobado={item.porcentAprobado}
                          rechazado={item.porcentRechazo}
                        />
                      )}
                    <div className="ml-metrics">
                      <div>
                        <label><strong>Porcentaje de Aprovado: </strong></label>
                        <span>{item.porcentAprobado != null?item.porcentAprobado:''}%</span>
                      </div>
                      <div>
                        <label><strong>Porcentaje de Rechazo: </strong> </label>
                        <span>{item.porcentRechazo != null?item.porcentRechazo:''}%</span>
                      </div>
                      <div style={{display: 'inline-block', width:'100%'}}>
                        <label><strong>Respuesta del Modelo: </strong> </label>
                        {item.rentable != null ? (
                          <span style={{ display: 'block', width: '100%'}}>{item.rentable == 1?'Su solicitud de crédito es rentable, ha sido aprobada':'Su solicitud de crédito no es rentable, ha sido rechazada'}</span>
                        ) : (
                          <span></span>
                        )}
                      </div>
                    </div>
                  </div></React.Fragment>
              ))}
            <div className="ml-connection">
            {creditoData.map((item,index) => (
              <React.Fragment key={index}>
                {item.estado == 0 ? (
                  <button onClick={(e) => evaluarCredito(item)}>Evaluar crédito</button>
                ) : (
                  <button onClick={() => enviarResultado(item)} style={{backgroundColor:'green'}}>Enviar Resultado</button>
                )}
                {correoData[item.id] && (
                  <span style={{ display: 'block', width: '100%', marginTop: '2px'}}>{correoData[item.id]}</span>
                )}
              </React.Fragment>
            ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CreditRiskDashboard;