#The code was run on PYCHARM IDE on WINDOWS python version 3.x
'''
Steps to recreate:
1)Open PYCHARM
2)Create a new project
3) Add a new python file and paste the code
4) Run the code
'''


# Referred https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/


# Referred  https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/

import time


# class graph declaration and initialization
class Graph:

    # Initialization
    def __init__(self, vertices):
        self.V=vertices
        self.Graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    # Function to print MST using Prim's algorithm
    def print_MST(self, parent):
        print(' Edge\t\t  Weight:')
        for i in range(1,self.V):
            print(parent[i],'-',i,'\t\t',self.Graph[i][parent[i]])

    # gives the nearest vertex that is not part of the MST
    def Minkey(self,key, mstset):

        minkey = float("inf")
        min_index=0

        for v in range(self.V):
            if key[v] < minkey and mstset[v]==False:
                minkey = key[v]
                min_index=v

        return min_index

    # Fetches the MST using prim's Algorithm
    def prim_MST(self):

        key=[float("inf")]*self.V

        parent=[]

        for i in range(self.V):
            parent.append(0)

        key[0]=0
        mstset=[False]*(self.V)

        parent[0]=-1

        for count in range(self.V):

            u = self.Minkey(key,mstset)

            mstset[u]=True

            for v in range(self.V):

                if self.Graph[u][v] > 0 and not mstset[v] and key[v] > self.Graph[u][v]:
                    key[v] = self.Graph[u][v]
                    parent[v]=u

        # Prints the MST formed
        self.print_MST(parent)


# class graph declaration and initialization
class graph:

    # Initialization
    def __init__(self, vertices):
        self.V=vertices
        self.graph=[]

    # Addition of edges
    def addEdge(self,u,v,w):
        self.graph.append([u, v, w])

    # checks if the node has any connections
    def find(self, parent,v):
        if parent[v]==v:
            return v
        else:
            return self.find(parent,parent[v])

    # Connects two disjoint nodes
    def union(self,parent, rank, v, u):
        v_root= self.find(parent,v)
        u_root=self.find(parent,u)

        if rank[v_root] < rank[u_root]:
            parent[v_root]=u_root

        elif rank[v_root] > rank[u_root]:
            parent[u_root] = v_root

        else:
            parent[u_root] = v_root
            rank[v_root]+=1

    # Kruskal's algorithm for MST
    def Kruskal_MST(self):

        result=[]

        i=0
        e=0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent=[]
        rank=[]

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e<self.V-1:

            u,v,w = self.graph[i]

            i = i+1
            x = self.find(parent,u)
            y = self.find(parent,v)

            if x != y:
                e += 1
                result.append([u,v,w])
                self.union(parent,rank,v,u)

        print('Minumum spanning tree:')
        print(' Edge\t\t  Weight:')

        for u, v, w in result:
            print(u, '-', v, ' \t ', w)






def main():

    f = open("mediumEWG.txt", "r")
    vertex_count = int(f.readline())
    g = graph(vertex_count)
    G = Graph(vertex_count)
    edge_count = int(f.readline())

    # generation of graph for Prim's and Kruskal's Algorithms
    for line in f.readlines():
        u = int(line.split(" ")[0])
        v = int(line.split(" ")[1])
        w = float(line.split(" ")[2])
        g.addEdge(u, v, w)
        G.Graph[u][v] = w
        G.Graph[v][u] = w

    start=time.time_ns()
    g.Kruskal_MST()
    stop = time.time_ns()

    runtime1=stop-start

    start = time.time_ns()
    G.prim_MST()
    stop = time.time_ns()
    print('Runtime for Kruskal\'s Algorithm is' ,runtime1,'ns')
    runtime2=stop-start
    print('Runtime for Prim\'s Algorithm is' ,runtime2,'ns')



if __name__ == "__main__":
    main()