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
class graph:

    is_cycle=False

    # Initialization
    def __init__(self, vertices):
        self.V=vertices
        self.graph=[[0 for column in range(vertices)]
                      for row in range(vertices)]


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

    # Runs Dijkstra's Algorithm on the graph from source 's'
    def dijkstra(self,s):

        dist = [float("inf")]*self.V

        dist[s]=0
        SPT=[False]*self.V

        for x in range(self.V):
            u = self.minDist(dist, SPT)

            SPT[u]=True

            for v in range(self.V):
                if self.graph[u][v] > 0 and SPT[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]


        print('Vertex \t Distance from Source:')
        for v in range(self.V):
            print(v,'\t\t ',dist[v])





def main():
    g1 = graph(8)
    g2 = graph(8)
    edge_list1 = [
        (4, 5, 0.35),
        (5, 4, -0.66),
        (4, 7, 0.37),
        (5, 7, 0.28),
        (7, 5, 0.28),
        (5, 1, 0.32),
        (0, 4, 0.38),
        (0, 2, 0.26),
        (7, 3, 0.39),
        (1, 3, 0.29),
        (2, 7, 0.34),
        (6, 2, .4),
        (3, 6, 0.52),
        (6, 0, 0.58),
        (6, 4, .93),
    ]

    for u, v, w in edge_list1:
        g1.graph[u][v] = w

    print("Shortest path from source S=0 for graph 4-b")
    g1.dijkstra(0)

    edge_list = [
        (4, 5, 0.35),
        (5, 4, 0.35),
        (4, 7, 0.37),
        (5, 7, 0.28),
        (7, 5, 0.28),
        (5, 1, 0.32),
        (0, 4, 0.38),
        (0, 2, 0.26),
        (7, 3, 0.39),
        (1, 3, 0.29),
        (2, 7, 0.34),
        (6, 2, -1.20),
        (3, 6, 0.52),
        (6, 0, -1.40),
        (6, 4, -1.25),
    ]

    for u, v, w in edge_list:
        g2.graph[u][v] = w

    print("Shortest path from source S=0 for 4-a")
    g2.dijkstra(0)




if __name__ == "__main__":
    main()




