# Kruskal's Algorithm to find the Minimum Spanning Tree (MST)
def kruskal(vertices, edges):
    # Initialize parent dictionary for Union-Find
    parent = {v: v for v in vertices}

    # Find function with path compression
    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])  # Recursively find the root parent
        return parent[v]

    # Union function to connect two trees
    def union(v1, v2):
        parent[find(v1)] = find(v2)

    mst = []  # List to store edges in MST

    # Sort all edges by weight (ascending order)
    for u, v, w in sorted(edges, key=lambda x: x[2]):
        # If u and v are in different sets, include this edge
        if find(u) != find(v):
            mst.append((u, v, w))  # Add edge to MST
            union(u, v)            # Union the sets

    return mst  # Return the minimum spanning tree
# Define graph vertices
vertices = ['A', 'B', 'C', 'D', 'E']

# Define graph edges as (node1, node2, weight)
edges = [
    ('A', 'B', 1),
    ('A', 'C', 5),
    ('B', 'C', 4),
    ('B', 'D', 2),
    ('C', 'D', 6),
    ('D', 'E', 3)
]

# Call Kruskal's algorithm
mst = kruskal(vertices, edges)

# Display result
print("Minimum Spanning Tree:", mst)
