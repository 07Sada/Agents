from dotenv import load_dotenv
import requests
import os
import smtplib
from email.message import EmailMessage

load_dotenv(override=True)

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_SMTP_SERVER = os.getenv("EMAIL_SMTP_SERVER")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")

def send_email(subject, text_body, html_body):
    msg = EmailMessage()
    msg['FROM'] = EMAIL_ADDRESS
    msg['TO'] = EMAIL_ADDRESS
    msg['SUBJECT'] = subject
    msg.set_content(text_body)
    msg.add_alternative(html_body, subtype='html')

    with smtplib.SMTP(EMAIL_SMTP_SERVER, 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_APP_PASSWORD)
        server.send_message(msg)
    
PUSHOVER_USER = os.getenv("PUSHOVER_USER")
PUSHOVER_TOKEN = os.getenv("PUSHOVER_TOKEN")
PUSHOVER_URL = "https://api.pushover.net/1/messages.json"

def push(message):
    print(f"Push: {message}")
    payload = {'user': PUSHOVER_USER, 'token': PUSHOVER_TOKEN, 'message': message}
    requests.post(PUSHOVER_URL, data=payload)