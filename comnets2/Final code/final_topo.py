#!/usr/bin/python

from mininet.net import Mininet
from mininet.cli import CLI
from mininet.node import Node
from mininet.link import Link
from mininet.link import TCLink
from mininet.log import setLogLevel, info

def run():







    net = Mininet ( )

    #Create hosts and routers. Also create a switch in case we would like to use
    #above method for sshd services
    info( "Creating nodes\n" )
    #Create switch to use with sshd
    #s1 = net.addSwitch ( 's1' )
    r1 = net.addHost( 'r1' , ip='192.168.1.2/24', inNamespace=False )
    r2 = net.addHost( 'r2' , ip='192.168.2.3/24', inNamespace=False )
    r3 = net.addHost( 'r3' , ip='192.168.1.4/24', inNamespace=False )
    r4 = net.addHost( 'r4' , ip='192.168.1.5/24', inNamespace=False )
    r5 = net.addHost( 'r5' , ip='192.168.5.3/24', inNamespace=False )
    r6 = net.addHost( 'r6' , ip='192.168.3.3/24', inNamespace=False )
    
    h1 = net.addHost( 'h1' , ip='192.168.1.1/24', defaultRoute= 'via 192.168.1.3', inNamespace=False  )
    h2 = net.addHost( 'h2' , ip='192.168.2.1/24', defaultRoute= 'via 192.168.2.2', inNamespace=False )
    h3 = net.addHost( 'h3' , ip='192.168.3.1/24', defaultRoute= 'via 192.168.3.2', inNamespace=False )
    h4 = net.addHost( 'h4' , ip='192.168.4.1/24', defaultRoute= 'via 192.168.4.2', inNamespace=False)
    #Establishing the links from hosts to routers
    info( "Creating links\n" )
    net.addLink( r1, r2)
    net.addLink( r1, r3)
    net.addLink( r3, r4)
    net.addLink( r3, r5)
    net.addLink( r5, r4)
    net.addLink( r6, r5)
    

    #net.addLink( r1, r2)

    net.addLink( h1, r1, intfName2='r1-eth2', params2={'ip' : '192.168.1.3/24' }  )
    net.addLink( h2, r2, intfName2='r2-eth1', params2={'ip' : '192.168.2.2/24' }  )
    net.addLink( h3, r4, intfName2='r4-eth2', params2={'ip' : '192.168.3.2/24' } )
    net.addLink( h4, r6, intfName2='r6-eth1', params2={'ip' : '192.168.4.2/24' } )
#    net.addLink( r1, r2 )

    #Build the specified network
    info( "Building network\n" )
    r1.cmd( 'sysctl net.ipv4.ip_forward=1' )
    r2.cmd( 'sysctl net.ipv4.ip_forward=1' )
    r3.cmd( 'sysctl net.ipv4.ip_forward=1' )
    r4.cmd( 'sysctl net.ipv4.ip_forward=1' )
    r5.cmd( 'sysctl net.ipv4.ip_forward=1' )
    r6.cmd( 'sysctl net.ipv4.ip_forward=1' )
    

    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )


    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    run()
