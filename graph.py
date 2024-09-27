class Graph:
    def __init__(self, is_directed=False):
        self.graph = {}  
        self.is_directed = is_directed  

    def add_Vertex(self, vertex):
       
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_Edge(self, source, destination):
        
        self.add_Vertex(source)
        self.add_Vertex(destination)

       
        self.graph[source].append(destination)

        
        if not self.is_directed:
            self.graph[destination].append(source)

    def displayGraph(self):
        
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

    def bfs(self, startVertex):
        queue = [startVertex]
        visited = {startVertex: True}

        while queue:
            currentVertex = queue.pop(0)
            print(currentVertex, end=' ')

            for neighbor in self.graph[currentVertex]:
                if neighbor not in visited:
                    visited[neighbor] = True
                    queue.append(neighbor)

    def dfs(self, vertex, visited):
        if vertex not in visited:
            print(vertex, end=' ')
            visited[vertex] = True

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)


G = Graph(is_directed=False)  
G.add_Edge('A', 'C')
G.add_Edge('B', 'D')
G.add_Edge('E', 'C')
G.add_Edge('C', 'A')
G.add_Edge('B', 'F')
G.add_Edge('D', 'A')

G.displayGraph()
print("Order after traversing by breadth:")
G.bfs('A')
visited = {}
print("\nOrder after traversing by depth:")
G.dfs('A', visited)
