#!/usr/bin/python
#Topology for Assignment 5 Comnetii ECE423/544
#Author: Sanyam Jain
from socket import socket, AF_INET, SOCK_DGRAM
import sys
import MulticastPacket as p
import HostDictionary as hD
import Routing as rOut

class Router:
    
    def __init__(self,nodeid,ip,port):
        self.nodeid = nodeid
        self.ip = ip
        self.port = port

    def sendReceive(self):
        r=rOut.Routing()
        typeData=hD.packetType.get('data')
        s = socket(AF_INET, SOCK_DGRAM)
        s.bind((self.ip, self.port))
        currentnode=self.nodeid
        try:
            while(True):
                data, addr = s.recvfrom(1024)                
                print("Header of packet ", p.read_header_datapacket(data))
                print("Message in the packet ", p.read_data_datapacket(data).decode('utf-8'))
                pkttype, pktlen, ndest, rdest, dest1, dest2, dest3, src, seq = p.read_header_datapacket(data)
                msg= p.read_data_datapacket(data)
                if pkttype==typeData:
                    self.sendAck(currentnode,addr,s)  
                    if currentnode!=rdest and rdest!=0:
                        self.send(pkttype,seq,src,ndest,rdest,dest1,dest2,dest3,msg,currentnode,rdest,s)
                    else:
                        rdest=0
                        if ndest==3:
                            if r.nexthop(currentnode,dest1)==r.nexthop(currentnode,dest2) and r.nexthop(currentnode,dest2)==r.nexthop(currentnode,dest3):
                                self.send(pkttype,seq,src,ndest,rdest,dest1,dest2,dest3,msg,currentnode,dest1,s)
                            elif r.nexthop(currentnode,dest1)==r.nexthop(currentnode,dest2) and r.nexthop(currentnode,dest2)!=r.nexthop(currentnode,dest3):
                                self.send(pkttype,seq,src,ndest-1,rdest,dest1,dest2,000,msg,currentnode,dest1,s)
                                self.send(pkttype,seq,src,ndest-2,rdest,dest3,000,000,msg,currentnode,dest3,s)                            
                            elif r.nexthop(currentnode,dest1)!=r.nexthop(currentnode,dest2) and r.nexthop(currentnode,dest2)==r.nexthop(currentnode,dest3): 
                                self.send(pkttype,seq,src,ndest-1,rdest,dest2,dest3,000,msg,currentnode,dest2,s)
                                self.send(pkttype,seq,src,ndest-2,rdest,dest1,000,000,msg,currentnode,dest1,s) 
                            elif r.nexthop(currentnode,dest1)!=r.nexthop(currentnode,dest2) and r.nexthop(currentnode,dest1)==r.nexthop(currentnode,dest3): 
                                self.send(pkttype,seq,src,ndest-1,rdest,dest1,dest3,000,msg,currentnode,dest1,s)
                                self.send(pkttype,seq,src,ndest-2,rdest,dest2,000,000,msg,currentnode,dest2,s)                            
                            else:
                                self.send(pkttype,seq,src,ndest-2,rdest,dest1,000,000,msg,currentnode,dest1,s)
                                self.send(pkttype,seq,src,ndest-2,rdest,dest2,000,000,msg,currentnode,dest2,s)
                                self.send(pkttype,seq,src,ndest-2,rdest,dest3,000,000,msg,currentnode,dest3,s)                                                  
    
                        elif ndest == 2:
                            if r.nexthop(currentnode,dest1)==r.nexthop(currentnode,dest2):
                                self.send(pkttype,seq,src,ndest,rdest,dest1,dest2,000,msg,currentnode,dest1,s)                           
                            elif r.nexthop(currentnode,dest1)!=r.nexthop(currentnode,dest2):
                                self.send(pkttype,seq,src,ndest-1,rdest,dest1,000,000,msg,currentnode,dest1,s)
                                self.send(pkttype,seq,src,ndest-1,rdest,dest2,000,000,msg,currentnode,dest2,s)
                            
                        elif ndest == 1:
                            self.send(pkttype,seq,src,ndest,rdest,dest1,000,000,msg,currentnode,dest1,s)
                        
        except KeyboardInterrupt:
            s.close()
            print('interrupted!')
        
    def send(self,pkttype,seq,src,ndest,rdest,dest1,dest2,dest3,msg,currentnode,dest,s):
            r=rOut.Routing()
            packet=p.create_datapacket(pkttype,seq,src,ndest,rdest,dest1,dest2,dest3,msg)
            print('Received From',src,' forwarding to ',r.nexthop(currentnode,dest1), " for destinations ", dest1,dest2,dest3, 'squence ', seq, 'Type', pkttype)
            s.sendto(packet,(hD.hostDic[r.nexthop(currentnode,dest)][0],hD.hostDic[r.nexthop(currentnode,dest)][1]))
            data, addr = s.recvfrom(1024)
            if data and p.read_dataack(data)[0]==hD.packetType.get('dataAck') and p.read_dataack(data)[1]==currentnode :
                print("Received acknowledgement form {}".format(p.read_dataack(data)[2]))

     
    def sendAck(self,currentnode,addr,s):
            r=rOut.Routing()
            seq=1
            ackPacket=p.create_dataack(hD.packetType.get('dataAck'),seq,currentnode,r.getNodeIdFromPort(addr[1]))
            s.sendto(ackPacket,addr)
            

def run():
    nodeid = int(sys.argv[1])
    ipaddress = hD.hostDic.get(nodeid)[0]
    port = hD.hostDic.get(nodeid)[1]
    print("Binding to ip address {} and port {}".format(ipaddress,port))
    R = Router(nodeid,ipaddress,port)
    R.sendReceive()

if __name__ == '__main__':
    run()
