import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_correo_recuperacion(destinatario: str, codigo: str):
    remitente = "scoringfinac@gmail.com"
    asunto = "Recuperación de contraseña"
    usuario = remitente
    contraseña = "mfontpwqizcqnglv"

    mensaje_html = f"""
    <html>
      <body style="font-family: Arial, sans-serif; color: #333;">
        <h2 style="color: #007bff;">Recuperación de Contraseña</h2>
        <p>Hola,</p>
        <p>Tu código para restablecer la contraseña es:</p>
        <h3 style="text-align: center; color: #007bff;">{codigo}</h3>
        <p>Ingresa este código en la aplicación para continuar con el proceso.</p>
        <p>Si tú no solicitaste este cambio, puedes ignorar este mensaje.</p>
        <p style="margin-top: 20px;">Saludos,<br><strong>Digital Solutions</strong></p>
      </body>
    </html>
    """

    mensaje = MIMEMultipart("alternative")
    mensaje["Subject"] = asunto
    mensaje["From"] = remitente
    mensaje["To"] = destinatario
    mensaje.attach(MIMEText(mensaje_html, "html"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
            servidor.starttls()
            servidor.login(usuario, contraseña)
            servidor.sendmail(remitente, destinatario, mensaje.as_string())
        print("✅ Correo de recuperación enviado correctamente.")
    except Exception as e:
        print(f"❌ Error al enviar correo de recuperación: {e}")
