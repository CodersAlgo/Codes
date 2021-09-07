import numpy as np

# Breadth first search in python
# Implementing the queue data structure

class Queue :
    def __init__(self) :
        self.queue = list()

    def enqueue(self,value) :
        self.queue.append(value)

    def dequeue(self) :
        deleted = self.queue[0]
        del self.queue[0]
        return deleted

    def isempty(self) :
        if len(self.queue) == 0 :
            return True
        else :
            return False

# Takes a vertex to strat BFS as argument

def BFS(vertex) :
    visited = np.array([None]*vertices)
    queue = Queue()
    visited[vertex] = 1
    print(vertex)
    queue.enqueue(vertex)

    while not queue.isempty() :
        v = queue.dequeue()

        for x in range(vertices) :
            if adjacency_matrix[v][x] == 1 and visited[x] == None :
                print(x)
                visited[x] = 1
                queue.enqueue(x)

vertices = int(input("enter number of vertices present in graph :- "))

# adjacency_matrix = np.array([[None]*vertices]*vertices)
# for x in range(vertices) :
#     for y in range(vertices) :
#         adjacency_matrix[x][y] = int(input(f"Enter adjacency_matrix[{x}][{y}] = "))

# Uncomment the lines above if you want to take user input
# The input should be in the form of adjacency matrix

adjacency_matrix = [[0,1,1,1,0,0,0],
                    [1,0,1,0,0,0,0],
                    [1,1,0,1,1,0,0],
                    [1,0,1,0,1,0,0],
                    [0,0,1,1,0,1,1],
                    [0,0,0,0,1,0,0],
                    [0,0,0,0,1,0,0]]

# Performing the BFS algorithm on given graph data structure
BFS(0)
