#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int minDistance(vector<int>& dist, vector<bool>& sptSet, int n) {
    int min = INT_MAX, min_index;

    for (int v = 0; v < n; v++)
        if (!sptSet[v] && dist[v] <= min)
            min = dist[v], min_index = v;

    return min_index;
}

void dijkstra(vector<vector<int>>& graph, int src) {
    int n = graph.size();
    vector<int> dist(n, INT_MAX);
    vector<bool> sptSet(n, false);

    dist[src] = 0;

    for (int count = 0; count < n-1; count++) {
        int u = minDistance(dist, sptSet, n);
        sptSet[u] = true;

        for (int v = 0; v < n; v++)
            if (!sptSet[v] && graph[u][v] && dist[u] != INT_MAX 
                && dist[u] + graph[u][v] < dist[v])
                dist[v] = dist[u] + graph[u][v];
    }

    cout << "Vertex \tDistance from Source\n";
    for (int i = 0; i < n; i++)
        cout << i << "\t" << dist[i] << endl;
}

int main() {
    vector<vector<int>> graph = {
        {0, 4, 0, 0, 0, 0, 0, 8, 0},
        {4, 0, 8, 0, 0, 0, 0, 11, 0},
        {0, 8, 0, 7, 0, 4, 0, 0, 2},
        {0, 0, 7, 0, 9, 14, 0, 0, 0},
        {0, 0, 0, 9, 0, 10, 0, 0, 0},
        {0, 0, 4, 14, 10, 0, 2, 0, 0},
        {0, 0, 0, 0, 0, 2, 0, 1, 6},
        {8, 11, 0, 0, 0, 0, 1, 0, 7},
        {0, 0, 2, 0, 0, 0, 6, 7, 0}
    };

    dijkstra(graph, 0);

    return 0;
}

