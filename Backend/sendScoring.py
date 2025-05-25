from fastapi import APIRouter, Depends, HTTPException
from auth import get_current_user
import smtplib
from pydantic import BaseModel
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

router = APIRouter()

class DatosCorreo(BaseModel):
    nombre: str
    documento: str
    correo: str
    credito: float
    cuotas: int
    resultado: int
    porcentajeAprobado: float
    porcentajeRechazo: float

@router.post("/sendScoring")

def send_scoring_email(data: DatosCorreo, current_user: dict = Depends(get_current_user)):
  # Datos de entrada
  nombre = data.nombre
  documento = data.documento
  correo = data.correo
  monto = data.credito
  cuotas = data.cuotas
  aceptado = data.resultado
  porcentajeAprobado = data.porcentajeAprobado
  porcentajeRechazo = data.porcentajeRechazo
  estado = "APROBADO" if aceptado else "RECHAZADO"
  color_estado = "#28a745" if aceptado else "#dc3545"

  # Cuerpo del mensaje en HTML
  mensaje_html = f"""
  <html>
    <body style="font-family: Arial, sans-serif; color: #333;">
      <h2 style="color: #007bff;">Consulta sobre Solicitud de Crédito</h2>
      <p>Estimado/a <strong>{nombre}</strong>,</p>
      <p>Le informamos que hemos procesado su solicitud de crédito. A continuación, los detalles:</p>

      <table style="border-collapse: collapse; width: 100%; max-width: 600px;">
        <tr>
          <td style="border: 1px solid #ccc; padding: 8px;">Nombre</td>
          <td style="border: 1px solid #ccc; padding: 8px;">{nombre}</td>
        </tr>
        <tr>
          <td style="border: 1px solid #ccc; padding: 8px;">Documento</td>
          <td style="border: 1px solid #ccc; padding: 8px;">{documento}</td>
        </tr>
        <tr>
          <td style="border: 1px solid #ccc; padding: 8px;">Monto solicitado</td>
          <td style="border: 1px solid #ccc; padding: 8px;">${monto:,.0f}</td>
        </tr>
        <tr>
          <td style="border: 1px solid #ccc; padding: 8px;">Cuotas</td>
          <td style="border: 1px solid #ccc; padding: 8px;">{cuotas}</td>
        </tr>
        <tr>
          <td style="border: 1px solid #ccc; padding: 8px;">Estado</td>
          <td style="border: 1px solid #ccc; padding: 8px; color: {color_estado}; font-weight: bold;">{estado}</td>
        </tr>
        <tr>
          <td style="border: 1px solid #ccc; padding: 8px;">Porcentaje de aprobación</td>
          <td style="border: 1px solid #ccc; padding: 8px;">{porcentajeAprobado:.0f}%</td>
        </tr>
        <tr>
          <td style="border: 1px solid #ccc; padding: 8px;">Porcentaje de Rechazo</td>
          <td style="border: 1px solid #ccc; padding: 8px;">{porcentajeRechazo:.0f}%</td>
        </tr>
      </table>

      <p>Gracias por confiar en nosotros.</p>
      <p style="margin-top: 20px;">Atentamente,<br><strong>Digital solutions</strong></p>
    </body>
  </html>
  """

  # Configuración del correo
  remitente = "scoringfinac@gmail.com"
  destinatario = correo
  asunto = "Resultado de solicitud de credito"

  # Autenticación
  usuario = "scoringfinac@gmail.com"
  contraseña = "mfontpwqizcqnglv"

  # Crear el correo
  correo = MIMEMultipart()
  correo['From'] = remitente
  correo['To'] = destinatario
  correo['Subject'] = asunto

  correo.attach(MIMEText(mensaje_html, "html"))

  # Enviar el correo
  try:
      servidor = smtplib.SMTP('smtp.gmail.com', 587)
      servidor.starttls()
      servidor.login(usuario, contraseña)
      servidor.sendmail(remitente, destinatario, correo.as_string())
      servidor.quit()
      return {"message": "Correo enviado correctamente."}
  except Exception as e:
      return {"message": "Error al enviar el correo: "}
