# mail_service.py
import smtplib
from email.message import EmailMessage
from app.config import settings

def send_confirmation_email(email: str, name: str):
    msg = EmailMessage()
    msg['Subject'] = 'Registration Confirmation'
    msg['From'] = settings.MAIL_FROM
    msg['To'] = email
    msg.set_content(f"Hello {name},\n\nYour registration is successful.\n\nThank you!")

    # Use Mailtrap for development/testing
    with smtplib.SMTP(settings.MAIL_SERVER, settings.MAIL_PORT) as server:
        server.login(settings.MAIL_USERNAME, settings.MAIL_PASSWORD)
        server.send_message(msg)

def send_confirmation_sms(phone: str, name: str, message: str):
    print(f"SMS notification to {phone} for {name}: {message}", flush=True)