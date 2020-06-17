from multicastpacket import *

from socket import socket, AF_INET, SOCK_DGRAM

i=0
# asks the user to denote the router number
s = socket(AF_INET, SOCK_DGRAM)
#print(addr, port)
s.bind(('localhost', 8888))

while True:
    data, r_addr = s.recvfrom(1024)
    # decapsulating the packet
    msg = read_data(packet)
    # header = packet[0:18]
    # pkttype,lent, dest, src, seq = read_header(packet)
    pkttype, pktlen, ndest, rdst, dest1, dest2, dest3, src, seq = read_header(packet)
    if dest1 == myaddres:
        print('Message from',src,':')
        print(msg)
        print('Sending Acknowldgement to', src)
        ack_packet=create_ack(5,1,myaddres,src)
        s.sendto(ack_packet, r_addr)