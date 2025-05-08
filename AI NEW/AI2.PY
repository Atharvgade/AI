import heapq  # Used to implement a priority queue (min-heap)

def a_star(grid, start, goal):
    # Heuristic function: Manhattan distance (no diagonal movement)
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # Priority queue to store (priority, node)
    open_set = [(0, start)]

    # Dictionary to store the best path to each node
    came_from = {}

    # Cost from start node to this node
    g_score = {start: 0}

    while open_set:
        # Get the node with the lowest estimated cost
        _, current = heapq.heappop(open_set)

        # If the goal is reached, reconstruct and return the path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Reverse to get path from start to goal

        # Explore neighbors: Up, Down, Left, Right
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)

            # Check if neighbor is within grid bounds and walkable
            if (0 <= neighbor[0] < len(grid) and
                0 <= neighbor[1] < len(grid[0]) and
                grid[neighbor[0]][neighbor[1]] == 0):  # 0 means walkable

                new_cost = g_score[current] + 1  # All moves cost 1
                # If neighbor not visited yet, or we found a shorter path
                if neighbor not in g_score or new_cost < g_score[neighbor]:
                    g_score[neighbor] = new_cost
                    # f(n) = g(n) + h(n)
                    priority = new_cost + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (priority, neighbor))
                    # Store how we reached this neighbor
                    came_from[neighbor] = current

    return None  # No path found
# 0 = walkable, 1 = wall
grid = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 0, 0],
]

start = (0, 0)
goal = (2, 2)

# Run the A* algorithm
path = a_star(grid, start, goal)

# Print the result
print(path)
