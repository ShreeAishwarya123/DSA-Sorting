class Graph:
    
    def __init__(self, edges, num_vertices):
        self.adj_list = [[] for _ in range(num_vertices)]
        self.indegree = [0] * num_vertices
        
        for (src, dest) in edges:
            self.adj_list[src].append(dest)
            self.indegree[dest] += 1

def find_topological_orders(graph, current_path, visited, num_vertices):
    for vertex in range(num_vertices):
        if graph.indegree[vertex] == 0 and not visited[vertex]:
            for neighbor in graph.adj_list[vertex]:
                graph.indegree[neighbor] -= 1
            
            current_path.append(vertex)
            visited[vertex] = True
            
            find_topological_orders(graph, current_path, visited, num_vertices)
            
            for neighbor in graph.adj_list[vertex]:
                graph.indegree[neighbor] += 1
            
            current_path.pop()
            visited[vertex] = False
            
    if len(current_path) == num_vertices:
        print(current_path)

def print_all_topological_orders(graph):
    num_vertices = len(graph.adj_list)
    visited = [False] * num_vertices
    current_path = []
    find_topological_orders(graph, current_path, visited, num_vertices)

if __name__ == '__main__':
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (4, 5)]
    
    print("All Topological Sorts:")
    
    num_vertices = 6
    graph = Graph(edges, num_vertices)
    
    print_all_topological_orders(graph)
