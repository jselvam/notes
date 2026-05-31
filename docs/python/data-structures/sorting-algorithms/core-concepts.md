# Sorting Algorithms in Python: Core Concepts

Sorting arranges data in a required order, usually ascending or descending.

This page covers:

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort

Examples use an online computer shopping system.

## Why Sorting Matters

In a shopping system, sorting helps with:

- showing products by price
- ranking products by rating
- ordering recent purchases by date
- sorting inventory by stock count
- preparing data for binary search

## Sorting Terminology

| Term | Meaning |
|------|---------|
| In-place | sorts using little extra memory |
| Stable | equal elements keep their original relative order |
| Comparison sort | sorts by comparing pairs of values |
| Divide and conquer | splits the problem, solves parts, combines results |

## Bubble Sort

Bubble sort repeatedly swaps adjacent items if they are in the wrong order.

```python
def bubble_sort(values):
    n = len(values)

    for pass_no in range(n):
        swapped = False
        for index in range(0, n - pass_no - 1):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]
                swapped = True

        if not swapped:
            break

    return values


print(bubble_sort([5000, 1200, 3000]))
```

Output:

```text
[1200, 3000, 5000]
```

Bubble sort is easy to understand but inefficient for large lists.

## Selection Sort

Selection sort repeatedly selects the smallest remaining element and places it at the front.

```python
def selection_sort(values):
    n = len(values)

    for start in range(n):
        min_index = start
        for index in range(start + 1, n):
            if values[index] < values[min_index]:
                min_index = index

        values[start], values[min_index] = values[min_index], values[start]

    return values


print(selection_sort([5000, 1200, 3000]))
```

Output:

```text
[1200, 3000, 5000]
```

Selection sort performs fewer swaps than bubble sort, but it is still `O(n^2)`.

## Insertion Sort

Insertion sort builds a sorted section one item at a time.

```python
def insertion_sort(values):
    for index in range(1, len(values)):
        current = values[index]
        position = index - 1

        while position >= 0 and values[position] > current:
            values[position + 1] = values[position]
            position -= 1

        values[position + 1] = current

    return values


print(insertion_sort([5000, 1200, 3000]))
```

Output:

```text
[1200, 3000, 5000]
```

Insertion sort is useful for small or nearly sorted lists.

## Merge Sort

Merge sort splits the list into halves, sorts each half, and merges sorted halves.

```python
def merge_sort(values):
    if len(values) <= 1:
        return values

    mid = len(values) // 2
    left = merge_sort(values[:mid])
    right = merge_sort(values[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


print(merge_sort([5000, 1200, 3000]))
```

Output:

```text
[1200, 3000, 5000]
```

Merge sort is stable and has predictable `O(n log n)` time.

## Quick Sort

Quick sort chooses a pivot and partitions values around it.

```python
def quick_sort(values):
    if len(values) <= 1:
        return values

    pivot = values[-1]
    smaller = []
    equal = []
    greater = []

    for value in values:
        if value < pivot:
            smaller.append(value)
        elif value == pivot:
            equal.append(value)
        else:
            greater.append(value)

    return quick_sort(smaller) + equal + quick_sort(greater)


print(quick_sort([5000, 1200, 3000]))
```

Output:

```text
[1200, 3000, 5000]
```

Quick sort is fast on average, but poor pivot choices can make it `O(n^2)`.

## Heap Sort

Heap sort uses a heap to repeatedly remove the smallest or largest element.

```python
import heapq


def heap_sort(values):
    heap = values[:]
    heapq.heapify(heap)

    result = []
    while heap:
        result.append(heapq.heappop(heap))

    return result


print(heap_sort([5000, 1200, 3000]))
```

Output:

```text
[1200, 3000, 5000]
```

Heap sort is useful when you need priority-queue behavior or top-k style sorting.

## Algorithm Comparison

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble Sort | `O(n)` | `O(n^2)` | `O(n^2)` | `O(1)` | Yes |
| Selection Sort | `O(n^2)` | `O(n^2)` | `O(n^2)` | `O(1)` | No |
| Insertion Sort | `O(n)` | `O(n^2)` | `O(n^2)` | `O(1)` | Yes |
| Merge Sort | `O(n log n)` | `O(n log n)` | `O(n log n)` | `O(n)` | Yes |
| Quick Sort | `O(n log n)` | `O(n log n)` | `O(n^2)` | `O(log n)` average stack | Not usually |
| Heap Sort | `O(n log n)` | `O(n log n)` | `O(n log n)` | `O(1)` in-place version | No |

## Choosing a Sorting Algorithm

| Scenario | Good choice |
|----------|-------------|
| learning basics | Bubble, Selection, Insertion |
| small nearly sorted list | Insertion Sort |
| stable predictable sorting | Merge Sort |
| fast average performance | Quick Sort |
| priority queue or top-k | Heap Sort |
| production Python code | built-in `sorted()` or `.sort()` |

## Python Built-in Sorting

Python's `sorted()` and list `.sort()` use Timsort, a stable hybrid sorting algorithm optimized for real-world data.

```python
products = [
    {"name": "Laptop", "price": 55000},
    {"name": "Mouse", "price": 700},
]

print(sorted(products, key=lambda product: product["price"]))
```

Output:

```text
[{'name': 'Mouse', 'price': 700}, {'name': 'Laptop', 'price': 55000}]
```

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| assuming all sorts are stable | check stability requirement |
| using `O(n^2)` sort for large data | prefer `O(n log n)` algorithms |
| forgetting quick sort worst case | choose pivot carefully |
| using heap sort when stable order is needed | use merge sort or Python built-in sort |
| sorting when only top-k is needed | use a heap |

## See also

- [Interview problems](interview-problems.md)
- [Interview questions](interview-questions.md)
- [Searching Algorithms](../searching-algorithms/core-concepts.md)
- [Heap and Priority Queue](../heap-priority-queue/core-concepts.md)
