# Heap and Priority Queue in Python: Core Concepts

A heap is a tree-based data structure used to quickly access the smallest or largest item.

Python provides a built-in heap module:

```python
import heapq
```

`heapq` implements a **min heap**.

Examples use an online computer shopping system.

## Why Heaps Matter

Heaps are useful when you repeatedly need the highest or lowest priority item.

Shopping examples:

- process urgent orders first
- find cheapest products
- find top selling products
- schedule delivery jobs by earliest time
- keep top `k` expensive products
- merge sorted inventory feeds

## Min Heap

In a min heap, the smallest item is always at index `0`.

```python
import heapq

prices = [999, 25, 75, 500]
heapq.heapify(prices)

print(prices[0])
```

Output:

```text
25
```

## Heap Operations

| Operation | Python API | Complexity |
|-----------|------------|------------|
| create heap | `heapq.heapify(items)` | `O(n)` |
| push item | `heapq.heappush(heap, item)` | `O(log n)` |
| pop smallest | `heapq.heappop(heap)` | `O(log n)` |
| read smallest | `heap[0]` | `O(1)` |
| push then pop | `heapq.heappushpop(heap, item)` | `O(log n)` |
| pop then push | `heapq.heapreplace(heap, item)` | `O(log n)` |

## Push and Pop

```python
import heapq

heap = []

heapq.heappush(heap, 500)
heapq.heappush(heap, 25)
heapq.heappush(heap, 999)

print(heapq.heappop(heap))
print(heapq.heappop(heap))
```

Output:

```text
25
500
```

## Max Heap Using Negative Values

Python has a min heap. To simulate a max heap, store negative values.

```python
import heapq

prices = [999, 25, 75]
max_heap = []

for price in prices:
    heapq.heappush(max_heap, -price)

print(-heapq.heappop(max_heap))
```

Output:

```text
999
```

## Priority Queue

A priority queue removes items by priority, not insertion order.

```python
import heapq

orders = []

heapq.heappush(orders, (1, "urgent-order"))
heapq.heappush(orders, (3, "normal-order"))
heapq.heappush(orders, (2, "gift-order"))

print(heapq.heappop(orders))
```

Output:

```text
(1, 'urgent-order')
```

Lower number means higher priority in this example.

## Tie Breaker

If two priorities are equal, Python compares the next tuple item. Use a counter to avoid comparison issues.

```python
import heapq

tasks = []
counter = 0

counter += 1
heapq.heappush(tasks, (1, counter, {"order_id": 1001}))

counter += 1
heapq.heappush(tasks, (1, counter, {"order_id": 1002}))

print(heapq.heappop(tasks)[2])
```

Output:

```text
{'order_id': 1001}
```

## Heap vs Sorted List

| Need | Better choice |
|------|---------------|
| repeatedly get min/max | heap |
| keep all values fully sorted | sorted list |
| frequent arbitrary search | dictionary or set |
| FIFO processing | queue |

## Common Mistakes

### Forgetting `heapq` is min heap

Use negative values for max heap behavior.

### Sorting every time

Repeated sorting is usually more expensive than using a heap.

### Mutating heap list directly

If you append directly, call `heapq.heapify()` or use `heappush()`.

### Tuple comparison surprises

Use `(priority, counter, item)` when items may not be directly comparable.

## See also

- [Interview problems](interview-problems.md)
- [Interview questions](interview-questions.md)
- [Hash table](../hash-table/core-concepts.md)
- [Trees](../trees/core-concepts.md)
