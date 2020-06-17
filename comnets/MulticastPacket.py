#/usr/bin/python
import time
from socket import socket, AF_INET, SOCK_DGRAM
import struct
import select
import random
import asyncore

def create_datapacket(pkttype, seq, src, ndst, rdst, dst1, dst2, dst3, data):
    """Create a new packet based on given id"""
    # Type(1),  LEN(4), SRCID(1),  DSTID(1), SEQ(4), DATA(1000)
    pktlen = len(data)
    header = struct.pack('BLBBBBBBL', pkttype, pktlen, ndst, rdst, dst1, dst2, dst3, src, seq)
    return header + data




def read_header_datapacket(pkt):
        #Change the bytes to account for network encapsulations


    header = pkt[0:20]
    #pktFormat = "BLBBL"
    #pktSize = struct.calcsize(pktFormat)
    pkttype, pktlen, ndst, rdst, dst1, dst2, dst3, src, seq = struct.unpack("BLBBBBBBL", header)
    return pkttype, pktlen, ndst, rdst, dst1, dst2, dst3, src, seq


def read_data_datapacket(pkt):
        #Change the bytes to account for network encapsulations
    data = pkt[20:]
    return data



def create_dataack(pkttype, seq, src, dest):
    """Create a new packet based on given id"""
    # Type(1),  LEN(4), SRCID(1),  DSTID(1), SEQ(4), DATA(1000)

    header = struct.pack("BBBL", pkttype, dest, src, seq)
    return header

def read_dataack(pkt):
        #Change the bytes to account for network encapsulations


    header = pkt[0:16]
    #pktFormat = "BLBBL"
    #pktSize = struct.calcsize(pktFormat)
    pkttype, dest, src, seq = struct.unpack("BBBL", header)
    return pkttype, dest, src, seq


def create_lsp(pkttype, seq, src, data):
    """Create a new packet based on given id"""
    # Type(1),  LEN(4), SRCID(1),  DSTID(1), SEQ(4), DATA(1000)
    pktlen = len(data)
    header = struct.pack('BLBL', pkttype, pktlen, src, seq)
    return header + data

def read_lspheader(pkt):
        #Change the bytes to account for network encapsulations


    header = pkt[0:16]
    #pktFormat = "BLBBL"
    #pktSize = struct.calcsize(pktFormat)
    pkttype, pktlen, src, seq = struct.unpack("BLBL", header)
    return pkttype, pktlen, src, seq

def read_lspdata(pkt):
        #Change the bytes to account for network encapsulations
    data = pkt[16:]
    return data



def hello(pkttype, seq,src):

    header = struct.pack("BBL", pktype,src,seq)
    return header





#def read(pkt)
#    pkttype, src, seq = struct.unpack("BBL",pkt)
#    return pkttype, src, seq
