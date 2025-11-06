import smtplib
from email.message import EmailMessage

def send_alert(transaction, recipient_email):
    msg = EmailMessage()
    msg.set_content(f"High-risk transaction detected:\n{transaction}")
    msg['Subject'] = "ALERT: Fraudulent Transaction"
    msg['From'] = "noreply@company.com"
    msg['To'] = recipient_email

    with smtplib.SMTP("smtp.yourserver.com") as server:
        server.send_message(msg)
