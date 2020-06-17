#The code was run on PYCHARM IDE on WINDOWS python version 3.x
'''
Steps to recreate:
1)Open PYCHARM
2)Create a new project
3) Add a new python file and paste the code
4) Run the code
'''



# Referred https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
import time



# Declaration of Graph class
from sys import maxsize


class graph:
    rout = []
    is_cycle=False

    # Initialization
    def __init__(self, vertices):
        global rout
        self.V=vertices
        self.graph=[[0 for column in range(vertices)]
                      for row in range(vertices)]

        for i in range(self.V):
            self.rout.append(0)



    # Adds Edge
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # Returns the vertex with minimum Distance
    def minDist(self,dist,spt):

        min_dist = float("inf")

       
        for v in range(self.V):
            if dist[v] < min_dist and not spt[v]:
                min_dist = dist[v]
                index = v

        return index

    def printPath(self, parent, j):

        # Base Case : If j is source
        if parent[j] == -1:
            print(j,)
            return
        self.printPath(parent, parent[j])
        print(j, )

    # Runs Dijkstra's Algorithm on the graph from source 's'
    def dijkstra(self,s):

        dist = [float("inf")]*self.V

        parent = [-1] * self.V



        dist[s]=0
        SPT=[False]*self.V

        for x in range(self.V):
            u = self.minDist(dist, SPT)

            SPT[u]=True

            for v in range(self.V):
                if self.graph[u][v] > 0 and SPT[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    parent[v]=u

        print(v)
        self.printPath(parent, v)


        print('Vertex \t Distance from Source:')
        for v in range(self.V):
            print(v,'\t\t ',dist[v])
            self.rout[v]=dist[v]

        return self.rout






def main():


    f = open("10000EWD.txt", "r")
    vertex_count = int(f.readline())
    g = graph(vertex_count)
    edge_count = int(f.readline())

    for line in f.readlines():
        u = int(line.split(" ")[0])
        v = int(line.split(" ")[1])
        w = float(line.split(" ")[2])

        g.graph[u][v] = w

    print("Shortest path from source S=0 for 4-a")
    for i in range(8):
        print('source',i)
        g.dijkstra(i)






if __name__ == "__main__":
    main()




