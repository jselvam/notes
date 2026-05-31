# Advanced Graph Algorithms: 10 Interview Questions

## 1. When should you use Dijkstra?

Use Dijkstra to find shortest paths from one source when all edge weights are non-negative.

## 2. Why does Dijkstra fail with negative weights?

Dijkstra assumes once a node has the smallest known distance, it is final. Negative edges can later reduce that distance.

## 3. When should you use Bellman-Ford?

Use Bellman-Ford when the graph may contain negative edge weights or when you need negative-cycle detection.

## 4. What is Floyd-Warshall used for?

Floyd-Warshall finds shortest paths between every pair of nodes.

## 5. What is topological sort?

Topological sort orders nodes in a directed acyclic graph so every dependency appears before the dependent task.

## 6. What is Union Find or DSU?

DSU is a data structure that tracks connected components and supports fast `find` and `union` operations.

## 7. What is path compression in DSU?

Path compression makes every visited node point directly to its root, speeding up future `find()` calls.

## 8. What does Kruskal's algorithm do?

Kruskal builds a minimum spanning tree by sorting edges and adding the cheapest edge that does not create a cycle.

## 9. What does Prim's algorithm do?

Prim builds a minimum spanning tree by starting from one node and repeatedly adding the cheapest edge to an unvisited node.

## 10. What is the difference between Kruskal and Prim?

Kruskal sorts all edges and uses DSU. Prim grows from a starting node using a priority queue.

## See also

- [Core concepts](core-concepts.md)
- [Interview problems](interview-problems.md)
