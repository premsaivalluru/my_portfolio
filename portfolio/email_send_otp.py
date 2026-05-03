import smtplib
from email.message import EmailMessage
import os
import threading
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")


# -----------------------------
# CORE EMAIL FUNCTION (BLOCKING)
# -----------------------------
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


# -----------------------------
# NON-BLOCKING WRAPPER (USE THIS IN VIEWS)
# -----------------------------
def send_email_async(subject, body):
    threading.Thread(
        target=send_email,
        args=(subject, body),
        daemon=True
    ).start()
