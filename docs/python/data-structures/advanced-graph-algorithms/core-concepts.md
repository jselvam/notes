# Advanced Graph Algorithms in Python: Core Concepts

Advanced graph algorithms solve routing, dependency, connectivity, and network optimization problems.

This page covers:

- Dijkstra
- Bellman-Ford
- Floyd-Warshall
- Topological Sort
- Union Find / DSU
- Kruskal
- Prim

Examples use an online computer shopping system.

## When These Algorithms Are Used

| Algorithm | Main use |
|-----------|----------|
| Dijkstra | shortest path with non-negative weights |
| Bellman-Ford | shortest path with negative edges and negative-cycle detection |
| Floyd-Warshall | shortest paths between every pair of nodes |
| Topological Sort | order tasks with dependencies |
| Union Find / DSU | track connected components efficiently |
| Kruskal | minimum spanning tree using sorted edges |
| Prim | minimum spanning tree growing from one node |

## Weighted Graph

A weighted graph has a cost on each edge.

```python
graph = {
    "warehouse": [("city-a", 4), ("city-b", 2)],
    "city-a": [("customer", 5)],
    "city-b": [("customer", 8)],
    "customer": [],
}
```

Weights can represent delivery time, distance, shipping cost, or risk score.

## Dijkstra

Dijkstra finds shortest paths from one source when all edge weights are non-negative.

```python
import heapq


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_distance, node = heapq.heappop(heap)

        if current_distance > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(heap, (new_distance, neighbor))

    return distances
```

Use Dijkstra for fastest delivery route when weights are not negative.

## Bellman-Ford

Bellman-Ford also finds shortest paths from one source. It can handle negative edge weights and detect negative cycles.

```python
def bellman_ford(nodes, edges, start):
    distances = {node: float("inf") for node in nodes}
    distances[start] = 0

    for _ in range(len(nodes) - 1):
        for source, target, weight in edges:
            if distances[source] + weight < distances[target]:
                distances[target] = distances[source] + weight

    for source, target, weight in edges:
        if distances[source] + weight < distances[target]:
            return None

    return distances
```

Use Bellman-Ford when discounts, credits, or adjustments create negative edge weights.

## Floyd-Warshall

Floyd-Warshall finds shortest paths between all pairs of nodes.

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
```

Use it when the graph is small enough and you need every city-to-city shortest route.

## Topological Sort

Topological sort orders directed acyclic graph (DAG) tasks so dependencies come first.

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
```

Use it for workflows such as payment before packing, packing before shipping.

## Union Find / DSU

Union Find, also called DSU, tracks connected groups.

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
```

DSU is useful for connectivity checks and Kruskal's MST algorithm.

## Kruskal

Kruskal builds a minimum spanning tree by sorting edges and adding the cheapest edge that does not form a cycle.

```python
def kruskal(nodes, edges):
    dsu = DSU(nodes)
    total_cost = 0
    result = []

    for cost, source, target in sorted(edges):
        if dsu.union(source, target):
            total_cost += cost
            result.append((source, target, cost))

    return total_cost, result
```

Use Kruskal for connecting warehouses with minimum cabling or road-building cost.

## Prim

Prim builds an MST by starting from one node and repeatedly adding the cheapest edge to a new node.

```python
import heapq


def prim(graph, start):
    visited = set()
    heap = [(0, start, None)]
    total_cost = 0
    result = []

    while heap:
        cost, node, parent = heapq.heappop(heap)
        if node in visited:
            continue

        visited.add(node)
        total_cost += cost
        if parent is not None:
            result.append((parent, node, cost))

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(heap, (weight, neighbor, node))

    return total_cost, result
```

Use Prim when you have an adjacency list and want to grow the network from one starting point.

## Algorithm Selection

| Scenario | Choose |
|----------|--------|
| shortest delivery route, no negative weights | Dijkstra |
| shortest route with negative adjustment | Bellman-Ford |
| all city-to-city shortest routes | Floyd-Warshall |
| task dependency order | Topological Sort |
| check if warehouses are connected | DSU |
| MST from edge list | Kruskal |
| MST from adjacency list | Prim |

## Complexity Summary

| Algorithm | Common complexity |
|-----------|-------------------|
| Dijkstra with heap | `O((V + E) log V)` |
| Bellman-Ford | `O(VE)` |
| Floyd-Warshall | `O(V^3)` |
| Topological Sort | `O(V + E)` |
| DSU operations | nearly `O(1)` amortized |
| Kruskal | `O(E log E)` |
| Prim with heap | `O(E log V)` |

## See also

- [Interview problems](interview-problems.md)
- [Interview questions](interview-questions.md)
- [Graphs](../graphs/core-concepts.md)
- [Heap and Priority Queue](../heap-priority-queue/core-concepts.md)
