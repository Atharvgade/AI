#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Graph {
private:
    int vertices;
    vector<vector<int>> adjList;

public:
    Graph(int V) {
        vertices = V;
        adjList.resize(V);
    }

    void addEdge(int u, int v) {
        adjList[u].push_back(v);
        adjList[v].push_back(u);
    }

    // Recursive DFS function
    void DFSRecursive(int v, vector<bool>& visited) {
        visited[v] = true;
        cout << v << " ";

        for (int neighbor : adjList[v]) {
            if (!visited[neighbor]) {
                DFSRecursive(neighbor, visited);
            }
        }
    }

    // DFS traversal (recursive)
    void DFS(int start) {
        vector<bool> visited(vertices, false);
        cout << "DFS Traversal (Recursive): ";
        DFSRecursive(start, visited);
        cout << endl;
    }

    // BFS traversal (using queue)
    void BFS(int start) {
        vector<bool> visited(vertices, false);
        queue<int> q;

        visited[start] = true;
        q.push(start);

        cout << "BFS Traversal: ";

        while (!q.empty()) {
            int v = q.front();
            q.pop();
            cout << v << " ";

            for (int neighbor : adjList[v]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }

        cout << endl;
    }
};

int main() {
    int V, E;
    cout << "Enter number of vertices: ";
    cin >> V;
    cout << "Enter number of edges: ";
    cin >> E;

    Graph g(V);

    cout << "Enter edges (u v):" << endl;
    for (int i = 0; i < E; i++) {
        int u, v;
        cin >> u >> v;
        g.addEdge(u, v);
    }

    int startVertex;
    cout << "Enter starting vertex for traversal: ";
    cin >> startVertex;

    g.DFS(startVertex); // Recursive DFS
    g.BFS(startVertex); // BFS

    return 0;
}

