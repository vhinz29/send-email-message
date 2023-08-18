import ssl
from tkinter import *
import tkinter
import smtplib
from email.message import EmailMessage


window = Tk()
window.title('vhinz')
window.geometry("500x500")

# Please replace below with your email address and password
email_sender = '_____'
email_password = 'your password or Two-factor authentication (2FA) '
email_receiver = '_____'

# Plain Text string as the email message
subject = 'This is a test email sent by Python.'

body = """
test email sent, succesfull sent!!!
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

mainloop()
