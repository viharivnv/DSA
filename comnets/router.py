from packet import *

from socket import socket, AF_INET, SOCK_DGRAM

i=0








# asks the user to denote the router number


def router(addr,port):

        s = socket(AF_INET, SOCK_DGRAM)
        print(addr, port)
        s.bind((addr, port))
        while True:

            #program for router 1 functioning
            packet, r_addr = s.recvfrom(1024)
            #decapsulating the packet
            data = read_data(packet)
            header = packet[0:18]
            pkttype,lent, dest, src, seq = read_header(packet)
            #forwarding to next hop
            if src==101:
                 client1=r_addr
            if dest == 102 or dest == 103:
                 server = ('192.168.2.3',8988)
            elif dest == 101:
                 server = client1
            print('Received From ',src,'forwarding to', dest, 'squence ', seq, 'Type', pkttype)
            #encaplsulating the packet
            forward_packet=create_packet(pkttype,src,dest,seq,data)
            s.sendto(forward_packet, server)

