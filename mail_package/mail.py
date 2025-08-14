import smtplib,ssl

from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.application import MIMEApplication
from email.utils import formatdate

smtp_server ="smtp.gmail.com"
port = 465
#email_sender = "rose.wnd87@gmail.com"
#pass_app ="tcwzborvxxkpsvig"
#receiver = ["zahra.navaeepour@gmail.com" ]


def config(sender,receiver,password):
    global email_sender,email_receiver,pass_app
    email_sender = sender
    email_receiver =receiver
    pass_app = password


context = ssl.create_default_context()
def send_smtp_email(sender,receiver,password,subject,body):
    config(sender,receiver,password)
    message=MIMEText(body)
    message["subject"]=subject 
    message["from"]=email_sender
    #message["to"] = email_receiver

    with smtplib.SMTP_SSL(smtp_server,port,context=context) as server :
        server.login(email_sender,pass_app)
        #for add_mail in email_receiver:
        server.sendmail(email_sender,email_receiver,message.as_string())

def send_email_attach(sender,receiver,password,subjet,body,file) :
    config(sender,receiver,password)
    msg=MIMEMultipart()
    msg["from"] = email_sender
    #msg["to"] = email_receiver
    msg["subjet"] = subjet
    msg["date"]= formatdate(localtime=True)
    part1=MIMEText(body)
    msg.attach(part1)
     
    with open(file,"rb") as attachment :
        part2=MIMEApplication(attachment.read(),_subtype="png")
        encoders.encode_base64(part2)
        part2.add_header("Content-Disposition","attachment",filename=file)
    msg.attach(part2)

    with smtplib.SMTP_SSL(smtp_server,port,context=context) as server :
        server.login(email_sender,pass_app)
        server.sendmail(email_sender,email_receiver,msg.as_string())

