import os
import email, smtplib, ssl
import imghdr
from email.message import EmailMessage

pw = os.environ.get('gmailpw_py')

port = 465  # For starttls
smtp_server = 'smtp.gmail.com'
sender_email = 'tftrankpt.py@gmail.com'
password = pw 

msg = EmailMessage()
msg['Subject'] = 'Lista Rank TFT PT'
msg['From'] = 'tftrankpt.py@gmail.com'
msg['To'] = 'onun.nuno@gmail.com'
msg.set_content('Lista Rank TFT PT')

with open('listarank.jpeg', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name)

with smtplib.SMTP_SSL(smtp_server, port) as server:
    server.login(sender_email, password)
    server.send_message(msg)

    print("Sent e-mail!")