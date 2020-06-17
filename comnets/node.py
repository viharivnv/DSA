from packet import *


from socket import socket, AF_INET, SOCK_DGRAM


c=0
def node_program(add,port):

        s = socket(AF_INET, SOCK_DGRAM)
        s.bind((add,port))

        print(ipaddr)
        server = ('192.168.1.2', 8888)

        src=101
        dest=input('Enter the destination:\n')
        data='This is assignment 6!'


        i=1

        while i<=100:

                # send(i) #calls send function with i as argument
                i+=1

        print('number of messages sent:',c)

        #creates and send the packets
def send(i):
          global c
          c+=1
          print('sending sequence:',i)
          packet = create_packet(1,src,dest,i,data )# creates the packet with the given data and sequence number
          s.sendto(packet, server)


#checks if the recieved packet is a proper acknowledgement
def check(packet, n):
    pktype, length, dest, src, seq =read_header(packet)
    if seq == n:
       return True
    else:
       return False

i=1

while i<=100:

     # send(i) #calls send function with i as argument
      i+=1

print('number of messages sent:',c)
