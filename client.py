# Optional code to calculate the time taken for the entire socket programming in server side
import time
start=time.time()

# Import socket module 
import socket                
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 8080    
  
# connect to the server on local computer 
# check using ifconfig or the alternative method according to your PC and then add the IP address here
s.connect(('172.27.2.196', port)) 
  
# receive data from the server 
print s.recv(1024) 

# close the connection 
s.close()       

# Calculate total time taken and print it to the screen
end=time.time()
print(end-start)
