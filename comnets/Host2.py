#!/usr/bin/python
#Topology for Assignment 5 Comnetii ECE423/544
#Author: Sanyam Jain
from socket import socket, AF_INET, SOCK_DGRAM
import MulticastPacket as p

class Host2:

    def sendReceive(self):
        currentNode=102
        file = open("ipaddrs.txt", "r")
        text = file.readline()
        s = socket(AF_INET, SOCK_DGRAM)
        port = 1025
        while True:
            try:
                s.bind(('localhost', port))
                print(port)
                print(text)
                break
            except:
                text = file.readline()
                port += 1

        try:
            while(True):
                data, addr = s.recvfrom(1024)
                pkttype, pktlen, ndest, rdst, dest1, dest2, dest3, src, seq = p.read_header_datapacket(data)
                print(p.read_data_datapacket(data).decode('utf-8') + " from ",src)
                if(currentNode==dest1):
                    ackPacket=p.create_dataack(5,1,currentNode,202)
                    s.sendto(ackPacket,addr)

        except KeyboardInterrupt:
            s.close()
            print('interrupted!')

def run():
    h2 = Host2()
    h2.sendReceive()

if __name__ == '__main__':
    run()
