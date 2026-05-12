import heapq

# Grid definition
grid = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

rows = len(grid)
cols = len(grid[0])

start = (0, 0)
goal = (4, 4)

# Manhattan Distance Heuristic
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):

    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_score = {start: 0}

    while open_list:

        current = heapq.heappop(open_list)[1]

        if current == goal:

            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)

            return path[::-1]

        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:

            neighbor = (current[0] + dx, current[1] + dy)

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:

                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue

                tentative_g = g_score[current] + 1

                if neighbor not in g_score or tentative_g < g_score[neighbor]:

                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g

                    f_score = tentative_g + heuristic(neighbor, goal)

                    heapq.heappush(open_list, (f_score, neighbor))

    return None

# Run A*
path = astar(grid, start, goal)

print("Shortest Path using A*:")
print(path)