# Heap and Priority Queue: Interview Problems

This page contains **20 interview problems** for heaps and priority queues in Python.

Problems avoid duplicates already used in earlier Python DSA notes and focus on heap-specific patterns.

## 1. Find Cheapest Product

### Problem

Given product prices, find the cheapest price using a heap.

### Solution

```python
import heapq

prices = [999, 25, 75, 500]
heapq.heapify(prices)

print(heapq.heappop(prices))
```

Output:

```text
25
```

## 2. Find Most Expensive Product With Max Heap

### Problem

Use Python's min heap to simulate a max heap.

### Solution

```python
import heapq

prices = [999, 25, 75, 500]
max_heap = [-price for price in prices]
heapq.heapify(max_heap)

print(-heapq.heappop(max_heap))
```

Output:

```text
999
```

## 3. Get K Cheapest Products

### Problem

Find the `k` cheapest product prices.

### Solution

```python
import heapq

prices = [999, 25, 75, 500, 40]
k = 3

print(heapq.nsmallest(k, prices))
```

Output:

```text
[25, 40, 75]
```

## 4. Get K Most Expensive Products

### Problem

Find the `k` most expensive prices.

### Solution

```python
import heapq

prices = [999, 25, 75, 500, 40]
k = 2

print(heapq.nlargest(k, prices))
```

Output:

```text
[999, 500]
```

## 5. Process Urgent Orders First

### Problem

Process orders by priority where smaller priority number means more urgent.

### Solution

```python
import heapq

orders = []
heapq.heappush(orders, (2, "normal-order"))
heapq.heappush(orders, (1, "urgent-order"))
heapq.heappush(orders, (3, "low-priority-order"))

while orders:
    print(heapq.heappop(orders)[1])
```

Output:

```text
urgent-order
normal-order
low-priority-order
```

## 6. Priority Queue With Stable Order

### Problem

If priorities are equal, process older order first.

### Solution

```python
import heapq

queue = []
counter = 0

for priority, order_id in [(1, "order-1002"), (1, "order-1001")]:
    counter += 1
    heapq.heappush(queue, (priority, counter, order_id))

print(heapq.heappop(queue)[2])
print(heapq.heappop(queue)[2])
```

Output:

```text
order-1002
order-1001
```

## 7. Merge Sorted Price Lists

### Problem

Merge sorted prices from multiple warehouses.

### Solution

```python
import heapq

warehouse_prices = [
    [20, 50, 100],
    [25, 75],
    [10, 90],
]

merged = list(heapq.merge(*warehouse_prices))

print(merged)
```

Output:

```text
[10, 20, 25, 50, 75, 90, 100]
```

## 8. Keep Top K Selling Products From Stream

### Problem

Keep only top `k` sales counts while reading a stream.

### Solution

```python
import heapq

sales_counts = [50, 20, 70, 10, 90, 60]
k = 3
heap = []

for count in sales_counts:
    heapq.heappush(heap, count)
    if len(heap) > k:
        heapq.heappop(heap)

print(sorted(heap, reverse=True))
```

Output:

```text
[90, 70, 60]
```

## 9. Find Kth Cheapest Product

### Problem

Find the kth cheapest price.

### Solution

```python
import heapq

prices = [999, 25, 75, 500, 40]
k = 3

print(heapq.nsmallest(k, prices)[-1])
```

Output:

```text
75
```

## 10. Find Kth Most Expensive Product

### Problem

Find the kth most expensive price.

### Solution

```python
import heapq

prices = [999, 25, 75, 500, 40]
k = 2

print(heapq.nlargest(k, prices)[-1])
```

Output:

```text
500
```

## 11. Schedule Deliveries by Earliest Time

### Problem

Process delivery jobs by earliest scheduled minute.

### Solution

```python
import heapq

deliveries = []
heapq.heappush(deliveries, (30, "deliver laptop"))
heapq.heappush(deliveries, (10, "deliver mouse"))
heapq.heappush(deliveries, (20, "deliver monitor"))

while deliveries:
    print(heapq.heappop(deliveries))
```

Output:

```text
(10, 'deliver mouse')
(20, 'deliver monitor')
(30, 'deliver laptop')
```

## 12. Reorder Support Tickets by Severity

### Problem

Serve highest severity support tickets first.

### Solution

```python
import heapq

tickets = []

for severity, ticket in [(5, "refund issue"), (9, "payment failed"), (3, "general query")]:
    heapq.heappush(tickets, (-severity, ticket))

print(heapq.heappop(tickets)[1])
```

Output:

```text
payment failed
```

## 13. Connect Cables With Minimum Cost

### Problem

Given cable lengths, connect two smallest at a time and return total cost.

### Solution

```python
import heapq

cables = [4, 3, 2, 6]
heapq.heapify(cables)
cost = 0

while len(cables) > 1:
    first = heapq.heappop(cables)
    second = heapq.heappop(cables)
    merged = first + second
    cost += merged
    heapq.heappush(cables, merged)

print(cost)
```

Output:

```text
29
```

## 14. Find Median From Product Price Stream

### Problem

Maintain median while prices arrive one by one.

### Solution

```python
import heapq

low = []
high = []


def add_price(price):
    heapq.heappush(low, -price)
    heapq.heappush(high, -heapq.heappop(low))

    if len(high) > len(low):
        heapq.heappush(low, -heapq.heappop(high))


def median():
    if len(low) > len(high):
        return -low[0]
    return (-low[0] + high[0]) / 2


for price in [100, 200, 50]:
    add_price(price)
    print(median())
```

Output:

```text
100
150.0
100
```

## 15. Find Products Within Smallest Price Range

### Problem

Given sorted prices from suppliers, find the smallest current range that includes one price from each supplier.

### Solution

```python
import heapq

lists = [[10, 20], [15, 25], [18, 30]]
heap = []
current_max = float("-inf")

for row, values in enumerate(lists):
    heapq.heappush(heap, (values[0], row, 0))
    current_max = max(current_max, values[0])

best = (float("-inf"), float("inf"))

while len(heap) == len(lists):
    current_min, row, index = heapq.heappop(heap)
    if current_max - current_min < best[1] - best[0]:
        best = (current_min, current_max)

    if index + 1 < len(lists[row]):
        next_value = lists[row][index + 1]
        current_max = max(current_max, next_value)
        heapq.heappush(heap, (next_value, row, index + 1))

print(best)
```

Output:

```text
(15, 20)
```

## 16. Replace Heap Root Efficiently

### Problem

Pop the smallest price and push a new price in one operation.

### Solution

```python
import heapq

prices = [25, 75, 999]
heapq.heapify(prices)

removed = heapq.heapreplace(prices, 50)

print(removed)
print(prices[0])
```

Output:

```text
25
50
```

## 17. Push Then Pop Efficiently

### Problem

Push a new price and pop the smallest in one operation.

### Solution

```python
import heapq

prices = [25, 75, 999]
heapq.heapify(prices)

result = heapq.heappushpop(prices, 10)

print(result)
print(prices)
```

Output:

```text
10
[25, 75, 999]
```

## 18. Find K Closest Prices to Budget

### Problem

Find `k` prices closest to a customer's budget.

### Solution

```python
import heapq

prices = [100, 250, 300, 450, 900]
budget = 280
k = 3

closest = heapq.nsmallest(k, prices, key=lambda price: abs(price - budget))

print(closest)
```

Output:

```text
[300, 250, 100]
```

## 19. Sort Nearly Sorted Order IDs

### Problem

Sort values where each item is at most `k` positions away from its sorted position.

### Solution

```python
import heapq

values = [3, 1, 2, 6, 4, 5]
k = 2
heap = values[: k + 1]
heapq.heapify(heap)
result = []

for value in values[k + 1:]:
    result.append(heapq.heappushpop(heap, value))

while heap:
    result.append(heapq.heappop(heap))

print(result)
```

Output:

```text
[1, 2, 3, 4, 5, 6]
```

## 20. Implement Priority Queue Class

### Problem

Build a reusable priority queue for order jobs.

### Solution

```python
import heapq


class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.counter = 0

    def push(self, priority, item):
        self.counter += 1
        heapq.heappush(self.heap, (priority, self.counter, item))

    def pop(self):
        if not self.heap:
            return None
        return heapq.heappop(self.heap)[2]


queue = PriorityQueue()
queue.push(2, "pack order")
queue.push(1, "refund failed payment")
queue.push(1, "call customer")

print(queue.pop())
print(queue.pop())
```

Output:

```text
refund failed payment
call customer
```

## Final Notes

- `heapq` is a min heap.
- Use negative numbers for max heap behavior.
- Use `(priority, counter, item)` for stable priority queues.
- Heaps are ideal for repeated min/max or top `k` problems.
- Heap operations are usually `O(log n)`.
