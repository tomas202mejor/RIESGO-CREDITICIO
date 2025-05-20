import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Datos de entrada
nombre = "Juan Pérez"
documento = "12345678"
monto = 15000
cuotas = 24
aceptado = True
probabilidad = 87.5
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
        <td style="border: 1px solid #ccc; padding: 8px;">${monto:,}</td>
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
        <td style="border: 1px solid #ccc; padding: 8px;">Probabilidad de aceptación</td>
        <td style="border: 1px solid #ccc; padding: 8px;">{probabilidad:.2f}%</td>
      </tr>
    </table>

    <p>Gracias por confiar en nosotros.</p>
    <p style="margin-top: 20px;">Atentamente,<br><strong>Digital solutions</strong></p>
  </body>
</html>
"""

# Configuración del correo
remitente = "scoringfinac@gmail.com"
destinatario = "tomas202mejor@gmail.com"
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
    print("Correo enviado correctamente.")
except Exception as e:
    print(f"Error al enviar el correo: {e}")
