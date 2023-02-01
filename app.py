import os
import smtplib
from receivers import receivers
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

server = smtplib.SMTP_SSL(os.environ["SERVER_ADDRESS"], os.environ["SERVER_PORT"])
server.login(os.environ["USER_LOGIN"], os.environ["USER_PASSWORD"])

for receiver in receivers:
    message = f"Olá {receiver['name']}, {os.environ['MESSAGE']}" 
    email_msg = MIMEMultipart()
    email_msg['From'] = 'menezes.icet@gmail.com'
    email_msg['To'] = receiver['email']
    email_msg['Subject'] = 'DESAFIO TALENT LAB ITACOATIARA'

    email_msg.attach(MIMEText(message, 'plain'))
    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())

server.quit()
