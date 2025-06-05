from fastapi import APIRouter, Depends
from auth import get_current_user
from pydantic import BaseModel
import smtplib
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

def armar_mensaje_html(data: DatosCorreo) -> str:
    estado = "APROBADO" if data.resultado else "RECHAZADO"
    color_estado = "#28a745" if data.resultado else "#dc3545"
    return f"""
    <html>
      <body style='font-family: Arial, sans-serif; color: #333;'>
        <h2 style='color: #007bff;'>Consulta sobre Solicitud de Crédito</h2>
        <p>Estimado/a <strong>{data.nombre}</strong>,</p>
        <p>Le informamos que hemos procesado su solicitud de crédito. A continuación, los detalles:</p>
        <table style='border-collapse: collapse; width: 100%; max-width: 600px;'>
          <tr><td style='border: 1px solid #ccc; padding: 8px;'>Nombre</td><td style='border: 1px solid #ccc; padding: 8px;'>{data.nombre}</td></tr>
          <tr><td style='border: 1px solid #ccc; padding: 8px;'>Documento</td><td style='border: 1px solid #ccc; padding: 8px;'>{data.documento}</td></tr>
          <tr><td style='border: 1px solid #ccc; padding: 8px;'>Monto solicitado</td><td style='border: 1px solid #ccc; padding: 8px;'>${data.credito:,.0f}</td></tr>
          <tr><td style='border: 1px solid #ccc; padding: 8px;'>Cuotas</td><td style='border: 1px solid #ccc; padding: 8px;'>{data.cuotas}</td></tr>
          <tr><td style='border: 1px solid #ccc; padding: 8px;'>Estado</td><td style='border: 1px solid #ccc; padding: 8px; color: {color_estado}; font-weight: bold;'>{estado}</td></tr>
          <tr><td style='border: 1px solid #ccc; padding: 8px;'>Porcentaje de aprobación</td><td style='border: 1px solid #ccc; padding: 8px;'>{data.porcentajeAprobado:.0f}%</td></tr>
          <tr><td style='border: 1px solid #ccc; padding: 8px;'>Porcentaje de Rechazo</td><td style='border: 1px solid #ccc; padding: 8px;'>{data.porcentajeRechazo:.0f}%</td></tr>
        </table>
        <p>Gracias por confiar en nosotros.</p>
        <p style='margin-top: 20px;'>Atentamente,<br><strong>Digital solutions</strong></p>
      </body>
    </html>
    """

class ServicioCorreo:
    def __init__(self):
        self.remitente = "scoringfinac@gmail.com"
        self.usuario = self.remitente
        self.contraseña = "mfontpwqizcqnglv"
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587

    def enviar(self, destinatario: str, asunto: str, mensaje_html: str):
        mensaje = MIMEMultipart("alternative")
        mensaje["Subject"] = asunto
        mensaje["From"] = self.remitente
        mensaje["To"] = destinatario
        mensaje.attach(MIMEText(mensaje_html, "html"))
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as servidor:
                servidor.starttls()
                servidor.login(self.usuario, self.contraseña)
                servidor.sendmail(self.remitente, destinatario, mensaje.as_string())
        except Exception as e:
            raise Exception(f"Error al enviar correo: {e}")

@router.post("/sendScoring")
def send_scoring_email(data: DatosCorreo, current_user: dict = Depends(get_current_user)):
    mensaje_html = armar_mensaje_html(data)
    servicio_correo = ServicioCorreo()
    try:
        servicio_correo.enviar(
            destinatario=data.correo,
            asunto="Resultado de solicitud de credito",
            mensaje_html=mensaje_html
        )
        return {"message": "Correo enviado correctamente."}
    except Exception as e:
        return {"message": f"Error al enviar el correo: {e}"}
