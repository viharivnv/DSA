from packet import *

from socket import socket, AF_INET, SOCK_DGRAM

i=0
# asks the user to denote the router number
s = socket(AF_INET, SOCK_DGRAM)
#print(addr, port)
s.bind(('192.168.1.2', 8888))

while True:

        #program for router 1 functioning
        packet, r_addr = s.recvfrom(1024)
        #decapsulating the packet
        data = read_data(packet)
        #header = packet[0:18]
        #pkttype,lent, dest, src, seq = read_header(packet)
        pkttype, pktlen, ndst, rdst, dst1, dst2, dst3, src, seq = read_header(packet)
        ndst=int(ndst)
        #forwarding to next hop
        if pkttype==send:
                if r_addr != nexthop(rdst):
                        if ndst==3:
                                if nexthop(dst1)==nexthop(dst2) and nexthop(dst2)==nexthop(dst3):
                                        server=()
                                        print('Received From ',src,'forwarding to', dest1,dest2,dest3, 'squence ', seq, 'Type', pkttype)
                                        forward_p=create_packet(pkttype,seq,src,ndst,rdst,dst1,dst3,data)
                                        s.sendto(forward_p,server)
                                elif nexthop(dst1)==nexthop(dst2) and nexthop(dst2)!=nexthop(dst3):
                                        forward_p1=create_packet(pkttype,seq,src,ndst-1,rdst,dst1,dst2,dst3,data)
                                        server1=()
                                        forward_p2=create_packet(pkttype,seq,src,ndst-2,rdst,dst3,dst2,dst1,data)
                                        server2=()
                                        print('Received From ',src,'forwarding to', dest1,dest2, 'squence ', seq, 'Type', pkttype)
                                        s.sendto(forward_p1,server1)
                                        print('Received From ',src,'forwarding to', dest3, 'squence ', seq, 'Type', pkttype)
                                        s.sendto(forward_p2,server2)
                                elif nexthop(dst1)!=nexthop(dst2) and nexthop(dst2)==nexthop(dst3):
                                        forward_p1=create_packet(pkttype,seq,src,ndst-1,rdst,dst2,dst3,dst3,data)
                                        server1=()
                                        forward_p2=create_packet(pkttype,seq,src,ndst-2,rdst,dst1,dst2,dst3,data)
                                        server2=()
                                        print('Received From ',src,'forwarding to', dest2,dest3, 'squence ', seq, 'Type', pkttype)
                                        s.sendto(forward_p1,server1)
                                        print('Received From ',src,'forwarding to', dest1, 'squence ', seq, 'Type', pkttype)
                                        s.sendto(forward_p2,server2)
                                elif nexthop(dst1)==nexthop(dst3) and nexthop(dst2)!=nexthop(dst3):
                                        forward_p1=create_packet(pkttype,seq,src,ndst-1,rdst,dst1,dst3,dst2,data)
                                        server1=()
                                        forward_p2=create_packet(pkttype,seq,src,ndst-2,rdst,dst2,dst3,dst1,data)
                                        server2=()
                                        print('Received From ',src,'forwarding to', dest1,dest3, 'squence ', seq, 'Type', pkttype)
                                        s.sendto(forward_p1,server1)
                                        print('Received From ',src,'forwarding to', dest2, 'squence ', seq, 'Type', pkttype)
                                        s.sendto(forward_p2,server2)

                                else:
                                        forward_p1=create_packet(pkttype,seq,src,ndst-2,rdst,dst1,dst2,dst3,data)
                                        server1=()
                                        forward_p2=create_packet(pkttype,seq,src,ndst-2,rdst,dst2,dst3,dst1,data)
                                        server2=()

                                        forward_p3=create_packet(pkttype,seq,src,ndst-2,rdst,dst3,dst2,dst1,data)
                                        server3=()
                                        print('Received From ',src,'forwarding to', dest2, 'squence ', seq, 'Type', pkttype)
                                        s.sendto(forward_p1,server1)
                                        print('Received From ',src,'forwarding to', dest2, 'squence ', seq, 'Type', pkttype)
                                        s.sendto(forward_p2,server2)
                                        print('Received From ',src,'forwarding to', dest2, 'squence ', seq, 'Type', pkttype)
                                        s.sendto(forward_p3,server3)



                        elif ndest == 2:
                                if nexthop(dst1)==nexthop(dst2):
                                        server=()
                                        print('Received From ',src,'forwarding to', dest1,dest2, 'squence ', seq, 'Type', pkttype)

                                        forward_p=create_packet(pkttype,seq,src,ndst,rdst,dst1,dst3,data)
                                        s.sendto(forward_p,server)
                                elif nexthop(dst1)!=nexthop(dst2):
                                        print('Received From ',src,'forwarding to', dest1, 'squence ', seq, 'Type', pkttype)
                                        forward_p1=create_packet(pkttype,seq,src,ndst-1,rdst,dst1,dst2,dst3,data)
                                        server1=()
                                        print('Received From ',src,'forwarding to', dest2, 'squence ', seq, 'Type', pkttype)
                                        forward_p2=create_packet(pkttype,seq,src,ndst-1,rdst,dst2,dst3,dst1,data)
                                        server2=()
                                        s.sendto(forward_p1,server1)
                                        s.sendto(forward_p2,server2)

                        elif ndest == 1:
                                        server = ()
                                        print('Received From ',src,'forwarding to', dest1, 'squence ', seq, 'Type', pkttype)
                                        forward_p=create_packet(pkttype,seq,src,ndst,rdst,dst1,dst3,data)
                                        s.sendto(forward_p,server)
