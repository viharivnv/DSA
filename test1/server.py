
from socket import socket, AF_INET, SOCK_DGRAM
import time

# asks the user to denote the router number
s = socket(AF_INET, SOCK_DGRAM)
#print(addr, port)
s.bind(('localhost', 8899))
d='success'

i=0

while True:
    data, r_addr = s.recvfrom(1024)
    time.sleep(1)
    s.sendto(d.encode(), r_addr)

    d = 'Second'
    data1, r_addr = s.recvfrom(1024)

    s.sendto(d.encode(), r_addr)