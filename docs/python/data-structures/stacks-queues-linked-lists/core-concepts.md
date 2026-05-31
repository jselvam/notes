# Stacks, Queues, and Linked Lists in Python: Core Concepts

Stacks, queues, and linked lists are foundational DSA topics. They are not Python-specific data types like `list` or `dict`, but Python can implement them cleanly using classes, lists, and `collections.deque`.

Examples use an online computer shopping system.

## Stack

A stack follows **LIFO**: last in, first out.

Common operations:

| Operation | Meaning | Complexity |
|-----------|---------|------------|
| push | add item to top | `O(1)` |
| pop | remove top item | `O(1)` |
| peek | read top item | `O(1)` |
| is empty | check if stack has no items | `O(1)` |

Shopping examples:

- undo recently added cart item
- browser back button in admin portal
- checking nested category brackets
- order workflow rollback

## Stack With Python List

```python
cart_actions = []

cart_actions.append("add laptop")
cart_actions.append("add mouse")

print(cart_actions.pop())
print(cart_actions[-1])
```

Output:

```text
add mouse
add laptop
```

Use `append()` for push and `pop()` for pop.

## Stack Class

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.items:
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0
```

## Queue

A queue follows **FIFO**: first in, first out.

Common operations:

| Operation | Meaning | Complexity with `deque` |
|-----------|---------|--------------------------|
| enqueue | add item at rear | `O(1)` |
| dequeue | remove item from front | `O(1)` |
| peek | read front item | `O(1)` |
| is empty | check if queue has no items | `O(1)` |

Shopping examples:

- customer support ticket queue
- order processing queue
- warehouse picking queue
- payment retry queue

## Queue With `deque`

Use `collections.deque` for efficient queue operations.

```python
from collections import deque

orders = deque()

orders.append("order-1001")
orders.append("order-1002")

print(orders.popleft())
print(orders[0])
```

Output:

```text
order-1001
order-1002
```

Avoid `list.pop(0)` for queues because it is `O(n)`.

## Queue Class

```python
from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.items:
            raise IndexError("dequeue from empty queue")
        return self.items.popleft()

    def peek(self):
        if not self.items:
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0
```

## Linked List

A linked list stores data in nodes. Each node points to the next node.

```text
Laptop -> Mouse -> Keyboard -> None
```

Each node has:

- `data`
- `next`

## Node Class

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

## Singly Linked List

```python
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
```

## Linked List Operations

| Operation | Complexity |
|-----------|------------|
| insert at head | `O(1)` |
| insert at tail without tail pointer | `O(n)` |
| search | `O(n)` |
| delete by value | `O(n)` |
| reverse | `O(n)` |

## Stack vs Queue vs Linked List

| Structure | Order rule | Best for |
|-----------|------------|----------|
| Stack | LIFO | undo, backtracking, parsing |
| Queue | FIFO | scheduling, order processing, BFS |
| Linked list | pointer-based sequence | dynamic insertion/deletion practice |

## Common Mistakes

### Using list as a queue with `pop(0)`

`pop(0)` shifts all remaining elements, so it is `O(n)`.

### Forgetting empty checks

Always handle empty stack or queue before removing an item.

### Losing linked list nodes

When deleting or reversing nodes, update pointers carefully.

### Confusing head and tail

The head is the first node. The tail is the last node.

## See also

- [Interview problems](interview-problems.md)
- [Interview questions](interview-questions.md)
- [Python lists](../../list/core-concepts.md)
- [Python classes and objects](../../classes-and-objects/core-concepts.md)
