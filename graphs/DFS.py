import numpy as np

def DFS(vertex) :
    if visited[vertex] == None :
        print(vertex)
        visited[vertex] = 1
        for x in range(vertices) :
            if visited[x] == None and adjacency_matrix[vertex][x] == 1 :
                DFS(x)
    else :
        return

vertices = int(input("enter number of vertices present in graph :- "))
# adjacency_matrix = np.array([[None]*vertices]*vertices)
# for x in range(vertices) :
#     for y in range(vertices) :
#         adjacency_matrix[x][y] = int(input(f"Enter adjacency_matrix[{x}][{y}] = "))

visited = np.array([None]*vertices)

adjacency_matrix = [[0,1,1,1,0,0,0],
                    [1,0,1,0,0,0,0],
                    [1,1,0,1,1,0,0],
                    [1,0,1,0,1,0,0],
                    [0,0,1,1,0,1,1],
                    [0,0,0,0,1,0,0],
                    [0,0,0,0,1,0,0]]

DFS(0)
