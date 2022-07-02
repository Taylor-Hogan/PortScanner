#!bin/bash/python
#port scanner will scan an IP and tell us what ports are opwen

#modules
# you need the socket module to read ports
#AF_INET specifies IPs
#Steam specifies if it is TCP traffic.
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM,)
socket.timeout(5)

host = input(" PLease enter the IP you want to scan ")
port = int(input(" Please enter the port you want to scan "))

#make function with the varibiles above
def portScanner(port):
    if s.connect_ex((host, port)):
        print(" port is closed")
    else:
        print("port is open")

portScanner(port)