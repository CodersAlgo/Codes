from queue import Queue

class graphs :

    def __init__(self,vertices) :
        self.vertices = vertices
        self.matrix = [[0 for x in range(0,vertices)] for x in range(0,vertices)] # Adjacency matrix

    def add_edge(self,v1,v2) :
        if v1 < self.vertices and v2 < self.vertices : # Checking if given vertices are present in graph
            self.matrix[v1][v2] = 1 # Adding two edges as it is undirected graph
            self.matrix[v2][v1] = 1
        else :
            print("Given vertices not present in the graph")

    def del_edge(self,v1,v2) :
        if v1 < self.vertices and v2 < self.vertices : # Checking if given vertices are present in graph
            self.matrix[v1][v2] = 0 # Removing two edges as it is undirected graph
            self.matrix[v2][v1] = 0
        else :
            print("Given vertices not present in the graph")

    def __get_path_bfs_helper(self,v1,v2) :
        q = Queue()
        q.put(v1)
        parent = {}
        while not q.empty() :
            vertex = q.get()
            for x in range(self.vertices) :
                if self.matrix[vertex][x] == 1 and self.visited[x] == 0 :
                    self.visited[x] = 1
                    q.put(x)
                    parent[x] = vertex
                    if x == v2 :
                        print(x)
                        break
        if parent.get(v2,-1) != -1 :
            for x in range(len(parent)) :
                v2 = parent.get(v2,-1)
                if v2 != -1 :
                    print(v2)
                else :
                    return
        print("None")

    def get_path_bfs(self,v1,v2) :
        self.visited = [0]*self.vertices
        self.visited[v1] = 1
        self.__get_path_bfs_helper(v1,v2)



g = graphs(6)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,3)
g.add_edge(2,4)
g.add_edge(3,5)
g.add_edge(4,5)
g.get_path_bfs(0,5)
