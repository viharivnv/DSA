#!/usr/bin/python



import cleanup
from topo5 import topo5
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from packet import *
from mininet.util import dumpNodeConnections
from printer import *
from client import *
from router1 import *


def lab5():


    '''
    packet=create_packet(3,1,101,102,103,104,105,'data')
    print(packet)
    #pktype, leng, src, dest, seq = read_header(packet)
    print(read_data(packet))
    print(read_header(packet))

    packet2=create_lsp(1,1,108,'data')
    print(packet2)
    #pktype, leng, src, dest, seq = read_header(packet)
    print(read_lspdata(packet2))
    print(read_lspheader(packet2))

    if read_header(packet) > read_lspheader(packet2):
        print('yes')

    packet3=create_ack(1,1,108,103)
    print(packet3)
    #pktype, leng, src, dest, seq = read_header(packet)
    print(read_ack(packet3))
    '''

    f = open("nodes.txt", "w")
    f1 = open("ports.txt", "w")
    net = topo5()
    info('*** Starting network\n')
    net.start()
    hosts = (net.hosts)
    i = 8888
    for host in hosts:
        print(host.IP())
        f.write(host.IP())
        f1.write(str(i))
        i += 10
    k = 0
    m = 8888
    for host in hosts:
        if k <= 1:
            router(host.IP(), m)
        K += 1
        m += 10
    j = 0
    l = 8888
    for host in hosts:
        if j >= 2:
            node_program(host.IP(), l)
        l += 10
        j += 1

    #dumpNodeConnections(net.hosts)


    info( '*** Running CLI\n' )
    CLI( net )




    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    lab5()
