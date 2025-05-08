from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    # Recursive DFS
    def dfs_recursive(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for neighbor in self.adj_list[v]:
            if not visited[neighbor]:
                self.dfs_recursive(neighbor, visited)

    def dfs(self, start):
        visited = [False] * self.vertices
        print("DFS Traversal (Recursive): ", end='')
        self.dfs_recursive(start, visited)
        print()

    # BFS using queue
    def bfs(self, start):
        visited = [False] * self.vertices
        queue = deque()

        visited[start] = True
        queue.append(start)

        print("BFS Traversal: ", end='')

        while queue:
            v = queue.popleft()
            print(v, end=' ')

            for neighbor in self.adj_list[v]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        print()

# Main program
def main():
    V = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))

    g = Graph(V)

    print("Enter edges (u v):")
    for _ in range(E):
        u, v = map(int, input().split())
        g.add_edge(u, v)

    start = int(input("Enter starting vertex for traversal: "))
    g.dfs(start)
    g.bfs(start)

if __name__ == "__main__":
    main()

