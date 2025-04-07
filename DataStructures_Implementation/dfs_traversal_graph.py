class Graph:
    def __init__(self, verticies):
        self.adjancency_list = [[] for _ in range(verticies)]
        self.verticies = verticies

    def addEdge(self, source, destination):
        self.adjancency_list[source].append(destination)
        self.adjancency_list[destination].append(source)
    
    def DFS(self, startVertex):
        visited = [False] * self.verticies
        stack = []
        stack.append(startVertex)

        while stack:
            current = stack.pop()
            if not visited[current]:
                print(current, end=" ")
                visited[current] = True
            
            for neighbour in self.adjancency_list[current]:
                if not visited[neighbour]:
                    stack.append(neighbour)


if __name__ ==  "__main__":
        g = Graph(5)
        g.addEdge(0, 1)
        g.addEdge(0, 2)
        g.addEdge(0, 3)
        g.addEdge(1, 2)
        g.addEdge(2, 4)

        print("DFS Traversal starting from vertex 0: ", end="")
        g.DFS(0)
