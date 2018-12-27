import time
start=time.time()
# Import socket module 
import socket                
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 8080    
  
# connect to the server on local computer 
s.connect(('172.27.2.196', port)) 
  
# receive data from the server 
print s.recv(1024) 
# close the connection 
s.close()        
end=time.time()
print(end-start)
