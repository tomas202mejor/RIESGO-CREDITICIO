import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import RegisterData from './Components/RegisterData/RegisterData.jsx';
import Menu from './Components/Menu/Menu';
import LoginSignup from './Components/LoginSignup/LoginSignup';

function App() {
  return (
    <Router>
        <Routes>
          <Route path="/" element={<LoginSignup />} />
          <Route path="/Menu" element={<Menu />} />
          <Route path="/RegisterData" element={<RegisterData />} />
        </Routes>
    </Router>
  );
}

export default App;
