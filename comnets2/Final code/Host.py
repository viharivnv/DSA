#!/usr/bin/python
#Topology for Assignment 5 Comnetii ECE423/544
#Author: Sanyam Jain
from socket import socket, AF_INET, SOCK_DGRAM
import MulticastPacket as p
import HostDictionary as hD
import Routing as rOut
import sys
class Host:
    
    def __init__(self,nodeid,ip,port):
        self.nodeid = nodeid
        self.ip = ip
        self.port = int(port)

    def sendReceive(self):
        r=rOut.Routing()
        currentNode=self.nodeid
        s = socket(AF_INET, SOCK_DGRAM)
        s.bind((self.ip, self.port))
        try:
            while(True):
                data, addr = s.recvfrom(1024)
                pkttype, pktlen, ndest, rdst, dest1, dest2, dest3, src, seq = p.read_header_datapacket(data)
                print(p.read_data_datapacket(data).decode('utf-8') + " from ",src)
                if(currentNode==dest1):
                    ackPacket=p.create_dataack(5,1,currentNode,r.getNodeIdFromPort(addr[1]))
                    s.sendto(ackPacket,addr)

        except KeyboardInterrupt:
            s.close()
            print('interrupted!')

def run():
    nodeid = int(sys.argv[1])
    ipaddress = hD.hostDic.get(nodeid)[0]
    port = hD.hostDic.get(nodeid)[1]
    print("Binding to ip address {} and port {}".format(ipaddress,port))
    h = Host(nodeid,ipaddress,port)
    h.sendReceive()

if __name__ == '__main__':
    run()
