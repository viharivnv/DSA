import socket
#from socket import socket, AF_INET, SOCK_DGRAM



# asks the user to denote the router number
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#print(addr, port)
s.settimeout(0)
s.bind(('localhost', 8888))
server=('localhost', 8899)
data="test"

s.sendto(data.encode(),server)

acknowledged = False

# spam dest until they acknowledge me (sounds like my kids)
while not acknowledged:
    try:
        ACK, address = s.recvfrom(1024)
        print(ACK)

        acknowledged = True
    except socket.timeout:
        s.sendto(data.encode(),server)







