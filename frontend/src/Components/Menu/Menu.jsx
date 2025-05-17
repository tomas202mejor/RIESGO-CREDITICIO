import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Menu.css';

const Menu = () => {
  const navigate = useNavigate();

  const handleLogout = () => {
    // Aquí puedes agregar cualquier lógica adicional de cierre de sesión (como limpiar el estado, cookies, etc.)
    navigate('/'); // Redirige al login
  };

  return (
    <>
      {/* Barra de navegación superior */}
      <nav className="navbar">
        <div className="navbar-logo">Gestión de Riesgos</div>
        <ul className="navbar-menu">
          <li><a href="#">Perfil</a></li>
          <li className="logout"><a href="#" onClick={handleLogout}>Cerrar sesión</a></li>
        </ul>
      </nav>

      {/* Panel de control con botones grandes */}
      <div className="dashboard-container">
        <h1 className="dashboard-title">Panel de Control</h1>
        <div className="dashboard-buttons">
          <button className="dashboard-btn" onClick={() => navigate('/RegisterData')}>
            Gestión de Solicitudes
          </button>
<<<<<<< HEAD
          <button className="dashboard-btn" onClick={() => navigate('/ConsultarRiesgo')}>Análisis de Riesgo</button>
          <button className="dashboard-btn">Reportes y Estadísticas</button>
=======
          <button className="dashboard-btn">Análisis de Riesgo</button>
          <button className="dashboard-btn" onClick={() => navigate('/finanzas/me')}>
            Reportes y Estadísticas
          </button>
>>>>>>> 9667c03d8008c7ceb3a45ed06e419c8191661515
        </div>
      </div>
    </>
  );
};

export default Menu;
