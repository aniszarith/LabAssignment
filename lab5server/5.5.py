import socket
import os

SEPERATOR="<SPERATOR>"
BUFFER_SIZE = 4096

s= socket.socket()
print("Berjaya buat sokett")

addr = "192.168.56.108"                      #Get Host IP
port = 5001

s.bind((addr,port))
s.listen(5)

print("soket tengah menunggu client!")

while True:

        clientsock, address = s.accept()
        print (f"Client: {address}")
        received = clientsock.recv(BUFFER_SIZE).decode()
        filename = received
        filename = os.path.basename(filename)
        print ("File received: " + filename)

