# Python List Interview Problems

Lists are the Python version of the classic interview “array” data structure. Many interview patterns use lists with indexing, two pointers, sorting, stacks, queues, and sliding windows.

## Interview Pattern: When to Think About Lists

Use a list when the problem needs:

- order
- duplicates
- indexing
- slicing
- two-pointer traversal
- sorting
- stack behavior with `append()` / `pop()`
- building a result sequence

## 1. Reverse a Product List

### Problem

Reverse a list without using `reverse()`.

```python
products = ["laptop", "mouse", "keyboard"]
```

### Brute Force Idea

Create a new list and insert each item at the beginning. This works but insertion at the front is inefficient.

### Optimized Approach

Use two pointers: one at the start and one at the end. Swap values until they meet.

### Python Solution

```python
def reverse_products(products):
    left = 0
    right = len(products) - 1

    while left < right:
        products[left], products[right] = products[right], products[left]
        left += 1
        right -= 1

    return products


print(reverse_products(["laptop", "mouse", "keyboard"]))
# ["keyboard", "mouse", "laptop"]
```

### Complexity

- Time: **O(n)**
- Space: **O(1)**

## 2. Find the Maximum Price

### Problem

Find the highest price in a list.

### Python Solution

```python
def max_price(prices):
    if not prices:
        return None

    maximum = prices[0]

    for price in prices[1:]:
        if price > maximum:
            maximum = price

    return maximum


print(max_price([999, 25, 75, 199]))  # 999
```

### Complexity

- Time: **O(n)**
- Space: **O(1)**

## 3. Find the Second Largest Price

### Problem

Find the second largest unique price.

### Optimized Approach

Track the largest and second largest values in one pass.

### Python Solution

```python
def second_largest_price(prices):
    largest = None
    second = None

    for price in prices:
        if price == largest:
            continue

        if largest is None or price > largest:
            second = largest
            largest = price
        elif second is None or price > second:
            second = price

    return second


print(second_largest_price([999, 25, 75, 199, 999]))  # 199
```

### Complexity

- Time: **O(n)**
- Space: **O(1)**

### Interview Follow-up

If duplicates count as separate values, sort the list and pick the second position from the end.

## 4. Remove Duplicates but Preserve Order

### Problem

Remove duplicate product IDs while keeping original order.

### Optimized Approach

Use a `seen` set for fast lookup and a list for ordered result.

### Python Solution

```python
def unique_ids_preserve_order(product_ids):
    seen = set()
    result = []

    for product_id in product_ids:
        if product_id not in seen:
            seen.add(product_id)
            result.append(product_id)

    return result


print(unique_ids_preserve_order([101, 102, 101, 103, 102]))
# [101, 102, 103]
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

## 5. Move Zero Stock Items to the End

### Problem

Given stock counts, move all zeros to the end while keeping non-zero order.

```python
stock_counts = [5, 0, 3, 0, 8]
```

### Optimized Approach

Use a write pointer for non-zero values.

### Python Solution

```python
def move_zero_stock_to_end(stock_counts):
    write = 0

    for read in range(len(stock_counts)):
        if stock_counts[read] != 0:
            stock_counts[write] = stock_counts[read]
            write += 1

    while write < len(stock_counts):
        stock_counts[write] = 0
        write += 1

    return stock_counts


print(move_zero_stock_to_end([5, 0, 3, 0, 8]))
# [5, 3, 8, 0, 0]
```

### Complexity

- Time: **O(n)**
- Space: **O(1)**

## 6. Merge Two Sorted Price Lists

### Problem

Merge two sorted price lists.

### Optimized Approach

Use two pointers.

### Python Solution

```python
def merge_sorted_prices(a, b):
    i = 0
    j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])

    return result


print(merge_sorted_prices([25, 75, 999], [50, 199]))
# [25, 50, 75, 199, 999]
```

### Complexity

- Time: **O(n + m)**
- Space: **O(n + m)**

## 7. Rotate Recently Viewed Products

### Problem

Rotate a list to the right by `k` positions.

```python
products = ["laptop", "mouse", "keyboard", "monitor"]
k = 2
```

### Python Solution

```python
def rotate_right(items, k):
    if not items:
        return items

    k = k % len(items)
    return items[-k:] + items[:-k]


print(rotate_right(["laptop", "mouse", "keyboard", "monitor"], 2))
# ["keyboard", "monitor", "laptop", "mouse"]
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

## 8. Find Product Pair With Target Budget

### Problem

Return `True` if any two prices add up to the target budget.

### Optimized Approach

Use a set to store previously seen prices.

### Python Solution

```python
def has_pair_with_budget(prices, target):
    seen = set()

    for price in prices:
        needed = target - price
        if needed in seen:
            return True
        seen.add(price)

    return False


print(has_pair_with_budget([499, 129, 99], 628))  # True
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

## 9. Find All Products Above Average Price

### Problem

Return prices greater than the average price.

### Python Solution

```python
def prices_above_average(prices):
    if not prices:
        return []

    average = sum(prices) / len(prices)
    return [price for price in prices if price > average]


print(prices_above_average([999, 25, 75, 199]))
# [999]
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

## 10. Validate Palindrome Product Code

### Problem

Check whether a product code list reads the same forward and backward.

```python
code = ["A", "B", "C", "B", "A"]
```

### Python Solution

```python
def is_palindrome_list(values):
    left = 0
    right = len(values) - 1

    while left < right:
        if values[left] != values[right]:
            return False
        left += 1
        right -= 1

    return True


print(is_palindrome_list(["A", "B", "C", "B", "A"]))  # True
```

### Complexity

- Time: **O(n)**
- Space: **O(1)**

## Summary: List Patterns to Remember

| Pattern | List idea | Example |
|---------|-----------|---------|
| Two pointers | start/end or two lists | reverse, palindrome, merge |
| Result building | `append()` | filtered products |
| In-place update | write pointer | move zeros |
| Sorting | `sort()` / `sorted()` | second max, ranking prices |
| Stack | `append()` / `pop()` | undo recent cart action |
| Preserve order | list + set | remove duplicates |

## See also

- [Python lists: core concepts](core-concepts.md)
- [Python list methods](methods.md)
- [Python list FAQ](frequently-asked-questions.md)
- [Python set interview problems](../set/interview-problems.md)
