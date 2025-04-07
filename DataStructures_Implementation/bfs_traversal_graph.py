from collections import defaultdict, deque
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjancency_list = defaultdict(list)
    
    def addEdge(self, source, destination):
        self.adjancency_list[source].append(destination)
        self.adjancency_list[destination].append(source)
    
    def BFS(self, startVertex):
        visited = [False]*self.vertices
        queue = deque()
        visited[startVertex] = True
        queue.append(startVertex)

        while queue:
            current = queue.popleft()
            print(current, end=" ")

            for neighbour in self.adjancency_list[current]:
                if not visited[neighbour]:
                    queue.append(neighbour)
                    visited[neighbour] = True

if __name__ ==  "__main__":
        g = Graph(5)
        g.addEdge(0, 1)
        g.addEdge(0, 2)
        g.addEdge(0, 3)
        g.addEdge(1, 2)
        g.addEdge(2, 4)

        print("BFS Traversal starting from vertex 0: ", end="")
        g.BFS(0)