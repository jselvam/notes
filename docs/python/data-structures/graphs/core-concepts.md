# Graphs in Python: Core Concepts

A graph is a data structure made of **vertices** and **edges**.

This page covers:

- graph vocabulary
- adjacency list
- adjacency matrix
- BFS
- DFS

Examples use an online computer shopping system.

## Graph Vocabulary

| Term | Meaning |
|------|---------|
| vertex / node | an item in the graph |
| edge | connection between two nodes |
| directed graph | edges have direction |
| undirected graph | edges work both ways |
| weighted graph | edges have costs |
| path | sequence of connected nodes |
| cycle | path that returns to an earlier node |
| connected graph | all nodes can be reached |

## Shopping Graph Examples

Graphs can model:

- warehouse route connections
- product recommendation links
- category relationships
- delivery city networks
- dependency order between tasks
- customer referral networks

## Adjacency List

An adjacency list stores each node with its neighbors.

```python
graph = {
    "Catalog": ["Laptop", "Mouse"],
    "Laptop": ["Monitor"],
    "Mouse": [],
    "Monitor": [],
}

print(graph["Catalog"])
```

Output:

```text
['Laptop', 'Mouse']
```

Adjacency lists are usually preferred for sparse graphs.

## Adjacency Matrix

An adjacency matrix uses a 2D grid.

```python
nodes = ["A", "B", "C"]
matrix = [
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 0],
]

print(matrix[0][1])
```

Output:

```text
1
```

`1` means an edge exists. `0` means no edge.

Adjacency matrices are useful when the graph is dense or you need `O(1)` edge checks.

## Adjacency List vs Matrix

| Feature | Adjacency list | Adjacency matrix |
|---------|----------------|------------------|
| Space | `O(V + E)` | `O(V^2)` |
| Edge check | up to `O(degree)` | `O(1)` |
| Iterate neighbors | efficient | may scan full row |
| Best for | sparse graphs | dense graphs |

## BFS

BFS means **Breadth-First Search**. It visits nodes level by level using a queue.

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

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

    return order
```

BFS is useful for shortest path in an unweighted graph.

## DFS

DFS means **Depth-First Search**. It explores as far as possible before backtracking.

```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    order = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            order.extend(dfs(graph, neighbor, visited))

    return order
```

DFS is useful for cycle detection, connected components, and dependency traversal.

## BFS vs DFS

| Feature | BFS | DFS |
|---------|-----|-----|
| Data structure | queue | recursion or stack |
| Visits | level by level | deep path first |
| Best for | shortest path in unweighted graph | cycle/component/dependency problems |
| Memory | can grow by level width | can grow by depth |

## Complexity

For adjacency list traversal:

```text
Time: O(V + E)
Space: O(V)
```

Where:

- `V` = vertices
- `E` = edges

## Common Mistakes

### Forgetting `visited`

Without `visited`, BFS or DFS can loop forever on cyclic graphs.

### Using matrix for sparse graph

Adjacency matrix can waste memory when few edges exist.

### Confusing BFS and DFS use cases

Use BFS for shortest unweighted paths. Use DFS for deep exploration and cycle/component patterns.

## See also

- [Interview problems](interview-problems.md)
- [Interview questions](interview-questions.md)
- [Stacks, queues, and linked lists](../stacks-queues-linked-lists/core-concepts.md)
- [Hash table](../hash-table/core-concepts.md)
