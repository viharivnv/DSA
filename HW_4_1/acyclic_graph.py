#The code was run on PYCHARM IDE on WINDOWS python version 3.x
'''
Steps to recreate:
1)Open PYCHARM
2)Create a new project
3) Add a new python file and paste the code
4) Run the code
'''


# Referred https://www.geeksforgeeks.org/detect-cycle-undirected-graph/

# class graph declaration and initialization
class graph:

    is_cycle=False

    # Initialization
    def __init__(self, vertices):
        self.V=vertices
        self.graph=[[] for _ in range(vertices)]

    # Addition of edges
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # Function to check if the graph is cyclic
    def is_cyclic(self):

        visited = [False]*(self.V)

        for v in range(self.V):
            if not visited[v]:
                return self.dfs(v, visited)

    # DFS on the graph which checks for loops
    def dfs(self,vertex,visited):

        visited[vertex]=True

        for v in self.graph[vertex]:
            if not visited[v]:
                if self.dfs(v,visited):
                    self.is_cycle = True
            else:
                self.is_cycle = True
        self.is_cycle = False



def main():

    f = open("mediumEWG.txt", "r")
    vertex_count = int(f.readline())
    g = graph(vertex_count)
    edge_count = int(f.readline())

    # creation of graph
    for line in f.readlines():
        u = int(line.split(" ")[0])
        v = int(line.split(" ")[1])
        w = float(line.split(" ")[2])
        g.addEdge(u, v)

    # checks if the graph is cyclic or acyclic
    print('Is the graph acyclic?')
    if g.is_cyclic:
        print('No, the graph is cyclic')
    else:
        print('Yes, the graph is Acyclic')



if __name__ == "__main__":
    main()