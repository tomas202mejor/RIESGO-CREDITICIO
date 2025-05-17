import React, { useState, useEffect } from 'react';

import { useNavigate } from 'react-router-dom';
import './ConsultarRiesgo.css';

const CreditRiskDashboard = () => {
  const navigate = useNavigate();
    const handleLogout = () => {
        // Aquí puedes agregar cualquier lógica adicional de cierre de sesión (como limpiar el estado, cookies, etc.)
        navigate('/'); // Redirige al login
      };
  // Estado para los datos del cliente
  const [clientData, setClientData] = useState({
    basicInfo: {
      name: 'Juan Pérez',
      id: '10',
      age: 35,
      maritalStatus: 'Casado',
      contact: 'juan.perez@email.com | 0991234567'
    },
    creditHistory: {
      score: 720,
        riskLevel: 'A',
        maxDelinquency: 'Nunca',
        activeCredits: 2,
        recentInquiries: 3
    },
    financialCapacity: {
      monthlyIncome: 4500,
        fixedExpenses: 1800,
        debtRatio: 0.4,
        assets: 125000
    },
    bankingBehavior: {
      bankingHistory: '5 años',
      averageBalance: 3200,
      unusualMovements: false,
      products: ['Cuenta Corriente', 'Tarjeta Platinum']
    },
    alerts: ['Sin reportes']
  });

  // Estado para la recomendación de ML
  const [mlRecommendation, setMlRecommendation] = useState({
    decision: 'APROBADO',
      creditLimit: 15000,
      interestRate: 12.5,
      confidence: 0.87
  });

  // Estado para la UI
  const [loading, setLoading] = useState(false);
  const [searchId, setSearchId] = useState('');

  // Simulación de conexión a API/ML
  const fetchCreditRiskData = async (clientId) => {
    setLoading(true);
    
    // Simulamos un delay de API
    await new Promise(resolve => setTimeout(resolve, 1500));
    
    // Datos simulados - en producción esto vendría de tu backend/ML
    const mockData = {
      basicInfo: {
        name: 'Juan Pérez',
        id: clientId,
        age: 35,
        maritalStatus: 'Casado',
        contact: 'juan.perez@email.com | 0991234567'
      },
      creditHistory: {
        score: 720,
        riskLevel: 'A',
        maxDelinquency: 'Nunca',
        activeCredits: 2,
        recentInquiries: 3
      },
      financialCapacity: {
        monthlyIncome: 4500,
        fixedExpenses: 1800,
        debtRatio: 0.4,
        assets: 125000
      },
      bankingBehavior: {
        bankingHistory: '5 años',
        averageBalance: 3200,
        unusualMovements: false,
        products: ['Cuenta Corriente', 'Tarjeta Platinum']
      },
      alerts: ['Sin reportes negativos']
    };

    // Simulación de respuesta del modelo ML
    const mockMLResponse = {
      decision: 'APROBADO',
      creditLimit: 15000,
      interestRate: 12.5,
      confidence: 0.87
    };

    setClientData(mockData);
    setMlRecommendation(mockMLResponse);
    setLoading(false);
  };


  // Función para conectar con el modelo ML real
  const connectToMLModel = async (clientData) => {
    // En una implementación real, aquí harías:
    // const response = await fetch('https://tu-api-ml.com/predict', {
    //   method: 'POST',
    //   headers: { 'Content-Type': 'application/json' },
    //   body: JSON.stringify(clientData)
    // });
    // const result = await response.json();
    // return result;
    
    console.log('Enviando datos al modelo ML:', clientData);
    return mlRecommendation; // Usamos los datos mock por ahora
  };

  const handleSearch = () => {
    if (searchId) {
      fetchCreditRiskData(searchId);
    }
  };

  const getRiskColor = (riskLevel) => {
    switch (riskLevel) {
      case 'A': return '#4CAF50'; // Verde
      case 'B': return '#FFC107'; // Amarillo
      case 'C': return '#FF9800'; // Naranja
      case 'D': return '#F44336'; // Rojo
      default: return '#9E9E9E'; // Gris
    }
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
                <div>
                  <label>Nombre:</label>
                  <span>{clientData.basicInfo.name}</span>
                </div>
                <div>
                  <label>Identificación:</label>
                  <span>{clientData.basicInfo.id}</span>
                </div>
                <div>
                  <label>Edad:</label>
                  <span>{clientData.basicInfo.age}</span>
                </div>
                <div>
                  <label>Estado Civil:</label>
                  <span>{clientData.basicInfo.maritalStatus}</span>
                </div>
                <div>
                  <label>Contacto:</label>
                  <span>{clientData.basicInfo.contact}</span>
                </div>
              </div>
            </div>

            <div className="info-card">
              <h3>Historial Crediticio</h3>
              <div className="info-grid">
                <div>
                  <label>Score Crediticio:</label>
                  <span>{clientData.creditHistory.score}</span>
                </div>
                <div>
                  <label>Nivel de Riesgo:</label>
                  <span style={{ color: getRiskColor(clientData.creditHistory.riskLevel) }}>
                    {clientData.creditHistory.riskLevel}
                  </span>
                </div>
                <div>
                  <label>Mora Máxima:</label>
                  <span>{clientData.creditHistory.maxDelinquency}</span>
                </div>
                <div>
                  <label>Créditos Activos:</label>
                  <span>{clientData.creditHistory.activeCredits}</span>
                </div>
                <div>
                  <label>Consultas Recientes:</label>
                  <span>{clientData.creditHistory.recentInquiries}</span>
                </div>
              </div>
            </div>

            <div className="info-card">
              <h3>Capacidad Financiera</h3>
              <div className="info-grid">
                <div>
                  <label>Ingresos Mensuales:</label>
                  <span>${clientData.financialCapacity.monthlyIncome.toLocaleString()}</span>
                </div>
                <div>
                  <label>Gastos Fijos:</label>
                  <span>${clientData.financialCapacity.fixedExpenses.toLocaleString()}</span>
                </div>
                <div>
                  <label>Ratio Endeudamiento:</label>
                  <span>{clientData.financialCapacity.debtRatio.toFixed(2)}</span>
                </div>
                <div>
                  <label>Patrimonio:</label>
                  <span>${clientData.financialCapacity.assets.toLocaleString()}</span>
                </div>
              </div>
            </div>

            <div className="info-card">
              <h3>Comportamiento Bancario</h3>
              <div className="info-grid">
                <div>
                  <label>Antigüedad:</label>
                  <span>{clientData.bankingBehavior.bankingHistory}</span>
                </div>
                <div>
                  <label>Saldo Promedio:</label>
                  <span>${clientData.bankingBehavior.averageBalance.toLocaleString()}</span>
                </div>
                <div>
                  <label>Movimientos Atípicos:</label>
                  <span>{clientData.bankingBehavior.unusualMovements ? 'Sí' : 'No'}</span>
                </div>
                <div>
                  <label>Productos:</label>
                  <span>{clientData.bankingBehavior.products.join(', ')}</span>
                </div>
              </div>
            </div>

           {clientData.alerts.length > 0 && (
              <div className="info-card alerts">
                <h3>Alertas</h3>
                <ul>
                  {clientData.alerts.map((alert, index) => (
                    <li key={index}>{alert}</li>
                  ))}
                </ul>
              </div>
            )}
          </div>

          <div className="recommendation-section">
            <h2>Recomendación Automatizada</h2>
            <div className={`recommendation-card ${mlRecommendation.decision.toLowerCase()}`}>
              <h3>Decisión: {mlRecommendation.decision}</h3>
              <div className="ml-metrics">
                <div>
                  <label>Límite de Crédito:</label>
                  <span>${mlRecommendation.creditLimit.toLocaleString()}</span>
                </div>
                <div>
                  <label>Tasa de Interés:</label>
                  <span>{mlRecommendation.interestRate}%</span>
                </div>
                <div>
                  <label>Confianza del Modelo:</label>
                  <span>{(mlRecommendation.confidence * 100).toFixed(1)}%</span>
                </div>
              </div>
              <div className="ml-connection">
                <p>Datos enviados al modelo de Machine Learning:</p>
                <pre>{JSON.stringify(clientData, null, 2)}</pre>
                <button onClick={() => connectToMLModel(clientData)}>
                  Re-evaluar con ML
                </button>
              </div>
            </div>
          </div>
        </div>
    </div>
  );
};

export default CreditRiskDashboard;