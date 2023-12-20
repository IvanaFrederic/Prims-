import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def prim(self, start):
        visited = set()
        min_spanning_tree = []
        heap = [(0, start, None)]

        while heap:
            weight, current_vertex, previous_vertex = heapq.heappop(heap)

            if current_vertex not in visited:
                visited.add(current_vertex)
                if previous_vertex is not None:
                    min_spanning_tree.append((previous_vertex, current_vertex, weight))

                for neighbor, edge_weight in self.graph[current_vertex]:
                    if neighbor not in visited:
                        heapq.heappush(heap, (edge_weight, neighbor, current_vertex))

        return min_spanning_tree

# Example usage:
g = Graph()
g.add_edge('A', 'B', 2)
g.add_edge('A', 'C', 3)
g.add_edge('B', 'C', 1)
g.add_edge('B', 'D', 4)
g.add_edge('C', 'D', 5)

start_vertex = 'A'
min_spanning_tree = g.prim(start_vertex)

print(f"Minimum Spanning Tree starting from vertex '{start_vertex}':")
for edge in min_spanning_tree:
    print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")
