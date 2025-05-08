import sys

def dijkstra(graph, src):
    n = len(graph)
    dist = [sys.maxsize] * n
    dist[src] = 0
    sptSet = [False] * n

    for _ in range(n):
        min_dist = sys.maxsize
        u = -1
        for v in range(n):
            if not sptSet[v] and dist[v] < min_dist:
                min_dist = dist[v]
                u = v

        sptSet[u] = True

        for v in range(n):
            if graph[u][v] and not sptSet[v] and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

    print("Vertex \tDistance from Source")
    for i in range(n):
        print(f"{i} \t{dist[i]}")

graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

dijkstra(graph, 0)

