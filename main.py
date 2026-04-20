
import smtplib, ssl
from dotenv import dotenv_values
config = dotenv_values()
email = config["EMAIL"]
receiver_email = config["RECEIVER_EMAIL"]
password =  config["PASSWORD"]

def sent_message(mail):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "sarvarrejametov41@gmail.com"  # Enter your address
    receiver_email = "sarvarrejametov41@gmail.com"  # Enter receiver address
    password = "vztahzosufsgyuph"
    message = f"""\
    {mail}"""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

sent_message("Salom")