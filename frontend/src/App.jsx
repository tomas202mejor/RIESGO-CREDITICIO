import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginSignup from './Components/LoginSignup/LoginSignup';
import Menu from './Components/Menu/Menu';
import RegisterData from './Components/RegisterData/RegisterData';
import ConsultaFinanciera from './Components/ConsultaFinanciera/Consultafinanciera.jsx';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginSignup />} />
        <Route path="/Menu" element={<Menu />} />
        <Route path="/RegisterData" element={<RegisterData />} />
        <Route path="/finanzas/me" element={<ConsultaFinanciera />} />
      </Routes>
    </Router>
  );
}

export default App;
