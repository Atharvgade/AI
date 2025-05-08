class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    parent[xroot] = yroot

def kruskal(edges, n):
    edges.sort(key=lambda edge: edge.weight)
    parent = [i for i in range(n)]

    print("Edge \tWeight")
    for edge in edges:
        x = find(parent, edge.src)
        y = find(parent, edge.dest)

        if x != y:
            print(f"{edge.src} - {edge.dest} \t{edge.weight}")
            union(parent, x, y)

edges = [
    Edge(0, 1, 10),
    Edge(0, 2, 6),
    Edge(0, 3, 5),
    Edge(1, 3, 15),
    Edge(2, 3, 4)
]
n = 4
kruskal(edges, n)

