#From: Can Xu 
#Mail: cx461@nyu.edu  

#import socket module 
from socket import * 
       
           

serverSocket = socket(AF_INET, SOCK_STREAM) 
#Prepare a sever socket 

#Fill in start 

serverReqPort=3000;  #Set 3000 as port
serverSocket.bind(('',serverReqPort));
serverSocket.listen(1);
print('We set server listening port as: ',serverReqPort);

#Fill in end 

while True: 

    #Establish the connection
    
    print('Ready to serve...'); 
    connectionSocket, addr =  serverSocket.accept(); 

    try: 
        message =     connectionSocket.recv(1024)    #Fill in this line               
        filename = message.split()[1]
        print('message is:',message) 
        print('relative add and actual filename:',filename,filename[1:]);                 
        #f = open(filename[1:]) 
        

        f=open(filename[1:], 'rb')  
        outputdata = f.read()  #Fill in this two lines 
        print(outputdata)                   
        #Send one HTTP header line into socket 
        #Fill in start 
        connectionSocket.send(b'\nHTTP/1.1 200 OK\n\n')            
        #connectionSocket.send(outputdata)
        #Fill in end   

        #Send the content of the requested file to the client 
        for i in range(0, len(outputdata)):
            #print(chr(outputdata[i]));            
            connectionSocket.send(bytes(chr(outputdata[i]),encoding='utf-8'))
        
        connectionSocket.close() 

    except IOError: 
        #Send response message for file not found 
        #Fill in start
        print('Fail to load IO; 404 Error')    
        connectionSocket.send(b'\nHTTP/1.1 404 Not Found\n\n')
        #connectionSocket.send(b'\nHTTP/1.1 404 Not Found\n\n')     
        #Fill in end 

        #Close client socket 
        #Fill in start 
        serverSocket.close()
        break; 
        #Fill in end   

serverSocket.close() 


          
