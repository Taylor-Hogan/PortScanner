import socket
import time

#make socket connection IPV4/TCP
opensocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#get target IP from user
target = input("What IP do you want to scan ?  \n")

#hardcode IP of test
# command ifconfig | grep brodcast
#target= "192.168.1.111"

#pass target IP to socket
target_ip = socket.gethostbyname(target)
print("Starting scan on host : ",target_ip)

#make function to scan ports.
#use TRY CATCH Block to attempt to conect from IP to port
#else the result is false.

def port_scan(port):
    try:
        opensocket.connect((target_ip,port))
        return True
    except:
        return False

#starts timer for total time used to scan..
start = time.time()


common_ports = ["22","21","80","443",]


#noresponse after 6 seconds from port the scanner moves on
socket.timeout(6)


#make for loop that loops through the function above (#portscan) each port in a list
# we will use the top 50 ports.
for port in range(50):
    if port_scan(port):
     print(f"port {port} is open ")
    else:
     print(f"port {port} is closed ")

#stop timer 
end = time.time()
print(f"Time taken  {end-start:.2f} seconds ")