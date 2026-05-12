# Minimum Spanning Tree using Prim's Algorithm

import heapq

graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

start = 'A'
visited = set()
min_heap = [(0, start)]
cost = 0

while min_heap:
    weight, node = heapq.heappop(min_heap)

    if node not in visited:
        visited.add(node)
        cost += weight

        for neighbor, w in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (w, neighbor))

print("Minimum Spanning Tree Cost:", cost)