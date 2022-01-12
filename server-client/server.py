import socket
import json
import time
import requests    
import os        
 

s = socket.socket()        
print ("Socket successfully created")
 

port = 80             
 

s.bind(('127.0.0.1', port))        
print ("socket binded to %s" %(port))
 
s.listen(5)    
print ("socket is listening")           
 
while True:
 
  c, addr = s.accept()    
  print ('Got connection from', addr )
 
  r = requests.get(s.bind())
  json.loads(r)
  c.close()

  