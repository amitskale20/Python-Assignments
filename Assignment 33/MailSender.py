##########################################################
#
#   Import Required Libraries
#
##########################################################

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

##########################################################
#
#   Function name :     SendMail
#   Input :             Receiver, LogFileName, Statistics
#   Output :            Boolean
#   Description :       Sends log file through email
#   Date :              24/07/2026
#   Author :            Amit Sahebrao Kale
#
##########################################################

def SendMail(Receiver,LogFileName,Statistics):

    try:

        Sender = "amitkalepython@gmail.com"
        Password = "yxqv nhdw fupm oolm"

        Message = MIMEMultipart()

        Message["From"] = Sender
        Message["To"] = Receiver
        Message["Subject"] = "Duplicate File Removal Automation Report"

        Body = f"""

Jay Ganesh,

The duplicate file removal operation has been completed successfully.

Operation Statistics

--------------------------------------------------

Starting Time            : {Statistics["StartTime"]}

Completion Time          : {Statistics["EndTime"]}

Directory Scanned        : {Statistics["Directory"]}

Total Files Scanned      : {Statistics["TotalFiles"]}

Duplicate Files Found    : {Statistics["Duplicate"]}

Duplicate Files Deleted  : {Statistics["Deleted"]}

--------------------------------------------------

Please find the attached log file.

Regards,

Marvellous Automation System

"""

        Message.attach(MIMEText(Body,"plain"))

        Attachment = open(LogFileName,"rb")

        Payload = MIMEBase("application","octet-stream")

        Payload.set_payload(Attachment.read())

        encoders.encode_base64(Payload)

        Payload.add_header(
            "Content-Disposition",
            "attachment; filename=%s"%(LogFileName)
        )

        Message.attach(Payload)

        Server = smtplib.SMTP("smtp.gmail.com",587)

        Server.starttls()

        Server.login(Sender,Password)

        Text = Message.as_string()

        Server.sendmail(Sender,Receiver,Text)

        Server.quit()

        Attachment.close()

        return True

    except Exception as E:

        print("Unable to send email")
        print(E)

        return False