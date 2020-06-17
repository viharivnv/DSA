#Topology for Assignment 5 Comnetii ECE423/544
#Author: Sanyam Jain
from socket import socket, AF_INET, SOCK_DGRAM
import MulticastPacket as p
import HostDictionary as hD
import Routing as rOut
import sys

class Source:

    def __init__(self,msg,numberOfDest,nodeid,ip,port):
        self.num = numberOfDest
        self.msg = msg
        self.nodeid = nodeid
        self.ip = ip
        self.port = int(port)


    def sendReceive(self):
        r=rOut.Routing()
        currentNode=self.nodeid
        s = socket(AF_INET, SOCK_DGRAM)
        s.bind((self.ip,self.port))
        rdest,dest=r.getdestination(self.num,currentNode)
        print("Best router is ",rdest)
        print("Destination hosts are {},{},{}".format(dest[0],dest[1],dest[2]))     
        router = (hD.hostDic[r.nexthop(currentNode,rdest)][0],hD.hostDic[r.nexthop(currentNode,rdest)][1])
        print("Connected to server ",router)
        pkttype=hD.packetType.get('data')
        seq=1
        print(pkttype,seq)
        s.sendto(p.create_datapacket(pkttype,seq,currentNode,self.num,rdest,int(dest[0]),int(dest[1]),int(dest[2]),self.msg.encode('utf-8')),router)
        data, addr = s.recvfrom(1024)
        if data and p.read_dataack(data)[0]==hD.packetType.get('dataAck') and p.read_dataack(data)[1]==currentNode:
            print("Received acknowledgement form {}".format(p.read_dataack(data)[2]))
        else :
            print("No Acknowledgement received")
        s.close()

def run():
        nodeid = int(sys.argv[1])
        ipaddress = hD.hostDic.get(nodeid)[0]
        port = hD.hostDic.get(nodeid)[1]
        print("Binding to ip address {} and port {}".format(ipaddress,port))
        input1 = raw_input("Enter the ping message ")
        if(input1!="NO MESSAGE"):
            input2 = int(input("Enter the no. of destinations for message (max 3) ") )
            h1 = Source(input1,input2,nodeid,ipaddress,port)
            print("Sending",input1,"to {} destinations".format(input2))
            h1.sendReceive()
            run()
        
        print("No message to send terminating application")

if __name__ == '__main__':
    run()
