import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("Berjaya buat sokett")

udpaddr = "192.168.56.108"
udpport = 12345

s.connect((udpaddr, udpport))
message = "Hi Server!".encode()

while True:
       message = str(input("Enter your message: "))
       message = message.encode()
       s.sendto(message,(udpaddr,udpport))

