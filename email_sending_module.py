# Dependencies
#   - pip install pydantic[email]


# args: receiver_email: To whom the email sent
#       sender_email: 
#       app_password: App password of a sender_email
#       email_body: Body text of email
#       email_subject: Subject text of email


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from pydantic import BaseModel, EmailStr, ValidationError

class EmailModel(BaseModel):
  receiver_email: EmailStr
  sender_email: EmailStr
  app_password: str
  email_body: str
  email_subject: str


def sent_email(receiver_email: str, sender_email: str,  email_subject: str, email_body: str, app_password: int ) -> None:

  try:
    email_data = EmailModel(receiver_email=receiver_email, sender_email=sender_email,
                            email_subject=email_subject, email_body=email_body, app_password=app_password)
  except ValidationError as e:
    raise ValueError(f"Email Model Error: {e}")

  
  message = MIMEMultipart() 
  message['From'] = email_data.sender_email 
  message['To'] = email_data.receiver_email 

  message['Subject'] = email_data.email_subject 
  body = email_data.email_body

  message.attach(MIMEText(body, 'plain')) 
  server = smtplib.SMTP('smtp.gmail.com', 587) 
  server.starttls()

  server.login(email_data.receiver_email, email_data.app_password)
  server.sendmail(email_data.receiver_email, email_data.sender_email, message.as_string()) 
  server.quit()
