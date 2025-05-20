import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import RegisterData from './Components/RegisterData/RegisterData.jsx';
import Menu from './Components/Menu/Menu';
import LoginSignup from './Components/LoginSignup/LoginSignup';
import ConsultaFinanciera from './Components/ConsultaFinanciera/Consultafinanciera.jsx';
import OlvidoContraseña from './Components/Olvido_contraseña/OlvidoContraseña.jsx';


function App() {
  return (
    <Router>
        <Routes>
          <Route path="/" element={<LoginSignup />} />
          <Route path="/Menu" element={<Menu />} />
          <Route path="/RegisterData" element={<RegisterData />} />
          <Route path="/olvide_password" element={<OlvidoContraseña />} />
          <Route path="/finanzas/me" element={<ConsultaFinanciera />} />
        </Routes>
    </Router>
  );
}

export default App;
