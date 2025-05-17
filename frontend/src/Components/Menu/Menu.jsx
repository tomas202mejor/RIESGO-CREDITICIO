import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Menu.css';

const Menu = () => {
  const navigate = useNavigate();
  const [menuOpen, setMenuOpen] = useState(false);

  const handleLogout = () => {
    navigate('/');
  };

  const toggleMenu = () => {
    setMenuOpen(!menuOpen);
  };

  const closeMenu = () => {
    setMenuOpen(false);
  };

  return (
    <>
      <nav className="navbar">
        <div className="navbar-logo">Gestión de Riesgos</div>

        {/* Botón hamburguesa */}
        <div className="navbar-toggle" onClick={toggleMenu}>
          ☰
        </div>

        <ul className={`navbar-menu ${menuOpen ? 'active' : ''}`}>
          <li>
            <a
              href="#"
              onClick={(e) => {
                e.preventDefault();
                navigate('/Profile');
                closeMenu();
              }}
            >
              Perfil
            </a>
          </li>
          <li className="logout">
            <a
              href="#"
              onClick={(e) => {
                e.preventDefault();
                handleLogout();
                closeMenu();
              }}
            >
              Cerrar sesión
            </a>
          </li>
        </ul>
      </nav>

      {/* Panel de control permanece intacto */}
      <div className="dashboard-container">
        <h1 className="dashboard-title">Panel de Control</h1>
        <div className="dashboard-buttons">
          <button className="dashboard-btn" onClick={() => navigate('/RegisterData')}>
            Gestión de Solicitudes
          </button>
          <button className="dashboard-btn">Análisis de Riesgo</button>
          <button className="dashboard-btn" onClick={() => navigate('/finanzas/me')}>
            Reportes y Estadísticas
          </button>
        </div>
      </div>
    </>
  );
};

export default Menu;
