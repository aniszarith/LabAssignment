import socket
import math
from math import *
import sys
import time
import errno
from multiprocessing import Process

ok_message = 'Great'
nok_message = 'Bye'

def logr(d):
    r =  str(math.log10(d))
    return r

def square(s):
    q = str(math.sqrt(s))
    return q

def expo(x):
    b = str(math.exp(x))
    return b

def process_start(s_sock):
    s_sock.send(str.encode('Welcome to Anis Calculator'))

    while True:
     try:
        data = s_sock.recv(2048).decode() # receive number or q
        print(data) # print number or Q
        if data == "Q":
            s_sock.send(nok_message.encode()) # send bye
            break
        else :
            s_sock.send(ok_message.encode()) # send great

            data2 = s_sock.recv(2048).decode() # receive L,S,E
            print(data2)
            if data2 == "L":
               print("Calculate Log10 of " + data)
               num = int(data)
               result = logr(num)
               print(result)
               s_sock.send(result.encode()) # send result
            elif data2 == "S" :
               print ("Calculate square root of " + data)
               num = int(data)
               result = square(num)
               print(result)
               s_sock.send(result.encode())
            elif data2 == "E" :
               print ("Calculate exponential of " + data)
               num = int(data)
               result = expo(num)
               print(result)
               s_sock.send(result.encode())
            else :
               print ("Invalid input")
            print ("Done")

     except (ZeroDivisionError):
               s_sock.send("ZeroDiv".encode())
     except (ArithmeticError):
               s_sock.send("MathError".encode())
     except (SyntaxError):
               s_sock.send("SyntaxError".encode())
     except (NameError):
               s_sock.send("NameError".encode())

    s_sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",4444))
    print("listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('got a socket error')

    except Exception as e:
                print('an exception occurred!')
                print(e)
                sys.exit(1)
    finally:
     	   s.close()
