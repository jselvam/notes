# Graphs: 10 Interview Questions

## 1. What is a graph?

A graph is a data structure made of nodes or vertices connected by edges.

## 2. What is an adjacency list?

An adjacency list stores each node with a list of its neighboring nodes.

## 3. What is an adjacency matrix?

An adjacency matrix is a 2D table where `matrix[i][j]` tells whether an edge exists between two nodes.

## 4. When should you use an adjacency list?

Use an adjacency list for sparse graphs because it saves space and makes neighbor traversal efficient.

## 5. When should you use an adjacency matrix?

Use an adjacency matrix when the graph is dense or when you need `O(1)` edge existence checks.

## 6. What is BFS?

BFS, or Breadth-First Search, visits nodes level by level using a queue.

## 7. What is DFS?

DFS, or Depth-First Search, explores one path deeply before backtracking.

## 8. Which algorithm finds shortest path in an unweighted graph?

BFS finds the shortest path in an unweighted graph.

## 9. Why do BFS and DFS need a visited set?

A visited set prevents repeated work and avoids infinite loops in cyclic graphs.

## 10. What is the time complexity of BFS or DFS with adjacency list?

The time complexity is `O(V + E)`, where `V` is vertices and `E` is edges.

## See also

- [Core concepts](core-concepts.md)
- [Interview problems](interview-problems.md)
