# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = 'xucanxucan123@gmail.com'
password = ''
to_addr = ''
smtp_server = 'smtp.gmail.com'
body_msg = "I love computer networks! and l am Jonathan Xu from NYU cx461."

msg = MIMEText(body_msg, 'plain', 'utf-8')
msg['From'] = _format_addr(u'Can Xu <%s>' % from_addr)
msg['To'] = _format_addr(u'Jonathan Xu <%s>' % to_addr)
msg['Subject'] = Header(u'My homework for Computer Networking', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()