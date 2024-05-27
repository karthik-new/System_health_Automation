#!/usr/bin/env python3

import os
import socket
import shutil
import psutil
import emails


subject = "System is healthy"
host_name = socket.gethostname()

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_memory_usage():
    mu = psutil.virtual_memory().available
    total = mu / (1024.0 ** 2)
    return total > 500

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 80


if not check_cpu_usage():
    subject = "Error - CPU usage is over 80%"
    print(subject)


if not check_memory_usage():
    subject = "Error - Available memory is less than 500MB"
    print(subject)

if not check_disk_usage('/'):
    subject = "Error - Available disk space is less than 20%"
    print(subject)


if not check_localhost():
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    print(subject)


# Email Code

#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText

smtp_server = 'smtp.gmail.com'
port = 587  # For TLS
sender_email = 'karthik2015kn@gmail.com'
receiver_email = 'karthik2015kn@gmail.com'
message = "Host Name: " + host_name + "\n" + "Message: " + subject

# Create a MIMEText object for the email content
msg = MIMEText(message)
msg['Subject'] = 'Automated Email'
msg['From'] = sender_email
msg['To'] = receiver_email

# Set up the connection to the SMTP server
with smtplib.SMTP(smtp_server, port) as server:
    # Start TLS encryption
    server.starttls()

    # Login to your Gmail account
    password = input("Enter your Gmail password and press enter: ")
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, [receiver_email], msg.as_string())