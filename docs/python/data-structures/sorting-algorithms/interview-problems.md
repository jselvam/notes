# Sorting Algorithms: Interview Problems

This page contains **20 interview problems** on sorting algorithms in Python.

It covers Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort, and Heap Sort.

## 1. Bubble Sort Product Prices

### Problem

Sort product prices using bubble sort.

### Explanation

Repeatedly swap adjacent prices if they are in the wrong order.

### Solution

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

## 2. Bubble Sort Descending Ratings

### Problem

Sort ratings in descending order.

### Explanation

Change the comparison so larger values move toward the front.

### Solution

```python
def bubble_sort_desc(values):
    n = len(values)

    for pass_no in range(n):
        for index in range(0, n - pass_no - 1):
            if values[index] < values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]

    return values


print(bubble_sort_desc([4.2, 4.9, 3.8]))
```

Output:

```text
[4.9, 4.2, 3.8]
```

## 3. Detect If Bubble Sort Stops Early

### Problem

Count passes needed for a nearly sorted list.

### Explanation

If no swap happens during a pass, the list is already sorted.

### Solution

```python
def bubble_sort_passes(values):
    n = len(values)
    passes = 0

    for pass_no in range(n):
        swapped = False
        passes += 1
        for index in range(0, n - pass_no - 1):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]
                swapped = True
        if not swapped:
            break

    return passes


print(bubble_sort_passes([1000, 2000, 3000]))
```

Output:

```text
1
```

## 4. Selection Sort Product Prices

### Problem

Sort product prices using selection sort.

### Explanation

Find the smallest value in the unsorted section and swap it to the front.

### Solution

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

## 5. Selection Sort Product Names

### Problem

Sort product names alphabetically.

### Explanation

Strings can be compared directly in Python.

### Solution

```python
products = ["Monitor", "Keyboard", "Laptop"]
print(selection_sort(products))
```

Output:

```text
['Keyboard', 'Laptop', 'Monitor']
```

## 6. Count Selection Sort Swaps

### Problem

Count how many actual swaps selection sort performs.

### Explanation

Avoid counting when the minimum is already at the current position.

### Solution

```python
def selection_sort_swap_count(values):
    swaps = 0

    for start in range(len(values)):
        min_index = start
        for index in range(start + 1, len(values)):
            if values[index] < values[min_index]:
                min_index = index

        if min_index != start:
            values[start], values[min_index] = values[min_index], values[start]
            swaps += 1

    return swaps


print(selection_sort_swap_count([3, 1, 2]))
```

Output:

```text
2
```

## 7. Insertion Sort Product Prices

### Problem

Sort product prices using insertion sort.

### Explanation

Take each value and insert it into the correct position in the sorted left side.

### Solution

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

## 8. Insertion Sort Nearly Sorted Stock Counts

### Problem

Sort a nearly sorted stock list.

### Explanation

Insertion sort performs well when only a few items are out of place.

### Solution

```python
print(insertion_sort([10, 20, 30, 25, 40]))
```

Output:

```text
[10, 20, 25, 30, 40]
```

## 9. Sort Products by Price With Insertion Sort

### Problem

Sort product dictionaries by price.

### Explanation

Compare the `price` field while shifting items.

### Solution

```python
def insertion_sort_by_price(products):
    for index in range(1, len(products)):
        current = products[index]
        position = index - 1

        while position >= 0 and products[position]["price"] > current["price"]:
            products[position + 1] = products[position]
            position -= 1

        products[position + 1] = current

    return products


items = [{"name": "Laptop", "price": 55000}, {"name": "Mouse", "price": 700}]
print(insertion_sort_by_price(items))
```

Output:

```text
[{'name': 'Mouse', 'price': 700}, {'name': 'Laptop', 'price': 55000}]
```

## 10. Merge Sort Product Prices

### Problem

Sort prices using merge sort.

### Explanation

Split the list, sort halves, and merge sorted halves.

### Solution

```python
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


def merge_sort(values):
    if len(values) <= 1:
        return values

    mid = len(values) // 2
    left = merge_sort(values[:mid])
    right = merge_sort(values[mid:])
    return merge(left, right)


print(merge_sort([5000, 1200, 3000, 999]))
```

Output:

```text
[999, 1200, 3000, 5000]
```

## 11. Merge Two Sorted Price Lists

### Problem

Merge two sorted supplier price lists.

### Explanation

Use two pointers and always pick the smaller current value.

### Solution

```python
print(merge([700, 1200, 5000], [650, 1500, 3000]))
```

Output:

```text
[650, 700, 1200, 1500, 3000, 5000]
```

## 12. Count Inversions With Merge Sort

### Problem

Count how many price pairs are out of order.

### Explanation

During merge, when a right value comes before a left value, it creates inversions.

### Solution

```python
def count_inversions(values):
    if len(values) <= 1:
        return values, 0

    mid = len(values) // 2
    left, left_count = count_inversions(values[:mid])
    right, right_count = count_inversions(values[mid:])

    merged = []
    i = 0
    j = 0
    split_count = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            split_count += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, left_count + right_count + split_count


print(count_inversions([3, 1, 2])[1])
```

Output:

```text
2
```

## 13. Quick Sort Product Prices

### Problem

Sort prices using quick sort.

### Explanation

Choose a pivot and partition values into smaller, equal, and greater groups.

### Solution

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


print(quick_sort([5000, 1200, 3000, 999]))
```

Output:

```text
[999, 1200, 3000, 5000]
```

## 14. Quick Sort With Duplicate Prices

### Problem

Sort prices that include duplicates.

### Explanation

Keeping an `equal` group handles duplicate pivot values cleanly.

### Solution

```python
print(quick_sort([3000, 1200, 3000, 999]))
```

Output:

```text
[999, 1200, 3000, 3000]
```

## 15. Partition Around Pivot

### Problem

Partition prices around a pivot value.

### Explanation

Return values less than pivot, equal to pivot, and greater than pivot.

### Solution

```python
def partition(values, pivot):
    smaller = [value for value in values if value < pivot]
    equal = [value for value in values if value == pivot]
    greater = [value for value in values if value > pivot]
    return smaller, equal, greater


print(partition([5, 2, 8, 5, 1], 5))
```

Output:

```text
([2, 1], [5, 5], [8])
```

## 16. Heap Sort Product Prices

### Problem

Sort prices using a heap.

### Explanation

Build a min heap and pop values in ascending order.

### Solution

```python
import heapq


def heap_sort(values):
    heap = values[:]
    heapq.heapify(heap)
    result = []

    while heap:
        result.append(heapq.heappop(heap))

    return result


print(heap_sort([5000, 1200, 3000, 999]))
```

Output:

```text
[999, 1200, 3000, 5000]
```

## 17. Heap Sort Product Names

### Problem

Sort product names alphabetically using a heap.

### Explanation

Python heaps order strings lexicographically.

### Solution

```python
print(heap_sort(["Monitor", "Keyboard", "Laptop"]))
```

Output:

```text
['Keyboard', 'Laptop', 'Monitor']
```

## 18. Sort Products by Rating Descending

### Problem

Sort product dictionaries by rating from high to low.

### Explanation

For real projects, Python's built-in stable sorting is preferred.

### Solution

```python
products = [
    {"name": "Laptop", "rating": 4.7},
    {"name": "Mouse", "rating": 4.3},
    {"name": "Keyboard", "rating": 4.8},
]

print(sorted(products, key=lambda product: product["rating"], reverse=True))
```

Output:

```text
[{'name': 'Keyboard', 'rating': 4.8}, {'name': 'Laptop', 'rating': 4.7}, {'name': 'Mouse', 'rating': 4.3}]
```

## 19. Find Top 3 Cheapest Products

### Problem

Find the three cheapest prices.

### Explanation

Sorting all values works, but heap-based selection can be better for large data.

### Solution

```python
import heapq


prices = [5000, 1200, 3000, 999, 8000]
print(heapq.nsmallest(3, prices))
```

Output:

```text
[999, 1200, 3000]
```

## 20. Choose Best Sorting Algorithm

### Problem

Map scenarios to good sorting choices.

### Explanation

Different sorting algorithms fit different constraints.

### Solution

```python
choices = {
    "small nearly sorted list": "Insertion Sort",
    "stable predictable sort": "Merge Sort",
    "fast average sort": "Quick Sort",
    "top-k prices": "Heap",
    "production Python": "sorted() / list.sort()",
}

print(choices["stable predictable sort"])
print(choices["top-k prices"])
```

Output:

```text
Merge Sort
Heap
```

## Final Notes

- Bubble, Selection, and Insertion Sort are useful for learning basics.
- Merge Sort and Quick Sort are important divide-and-conquer algorithms.
- Heap Sort connects sorting with priority queues.
- In production Python, prefer `sorted()` and `.sort()` unless an interview asks for manual sorting.
