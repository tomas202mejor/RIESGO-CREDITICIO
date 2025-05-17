import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginSignup from './Components/LoginSignup/LoginSignup';
import Menu from './Components/Menu/Menu';
import RegisterData from './Components/RegisterData/RegisterData';
<<<<<<< HEAD
import Profile from './Components/Profile/Profile';

=======
import ConsultaFinanciera from './Components/ConsultaFinanciera/Consultafinanciera.jsx';
>>>>>>> 9667c03d8008c7ceb3a45ed06e419c8191661515

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginSignup />} />
        <Route path="/Menu" element={<Menu />} />
        <Route path="/RegisterData" element={<RegisterData />} />
<<<<<<< HEAD
        <Route path="/Profile" element={<Profile />} />
=======
        <Route path="/finanzas/me" element={<ConsultaFinanciera />} />
>>>>>>> 9667c03d8008c7ceb3a45ed06e419c8191661515
      </Routes>
    </Router>
  );
}

export default App;
