import string
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def generate_string(length=10):
    letter = string.ascii_letters
    otp = "".join(random.choice(letter)for _ in range(length))
    return otp


def verify_mail_send(to_address, name, link):
    msg = MIMEMultipart()
    msg['From'] = "Django Project Email"
    msg['Subject'] = "verify LInk Mail"
    msg['To'] = to_address

    body = "hey {}! your verify link is {}".format(name, link)
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("chhavisharma481@gmail.com", "chhavi481")
    text = msg.as_string()
    server.sendmail("chhavisharma481@gmail.com", to_address, text)

