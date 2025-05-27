import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Menu.css';
import '../Menu/Profile.css';
import Profile from './Profile';
import ConsultaFinanciera from './ConsultaFinanciera';
import ConsultarRiesgo from './consultarRiesgo';
import RegisterData from './RegisterData';


const Menu = () => {
  const navigate = useNavigate();
  const [menuOpen, setMenuOpen] = useState(false);
  const [activeSection, setActiveSection] = useState(null);

  const handleLogout = () => {
    navigate('/');
  };

  const toggleMenu = () => {
    setMenuOpen(!menuOpen);
  };

  return (
    <div className="dashboard-wrapper">
      <aside className="sidebar">
        <div className="sidebar-logo">Gestión de Riesgos</div>
        <ul className="sidebar-menu">
          <li onClick={() => setActiveSection('perfil')}>Perfil</li>
          <li onClick={() => setActiveSection('solicitudes')}>Gestión de Solicitudes</li>
       
          <li onClick={() => setActiveSection('reportes')}>Reportes y Estadísticas</li>
          <li className="logout" onClick={handleLogout}>Cerrar sesión</li>
        </ul>
      </aside>

      <main className="main-panel">
    

        <div className="dashboard-container">
          <h1 className="dashboard-title">Panel de Control</h1>

          {activeSection === 'perfil' && <Profile />}
          {activeSection === 'solicitudes' && <RegisterData />}
          {activeSection === 'riesgo' && <ConsultarRiesgo />}
          {activeSection === 'reportes' && <ConsultaFinanciera />}
          {!activeSection && <p>Selecciona una opción del menú izquierdo.</p>}
        </div>
      </main>
    </div>
  );
};

export default Menu;
