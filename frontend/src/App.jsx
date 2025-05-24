import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginSignup from './Components/LoginSignup/LoginSignup';
import Menu from './Components/Menu/Menu';
import RegisterData from './Components/RegisterData/RegisterData';
import ConsultarRiesgo from './Components/ConsultarRiesgo/consultarRiesgo';
import Profile from './Components/Profile/Profile';
import ConsultaFinanciera from './Components/ConsultaFinanciera/Consultafinanciera.jsx';
import OlvidoContraseña from './Components/Olvido_contraseña/OlvidoContraseña.jsx';
import CreditRiskDashboard from './Components/ConsultarRiesgo/consultarRiesgo/'; 


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
