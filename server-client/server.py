import socket
import json
import time
import requests    
import os

from requests.api import request        
 

s = socket.socket()        
print ("Socket successfully created")
 

port = 9999            
 

s.bind(('192.168.0.104', port))        
print ("socket binded to %s" %(port))
 
s.listen(5)    
print ("socket is listening")           
 
while True:
 
  c, addr = s.accept()    
  print ('Got connection from', addr )
 
  r = requests.get(s.bind())
  json.loads(r.read())

if r.read(0) == 0:
    print ('Execution Unsuccessful')

else:
  r.read(json(0))

  c.close()

  