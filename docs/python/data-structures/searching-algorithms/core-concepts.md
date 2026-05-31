# Searching Algorithms in Python: Core Concepts

Searching means finding whether an item exists and where it is located.

This page covers:

- Linear Search
- Binary Search
- Search in Rotated Array
- First and Last Position
- Peak Element

Examples use an online computer shopping system.

## Why Searching Matters

In a shopping system, search is used to:

- find a product by SKU
- find a price in a sorted price list
- find first and last occurrence of a repeated product rating
- find a peak sales day
- search in rotated inventory batches

## Linear Search

Linear search checks every element one by one.

```python
def linear_search(items, target):
    for index, item in enumerate(items):
        if item == target:
            return index

    return -1


products = ["mouse", "keyboard", "monitor"]
print(linear_search(products, "monitor"))
```

Output:

```text
2
```

### When to Use Linear Search

Use linear search when:

- data is unsorted
- list is small
- only one pass is acceptable
- the search condition is custom

Complexity: `O(n)` time and `O(1)` extra space.

## Binary Search

Binary search works on sorted data.

It compares the target with the middle element and eliminates half of the search space each time.

```python
def binary_search(values, target):
    left = 0
    right = len(values) - 1

    while left <= right:
        mid = (left + right) // 2

        if values[mid] == target:
            return mid
        if target < values[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


prices = [999, 1499, 2999, 4999, 8999]
print(binary_search(prices, 4999))
```

Output:

```text
3
```

Complexity: `O(log n)` time and `O(1)` extra space.

## Recursive Binary Search

```python
def recursive_binary_search(values, target, left=0, right=None):
    if right is None:
        right = len(values) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if values[mid] == target:
        return mid
    if target < values[mid]:
        return recursive_binary_search(values, target, left, mid - 1)
    return recursive_binary_search(values, target, mid + 1, right)


print(recursive_binary_search([10, 20, 30, 40], 30))
```

Output:

```text
2
```

## Linear Search vs Binary Search

| Feature | Linear Search | Binary Search |
|---------|---------------|---------------|
| Data requirement | unsorted or sorted | sorted |
| Time complexity | `O(n)` | `O(log n)` |
| Space complexity | `O(1)` | `O(1)` iterative |
| Best use | small/custom search | sorted large data |

## Binary Search Template

```python
left = 0
right = len(values) - 1

while left <= right:
    mid = (left + right) // 2

    if condition_found(mid):
        return mid
    elif should_go_left(mid):
        right = mid - 1
    else:
        left = mid + 1
```

## First and Last Position

When duplicates exist, binary search can be modified to find boundaries.

```python
def find_boundary(values, target, find_first):
    left = 0
    right = len(values) - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        if values[mid] == target:
            answer = mid
            if find_first:
                right = mid - 1
            else:
                left = mid + 1
        elif values[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return answer


ratings = [1, 2, 2, 2, 3]
print(find_boundary(ratings, 2, True), find_boundary(ratings, 2, False))
```

Output:

```text
1 3
```

## Search in Rotated Sorted Array

A rotated sorted array is sorted but shifted.

Example: `[4, 5, 6, 7, 0, 1, 2]`

At least one side is always sorted.

```python
def search_rotated(values, target):
    left = 0
    right = len(values) - 1

    while left <= right:
        mid = (left + right) // 2

        if values[mid] == target:
            return mid

        if values[left] <= values[mid]:
            if values[left] <= target < values[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if values[mid] < target <= values[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))
```

Output:

```text
4
```

## Peak Element

A peak element is greater than its neighbor or neighbors.

```python
def find_peak(values):
    left = 0
    right = len(values) - 1

    while left < right:
        mid = (left + right) // 2

        if values[mid] < values[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left


print(find_peak([1, 3, 5, 4, 2]))
```

Output:

```text
2
```

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| using binary search on unsorted data | sort first or use linear search |
| wrong loop condition | choose `left <= right` or `left < right` carefully |
| infinite loop | update `left` and `right` every iteration |
| boundary off-by-one | test one item and two item arrays |
| losing duplicate boundaries | keep searching after finding a match |

## Complexity Summary

| Problem | Time | Space |
|---------|------|-------|
| Linear Search | `O(n)` | `O(1)` |
| Binary Search | `O(log n)` | `O(1)` |
| First and Last Position | `O(log n)` | `O(1)` |
| Search in Rotated Array | `O(log n)` | `O(1)` |
| Peak Element | `O(log n)` | `O(1)` |

## See also

- [Interview problems](interview-problems.md)
- [Interview questions](interview-questions.md)
- [Recursion](../recursion/core-concepts.md)
