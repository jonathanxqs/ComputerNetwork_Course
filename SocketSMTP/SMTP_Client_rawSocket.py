

"""
#Mail client without using library, 
but pnly works in the smtp server that doesn't require ssl/tls. 

"""

from socket import *

msg = "\r\n I love computer networks! and l am Jonathan Xu from NYU cx461"   # must be true, trust me 
endmsg = "\r\n.\r\n"    # single period end
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'www.gmail.com'   #Fill in already

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start  
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))
#Fill in end


recvconnect = clientSocket.recv(1024)
print(recvconnect)

if (recvconnect[:3] != '220'):
	print('220 reply not received from server.')


#Send HELO command and print server response
print("Sending First HELO")
clientSocket.send(helloWords)
recv2 = clientSocket.recv(1024)
print(recv2)
if (recv2[:3] != '250'):
    print('Error: received code from server is not 250.')

#Send AUTH command and print server response.
print("Sending AUTH Command")

#AUTH with base64 encoded user name password
clientSocket.send("AUTH PLAIN =\r\n")
recv2 = clientSocket.recv(1024)
print(recv2)
if (recv2[:3] != '250'):
    print('Error: received code from server is not 250.')


#Send MAIL FROM command and print server response.
print("Sending MAIL FROM Command") 
clientSocket.send("MAIL From:xucanxucan123@gmail\r\n")
recv2 = clientSocket.recv(1024)
print(recv2)
if (recv2[:3] != '250'):
    print('Error: received code from server is not 250.')

#Send RCPT TO command and print server response.
print("Sending RCPT TO Command")
clientSocket.send("RCPT TO: xucanxucan123@gmail\r\n")
recv2 = clientSocket.recv(1024)
print(recv2)
if (recv2[:3] != '250'):
    print('Error: received code from server is not 250.')

#Send DATA command and print server response.
print("Sending DATA Command") 
clientSocket.send("DATA\r\n")
recv2 = clientSocket.recv(1024)
print(recv2)
if (recv2[:3] != '250'):
    print('Error: received code from server is not 250.')



# Send message data.
# Fill in start
print("Sending Message Data")
clientSocket.send(msg)
recv2 = clientSocket.recv(1024)
print(recv2)
if (recv2[:3] != '250'):
    print('Error: received code from server is not 250.')
# Fill in end 


# Message ends with a single period.
# Fill in start 
print("Sending Message end period")
clientSocket.send(endmsg)
recv2 = clientSocket.recv(1024)
print(recv2)
if (recv2[:3] != '250'):
    print('Error: received code from server is not 250.')

# Fill in end
 

# Send QUIT command and get server response.
# Fill in start

print("Sending QUIT command")
clientSocket.send("QUIT\r\n")
recv2 = clientSocket.recv(1024)
print(recv2)
if (recv2[:3] != '250'):
    print('Error: received code from server is not 250.')

print("Get server response correctly.\nMail Sent!")

# Fill in end 
