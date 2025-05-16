import React, { useEffect, useState } from "react";
import axios from "axios";
import './Profile.css';
import { useNavigate } from "react-router-dom";


const Profile = () => {
  const [userData, setUserData] = useState(null);
  const navigate = useNavigate();
  useEffect(() => {
    const token = localStorage.getItem("token");
    


    axios.get("http://localhost:8000/usuario/me", {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
    .then(response => {
      setUserData(response.data);
    })
    .catch(error => {
      console.error("Error al obtener datos del usuario:", error);
    });
  }, []);

  if (!userData) return <p className="loading">Cargando perfil...</p>;





  return (
    <div className="profile-container">
     
      <h2 className="profile-title">Perfil del Usuario</h2>
      <div className="profile-item"><strong>ID:</strong> {userData.id}</div>
      <div className="profile-item"><strong>Usuario:</strong> {userData.username}</div>
      <div className="profile-item"><strong>Email:</strong> {userData.email}</div>
      <div className="profile-item"><strong>Nombre completo:</strong> {userData.nombre}</div>
      <div className="profile-item"><strong>Teléfono:</strong> {userData.telefono}</div>
      <div className="profile-item"><strong>Número de documento:</strong> {userData.Ndocumento}</div>
      <div className="back-button-wrapper">
      <button className="back-button" onClick={() => navigate("/Menu")}>
       ⟵ Regresar
       </button>
</div>

    </div>
  );
};

export default Profile;
