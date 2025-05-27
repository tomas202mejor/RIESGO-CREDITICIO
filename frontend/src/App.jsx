import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginSignup from './Components/LoginSignup/LoginSignup';
import Menu from './Components/Menu/Menu';
import RegisterData from './Components/Menu/RegisterData.jsx';
import ConsultarRiesgo from './Components/Menu/consultarRiesgo';
import Profile from './Components/Menu/Profile';
import ConsultaFinanciera from './Components/Menu/ConsultaFinanciera.jsx';
import OlvidoContraseña from './Components/Olvido_contraseña/OlvidoContraseña.jsx';
import CreditRiskDashboard from './Components/Menu/consultarRiesgo/'; 


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginSignup />} />
        <Route path="/Menu" element={<Menu />} />
        <Route path="/RegisterData" element={<RegisterData />} />
        <Route path="/olvide_password" element={<OlvidoContraseña />} />
        <Route path="/ConsultarRiesgo" element={<ConsultarRiesgo />} />
        <Route path="/Profile" element={<Profile />} />
        <Route path="/finanzas/me" element={<ConsultaFinanciera />} />
        <Route path="/ConsultarRiesgo/:id" element={<CreditRiskDashboard />} />
        <Route path="/ConsultarRiesgo/:id" element={<ConsultarRiesgo />} />
      </Routes>
    </Router>
  );
}

export default App;
