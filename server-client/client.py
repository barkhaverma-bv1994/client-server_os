import socket
import requests
import subprocess
import os
import time


serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('', 9999))
serv.listen(5)
while True:
    conn, addr = serv.accept()
    from_client = ''
    print("connection established")

while True:
 data = s.recv(1024)
if data[:2].decode("utf-8") == 'cat':
 os.chdir(data[3:].decode("utf-8"))

r = requests.request('GET', json=  {
        "method": "mkdir /libraries/documents/data",
        "open" : "cat /libraries/desktop/server-client/client.py",
         "id": "242c41d4-2cc5-4cfb-b815-89e56862e125",
    }
)
print('Client Disconnected')