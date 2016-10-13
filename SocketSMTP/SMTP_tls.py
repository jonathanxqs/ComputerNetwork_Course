#!/usr/bin/python

import smtplib
from time import sleep

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'xucanxucan123@gmail.com'
password = ""
recipient = 'xucanxucan123@gmail.com'
subject = 'My homework for Computer Networking'
body = "I love computer networks! and l am Jonathan Xu from NYU cx461."



headers = ["From: " + sender,
           "Subject: " + subject,
           "To: " + recipient,
           "MIME-Version: 1.0",
           "Content-Type: text/html"]
headers = "\r\n".join(headers)




# SMTP_SSL 
server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server_ssl.ehlo()           # optional, called by login() in smtp_ssl
print("Logging in e-mail account...")
server_ssl.login(sender, password)  

# ssl server doesn't support or need tls, so don't call server_ssl.starttls() 
server_ssl.sendmail(sender, recipient, body)
#server_ssl.quit()
server_ssl.close()
print('successfully sent the mail')


# session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT);
# session.ehlo()
# print("start tls...")
# session.starttls()      # tls , secured
# session.ehlo()
# print("Logging in e-mail account...")
# session.login(sender, password)
# print("Sending e-mail...")
# session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
# sleep(2);               #prevent to soon to quit before sendmail terminate properly
# session.quit()
