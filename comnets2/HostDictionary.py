#!/usr/bin/python
#Topology for Assignment 5 Comnetii ECE423/544
#Author: Sanyam Jain
hostDic = {151:['localhost',1024],102:['localhost',1025],103:['localhost',1026], 201:['localhost',8089], 202:['localhost',8090]}
RoutingTables={151: [{201: {'path': 201, 'cost': 1}}, {202: {'path': 201, 'cost': 2}}, {102: {'path': 201, 'cost': 3}}, {103: {'path': 201, 'cost': 3}}], 201: [{151: {'path': 151, 'cost': 1}}, {202: {'path': 202, 'cost': 1}}, {102: {'path': 202, 'cost': 2}}, {103: {'path': 202, 'cost': 2}}], 202: [{151: {'path': 201, 'cost': 2}}, {201: {'path': 201, 'cost': 1}}, {102: {'path': 102, 'cost': 1}}, {103: {'path': 103, 'cost': 1}}], 102: [{151: {'path': 202, 'cost': 3}}, {201: {'path': 202, 'cost': 2}}, {202: {'path': 202, 'cost': 1}}, {103: {'path': 202, 'cost': 2}}], 103: [{151: {'path': 202, 'cost': 3}}, {201: {'path': 202, 'cost': 2}}, {202: {'path': 202, 'cost': 1}}, {102: {'path': 202, 'cost': 2}}]}
MulticastTable={201: {'number': 2, 'hosts': '102,103', 'Totalcost': 4}, 202: {'number': 2, 'hosts': '102,103', 'Totalcost': 2}}
