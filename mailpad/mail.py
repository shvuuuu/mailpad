import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

class mailpad:
    def __init__(self, smtp_server='smtp-relay.brevo.com', smtp_port=587, smtp_email=None, smtp_password=None):
        self.context = ssl.create_default_context()
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_email = smtp_email
        self.smtp_password = smtp_password

    def send_mail(self, from_email, to_email, subject, message):
        user_email = self.smtp_email or os.environ.get('MAILPAD_EMAIL')
        user_password = self.smtp_password or os.environ.get('MAILPAD_PASSWORD')

        if not user_email or not user_password:
            raise ValueError("Email user or password not set.")

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message))
        
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as mailserver:
            mailserver.starttls(context=self.context)
            mailserver.login(user_email, user_password)
            mailserver.sendmail(from_email, to_email, msg.as_string())
        
        print(f"Mail sent to - {to_email}: Email sent successfully")