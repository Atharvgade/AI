from collections import deque

class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]

    def heuristic(self, node):
        heuristic_values = {
            'A': 5,
            'B': 4,
            'C': 3,
            'D': 2,
            'E': 1,
            'F': 1,
            'G': 0
        }
        return heuristic_values[node]

    def a_star_algorithm(self, start, goal):
        open_list = set([start])
        closed_list = set()
        cost_to_reach = {start: 0}
        parent = {start: start}

        while open_list:
            current_node = None
            for node in open_list:
                if current_node is None or cost_to_reach[node] + self.heuristic(node) < cost_to_reach[current_node] + self.heuristic(current_node):
                    current_node = node

            if current_node is None:
                print('Path not found')
                return None

            if current_node == goal:
                reconstructed_path = []
                while parent[current_node] != current_node:
                    reconstructed_path.append(current_node)
                    current_node = parent[current_node]
                reconstructed_path.append(start)
                reconstructed_path.reverse()
                print('Path found:', reconstructed_path)
                return reconstructed_path

            open_list.remove(current_node)
            closed_list.add(current_node)

            for neighbor, weight in self.get_neighbors(current_node):
                if neighbor not in open_list and neighbor not in closed_list:
                    open_list.add(neighbor)
                    parent[neighbor] = current_node
                    cost_to_reach[neighbor] = cost_to_reach[current_node] + weight
                else:
                    if cost_to_reach[neighbor] > cost_to_reach[current_node] + weight:
                        cost_to_reach[neighbor] = cost_to_reach[current_node] + weight
                        parent[neighbor] = current_node
                        if neighbor in closed_list:
                            closed_list.remove(neighbor)
                            open_list.add(neighbor)

        print('Path not found')
        return None


if __name__ == '__main__':
    adjacency_list = {
        'A': [('B', 1), ('C', 5), ('D', 3)],
        'B': [('A', 1), ('E', 2)],
        'C': [('A', 5), ('F', 4)],
        'D': [('A', 3), ('E', 1), ('G', 6)],
        'E': [('B', 2), ('D', 1), ('F', 3)],
        'F': [('C', 4), ('E', 3), ('G', 2)],
        'G': [('D', 6), ('F', 2)]
    }

    graph = Graph(adjacency_list)

    graph.a_star_algorithm('A', 'G')

