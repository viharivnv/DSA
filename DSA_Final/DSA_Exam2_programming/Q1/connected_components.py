# The code was run on PYCHARM IDE on WINDOWS python version 3.x
'''
Steps to recreate:
1)Open PYCHARM
2)Create a new project
3) Add a new python file and paste the code
4) Run the code
'''

import time


# Global declaration of the count which can be used as the id of a component
count=0

# Stores the component id of each vertex
id_count=[]

# Stores the mapping of component id with the vertex
id_={}


# Runs dfs and find the connected components and their count
def dfs(graph):

    global id_
    global count
    visited = set()
    stack=[]

    # Run dfs on each vertex of the graph
    for i in graph:

        # Executes only if the Vertex i is not visited
        if i not in visited:

            # add it to the set visited and the stack used for dfs
            visited.add(i)
            stack.append(i)

            # if the stack is not empty
            while stack:

                # pops the most recently added value
                s = stack.pop()
                # add the count i.e. the component id tp id_count and map it to the component in id_
                id_count.append(count)
                id_.setdefault(s, []).append(count)

                # Try to reach all other neighbor vertices
                for next in graph[s]:

                    # if the neighbor vertex is not visited mark it as visited and add it to the stack
                    if next not in visited:

                        stack.append(next)
                        visited.add(next)

            count += 1


def main():
    graph = {}

    file=open ("movies.txt", "r", encoding='utf-8')

    print('\nImporting data from movies.txt')

    check2 = 1
    check=0

    # tries to read and store all the readable vertices from the text file provided
    while (True):
        check+=1
        fp = file.readline()

        if not fp:
            break
        else:
            fp = fp.split('/')
            for i in range(1, len(fp)):
                graph.setdefault(fp[0], []).append((fp[i]))
                graph.setdefault(fp[i], []).append((fp[0]))




    #print(check,check2)
    print('\nGraph created successfully for nearly',check,'movies and the performers of each movie')
    print('\nStarting the timer in nano seconds')
    start=time.time_ns()

    # Calls dfs on the graph created from the data set
    dfs(graph)
    print('Number of vertices visited:',len(id_))
    print('\nThe total number of connected components in the given graph is',count)
    print('Time taken to run DFS on the graph is',time.time_ns()-start,'ns')
    components_count={i: id_count.count(i) for i in id_count}
    #print(components_count)
    maximum = max(components_count.values())  # Just use 'min' instead of 'max' for minimum.
    print('The size of the largest component is',maximum)
    c10=sum(1 for i in components_count.values() if i<10)
    # for x in components_count.keys():
    #     if components_count[x]<10:
    #         print(x)
    #         print(components_count[x])
    print('A total of',c10,'components have size less than 10')
    stop=time.time_ns()
    print('The total runtime after the graph is created is',stop-start,'ns')


if __name__ == "__main__":
    main()




