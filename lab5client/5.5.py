import socket
import os

SEPERATOR ="<SEPERATOR>"

s = socket.socket()

host = "192.168.56.108"
port = 5001
filename = "5.1.py"
filesize = os.path.getsize(filename)

print (f"Connect to server {host} at port {port}")
s.connect((host, port))
print ("[+] Connected")

s.send(f"{filename}".encode())
print (f"Sent :{filename}")
