# Single Source Shortest Path using Dijkstra

import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start = 'A'

dist = {node: float('inf') for node in graph}
dist[start] = 0

pq = [(0, start)]

while pq:
    current_dist, node = heapq.heappop(pq)

    for neighbor, weight in graph[node]:
        distance = current_dist + weight

        if distance < dist[neighbor]:
            dist[neighbor] = distance
            heapq.heappush(pq, (distance, neighbor))

print("Shortest Distances:")
print(dist)