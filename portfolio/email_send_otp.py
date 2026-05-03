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

def send_otp_email(receiver_email):
    otp = str(random.randint(100000, 999999))
    subject = "Your OTP for Email Verification on Smart Time Table Management System"
    body = f"Your OTP code is: {otp}"

    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)
        print("OTP Email sent successfully!")
        return {"otp": otp, "status": "success", "message": "OTP sent successfully"}
    except Exception as e:
        print(f"Failed to send OTP email: {e}")
        return {"status": "failure", "message": str(e)}
    
def send_swap_request(sender, sender_name, receiver_email, message):
    subject = f"Swap Request from {sender_name}"
    body = f"{message}\n\nNote: Login to the website to accept or reject the request!\n\nFrom Faculty: {sender}"
    
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)
        print("Swap Request Email sent successfully!")
        return {"status": "success", "message": "Swap Request Email sent successfully"}
    except Exception as e:
        print(f"Failed to send Swap Request E#mail: {e}")
        return {"status": "failure", "message": str(e)}

def notify_student(receiver_email, message):
    subject = f"Scheduled Lecture Swap!"
    body = f"{message}"
    
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)
        print("Swap Request Email sent successfully!")
        return {"status": "success", "message": "Swap Request Email sent successfully"}
    except Exception as e:
        print(f"Failed to send Swap Request E#mail: {e}")
        return {"status": "failure", "message": str(e)}

def send_email(subject, body):
    receiver_email = "vallurupremsai590@gmail.com"
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)
        print("Email sent successfully!")
        return {"status": "success", "message": "Email sent successfully"}
    except Exception as e:
        print(f"Failed to send email: {e}")
        return {"status": "failure", "message": str(e)}