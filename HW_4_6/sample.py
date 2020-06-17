
import cleanup
from topo5 import topo5
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from packet import *

from printer import *


def dijkstra(graph, src, dest, visited=[], distances={}, predecessors={}):
    """ calculates a shortest path tree routed in src
    """
    # a few sanity checks
    if src not in graph:
        raise TypeError('The root of the shortest path tree cannot be found')
    if dest not in graph:
        raise TypeError('The target of the shortest path cannot be found')
        # ending condition
    if src == dest:
        # We build the shortest path and display it
        path = []
        pred = dest
        while pred != None:
            path.append(pred)
            pred = predecessors.get(pred, None)
        print('shortest path:  ' + str(path) + " cost= " + str(distances[dest]))
        global path2
        path2 = path

    else:
        # if it is the initial  run, initializes the cost
        if not visited:
            distances[src] = 0
        # visit the neighbors
        for neighbor in graph[src]:
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                print(new_distance)
                if new_distance <= distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        # mark as visited
        visited.append(src)
        # now that all neighbors have been visited: recurse
        # select the non visited node with lowest distance 'x'
        # run Dijskstra with src='x'
        unvisited = {}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k, float('inf'))
        x = min(unvisited, key=unvisited.get)
        dijkstra(graph, x, dest, visited, distances, predecessors)




# def dijkstraHelperFunction(topo, src, dst):
#     ''' dijkstra's helper function:
#     makes link dictionary
#     calls dijkstras on it
#     '''
#
#     topoG = topo.g
#
#     graphDic = {}  # empty dictionary
#     for node in topoG.nodes():  # make switch dictionary without links
#         graphDic[node] = {}
#     for edge in topoG.edges():  # adds each link to each switch
#         graphDic[edge[0]][edge[1]] = 1
#         graphDic[edge[1]][edge[0]] = 1
#
#     path = dijkstra(graphDic, src, dst, visited=[], distances={}, predecessors={})
#
#     dpidPath = []
#     for switch in path:
#         dpidPath.append(topo.id_gen(name=switch).dpid)
#
#     return path




#Edited:


def dijkstraTable(topo, src):
    # Routing table creater for each node in network

    # open file for saving paths

    filename = "src.txt"
    f = open(filename, 'w+')

    topoG = topo.g

    graphDic = {}  # empty dictionary
    for node in topoG.nodes():  # make switch dictionary without links
        graphDic[node] = {}
    for edge in topoG.edges():  # adds each link to each switch
        graphDic[edge[0]][edge[1]] = 1
        graphDic[edge[1]][edge[0]] = 1

    # get paths to all other node from src

    for node in graphDic:

        path = dijkstra(graphDic, src, node, visited=[], distances={}, predecessors={})

        dpidPath = []

        # add switch names

        for switch in path:
            dpidPath.append(topo.id_gen(name=switch).dpid)

        # write paths to file for the src

        route = "%s %s \n" % node % path
        f.write(route)

