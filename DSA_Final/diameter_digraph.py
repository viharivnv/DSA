"""
This code helps us to find the diameter of a Directed acyclic graph i.e. the maximum length shortest path
"""

# The code was run on PYCHARM IDE on WINDOWS python version 3.x
'''
Steps to recreate:
1)Open PYCHARM
2)Create a new project
3) Add a new python file and paste the code
4) Run the code
'''


'''

Test Data:
Save this data into a text file:

8
15
4 5 0.35
5 4 0.35
4 7 0.37
5 7 0.28
7 5 0.28
5 1 0.32
0 4 0.38
0 2 0.26
7 3 0.39
1 3 0.29
2 7 0.34
6 2 0.40
3 6 0.52
6 0 0.58
6 4 0.93

'''

import time

# Declaration of Graph class


class graph:
    rout = []
    is_cycle = False

    # Initialization
    def __init__(self, vertices):

        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

        for i in range(self.V):
            self.rout.append(0)

    # Adds Edge
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Returns the vertex with minimum Distance
    def minDist(self, dist, spt):

        min_dist = float("inf")

        for v in range(self.V):
            if dist[v] < min_dist and not spt[v]:
                min_dist = dist[v]
                index = v

        return index

    # Calculates and returns the diameter of the Digraph
    def diameter(self,dist):
        return max(dist)

    # Returns the path to the destination
    def FindPath(self, parent, j):
        path=[]
        # Computes the path to the destination
        while parent[j]!=-1:
            path.append(j)
            j=parent[j]
        path.append(j)

        return path

    # Runs Dijkstra's Algorithm on the graph from source 's' and returns the diameter and its path length
    def dijkstra(self, s):
        max_path=[]
        max_length=0

        dist = [float("inf")] * self.V

        parent = [-1] * self.V

        dist[s] = 0
        SPT = [False] * self.V

        for x in range(self.V):
            u = self.minDist(dist, SPT)

            SPT[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and SPT[v] is False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    parent[v] = u

        # finds the maximum shortest path
        for i in range(self.V):
            path = self.FindPath(parent, i)

            if max_length < len(path):
                max_length=len(path)
                max_path = path

        return self.diameter(dist),max_path



def main():
    files = ["tinyEWD.txt", "mediumEWD.txt", "1000EWD.txt"]#, "10000EWD.txt"]

    for file in files:

        print('\nFor data set:',file)
        print('Importing the data')
        f = open(file, "r")
        vertex_count = int(f.readline())
        g = graph(vertex_count)
        edge_count = int(f.readline())

        # Adds edges to the graph
        for line in f.readlines():
            u = int(line.split(" ")[0])
            v = int(line.split(" ")[1])
            w = float(line.split(" ")[2])

            g.graph[u][v] = w

        print('\nGraph created successfully')
        max_len = 0
        result = []
        vertex = 0
        print('\nStarting the timer in ns')
        start = time.time_ns()
        # Calls the dijkstra function to calculate diameter with each vertex as starting point
        for i in range(vertex_count):
            pathlen, path = g.dijkstra(i)
            if max_len < pathlen:
                max_len = pathlen
                result = path
                vertex = i

        maxpath = result[::-1]
        stop = time.time_ns()
        print('\nThe results of the algorithm are as below:')
        print('The maximum shortest path in the graph is as below:')
        print(maxpath)
        print('The Diameter ends are as follows:')
        print('The starting point is', vertex, 'and the end point is', maxpath[len(maxpath) - 1])
        print('The length of diameter is', max_len)
        print('Run time of the algorithm is:', stop - start, 'ns')
        print('\n')


if __name__ == "__main__":
    main()




