import socket
import math

ClientSocket = socket.socket()
host = '192.168.56.108'
port = 4444

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024) # print welcome
print(Response)
while True:
    Input = input('\nEnter a number to calculate or Q to Quit :  ')
    ClientSocket.send(Input.encode()) # send number or Q

    Reply = ClientSocket.recv(1024) # receive great/bye
    print(Reply.decode('utf-8'))
    if Input == "Q":
       break
    else :
       Input2 = input('Choose either to calculate the:\n Logarithmic enter L\n SquareRoot enter S \n Exponential enter E \n Enter :')
       ClientSocket.send(Input2.encode()) # send L,S,E
       Response = ClientSocket.recv(1024) # receive result
       print("Result : ", Response.decode()) # print result

ClientSocket.close()
