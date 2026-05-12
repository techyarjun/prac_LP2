# Dijkstra's Algorithm

import heapq

graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

start = 0

distance = {node: float('inf') for node in graph}
distance[start] = 0

pq = [(0, start)]

while pq:
    dist, node = heapq.heappop(pq)

    for neighbor, weight in graph[node]:
        new_dist = dist + weight

        if new_dist < distance[neighbor]:
            distance[neighbor] = new_dist
            heapq.heappush(pq, (new_dist, neighbor))

print("Shortest Distance:")
print(distance)