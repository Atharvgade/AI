#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Edge {
    int src, dest, weight;
};

bool compare(Edge a, Edge b) {
    return a.weight < b.weight;
}

int find(vector<int>& parent, int i) {
    if (parent[i] != i)
        parent[i] = find(parent, parent[i]);
    return parent[i];
}

void unionSet(vector<int>& parent, int x, int y) {
    int xroot = find(parent, x);
    int yroot = find(parent, y);
    parent[xroot] = yroot;
}

void kruskalMST(vector<Edge>& edges, int n) {
    sort(edges.begin(), edges.end(), compare);

    vector<int> parent(n);
    for (int i = 0; i < n; i++)
        parent[i] = i;

    cout << "Edge \tWeight\n";
    for (auto& edge : edges) {
        int x = find(parent, edge.src);
        int y = find(parent, edge.dest);

        if (x != y) {
            cout << edge.src << " - " << edge.dest << "\t" << edge.weight << endl;
            unionSet(parent, x, y);
        }
    }
}

int main() {
    int n = 4; // vertices
    vector<Edge> edges = {
        {0, 1, 10},
        {0, 2, 6},
        {0, 3, 5},
        {1, 3, 15},
        {2, 3, 4}
    };

    kruskalMST(edges, n);

    return 0;
}

