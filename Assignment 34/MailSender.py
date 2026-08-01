import smtplib
import os
from email.message import EmailMessage

def SendMail(receiver, logfile):
    sender='yourgmail@gmail.com'
    password='YOUR_16_DIGIT_APP_PASSWORD'
    try:
        msg=EmailMessage()
        msg['From']=sender
        msg['To']=receiver
        msg['Subject']='Process Information Log'
        msg.set_content('Please find attached log.')
        with open(logfile,'rb') as f:
            msg.add_attachment(f.read(),maintype='text',subtype='plain',filename=os.path.basename(logfile))
        s=smtplib.SMTP_SSL('smtp.gmail.com',465)
        s.login(sender,password)
        s.send_message(msg)
        s.quit()
        return True
    except Exception as e:
        print(e)
        return False
