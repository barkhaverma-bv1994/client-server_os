import socket
import requests
import os
import time


serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('localhost', 1221))
serv.listen(5)
while True:
    conn, addr = serv.accept()
    from_client = ''
    print("connection established")
    data = {
        "method": "mkdir /libraries/documents/data",
        "open" : "cat /libraries/documents/data",
         "id": "242c41d4-2cc5-4cfb-b815-89e56862e125",
    }
    r = requests.request('', json=data)
print('Client Disconnected')