import HostDictionary as hD
import sys
import os

class Routing:
    
    def __init__(self,method):{}

        
    def dijkstra(self,graph, src, dest, visited=[], distances={}, predecessors={}):
        """ calculates a shortest path tree routed in src"""
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
            #print('shortest path:  ' + str(path[len(path) - 2]) + " cost= " + str(distances[dest]))
            p = path[len(path) - 2]
            h = distances[dest]
            
            global path2
            path2 = path
            return p, h
        
        else:
            # if it is the initial  run, initializes the cost
            if not visited:
                distances[src] = 0
            # visit the neighbors
            for neighbor in graph[src]:
                if neighbor not in visited:
                    new_distance = distances[src] + graph[src][neighbor]
                    #print(new_distance)
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
            return(self.dijkstra(graph, x, dest, visited, distances, predecessors))
            
            
    def createRoutingTable(self):
        i=int(input("Enter number of nodes"))
        RouterDictionary = {}
        router={}
        for x in range(i):
            temp={}
            a=int(input("Enter node id for node {} ".format(x+1)))
            b=int(input("Enter number of neighbors for node {} ".format(x+1)))
            for r in range(b):
                c=int(input("Enter node id for neigbhour {} ".format(r+1)))
                temp[c]=1
            router[a]=temp
        
        for key in router.keys():
            a = []    
            for key1 in router.keys():
                visited = []
                distances = {}
                predecessors = {}
                if (key1 != key):
                    p, b = Routing.dijkstra(self,router, key, key1, visited, distances, predecessors)
                    temp = {}
                    temp1 = {}
                    temp1['path'] = p
                    temp1['cost'] = b
                    temp[key1] = temp1
                    a.append(temp)
            RouterDictionary[key] = a
        print(RouterDictionary)
        file1 = open(r'C:\Users\vihar\PycharmProjects\comnets\HostDictionary.py', 'a')
        s="RoutingTables="+str(RouterDictionary)+"\n"
        file1.write(s)
        file1.close()
        self.multicastrouter(RouterDictionary)
    

    def multicastrouter(self,RoutingTables):
        multicastTable = {}
        #RoutingTables = {151: [{201: {'path': 201, 'cost': 1}}, {202: {'path': 201, 'cost': 2}}, {102: {'path': 201, 'cost': 3}}, {103: {'path': 201, 'cost': 3}}], 201: [{151: {'path': 151, 'cost': 1}}, {202: {'path': 202, 'cost': 1}}, {102: {'path': 202, 'cost': 2}}, {103: {'path': 202, 'cost': 2}}], 202: [{151: {'path': 201, 'cost': 2}}, {201: {'path': 201, 'cost': 1}}, {102: {'path': 102, 'cost': 1}}, {103: {'path': 103, 'cost': 1}}], 102: [{151: {'path': 202, 'cost': 3}}, {201: {'path': 202, 'cost': 2}}, {202: {'path': 202, 'cost': 1}}, {103: {'path': 202, 'cost': 2}}], 103: [{151: {'path': 202, 'cost': 3}}, {201: {'path': 202, 'cost': 2}}, {202: {'path': 202, 'cost': 1}}, {102: {'path': 202, 'cost': 2}}]}
        rTables=RoutingTables
        print(rTables)
        for i in rTables.keys():
            if int(i/200)==1:
                outlist = {}
                Temp = rTables.get(i)
                number = 0
                Totalcost = 0
                hosts = ""
                for j in range(len(Temp)):
                    if int(list(Temp[j].keys())[0]/100)==1 and list(Temp[j].keys())[0]<=150:
                        Temp1 = list(Temp[j].values())
                        if Temp1[0]['cost'] <= 3:
                            number = number + 1
                            Totalcost = Totalcost + Temp1[0]['cost']
                            if hosts != "":
                                hosts = hosts + ","
                            hosts = hosts + str(list(Temp[j].keys())[0])
                outlist["number"] = number
                outlist["hosts"] = hosts
                outlist["Totalcost"] = Totalcost
                multicastTable[i] = outlist
        print(multicastTable)
        file1 = open(r'C:\Users\vihar\PycharmProjects\comnets\HostDictionary.py', 'a')
        s="MulticastTable="+str(multicastTable)+"\n"
        file1.write(s)
        file1.close()
    
    def multicast(self,numberOfDest):
        k = numberOfDest    
        cost = 0
        number = 0
        bestRouter = {}
        multicastTable=hD.MulticastTable
        for i in multicastTable.keys():
            if multicastTable[i]['number'] >= k:
                if cost == 0 and number == 0:
                    cost = multicastTable[i]['Totalcost']
                    number = multicastTable[i]['number']
                elif multicastTable[i]['Totalcost'] < cost:
                    bestRouter = {}
                    cost = multicastTable[i]['Totalcost']
                    number = multicastTable[i]['number']
                    bestRouter[i] = multicastTable[i]
                elif multicastTable[i]['Totalcost'] == cost and multicastTable[i]['number'] > number:
                    bestRouter = {}
                    cost = multicastTable[i]['Totalcost']
                    number = multicastTable[i]['number']
                    bestRouter[i] = multicastTable[i]
        return(bestRouter)
                
    
    def nexthop(self,src,dest):
        #RoutingTables = {151: [{201: {'path': 201, 'cost': 1}}, {202: {'path': 201, 'cost': 2}}, {102: {'path': 201, 'cost': 3}}, {103: {'path': 201, 'cost': 3}}], 201: [{151: {'path': 151, 'cost': 1}}, {202: {'path': 202, 'cost': 1}}, {102: {'path': 202, 'cost': 2}}, {103: {'path': 202, 'cost': 2}}], 202: [{151: {'path': 201, 'cost': 2}}, {201: {'path': 201, 'cost': 1}}, {102: {'path': 102, 'cost': 1}}, {103: {'path': 103, 'cost': 1}}], 102: [{151: {'path': 202, 'cost': 3}}, {201: {'path': 202, 'cost': 2}}, {202: {'path': 202, 'cost': 1}}, {103: {'path': 202, 'cost': 2}}], 103: [{151: {'path': 202, 'cost': 3}}, {201: {'path': 202, 'cost': 2}}, {202: {'path': 202, 'cost': 1}}, {102: {'path': 202, 'cost': 2}}]}
        RoutingTables = hD.RoutingTables
        if src in RoutingTables.keys():
           Temp = RoutingTables.get(src)
           for j in range(len(Temp)):
               if dest in Temp[j].keys():
                   Temp1 = list(Temp[j].values())
                   return Temp1[0]['path']
    
    
    
def run():   
    R1 = Routing(sys.argv[1])
    if (sys.argv[1] == "createRoutingTable"):
        R1.createRoutingTable()

if __name__ == '__main__':
    run()
        
#    #multicastrouter()
#    #multicast()
#    src=input("source")
#    dest=input("dest")
#    x=nexthop(src,dest)
#    print(x)