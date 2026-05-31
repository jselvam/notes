# Stacks, Queues, and Linked Lists: Interview Problems

This page contains **20 interview problems** for stacks, queues, and linked lists in Python.

Problems intentionally avoid common duplicates already used elsewhere in the Python notes, such as reverse string, palindrome, remove duplicates, frequency count, anagram, Two Sum, valid parentheses, merge two sorted lists, FizzBuzz, Fibonacci, and factorial.

## 1. Implement a Stack for Cart Actions

### Problem

Create a stack that stores cart actions and supports undo.

### Solution

```python
class CartActionStack:
    def __init__(self):
        self.actions = []

    def push(self, action):
        self.actions.append(action)

    def undo(self):
        if not self.actions:
            return "No action to undo"
        return self.actions.pop()


stack = CartActionStack()
stack.push("add laptop")
stack.push("add mouse")
print(stack.undo())
print(stack.undo())
```

Output:

```text
add mouse
add laptop
```

## 2. Get Minimum Price From Stack in O(1)

### Problem

Design a stack that can return the minimum product price in `O(1)`.

### Solution

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, price):
        self.stack.append(price)
        if not self.min_stack or price <= self.min_stack[-1]:
            self.min_stack.append(price)

    def pop(self):
        price = self.stack.pop()
        if price == self.min_stack[-1]:
            self.min_stack.pop()
        return price

    def get_min(self):
        return self.min_stack[-1]


prices = MinStack()
prices.push(999)
prices.push(25)
prices.push(75)
print(prices.get_min())
prices.pop()
print(prices.get_min())
```

Output:

```text
25
25
```

## 3. Decode Nested Product Bundle String

### Problem

Decode a pattern such as `2[Laptop3[Mouse]]`.

### Solution

```python
def decode_bundle(text):
    stack = []
    current = ""
    number = 0

    for char in text:
        if char.isdigit():
            number = number * 10 + int(char)
        elif char == "[":
            stack.append((current, number))
            current = ""
            number = 0
        elif char == "]":
            previous, count = stack.pop()
            current = previous + current * count
        else:
            current += char

    return current


print(decode_bundle("2[Laptop3[Mouse]]"))
```

Output:

```text
LaptopMouseMouseMouseLaptopMouseMouseMouse
```

## 4. Remove Adjacent Duplicate Cart Codes

### Problem

Remove adjacent duplicate item codes repeatedly.

### Solution

```python
def remove_adjacent_codes(codes):
    stack = []

    for code in codes:
        if stack and stack[-1] == code:
            stack.pop()
        else:
            stack.append(code)

    return stack


print(remove_adjacent_codes(["LAP", "MOU", "MOU", "KEY"]))
```

Output:

```text
['LAP', 'KEY']
```

## 5. Find Next Higher Price

### Problem

For each product price, find the next price on the right that is higher.

### Solution

```python
def next_higher_prices(prices):
    result = [-1] * len(prices)
    stack = []

    for index, price in enumerate(prices):
        while stack and prices[stack[-1]] < price:
            old_index = stack.pop()
            result[old_index] = price
        stack.append(index)

    return result


print(next_higher_prices([30, 20, 50, 40]))
```

Output:

```text
[50, 50, -1, -1]
```

## 6. Calculate Stock Span for Product Prices

### Problem

For each day, calculate how many previous consecutive days had price less than or equal to today's price.

### Solution

```python
def stock_span(prices):
    spans = []
    stack = []

    for index, price in enumerate(prices):
        while stack and stack[-1][0] <= price:
            stack.pop()

        span = index + 1 if not stack else index - stack[-1][1]
        spans.append(span)
        stack.append((price, index))

    return spans


print(stock_span([100, 80, 60, 70, 60, 75, 85]))
```

Output:

```text
[1, 1, 1, 2, 1, 4, 6]
```

## 7. Simplify Warehouse Path

### Problem

Simplify a warehouse path using stack logic.

### Solution

```python
def simplify_path(path):
    stack = []

    for part in path.split("/"):
        if part == "" or part == ".":
            continue
        if part == "..":
            if stack:
                stack.pop()
        else:
            stack.append(part)

    return "/" + "/".join(stack)


print(simplify_path("/warehouse/./laptops/../monitors/"))
```

Output:

```text
/warehouse/monitors
```

## 8. Evaluate Reverse Polish Order Total

### Problem

Evaluate a postfix expression for a cart calculation.

### Solution

```python
def evaluate_postfix(tokens):
    stack = []

    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))
        else:
            stack.append(int(token))

    return stack[-1]


print(evaluate_postfix(["100", "20", "-", "2", "*"]))
```

Output:

```text
160
```

## 9. Implement Queue for Order Processing

### Problem

Create a queue that processes orders in FIFO order.

### Solution

```python
from collections import deque


orders = deque()
orders.append("order-1001")
orders.append("order-1002")
orders.append("order-1003")

print(orders.popleft())
print(orders.popleft())
```

Output:

```text
order-1001
order-1002
```

## 10. Implement Queue Using Two Stacks

### Problem

Build a queue using two stacks.

### Solution

```python
class QueueUsingStacks:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def enqueue(self, value):
        self.input_stack.append(value)

    def dequeue(self):
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        if not self.output_stack:
            return None
        return self.output_stack.pop()


queue = QueueUsingStacks()
queue.enqueue("payment-1")
queue.enqueue("payment-2")
print(queue.dequeue())
print(queue.dequeue())
```

Output:

```text
payment-1
payment-2
```

## 11. Implement Circular Queue

### Problem

Design a fixed-size circular queue for warehouse tasks.

### Solution

```python
class CircularQueue:
    def __init__(self, size):
        self.data = [None] * size
        self.size = size
        self.front = 0
        self.count = 0

    def enqueue(self, value):
        if self.count == self.size:
            return False
        rear = (self.front + self.count) % self.size
        self.data[rear] = value
        self.count += 1
        return True

    def dequeue(self):
        if self.count == 0:
            return None
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return value


queue = CircularQueue(2)
print(queue.enqueue("pick laptop"))
print(queue.enqueue("pack mouse"))
print(queue.enqueue("ship keyboard"))
print(queue.dequeue())
```

Output:

```text
True
True
False
pick laptop
```

## 12. First Non-Repeating Product Code in Stream

### Problem

For each product code arriving in a stream, print the first code that has appeared only once.

### Solution

```python
from collections import defaultdict, deque


def first_unique_stream(codes):
    counts = defaultdict(int)
    queue = deque()
    result = []

    for code in codes:
        counts[code] += 1
        queue.append(code)

        while queue and counts[queue[0]] > 1:
            queue.popleft()

        result.append(queue[0] if queue else None)

    return result


print(first_unique_stream(["LAP", "MOU", "LAP", "KEY"]))
```

Output:

```text
['LAP', 'LAP', 'MOU', 'MOU']
```

## 13. Moving Average of Last K Order Totals

### Problem

Find the moving average of the last `k` order totals.

### Solution

```python
from collections import deque


class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.window = deque()
        self.total = 0

    def next(self, value):
        self.window.append(value)
        self.total += value
        if len(self.window) > self.size:
            self.total -= self.window.popleft()
        return self.total / len(self.window)


avg = MovingAverage(3)
print(avg.next(100))
print(avg.next(200))
print(avg.next(300))
print(avg.next(400))
```

Output:

```text
100.0
150.0
200.0
300.0
```

## 14. Generate Order Processing Sequence with BFS

### Problem

Process warehouse zones level by level using a queue.

### Solution

```python
from collections import deque


warehouse = {
    "root": ["laptops", "accessories"],
    "laptops": ["gaming", "business"],
    "accessories": ["mouse", "keyboard"],
    "gaming": [],
    "business": [],
    "mouse": [],
    "keyboard": [],
}


def bfs(start):
    queue = deque([start])
    order = []

    while queue:
        zone = queue.popleft()
        order.append(zone)
        queue.extend(warehouse[zone])

    return order


print(bfs("root"))
```

Output:

```text
['root', 'laptops', 'accessories', 'gaming', 'business', 'mouse', 'keyboard']
```

## 15. Interleave First and Second Half of Queue

### Problem

Interleave a queue like `[1, 2, 3, 4]` into `[1, 3, 2, 4]`.

### Solution

```python
from collections import deque


def interleave_queue(values):
    queue = deque(values)
    half = len(queue) // 2
    first_half = deque()

    for _ in range(half):
        first_half.append(queue.popleft())

    result = []
    while first_half:
        result.append(first_half.popleft())
        result.append(queue.popleft())

    return result


print(interleave_queue([1, 2, 3, 4]))
```

Output:

```text
[1, 3, 2, 4]
```

## 16. Create and Display a Linked List

### Problem

Create a linked list of product names and display it.

### Solution

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result


items = LinkedList()
items.append("Laptop")
items.append("Mouse")
items.append("Keyboard")
print(items.to_list())
```

Output:

```text
['Laptop', 'Mouse', 'Keyboard']
```

## 17. Insert Product at Linked List Head

### Problem

Insert a new urgent product at the beginning of a linked list.

### Solution

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_head(head, data):
    node = Node(data)
    node.next = head
    return node


head = Node("Mouse")
head.next = Node("Keyboard")
head = insert_head(head, "Laptop")

current = head
while current:
    print(current.data)
    current = current.next
```

Output:

```text
Laptop
Mouse
Keyboard
```

## 18. Delete a Product From Linked List

### Problem

Delete a node by value from a linked list.

### Solution

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_value(head, value):
    if head is None:
        return None
    if head.data == value:
        return head.next

    current = head
    while current.next and current.next.data != value:
        current = current.next

    if current.next:
        current.next = current.next.next

    return head


head = Node("Laptop")
head.next = Node("Mouse")
head.next.next = Node("Keyboard")
head = delete_value(head, "Mouse")

current = head
while current:
    print(current.data)
    current = current.next
```

Output:

```text
Laptop
Keyboard
```

## 19. Find Middle Product in Linked List

### Problem

Find the middle node using slow and fast pointers.

### Solution

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.data


head = Node("Laptop")
head.next = Node("Mouse")
head.next.next = Node("Keyboard")
print(find_middle(head))
```

Output:

```text
Mouse
```

## 20. Detect Cycle in Linked List

### Problem

Detect whether a linked list has a cycle.

### Solution

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


head = Node("Laptop")
head.next = Node("Mouse")
head.next.next = Node("Keyboard")
head.next.next.next = head.next

print(has_cycle(head))
```

Output:

```text
True
```

## Final Notes

- Stack problems often use a helper stack to remember previous values.
- Queue problems often use `collections.deque`.
- Linked list problems usually need careful pointer movement.
- Always mention edge cases such as empty input, one node, full queue, or missing value.
