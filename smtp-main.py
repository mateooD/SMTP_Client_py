import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass

# Configuración del servidor SMTP de Gmail
smtp_server = "smtp.gmail.com"
smtp_port = 587
# Credenciales de la cuenta de Gmail
sender_email = input("Correo electrónico del remitente: ")
sender_password = getpass("Contraseña: ")

# Información del destinatario y del correo electrónico
recipient_email = input("Correo electrónico del destinatario: ")
subject = input("Asunto del correo: ")
message = input("Contenido del correo: ")

# Crear el objeto MIMEText con el contenido del correo
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

# Crear una conexión segura con el servidor SMTP de Gmail
smtp = smtplib.SMTP(smtp_server, smtp_port)
smtp.starttls()
smtp.login(sender_email, sender_password)

# Enviar el correo electrónico
smtp.sendmail(sender_email, recipient_email, msg.as_string())

# Cerrar la conexión SMTP
smtp.quit()
