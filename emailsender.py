import os

import smtplib

from email.message import EmailMessage

from email.utils import formataddr

from pathlib import Path

from dotenv import load_dotenv

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


# current_dir=Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
# envars=current_dir/".env"
# load_dotenv(envars)
PORT= 587
EMAIL_SERVER='smtp.gmail.com'
sender_email='girishsaana2513@gmail.com'
password_email='pdoiooymmoznptxx'

def send_email(subject,receiver_email,name,duedate,due,totalfee,rollno):
    msg=MIMEMultipart()
    msg["Subject"]=subject
    msg["From"] = sender_email
    msg["To"]=receiver_email
    # msg["BCC"]=sender_email
    body=f"""\
        Dear {name} ({rollno}),

I hope this message finds you well. This is a friendly reminder that your payment of {due} is due on {duedate}.

Invoice Details:
Total Fee: {totalfee}
Amount Paid: {totalfee-due}
Amount Due: {due}
Due Date: {duedate}
We greatly appreciate your prompt attention to this matter. If you have already made the payment, please disregard this reminder and accept our thanks.

If you need any assistance or have questions regarding your invoice, feel free to reach out to us. We are here to help!

Thank you for your continued trust in our services.

Best regards,

MRCE
        """
    msg.attach(MIMEText(body,'plain'))
    filename='NumetryList.xlsx'
    attachment= open(filename, 'rb') 
    attachment_package = MIMEBase('application', 'octet-stream')
    attachment_package.set_payload((attachment).read())
    encoders.encode_base64(attachment_package)
    attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
    msg.attach(attachment_package)





    # server = smtplib.SMTP(EMAIL_SERVER,PORT)
    # server.starttls()
    # server.login(sender_email,password_email)
    # server.sendmail(sender_email,receiver_email,msg.as_string())
    server = smtplib.SMTP(EMAIL_SERVER,PORT)
    server.starttls()
    server.login(sender_email,password_email)
    server.sendmail(sender_email,receiver_email, msg.as_string())
    server.quit()



