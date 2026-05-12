# Graph Coloring using Backtracking

graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

m = 3
n = len(graph)

colors = [0] * n

def is_safe(node, color):
    for k in range(n):
        if graph[node][k] == 1 and colors[k] == color:
            return False
    return True

def solve(node):
    if node == n:
        return True

    for color in range(1, m + 1):
        if is_safe(node, color):
            colors[node] = color

            if solve(node + 1):
                return True

            colors[node] = 0

    return False

if solve(0):
    print("Color Assignment:", colors)
else:
    print("No Solution")