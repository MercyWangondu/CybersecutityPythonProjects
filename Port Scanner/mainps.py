# Open ports might be a security gap
# Port scanning is  illegal
# We use sockets to connect to a server/ip address ,if connection succeds the port is open if not the port is closed

import socket

from PythonPersonalProjects.PythonCalculator import result

target='192.168.0.1'

# You can also scan your own machine using local host'127.0.0.1'
def portscan(port):
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((target,port))
        return True
    except:
        return  False

for port in range(1,1024):
    result=portscan(port)
    if result:
        print("Port {} is open!.".format(port))
    else:
        print("Port {} is closed!.".format(port))

# print(portscan(98))