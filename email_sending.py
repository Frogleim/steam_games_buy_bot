import smtplib
from email.mime.multipart import MIMEMultipart
import json
from email.mime.text import MIMEText


def send_confirm_mail(receiver):
    with open("./client_accounts/client_account.json", "r") as client_file:
        data = json.load(client_file)
        gmail_password = "vjadcjnzrndinjfa"
        gmail_user = 'gameacseu@gmail.com'
        msg = MIMEMultipart()
        msg['From'] = 'Gameacs.eu'
        msg['To'] = receiver
        email_body = f"Hi, we want to inform you that your purchase is complete\n Here is you new Steam account data\n" \
                     f"username: {data['username']}\n" \
                     f"password: {data['password']}\n" \
                     f"email {data['email']}\n" \
                     f"email password {data['email password']}\n"
        body = MIMEText(email_body, 'html')
        msg.attach(body)

    # Send the email using Gmail's SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(gmail_user, gmail_password)
        smtp.send_message(msg)


def send_confirm_mail_to_admin():
    with open("./client_accounts/client_account.json", "r") as client_file:
        data = json.load(client_file)
        gmail_password = "vjadcjnzrndinjfa"
        gmail_user = 'gameacseu@gmail.com'
        msg = MIMEMultipart()
        msg['From'] = 'Gameacs.eu'
        msg['To'] = 'gameacseu@gmail.com'
        email_body = f"Hi, we want to inform you that your purchase is complete for user:\nusername: {data['username']}\n"
        body = MIMEText(email_body, 'html')
        msg.attach(body)

    # Send the email using Gmail's SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(gmail_user, gmail_password)
        smtp.send_message(msg)


def send_error_mail_to_admin():
    with open("./client_accounts/client_account.json", "r") as client_file:
        gmail_password = "vjadcjnzrndinjfa"
        gmail_user = 'gameacseu@gmail.com'
        msg = MIMEMultipart()
        msg['From'] = 'Gameacs.eu'
        msg['To'] = 'gameacseu@gmail.com'
        email_body = f"Hi, we want to inform you that your purchase is failed! Please contact with developer\n"
        body = MIMEText(email_body, 'html')
        msg.attach(body)

    # Send the email using Gmail's SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(gmail_user, gmail_password)
        smtp.send_message(msg)