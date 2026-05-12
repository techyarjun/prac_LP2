# Kruskal's MST Algorithm

edges = [
    (1, 0, 1),
    (3, 1, 2),
    (2, 0, 2),
    (4, 2, 3),
    (5, 1, 3)
]

parent = {}

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

def union(x, y):
    parent[find(x)] = find(y)

vertices = [0, 1, 2, 3]

for v in vertices:
    parent[v] = v

edges.sort()

mst_cost = 0

for weight, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        mst_cost += weight
        print(u, "-", v, "=", weight)

print("Minimum Cost:", mst_cost)