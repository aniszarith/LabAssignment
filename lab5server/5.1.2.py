import socket

s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      #UDP Socket
print("Berjaya buat sokett")

udpaddr = "192.168.56.108"		        #Get Host IP
udpport = 12345

s.bind((udpaddr,udpport))
print("soket tengah menunggu client!")

while True:
	c,addr = s.recvfrom(1024)
	print ("Mesej dari client: "+ c.decode())
