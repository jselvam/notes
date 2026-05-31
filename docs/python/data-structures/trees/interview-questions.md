# Binary Trees, BSTs, and AVL Trees: 10 Interview Questions

## 1. What is a binary tree?

A binary tree is a tree where each node has at most two children: left and right.

## 2. What is a binary search tree?

A BST is a binary tree where values in the left subtree are smaller than the node and values in the right subtree are larger.

## 3. What is an AVL tree?

An AVL tree is a self-balancing BST where every node has a balance factor of `-1`, `0`, or `1`.

## 4. What is inorder traversal?

Inorder traversal visits left subtree, root, then right subtree. In a BST, it returns values in sorted order.

## 5. What is level-order traversal?

Level-order traversal visits nodes level by level using a queue.

## 6. What is the time complexity of search in a balanced BST?

Search in a balanced BST is `O(log n)`.

## 7. What is the worst-case time complexity of search in a normal BST?

The worst case is `O(n)` when the BST becomes skewed like a linked list.

## 8. What is a balance factor in AVL trees?

Balance factor is `height(left subtree) - height(right subtree)`.

## 9. What are the four AVL rotation cases?

The four cases are LL, RR, LR, and RL.

## 10. What is the main difference between BST and AVL tree?

A BST follows ordering rules, but it may become unbalanced. An AVL tree is a BST that automatically balances itself using rotations.

## See also

- [Core concepts](core-concepts.md)
- [Interview problems](interview-problems.md)
