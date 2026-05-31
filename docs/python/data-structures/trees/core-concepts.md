# Binary Trees, BSTs, and AVL Trees in Python: Core Concepts

Trees are hierarchical data structures made of nodes connected by edges.

This page covers:

- binary trees
- binary search trees (BSTs)
- AVL trees
- tree traversals
- common interview patterns

Examples use an online computer shopping system.

## Tree Vocabulary

| Term | Meaning |
|------|---------|
| root | top node of the tree |
| parent | node that points to a child |
| child | node below another node |
| leaf | node with no children |
| edge | connection between nodes |
| height | longest path from node to leaf |
| depth | distance from root to node |
| subtree | tree formed from any node and its descendants |

## Binary Tree

A binary tree is a tree where each node has at most two children:

- left child
- right child

```text
        Laptop
       /      \
    Mouse    Monitor
```

Python node class:

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

## Binary Tree Traversals

Traversal means visiting every node.

| Traversal | Order | Use case |
|-----------|-------|----------|
| preorder | root, left, right | copy tree, serialize tree |
| inorder | left, root, right | sorted order in BST |
| postorder | left, right, root | delete/free tree, folder size |
| level order | level by level | BFS, shortest levels |

## Traversal Example

```python
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)


root = TreeNode("Mouse")
root.left = TreeNode("Laptop")
root.right = TreeNode("Monitor")

print(inorder(root))
```

Output:

```text
['Laptop', 'Mouse', 'Monitor']
```

## Binary Search Tree

A BST is a binary tree with an ordering rule:

- left subtree values are smaller
- right subtree values are larger

For product prices:

```text
        500
       /   \
     200   900
```

BST search is efficient when the tree is balanced.

## BST Search

```python
def search_bst(root, target):
    current = root
    while current:
        if current.value == target:
            return True
        if target < current.value:
            current = current.left
        else:
            current = current.right
    return False
```

## BST Complexity

| Operation | Balanced BST | Skewed BST |
|-----------|--------------|------------|
| search | `O(log n)` | `O(n)` |
| insert | `O(log n)` | `O(n)` |
| delete | `O(log n)` | `O(n)` |

A sorted insertion order can make a normal BST skewed.

## AVL Tree

An AVL tree is a self-balancing BST.

For every node:

```text
balance factor = height(left subtree) - height(right subtree)
```

Allowed balance factors:

- `-1`
- `0`
- `1`

If the balance factor becomes less than `-1` or greater than `1`, rotations are used to restore balance.

## AVL Rotations

Common rotation cases:

| Case | Problem | Fix |
|------|---------|-----|
| LL | inserted into left-left subtree | right rotation |
| RR | inserted into right-right subtree | left rotation |
| LR | inserted into left-right subtree | left rotation then right rotation |
| RL | inserted into right-left subtree | right rotation then left rotation |

## Why AVL Trees Matter

AVL trees keep search, insert, and delete operations at `O(log n)` by maintaining balance.

In interviews, AVL trees test whether you understand:

- BST ordering
- height
- balance factor
- rotations
- self-balancing trees

## Shopping Examples

| Problem | Tree idea |
|---------|-----------|
| category hierarchy | binary tree or general tree |
| products sorted by price | BST |
| fast changing searchable price index | AVL tree |
| warehouse zones by levels | level-order traversal |
| validate price tree ordering | BST validation |

## Common Mistakes

### Confusing binary tree with BST

Every BST is a binary tree, but not every binary tree is a BST.

### Forgetting empty tree cases

Always handle `root is None`.

### Thinking BST is always `O(log n)`

Only balanced BSTs are `O(log n)`. Skewed BSTs can become `O(n)`.

### AVL rotation order matters

LL, RR, LR, and RL cases need different rotation steps.

## See also

- [Interview problems](interview-problems.md)
- [Interview questions](interview-questions.md)
- [Stacks, queues, and linked lists](../stacks-queues-linked-lists/core-concepts.md)
- [Hash table](../hash-table/core-concepts.md)
