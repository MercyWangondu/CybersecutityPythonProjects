import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from pyexpat.errors import messages

# smtp is the protocal used to send mails after logging into an existing mail account

server =smtplib.SMTP('smtp.gmail.com',587)

# Function to start the process
server.ehlo()
server.starttls()

# server.login('mail@mail.com','password123')
with open('password.txt','r') as f:
    password=f.read().strip()

server.login('jnjiwa83@gmail.com' ,password)

msg= MIMEMultipart()
msg['From']='MercyM'
msg['To']='wangondumercy443@gmail.com'
msg['Subject']='Just a test mail'

with open('message.txt','r') as f:
    message=f.read()

msg.attach(MIMEText(message,'plain'))

filename='Bags.jpeg'
attachment=open(filename,'rb')

p=MIMEBase('application','octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment; filename={filename}')
msg.attach(p)

# Send the email
text=msg.as_string()
server.sendmail('jnjiwa83@gmail.com','wangondumercy443@gmail.com',text)

# Close the server connection
server.quit()