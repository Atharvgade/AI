from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # since it's an undirected graph

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        print(start, end=' ')
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)
                queue.extend([neighbor for neighbor in self.graph[vertex] if neighbor not in visited])

if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)
    g.add_edge(3, 6)
    g.add_edge(4, 7)
    g.add_edge(4, 8)
    g.add_edge(5, 9)

    print("DFS Traversal:")
    g.dfs(1)
    print("\nBFS Traversal:")
    g.bfs(1)
