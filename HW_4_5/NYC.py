#The code was run on PYCHARM IDE on WINDOWS python version 3.x
'''
Steps to recreate:
1)Open PYCHARM
2)Create a new project
3) Add a new python file and paste the code
4) Run the code
'''




# Referred https://www.geeksforgeeks.org/stack-and-queues-in-python/
import time


# Declaration of class graph
class graph:

    is_cycle=False

    # Initialization
    def __init__(self, vertices):
        self.V=vertices
        self.graph=[[] for _ in range(vertices)]

    # Adds edges
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # Executes BFS iteratively using queue
    def bfs(self,s):

        visited = [False]*self.V

        queue = []
        res=[]

        queue.append(s)

        visited[s]=True

        while queue:

            # pops the least recently added value
            s = queue.pop(0)
            print(s)

            for i in self.graph[s]:
                res.append(i)
                if not visited[i]:
                    queue.append(i)

                    visited[i]=True

        print(res)

    # Executes DFS iteratively using stack
    def dfs(self,s):

        visited = [False]*self.V

        stack = []

        stack.append(s)

        visited[s]=True

        while stack:

            # pops the most recently added value
            s = stack.pop()
            print(s)

            for i in self.graph[s]:
                if not visited[i]:
                    stack.append(i)
                    visited[i]=True







def main():

    f = open("tinyEWD.txt", "r")
    vertex_count = int(f.readline())
    print('Number of vertices:',vertex_count)
    g = graph(vertex_count)
    edge_count = int(f.readline())
    print('Number of edges:', edge_count)
    for line in f.readlines():
        u = int(line.split(" ")[0])
        v = int(line.split(" ")[1])
        w = float(line.split(" ")[2])
        g.addEdge(u, v)

    print("Executing DFS")

    g.dfs(0)

    print("Executing BFS")

    g.bfs(0)

if __name__ == "__main__":
    main()