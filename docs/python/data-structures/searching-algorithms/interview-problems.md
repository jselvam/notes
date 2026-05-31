# Searching Algorithms: Interview Problems

This page contains **20 interview problems** on searching algorithms in Python.

It covers Linear Search, Binary Search, Search in Rotated Array, First and Last Position, and Peak Element.

## 1. Linear Search Product Name

### Problem

Find the index of a product in an unsorted list.

### Explanation

Check each product from left to right.

### Solution

```python
def linear_search(products, target):
    for index, product in enumerate(products):
        if product == target:
            return index

    return -1


print(linear_search(["mouse", "laptop", "keyboard"], "laptop"))
```

Output:

```text
1
```

## 2. Linear Search First Product Under Budget

### Problem

Find the first product price less than or equal to a budget.

### Explanation

Linear search is good when the condition is custom and data is unsorted.

### Solution

```python
def first_under_budget(prices, budget):
    for index, price in enumerate(prices):
        if price <= budget:
            return index

    return -1


print(first_under_budget([90000, 65000, 45000], 50000))
```

Output:

```text
2
```

## 3. Linear Search All Matching Brands

### Problem

Return all indexes where a brand appears.

### Explanation

Scan the whole list because there may be multiple matches.

### Solution

```python
def all_brand_positions(brands, target):
    positions = []

    for index, brand in enumerate(brands):
        if brand == target:
            positions.append(index)

    return positions


print(all_brand_positions(["Dell", "HP", "Dell", "Lenovo"], "Dell"))
```

Output:

```text
[0, 2]
```

## 4. Binary Search Product Price

### Problem

Find a product price in a sorted price list.

### Explanation

Compare the target with the middle value and eliminate half the list.

### Solution

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


print(binary_search([999, 1499, 2999, 4999], 2999))
```

Output:

```text
2
```

## 5. Recursive Binary Search

### Problem

Implement binary search recursively.

### Explanation

The base case is when `left > right`.

### Solution

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


print(recursive_binary_search([10, 20, 30, 40], 40))
```

Output:

```text
3
```

## 6. Insert Position in Sorted Prices

### Problem

Find where a new price should be inserted to keep the list sorted.

### Explanation

This is a lower-bound binary search.

### Solution

```python
def search_insert_position(values, target):
    left = 0
    right = len(values)

    while left < right:
        mid = (left + right) // 2
        if values[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


print(search_insert_position([1000, 2000, 4000], 3000))
```

Output:

```text
2
```

## 7. First Position of Target

### Problem

Find the first position of a repeated rating.

### Explanation

When a match is found, store it and continue searching left.

### Solution

```python
def first_position(values, target):
    left = 0
    right = len(values) - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        if values[mid] == target:
            answer = mid
            right = mid - 1
        elif values[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return answer


print(first_position([1, 2, 2, 2, 3], 2))
```

Output:

```text
1
```

## 8. Last Position of Target

### Problem

Find the last position of a repeated rating.

### Explanation

When a match is found, store it and continue searching right.

### Solution

```python
def last_position(values, target):
    left = 0
    right = len(values) - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        if values[mid] == target:
            answer = mid
            left = mid + 1
        elif values[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return answer


print(last_position([1, 2, 2, 2, 3], 2))
```

Output:

```text
3
```

## 9. First and Last Position

### Problem

Return both first and last position of a target.

### Explanation

Run boundary binary search twice.

### Solution

```python
def search_range(values, target):
    return [first_position(values, target), last_position(values, target)]


print(search_range([5, 7, 7, 8, 8, 10], 8))
```

Output:

```text
[3, 4]
```

## 10. Count Target Occurrences

### Problem

Count how many times a target appears in a sorted list.

### Explanation

Use last position minus first position plus one.

### Solution

```python
def count_occurrences(values, target):
    first = first_position(values, target)
    if first == -1:
        return 0

    last = last_position(values, target)
    return last - first + 1


print(count_occurrences([1, 2, 2, 2, 3], 2))
```

Output:

```text
3
```

## 11. Search in Rotated Sorted Array

### Problem

Find a target in a rotated sorted array.

### Explanation

At every step, one side is sorted. Decide whether the target lies in that side.

### Solution

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

## 12. Search Missing Target in Rotated Array

### Problem

Return `-1` when the target is not present.

### Explanation

The same rotated search eventually exhausts the search space.

### Solution

```python
print(search_rotated([4, 5, 6, 7, 0, 1, 2], 3))
```

Output:

```text
-1
```

## 13. Find Minimum in Rotated Sorted Array

### Problem

Find the minimum value in a rotated sorted price list.

### Explanation

If middle is greater than right, the minimum is on the right side.

### Solution

```python
def find_min_rotated(values):
    left = 0
    right = len(values) - 1

    while left < right:
        mid = (left + right) // 2
        if values[mid] > values[right]:
            left = mid + 1
        else:
            right = mid

    return values[left]


print(find_min_rotated([4, 5, 6, 1, 2, 3]))
```

Output:

```text
1
```

## 14. Find Rotation Count

### Problem

Find how many times a sorted array was rotated.

### Explanation

The index of the minimum value is the rotation count.

### Solution

```python
def rotation_count(values):
    left = 0
    right = len(values) - 1

    while left < right:
        mid = (left + right) // 2
        if values[mid] > values[right]:
            left = mid + 1
        else:
            right = mid

    return left


print(rotation_count([30, 40, 50, 10, 20]))
```

Output:

```text
3
```

## 15. Peak Element Index

### Problem

Find any peak element index.

### Explanation

If the middle is rising toward the right, a peak exists on the right side.

### Solution

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

## 16. Peak Sales Day Value

### Problem

Return the value of a peak sales day.

### Explanation

Find the peak index first, then return its value.

### Solution

```python
sales = [10, 20, 35, 30, 25]
peak_index = find_peak(sales)

print(sales[peak_index])
```

Output:

```text
35
```

## 17. Square Root Using Binary Search

### Problem

Find the integer square root of a number.

### Explanation

Binary search can be used over the answer range.

### Solution

```python
def integer_sqrt(number):
    left = 0
    right = number
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square <= number:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer


print(integer_sqrt(27))
```

Output:

```text
5
```

## 18. Find Smallest Product Greater Than Budget

### Problem

Find the first sorted price greater than a budget.

### Explanation

This is an upper-bound binary search.

### Solution

```python
def first_greater(values, target):
    left = 0
    right = len(values)

    while left < right:
        mid = (left + right) // 2
        if values[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left if left < len(values) else -1


print(first_greater([1000, 2000, 3000, 5000], 3000))
```

Output:

```text
3
```

## 19. Search in 2D Sorted Matrix

### Problem

Search for a price in a matrix sorted like a flattened array.

### Explanation

Treat the matrix as one sorted list and convert index to row and column.

### Solution

```python
def search_matrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    left = 0
    right = rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        row = mid // cols
        col = mid % cols

        if matrix[row][col] == target:
            return True
        if matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


matrix = [[1, 3, 5], [7, 9, 11]]
print(search_matrix(matrix, 9))
```

Output:

```text
True
```

## 20. Find Missing Number in Sorted Sequence

### Problem

Find the missing number in a sorted sequence from `0` to `n`.

### Explanation

If `values[mid] == mid`, the missing number is on the right. Otherwise it is on the left.

### Solution

```python
def missing_number_sorted(values):
    left = 0
    right = len(values) - 1

    while left <= right:
        mid = (left + right) // 2
        if values[mid] == mid:
            left = mid + 1
        else:
            right = mid - 1

    return left


print(missing_number_sorted([0, 1, 2, 4, 5]))
```

Output:

```text
3
```

## Final Notes

- Use linear search for unsorted data or custom conditions.
- Use binary search only when the search space is ordered.
- Boundary problems keep searching after a match.
- Rotated search depends on identifying the sorted half.
- Peak search moves toward the higher neighbor.
