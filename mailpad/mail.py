import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

class mailpad:
    default_smtp_server = 'smtp-relay.brevo.com'
    default_smtp_port = 587

    @classmethod
    def brevo(cls):
        cls.default_smtp_server = 'smtp-relay.brevo.com'
        cls.default_smtp_port = 587

    def __init__(self, smtp_server=None, smtp_port=None, smtp_email=None, smtp_password=None):
        self.context = ssl.create_default_context()

        if smtp_server is None and smtp_port is None:
            self.smtp_server = mailpad.default_smtp_server
            self.smtp_port = mailpad.default_smtp_port
        else:
            self.smtp_server = smtp_server
            self.smtp_port = smtp_port

        # Automatically fetch SMTP email and password from environment variables
        self.smtp_email = os.environ.get('MAILPAD_EMAIL') if smtp_email is None else smtp_email
        self.smtp_password = os.environ.get('MAILPAD_PASSWORD') if smtp_password is None else smtp_password

    def send_mail(self, from_email, to_email, subject, message):
        if not self.smtp_email or not self.smtp_password:
            raise ValueError("Email user or password not set.")

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = ', '.join(to_email)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as mailserver:
            mailserver.starttls(context=self.context)
            mailserver.login(self.smtp_email, self.smtp_password)
            mailserver.sendmail(from_email, to_email, msg.as_string())

        print(f"Mail sent to - {', '.join(to_email)}: Email sent successfully")
    
    def send_mail_with_attachment(self, from_email, to_email, subject, message, attachment_path):
        if not self.smtp_email or not self.smtp_password:
            raise ValueError("Email user or password not set.")

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = ', '.join(to_email)
        msg['Subject'] = subject

        # Attach the message body
        part = MIMEText(message)
        msg.attach(part)

        # Attach the file
        with open(attachment_path, 'rb') as f:
            part = MIMEApplication(f.read())
            part.add_header('Content-Disposition', 'attachment; filename="' + attachment_path.split('/')[-1] + '"')
            msg.attach(part)

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as mailserver:
            mailserver.starttls(context=self.context)
            mailserver.login(self.smtp_email, self.smtp_password)
            mailserver.sendmail(from_email, to_email, msg.as_string())

            print(f"Mail sent to - {', '.join(to_email)}: Email sent successfully")

__all__ = ['mailpad']