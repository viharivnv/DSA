# Efficient python3 program to find out Eulerian path

# Function to find out the path
# It takes the adjacency matrix representation of the
# graph as input
def findpath(graph):
    n = len(graph)
    numofadj = list()

    # Find out number of edges each vertex has
    for i in range(n):
        numofadj.append(sum(graph[i]))

    # Find out how many vertex has odd number edges
    startpoint = 0
    numofodd = 0
    for i in range(n - 1, -1, -1):
        if (numofadj[i] % 2 == 1):
            numofodd += 1
            startpoint = i

        # If number of vertex with odd number of edges
    # is greater than two return "No Solution".
    if (numofodd > 2):
        print("No Solution")
        return

    # If there is a path find the path
    # Initialize empty stack and path
    # take the starting current as discussed
    stack = list()
    path = list()
    cur = startpoint

    # Loop will run until there is element in the stack
    # or current edge has some neighbour.
    while (stack != [] or sum(graph[cur]) != 0):

        # If current node has not any neighbour
        # add it to path and pop stack
        # set new current to the popped element
        if (sum(graph[cur]) == 0):
            path.append(cur + 1)
            cur = stack.pop(-1)

        # If the current vertex has at least one
        # neighbour add the current vertex to stack,
        # remove the edge between them and set the
        # current to its neighbour.
        else:
            for i in range(n):
                if graph[cur][i] == 1:
                    stack.append(cur)
                    graph[cur][i] = 0
                    graph[i][cur] = 0
                    cur = i
                    break
    # print the path
    for ele in path:
        print(ele, "-> ", end='')
    print(cur + 1)


# Driver Program
# Test case 1
graph1 = [[0, 1, 0, 0, 1],
          [1, 0, 1, 1, 0],
          [0, 1, 0, 1, 0],
          [0, 1, 1, 0, 0],
          [1, 0, 0, 0, 0]]
findpath(graph1)

# Test case 2
graph2 = [[0, 1, 0, 1, 1],
          [1, 0, 1, 0, 1],
          [0, 1, 0, 1, 1],
          [1, 1, 1, 0, 0],
          [1, 0, 1, 0, 0]]
findpath(graph2)

# Test case 3
graph3 = [[0, 1, 0, 0, 1],
          [1, 0, 1, 1, 1],
          [0, 1, 0, 1, 0],
          [0, 1, 1, 0, 1],
          [1, 1, 0, 1, 0]]
findpath(graph3)
