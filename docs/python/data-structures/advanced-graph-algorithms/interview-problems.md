# Advanced Graph Algorithms: Interview Problems

This page contains **20 interview problems** for advanced graph algorithms in Python.

Topics covered: Dijkstra, Bellman-Ford, Floyd-Warshall, Topological Sort, Union Find / DSU, Kruskal, and Prim.

## 1. Dijkstra: Shortest Delivery Cost

### Problem

Find shortest delivery cost from warehouse to all locations.

### Solution

```python
import heapq


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        distance, node = heapq.heappop(heap)
        if distance > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            new_distance = distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(heap, (new_distance, neighbor))

    return distances


graph = {
    "WH": [("A", 4), ("B", 2)],
    "A": [("C", 3)],
    "B": [("A", 1), ("C", 7)],
    "C": [],
}

print(dijkstra(graph, "WH"))
```

Output:

```text
{'WH': 0, 'A': 3, 'B': 2, 'C': 6}
```

## 2. Dijkstra: Shortest Path, Not Just Distance

### Problem

Return the actual route from source to destination.

### Solution

```python
import heapq


def shortest_path(graph, start, target):
    heap = [(0, start, [start])]
    best = {start: 0}

    while heap:
        distance, node, path = heapq.heappop(heap)
        if node == target:
            return distance, path

        for neighbor, weight in graph[node]:
            new_distance = distance + weight
            if new_distance < best.get(neighbor, float("inf")):
                best[neighbor] = new_distance
                heapq.heappush(heap, (new_distance, neighbor, path + [neighbor]))

    return float("inf"), []


graph = {"WH": [("A", 4), ("B", 2)], "A": [("C", 3)], "B": [("C", 2)], "C": []}
print(shortest_path(graph, "WH", "C"))
```

Output:

```text
(4, ['WH', 'B', 'C'])
```

## 3. Dijkstra: Ignore Stale Heap Entries

### Problem

Show why stale heap entries are skipped.

### Solution

```python
import heapq


graph = {"A": [("B", 10), ("C", 1)], "C": [("B", 1)], "B": []}
distances = {"A": 0, "B": float("inf"), "C": float("inf")}
heap = [(0, "A")]

while heap:
    distance, node = heapq.heappop(heap)
    if distance > distances[node]:
        continue

    for neighbor, weight in graph[node]:
        new_distance = distance + weight
        if new_distance < distances[neighbor]:
            distances[neighbor] = new_distance
            heapq.heappush(heap, (new_distance, neighbor))

print(distances)
```

Output:

```text
{'A': 0, 'B': 2, 'C': 1}
```

## 4. Bellman-Ford: Shortest Path With Negative Edge

### Problem

Find shortest costs when one route has a negative adjustment.

### Solution

```python
def bellman_ford(nodes, edges, start):
    distances = {node: float("inf") for node in nodes}
    distances[start] = 0

    for _ in range(len(nodes) - 1):
        for source, target, weight in edges:
            if distances[source] != float("inf") and distances[source] + weight < distances[target]:
                distances[target] = distances[source] + weight

    return distances


nodes = ["WH", "A", "B"]
edges = [("WH", "A", 5), ("A", "B", -2), ("WH", "B", 10)]

print(bellman_ford(nodes, edges, "WH"))
```

Output:

```text
{'WH': 0, 'A': 5, 'B': 3}
```

## 5. Bellman-Ford: Detect Negative Cycle

### Problem

Detect an invalid route cycle that keeps reducing cost.

### Solution

```python
def has_negative_cycle(nodes, edges, start):
    distances = {node: float("inf") for node in nodes}
    distances[start] = 0

    for _ in range(len(nodes) - 1):
        for source, target, weight in edges:
            if distances[source] != float("inf") and distances[source] + weight < distances[target]:
                distances[target] = distances[source] + weight

    for source, target, weight in edges:
        if distances[source] != float("inf") and distances[source] + weight < distances[target]:
            return True

    return False


nodes = ["A", "B", "C"]
edges = [("A", "B", 1), ("B", "C", -2), ("C", "A", -2)]

print(has_negative_cycle(nodes, edges, "A"))
```

Output:

```text
True
```

## 6. Bellman-Ford: Unreachable Nodes

### Problem

Keep unreachable locations as infinity.

### Solution

```python
nodes = ["WH", "A", "B", "X"]
edges = [("WH", "A", 4), ("A", "B", 2)]

print(bellman_ford(nodes, edges, "WH"))
```

Output:

```text
{'WH': 0, 'A': 4, 'B': 6, 'X': inf}
```

## 7. Floyd-Warshall: All-Pairs Shortest Paths

### Problem

Find shortest distances between every pair of cities.

### Solution

```python
def floyd_warshall(matrix):
    distance = [row[:] for row in matrix]
    n = len(distance)

    for mid in range(n):
        for source in range(n):
            for target in range(n):
                distance[source][target] = min(
                    distance[source][target],
                    distance[source][mid] + distance[mid][target],
                )

    return distance


inf = float("inf")
matrix = [
    [0, 3, inf],
    [inf, 0, 2],
    [4, inf, 0],
]

print(floyd_warshall(matrix))
```

Output:

```text
[[0, 3, 5], [6, 0, 2], [4, 7, 0]]
```

## 8. Floyd-Warshall: Check Reachability

### Problem

Use all-pairs results to check if one city can reach another.

### Solution

```python
inf = float("inf")
matrix = [[0, 1, inf], [inf, 0, inf], [inf, 1, 0]]
dist = floyd_warshall(matrix)

print(dist[0][1] != inf)
print(dist[1][2] != inf)
```

Output:

```text
True
False
```

## 9. Floyd-Warshall: Detect Negative Cycle

### Problem

Detect a negative cycle using diagonal values.

### Solution

```python
inf = float("inf")
matrix = [[0, 1, inf], [inf, 0, -3], [-1, inf, 0]]
dist = floyd_warshall(matrix)

has_negative_cycle = any(dist[i][i] < 0 for i in range(len(dist)))

print(has_negative_cycle)
```

Output:

```text
True
```

## 10. Topological Sort With Kahn's Algorithm

### Problem

Order checkout tasks by dependency.

### Solution

```python
from collections import deque


def topological_sort(graph):
    indegree = {node: 0 for node in graph}

    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    queue = deque([node for node in graph if indegree[node] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == len(graph) else []


graph = {"pay": ["pack"], "pack": ["ship"], "ship": []}
print(topological_sort(graph))
```

Output:

```text
['pay', 'pack', 'ship']
```

## 11. Topological Sort: Detect Cycle

### Problem

Return empty list if dependencies contain a cycle.

### Solution

```python
graph = {"pay": ["pack"], "pack": ["ship"], "ship": ["pay"]}
print(topological_sort(graph))
```

Output:

```text
[]
```

## 12. Topological Sort With DFS

### Problem

Use DFS postorder to order tasks.

### Solution

```python
def topo_dfs(graph):
    visited = set()
    order = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        order.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return order[::-1]


graph = {"validate": ["pay"], "pay": ["pack"], "pack": []}
print(topo_dfs(graph))
```

Output:

```text
['validate', 'pay', 'pack']
```

## 13. DSU: Connect Warehouses

### Problem

Union connected warehouses and test connectivity.

### Solution

```python
class DSU:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, first, second):
        root_first = self.find(first)
        root_second = self.find(second)
        if root_first == root_second:
            return False
        if self.rank[root_first] < self.rank[root_second]:
            self.parent[root_first] = root_second
        elif self.rank[root_first] > self.rank[root_second]:
            self.parent[root_second] = root_first
        else:
            self.parent[root_second] = root_first
            self.rank[root_first] += 1
        return True


dsu = DSU(["A", "B", "C"])
dsu.union("A", "B")
print(dsu.find("A") == dsu.find("B"))
print(dsu.find("A") == dsu.find("C"))
```

Output:

```text
True
False
```

## 14. DSU: Count Connected Components

### Problem

Count connected warehouse groups after adding routes.

### Solution

```python
nodes = ["A", "B", "C", "D"]
routes = [("A", "B"), ("C", "D")]
dsu = DSU(nodes)

for source, target in routes:
    dsu.union(source, target)

components = len({dsu.find(node) for node in nodes})

print(components)
```

Output:

```text
2
```

## 15. DSU: Detect Cycle in Undirected Edges

### Problem

Detect whether adding an edge creates a cycle.

### Solution

```python
nodes = ["A", "B", "C"]
edges = [("A", "B"), ("B", "C"), ("A", "C")]
dsu = DSU(nodes)
has_cycle = False

for source, target in edges:
    if not dsu.union(source, target):
        has_cycle = True
        break

print(has_cycle)
```

Output:

```text
True
```

## 16. Kruskal: Minimum Spanning Tree Cost

### Problem

Connect all warehouses with minimum cabling cost.

### Solution

```python
def kruskal(nodes, edges):
    dsu = DSU(nodes)
    total = 0
    selected = []

    for cost, source, target in sorted(edges):
        if dsu.union(source, target):
            total += cost
            selected.append((source, target, cost))

    return total, selected


nodes = ["A", "B", "C"]
edges = [(4, "A", "B"), (1, "B", "C"), (3, "A", "C")]

print(kruskal(nodes, edges))
```

Output:

```text
(4, [('B', 'C', 1), ('A', 'C', 3)])
```

## 17. Kruskal: Check If Full MST Exists

### Problem

Verify whether all nodes can be connected.

### Solution

```python
nodes = ["A", "B", "C", "D"]
edges = [(1, "A", "B"), (2, "B", "C")]
cost, selected = kruskal(nodes, edges)

print(len(selected) == len(nodes) - 1)
```

Output:

```text
False
```

## 18. Prim: Minimum Spanning Tree Cost

### Problem

Use Prim's algorithm from a start warehouse.

### Solution

```python
import heapq


def prim(graph, start):
    visited = set()
    heap = [(0, start, None)]
    total = 0
    selected = []

    while heap:
        cost, node, parent = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        total += cost
        if parent is not None:
            selected.append((parent, node, cost))
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(heap, (weight, neighbor, node))

    return total, selected


graph = {
    "A": [("B", 4), ("C", 3)],
    "B": [("A", 4), ("C", 1)],
    "C": [("A", 3), ("B", 1)],
}

print(prim(graph, "A"))
```

Output:

```text
(4, [('A', 'C', 3), ('C', 'B', 1)])
```

## 19. Prim: Disconnected Graph Visit Count

### Problem

Detect that Prim from one node does not reach all warehouses.

### Solution

```python
graph = {"A": [("B", 1)], "B": [("A", 1)], "C": []}
cost, selected = prim(graph, "A")
visited_count = len(selected) + 1 if graph else 0

print(cost)
print(visited_count == len(graph))
```

Output:

```text
1
False
```

## 20. Choose Correct Advanced Graph Algorithm

### Problem

Map business scenarios to algorithms.

### Solution

```python
choices = {
    "fastest non-negative route": "Dijkstra",
    "route with negative adjustments": "Bellman-Ford",
    "all city pair distances": "Floyd-Warshall",
    "checkout task order": "Topological Sort",
    "warehouse connectivity": "DSU",
    "minimum network from edge list": "Kruskal",
    "minimum network from adjacency list": "Prim",
}

print(choices["checkout task order"])
print(choices["minimum network from edge list"])
```

Output:

```text
Topological Sort
Kruskal
```

## Final Notes

- Dijkstra does not work with negative edge weights.
- Bellman-Ford can detect negative cycles.
- Floyd-Warshall is simple but `O(V^3)`.
- Topological sort works only on DAGs.
- DSU is excellent for connectivity and cycle detection.
- Kruskal and Prim both build MSTs.
