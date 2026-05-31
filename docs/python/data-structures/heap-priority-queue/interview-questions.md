# Heap and Priority Queue: 10 Interview Questions

## 1. What is a heap?

A heap is a tree-based data structure where the smallest or largest element can be accessed quickly.

## 2. What type of heap does Python's `heapq` provide?

Python's `heapq` provides a min heap.

## 3. What is a priority queue?

A priority queue removes items based on priority instead of insertion order.

## 4. What is the time complexity of `heappush()`?

`heappush()` takes `O(log n)` time.

## 5. What is the time complexity of `heappop()`?

`heappop()` takes `O(log n)` time.

## 6. How do you simulate a max heap in Python?

Store negative values in the min heap and multiply by `-1` when reading values back.

## 7. What is the benefit of `heapify()`?

`heapify()` converts a list into a heap in `O(n)` time.

## 8. When should you use a heap instead of sorting?

Use a heap when you repeatedly need min/max or top `k` values without fully sorting everything.

## 9. Why use a counter in priority queue tuples?

A counter preserves insertion order for equal priorities and prevents Python from comparing non-comparable items.

## 10. What are common heap interview patterns?

Common patterns include top `k`, kth smallest/largest, merge sorted lists, scheduling by priority, and median from stream.

## See also

- [Core concepts](core-concepts.md)
- [Interview problems](interview-problems.md)
