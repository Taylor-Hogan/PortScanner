#!bin/bash/python
#port scanner will scan an IP and tell us what ports are opwen

#modules
# you need the socket module to read ports
#AF_INET specifies IPs
#Steam specifies if it is TCP traffic.
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM,)

#host= "IP you want to scan"
host = "127.0.0.1"
port = 22

#make function with the varibiles above
def portScanner(port):
    if s.connect_ex((host, port)):
        print(" port is closed")
    else:
        print("port is open")

portScanner(port)