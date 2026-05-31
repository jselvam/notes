# Binary Trees, BSTs, and AVL Trees: Interview Problems

This page contains **20 interview problems** for Binary Trees, BSTs, and AVL Trees in Python.

Problems avoid duplicates already used in earlier Python notes and focus on tree-specific interview skills.

## Common Setup

Many examples use this node class:

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

## 1. Preorder Traversal of Product Tree

### Problem

Visit root, left subtree, then right subtree.

### Solution

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(root):
    if root is None:
        return []
    return [root.value] + preorder(root.left) + preorder(root.right)


root = TreeNode("Laptop")
root.left = TreeNode("Mouse")
root.right = TreeNode("Monitor")

print(preorder(root))
```

Output:

```text
['Laptop', 'Mouse', 'Monitor']
```

## 2. Inorder Traversal of Binary Tree

### Problem

Visit left subtree, root, then right subtree.

### Solution

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

## 3. Postorder Traversal of Binary Tree

### Problem

Visit left subtree, right subtree, then root.

### Solution

```python
def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.value]


root = TreeNode("Laptop")
root.left = TreeNode("Mouse")
root.right = TreeNode("Monitor")

print(postorder(root))
```

Output:

```text
['Mouse', 'Monitor', 'Laptop']
```

## 4. Level Order Traversal

### Problem

Print nodes level by level.

### Solution

```python
from collections import deque


def level_order(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.value)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


root = TreeNode("Catalog")
root.left = TreeNode("Hardware")
root.right = TreeNode("Software")

print(level_order(root))
```

Output:

```text
['Catalog', 'Hardware', 'Software']
```

## 5. Calculate Height of Binary Tree

### Problem

Return the number of nodes on the longest path from root to leaf.

### Solution

```python
def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


root = TreeNode("Catalog")
root.left = TreeNode("Hardware")
root.left.left = TreeNode("Laptop")

print(height(root))
```

Output:

```text
3
```

## 6. Count Nodes in Binary Tree

### Problem

Count all nodes in a product category tree.

### Solution

```python
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


root = TreeNode("Catalog")
root.left = TreeNode("Hardware")
root.right = TreeNode("Software")

print(count_nodes(root))
```

Output:

```text
3
```

## 7. Count Leaf Nodes

### Problem

Count nodes with no children.

### Solution

```python
def count_leaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)


root = TreeNode("Catalog")
root.left = TreeNode("Laptop")
root.right = TreeNode("Mouse")

print(count_leaves(root))
```

Output:

```text
2
```

## 8. Search Value in Binary Tree

### Problem

Search for a product category in a normal binary tree.

### Solution

```python
def search_tree(root, target):
    if root is None:
        return False
    if root.value == target:
        return True
    return search_tree(root.left, target) or search_tree(root.right, target)


root = TreeNode("Catalog")
root.left = TreeNode("Hardware")
root.right = TreeNode("Software")

print(search_tree(root, "Software"))
```

Output:

```text
True
```

## 9. Insert Price Into BST

### Problem

Insert a product price into a BST.

### Solution

```python
def insert_bst(root, value):
    if root is None:
        return TreeNode(value)

    if value < root.value:
        root.left = insert_bst(root.left, value)
    elif value > root.value:
        root.right = insert_bst(root.right, value)

    return root


root = None
for price in [500, 200, 900]:
    root = insert_bst(root, price)

print(inorder(root))
```

Output:

```text
[200, 500, 900]
```

## 10. Search Price in BST

### Problem

Search for a price using BST ordering.

### Solution

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


root = TreeNode(500)
root.left = TreeNode(200)
root.right = TreeNode(900)

print(search_bst(root, 900))
```

Output:

```text
True
```

## 11. Find Minimum Value in BST

### Problem

Find the lowest product price in a BST.

### Solution

```python
def find_min(root):
    current = root
    while current.left:
        current = current.left
    return current.value


root = TreeNode(500)
root.left = TreeNode(200)
root.right = TreeNode(900)

print(find_min(root))
```

Output:

```text
200
```

## 12. Validate a BST

### Problem

Check whether a binary tree satisfies BST ordering.

### Solution

```python
def is_valid_bst(root, low=float("-inf"), high=float("inf")):
    if root is None:
        return True
    if not (low < root.value < high):
        return False
    return (
        is_valid_bst(root.left, low, root.value)
        and is_valid_bst(root.right, root.value, high)
    )


root = TreeNode(500)
root.left = TreeNode(200)
root.right = TreeNode(900)

print(is_valid_bst(root))
```

Output:

```text
True
```

## 13. Find Lowest Common Ancestor in BST

### Problem

Find the lowest common ancestor of two prices in a BST.

### Solution

```python
def lca_bst(root, first, second):
    current = root

    while current:
        if first < current.value and second < current.value:
            current = current.left
        elif first > current.value and second > current.value:
            current = current.right
        else:
            return current.value


root = TreeNode(500)
root.left = TreeNode(200)
root.right = TreeNode(900)
root.left.left = TreeNode(100)
root.left.right = TreeNode(300)

print(lca_bst(root, 100, 300))
```

Output:

```text
200
```

## 14. Find Kth Smallest Price in BST

### Problem

Return the kth smallest price using inorder traversal.

### Solution

```python
def kth_smallest(root, k):
    values = inorder(root)
    return values[k - 1]


root = None
for price in [500, 200, 900, 100, 300]:
    root = insert_bst(root, price)

print(kth_smallest(root, 3))
```

Output:

```text
300
```

## 15. Delete Leaf Node From BST

### Problem

Delete a leaf value from a BST.

### Solution

```python
def delete_bst(root, value):
    if root is None:
        return None

    if value < root.value:
        root.left = delete_bst(root.left, value)
    elif value > root.value:
        root.right = delete_bst(root.right, value)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        successor_value = find_min(root.right)
        root.value = successor_value
        root.right = delete_bst(root.right, successor_value)

    return root


root = None
for price in [500, 200, 900]:
    root = insert_bst(root, price)

root = delete_bst(root, 200)
print(inorder(root))
```

Output:

```text
[500, 900]
```

## 16. Check if Binary Tree Is Balanced

### Problem

Check whether every node has left and right subtree heights differing by at most one.

### Solution

```python
def is_balanced(root):
    def check(node):
        if node is None:
            return 0

        left = check(node.left)
        if left == -1:
            return -1

        right = check(node.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)

    return check(root) != -1


root = TreeNode(500)
root.left = TreeNode(200)
root.left.left = TreeNode(100)

print(is_balanced(root))
```

Output:

```text
False
```

## 17. Calculate AVL Balance Factor

### Problem

Calculate balance factor of a node.

### Solution

```python
def balance_factor(root):
    if root is None:
        return 0
    return height(root.left) - height(root.right)


root = TreeNode(500)
root.left = TreeNode(200)
root.right = TreeNode(900)

print(balance_factor(root))
```

Output:

```text
0
```

## 18. Right Rotation for AVL LL Case

### Problem

Perform right rotation on an unbalanced node.

### Solution

```python
def right_rotate(y):
    x = y.left
    moved_subtree = x.right

    x.right = y
    y.left = moved_subtree

    return x


root = TreeNode(30)
root.left = TreeNode(20)
root.left.left = TreeNode(10)

new_root = right_rotate(root)
print(new_root.value)
print(new_root.left.value)
print(new_root.right.value)
```

Output:

```text
20
10
30
```

## 19. Left Rotation for AVL RR Case

### Problem

Perform left rotation on an unbalanced node.

### Solution

```python
def left_rotate(x):
    y = x.right
    moved_subtree = y.left

    y.left = x
    x.right = moved_subtree

    return y


root = TreeNode(10)
root.right = TreeNode(20)
root.right.right = TreeNode(30)

new_root = left_rotate(root)
print(new_root.value)
print(new_root.left.value)
print(new_root.right.value)
```

Output:

```text
20
10
30
```

## 20. Insert Into Simple AVL Tree

### Problem

Insert values and keep the tree balanced using AVL rotations.

### Solution

```python
class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


def node_height(node):
    return node.height if node else 0


def update_height(node):
    node.height = 1 + max(node_height(node.left), node_height(node.right))


def avl_balance(node):
    return node_height(node.left) - node_height(node.right)


def avl_right_rotate(y):
    x = y.left
    moved = x.right
    x.right = y
    y.left = moved
    update_height(y)
    update_height(x)
    return x


def avl_left_rotate(x):
    y = x.right
    moved = y.left
    y.left = x
    x.right = moved
    update_height(x)
    update_height(y)
    return y


def insert_avl(root, value):
    if root is None:
        return AVLNode(value)

    if value < root.value:
        root.left = insert_avl(root.left, value)
    elif value > root.value:
        root.right = insert_avl(root.right, value)
    else:
        return root

    update_height(root)
    balance = avl_balance(root)

    if balance > 1 and value < root.left.value:
        return avl_right_rotate(root)
    if balance < -1 and value > root.right.value:
        return avl_left_rotate(root)
    if balance > 1 and value > root.left.value:
        root.left = avl_left_rotate(root.left)
        return avl_right_rotate(root)
    if balance < -1 and value < root.right.value:
        root.right = avl_right_rotate(root.right)
        return avl_left_rotate(root)

    return root


root = None
for price in [10, 20, 30]:
    root = insert_avl(root, price)

print(root.value)
print(root.left.value)
print(root.right.value)
```

Output:

```text
20
10
30
```

## Final Notes

- Binary trees do not require ordering.
- BSTs require left smaller and right larger.
- AVL trees are self-balancing BSTs.
- Inorder traversal of a BST gives sorted values.
- AVL rotations keep operations near `O(log n)`.
