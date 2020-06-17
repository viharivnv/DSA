#Topology for Assignment 5 Comnetii ECE423/544
#Author: Sanyam Jain
from socket import socket, AF_INET, SOCK_DGRAM
import MulticastPacket as p
import HostDictionary as hD

class Host1:

    def __init__(self,msg,numberOfDest):
        self.num = numberOfDest
        self.msg = msg

    def sendReceive(self):
        currentNode=151
        s = socket(AF_INET, SOCK_DGRAM)
        s.bind(('localhost',1024))
        router = ('localhost',8089)
        print("Connected to server ",router)
        s.sendto(p.create_datapacket(1,1,currentNode,self.num,201,102,103,000,self.msg.encode('utf-8')),router)
        data, addr = s.recvfrom(1024)
        if data and p.read_dataack(data)[0]==5 and p.read_dataack(data)[1]==currentNode:
            print("Received acknowledgement form {}".format(p.read_dataack(data)[2]))
        else :
            print("No Acknowledgement received")
        s.close()

def run():
        input1 = input("Enter the ping message ")
        if(input1!="NO MESSAGE"):
            input2 = int(input("Enter the no. of destinations for message ") )
            h1 = Host1(input1,input2)
            print("Sending",input1,"to {} destinations".format(input2))
            h1.sendReceive()
            run()
        
        print("No message to send terminating application")

if __name__ == '__main__':
    run()
