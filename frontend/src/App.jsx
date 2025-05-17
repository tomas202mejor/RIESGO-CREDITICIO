import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginSignup from './Components/LoginSignup/LoginSignup';
import Menu from './Components/Menu/Menu';
import RegisterData from './Components/RegisterData/RegisterData';
import ConsultarRiesgo from './Components/ConsultarRiesgo/consultarRiesgo';


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginSignup />} />
        <Route path="/Menu" element={<Menu />} />
        <Route path="/RegisterData" element={<RegisterData />} />
        <Route path="/ConsultarRiesgo" element={<ConsultarRiesgo />} />

      </Routes>
    </Router>
  );
}

export default App;
