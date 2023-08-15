import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

smtp_email = os.environ.get('MAILPAD_EMAIL')
smtp_password = os.environ.get('MAILPAD_PASSWORD')

class mailpad:
    def __init__(self, smtp_server=None, smtp_port=None):
        self.smtp_server=smtp_server
        self.smtp_port=smtp_port
        self.context = ssl.create_default_context()
    
    def brevo(self):
        self.smtp_server = 'smtp-relay.brevo.com'
        self.smtp_port = 587

    def send_mail(self, from_email, to_email, subject, message):

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = ', '.join(to_email)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as mailserver:
            mailserver.starttls(context=self.context)
            mailserver.login(self.smtp_email, self.smtp_password)
            mailserver.sendmail(from_email, to_email, msg.as_string())

        print(f"Mail sent to - {to_email}")
    
    def send_mail_with_attachment(self, from_email, to_email, subject, message, attachment_path):
        
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = ', '.join(to_email)
        msg['Subject'] = subject

        part = MIMEText(message)
        msg.attach(part)

        with open(attachment_path, 'rb') as f:
            part = MIMEApplication(f.read())
            part.add_header('Content-Disposition', 'attachment; filename="' + attachment_path.split('/')[-1] + '"')
            msg.attach(part)

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as mailserver:
            mailserver.starttls(context=self.context)
            mailserver.login(self.smtp_email, self.smtp_password)
            mailserver.sendmail(from_email, to_email, msg.as_string())

            print(f"Mail sent to - {to_email}")

__all__ = ['mailpad']