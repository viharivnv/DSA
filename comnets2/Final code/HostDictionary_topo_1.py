#!/usr/bin/python
#Topology for Assignment 5 Comnetii ECE423/544
#Author: Sanyam Jain
packetType={'data':4,'dataAck':5}
hostDic = {151:['192.168.1.1',1024],102:['192.168.2.1',1025],103:['192.168.3.1',1026], 201:['192.168.1.2',8089], 202:['192.168.2.3',8090]}
RoutingTables={201: [{202: {'path': 202, 'cost': 1}}, {103: {'path': 202, 'cost': 2}}, {102: {'path': 202, 'cost': 2}}, {151: {'path': 151, 'cost': 1}}], 202: [{201: {'path': 201, 'cost': 1}}, {103: {'path': 103, 'cost': 1}}, {102: {'path': 102, 'cost': 1}}, {151: {'path': 201, 'cost': 2}}], 151: [{201: {'path': 201, 'cost': 1}}, {202: {'path': 201, 'cost': 2}}, {103: {'path': 201, 'cost': 3}}, {102: {'path': 201, 'cost': 3}}], 102: [{201: {'path': 202, 'cost': 2}}, {202: {'path': 202, 'cost': 1}}, {103: {'path': 202, 'cost': 2}}, {151: {'path': 202, 'cost': 3}}], 103: [{201: {'path': 202, 'cost': 2}}, {202: {'path': 202, 'cost': 1}}, {102: {'path': 202, 'cost': 2}}, {151: {'path': 202, 'cost': 3}}]}
MulticastTable={201: {'Totalcost': 4, 'cost': '2,2', 'hosts': '102,103', 'number': 2}, 202: {'Totalcost': 2, 'cost': '1,1', 'hosts': '102,103', 'number': 2}}
