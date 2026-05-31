# Graphs: Interview Problems

This page contains **20 interview problems** for graph representations, BFS, and DFS in Python.

Problems avoid duplicates already used in earlier Python DSA notes and focus on graph-specific skills.

## 1. Build an Adjacency List

### Problem

Build an undirected graph from warehouse route pairs.

### Solution

```python
routes = [("A", "B"), ("A", "C"), ("B", "D")]
graph = {}

for source, destination in routes:
    graph.setdefault(source, []).append(destination)
    graph.setdefault(destination, []).append(source)

print(graph)
```

Output:

```text
{'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
```

## 2. Build an Adjacency Matrix

### Problem

Build a matrix for delivery city connections.

### Solution

```python
nodes = ["A", "B", "C"]
edges = [("A", "B"), ("A", "C")]
index = {node: i for i, node in enumerate(nodes)}
matrix = [[0] * len(nodes) for _ in nodes]

for source, destination in edges:
    i = index[source]
    j = index[destination]
    matrix[i][j] = 1
    matrix[j][i] = 1

print(matrix)
```

Output:

```text
[[0, 1, 1], [1, 0, 0], [1, 0, 0]]
```

## 3. Check Edge in Adjacency List

### Problem

Check whether two warehouses are directly connected.

### Solution

```python
graph = {"A": ["B", "C"], "B": ["A"], "C": ["A"]}

print("B" in graph["A"])
print("C" in graph["B"])
```

Output:

```text
True
False
```

## 4. Check Edge in Adjacency Matrix

### Problem

Check whether two nodes have an edge using a matrix.

### Solution

```python
nodes = ["A", "B", "C"]
index = {node: i for i, node in enumerate(nodes)}
matrix = [[0, 1, 1], [1, 0, 0], [1, 0, 0]]

print(matrix[index["A"]][index["C"]] == 1)
```

Output:

```text
True
```

## 5. BFS Traversal

### Problem

Traverse a graph level by level from a starting warehouse.

### Solution

```python
from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        queue.extend(graph[node])

    return order


graph = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
print(bfs(graph, "A"))
```

Output:

```text
['A', 'B', 'C', 'D']
```

## 6. DFS Traversal Recursive

### Problem

Traverse a graph deeply from a starting node.

### Solution

```python
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    order = [node]

    for neighbor in graph[node]:
        if neighbor not in visited:
            order.extend(dfs(graph, neighbor, visited))

    return order


graph = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
print(dfs(graph, "A"))
```

Output:

```text
['A', 'B', 'D', 'C']
```

## 7. DFS Traversal Iterative

### Problem

Implement DFS without recursion.

### Solution

```python
def dfs_iterative(graph, start):
    stack = [start]
    visited = set()
    order = []

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        stack.extend(reversed(graph[node]))

    return order


graph = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
print(dfs_iterative(graph, "A"))
```

Output:

```text
['A', 'B', 'D', 'C']
```

## 8. Find Path With BFS

### Problem

Find one path between two warehouses.

### Solution

```python
from collections import deque


def bfs_path(graph, start, target):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()
        if node == target:
            return path
        if node in visited:
            continue
        visited.add(node)

        for neighbor in graph[node]:
            queue.append((neighbor, path + [neighbor]))

    return []


graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
print(bfs_path(graph, "A", "D"))
```

Output:

```text
['A', 'B', 'D']
```

## 9. Shortest Path Length in Unweighted Graph

### Problem

Find shortest delivery hops from source to target.

### Solution

```python
from collections import deque


def shortest_hops(graph, start, target):
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        node, distance = queue.popleft()
        if node == target:
            return distance

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return -1


graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
print(shortest_hops(graph, "A", "D"))
```

Output:

```text
2
```

## 10. Count Connected Components

### Problem

Count disconnected warehouse groups.

### Solution

```python
def count_components(graph):
    visited = set()
    count = 0

    def visit(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visit(neighbor)

    for node in graph:
        if node not in visited:
            count += 1
            visit(node)

    return count


graph = {"A": ["B"], "B": ["A"], "C": [], "D": ["E"], "E": ["D"]}
print(count_components(graph))
```

Output:

```text
3
```

## 11. Detect Cycle in Undirected Graph

### Problem

Detect whether an undirected graph has a cycle.

### Solution

```python
def has_cycle_undirected(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in graph:
        if node not in visited and dfs(node, None):
            return True

    return False


graph = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}
print(has_cycle_undirected(graph))
```

Output:

```text
True
```

## 12. Detect Cycle in Directed Graph

### Problem

Detect whether task dependencies contain a cycle.

### Solution

```python
def has_cycle_directed(graph):
    visiting = set()
    visited = set()

    def dfs(node):
        if node in visiting:
            return True
        if node in visited:
            return False

        visiting.add(node)
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        visiting.remove(node)
        visited.add(node)
        return False

    return any(dfs(node) for node in graph)


graph = {"pay": ["pack"], "pack": ["ship"], "ship": ["pay"]}
print(has_cycle_directed(graph))
```

Output:

```text
True
```

## 13. Check If Route Exists

### Problem

Check whether delivery can go from source to destination.

### Solution

```python
def route_exists(graph, start, target):
    return bool(bfs_path(graph, start, target))


graph = {"A": ["B"], "B": ["C"], "C": [], "D": []}
print(route_exists(graph, "A", "C"))
print(route_exists(graph, "A", "D"))
```

Output:

```text
True
False
```

## 14. Find All Reachable Nodes

### Problem

Return all warehouses reachable from a given warehouse.

### Solution

```python
def reachable_nodes(graph, start):
    return set(bfs(graph, start))


graph = {"A": ["B", "C"], "B": ["D"], "C": [], "D": [], "E": []}
print(reachable_nodes(graph, "A"))
```

Output:

```text
{'A', 'B', 'C', 'D'}
```

## 15. Count Edges in Undirected Graph

### Problem

Count edges from an adjacency list.

### Solution

```python
graph = {"A": ["B", "C"], "B": ["A"], "C": ["A"]}
edge_count = sum(len(neighbors) for neighbors in graph.values()) // 2

print(edge_count)
```

Output:

```text
2
```

## 16. Convert Matrix to Adjacency List

### Problem

Convert an adjacency matrix into adjacency list format.

### Solution

```python
nodes = ["A", "B", "C"]
matrix = [[0, 1, 1], [1, 0, 0], [1, 0, 0]]
graph = {node: [] for node in nodes}

for i, row in enumerate(matrix):
    for j, value in enumerate(row):
        if value == 1:
            graph[nodes[i]].append(nodes[j])

print(graph)
```

Output:

```text
{'A': ['B', 'C'], 'B': ['A'], 'C': ['A']}
```

## 17. Convert Adjacency List to Matrix

### Problem

Convert adjacency list into matrix format.

### Solution

```python
graph = {"A": ["B", "C"], "B": ["A"], "C": ["A"]}
nodes = list(graph)
index = {node: i for i, node in enumerate(nodes)}
matrix = [[0] * len(nodes) for _ in nodes]

for node, neighbors in graph.items():
    for neighbor in neighbors:
        matrix[index[node]][index[neighbor]] = 1

print(matrix)
```

Output:

```text
[[0, 1, 1], [1, 0, 0], [1, 0, 0]]
```

## 18. Topological Order for Tasks

### Problem

Order tasks so dependencies come first.

### Solution

```python
def topological_sort(graph):
    visited = set()
    result = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        result.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return result[::-1]


graph = {"pay": ["pack"], "pack": ["ship"], "ship": []}
print(topological_sort(graph))
```

Output:

```text
['pay', 'pack', 'ship']
```

## 19. Clone a Graph

### Problem

Clone a graph represented by adjacency list.

### Solution

```python
def clone_graph(graph):
    return {node: neighbors[:] for node, neighbors in graph.items()}


graph = {"A": ["B"], "B": ["A", "C"], "C": ["B"]}
copy = clone_graph(graph)
copy["A"].append("C")

print(graph)
print(copy)
```

Output:

```text
{'A': ['B'], 'B': ['A', 'C'], 'C': ['B']}
{'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['B']}
```

## 20. Find Nearest Pickup Location

### Problem

Use BFS to find the nearest pickup location from a customer zone.

### Solution

```python
from collections import deque


def nearest_pickup(graph, start, pickups):
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        node, distance = queue.popleft()
        if node in pickups:
            return node, distance

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return None, -1


graph = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": [], "E": []}
pickups = {"E", "D"}
print(nearest_pickup(graph, "A", pickups))
```

Output:

```text
('D', 2)
```

## Final Notes

- Use adjacency lists for most sparse graph problems.
- Use adjacency matrices when edge checks must be very fast and graph size is manageable.
- BFS uses a queue.
- DFS uses recursion or a stack.
- Always track visited nodes in cyclic graphs.
