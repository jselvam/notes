# Stacks, Queues, and Linked Lists: 10 Interview Questions

## 1. What is a stack?

A stack is a linear data structure that follows **LIFO**: last in, first out. In Python, a list can act as a stack using `append()` and `pop()`.

## 2. What is a queue?

A queue is a linear data structure that follows **FIFO**: first in, first out. In Python, `collections.deque` is preferred for queue operations.

## 3. Why should `deque` be used for queues instead of `list.pop(0)`?

`deque.popleft()` is `O(1)`, while `list.pop(0)` is `O(n)` because all remaining elements shift left.

## 4. What is a linked list?

A linked list is a sequence of nodes where each node stores data and a pointer to the next node.

## 5. What is the time complexity of stack push and pop?

For a Python list used as a stack, `append()` and `pop()` at the end are amortized `O(1)`.

## 6. What is the time complexity of queue enqueue and dequeue with `deque`?

With `collections.deque`, `append()` and `popleft()` are `O(1)`.

## 7. What is the difference between array/list and linked list?

A Python list supports fast indexing but insertions in the middle can be costly. A linked list does not support direct indexing, but pointer changes can make insertion and deletion efficient when the node is known.

## 8. What is the slow and fast pointer technique?

It uses two pointers moving at different speeds. It is commonly used to find the middle of a linked list or detect a cycle.

## 9. What is a circular queue?

A circular queue is a fixed-size queue where the rear wraps around to the beginning when space is available.

## 10. How do you explain stack, queue, and linked list in one line?

A stack removes the newest item first, a queue removes the oldest item first, and a linked list connects items using node pointers.

## See also

- [Core concepts](core-concepts.md)
- [Interview problems](interview-problems.md)
