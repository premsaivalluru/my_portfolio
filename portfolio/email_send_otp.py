import smtplib
from email.message import EmailMessage
from pathlib import Path
import mimetypes
import os
from dotenv import load_dotenv
import random

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

def send_email(subject, body):
    receiver_email = "vallurupremsai590@gmail.com"

    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)

        print("Email sent successfully!")
        return {"status": "success", "message": "Email sent successfully"}

    except Exception as e:
        print(f"Failed to send email: {e}")
        return {"status": "failure", "message": str(e)}
