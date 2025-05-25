// src/components/CreditPieChart.js
import React from 'react';
import { Doughnut } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';

ChartJS.register(ArcElement, Tooltip, Legend);

const Grafico = ({ aprobado, rechazado }) => {
  const data = {
    labels: ['Aprobado', 'Rechazado'],
    datasets: [
      {
        data: [aprobado, rechazado],
        backgroundColor: ['#36A2EB', '#FF6384'],
        hoverBackgroundColor: ['#36A2EB', '#FF6384'],
      },
    ],
  };

  return (
    <div style={{ maxWidth: '300px', margin: '0 auto' }}>
      <Doughnut data={data} />
    </div>
  );
};

export default Grafico;
