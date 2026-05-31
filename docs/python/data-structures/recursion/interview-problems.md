# Recursion: Interview Problems

This page contains **20 interview problems** on recursion, base cases, recursive calls, and backtracking.

Each problem includes a short explanation, Python solution, and output.

## 1. Count Cart Items Recursively

### Problem

Count how many products are in a cart without using `len()`.

### Explanation

The base case is an empty list. Each recursive call removes one item.

### Solution

```python
def count_items(items):
    if not items:
        return 0

    return 1 + count_items(items[1:])


print(count_items(["laptop", "mouse", "keyboard"]))
```

Output:

```text
3
```

## 2. Sum Product Prices

### Problem

Find total cart price recursively.

### Explanation

Add the first price to the sum of the remaining prices.

### Solution

```python
def sum_prices(prices, index=0):
    if index == len(prices):
        return 0

    return prices[index] + sum_prices(prices, index + 1)


print(sum_prices([50000, 1500, 2500]))
```

Output:

```text
54000
```

## 3. Find Maximum Product Price

### Problem

Find the highest product price recursively.

### Explanation

Compare the current price with the maximum from the rest of the list.

### Solution

```python
def max_price(prices, index=0):
    if index == len(prices) - 1:
        return prices[index]

    return max(prices[index], max_price(prices, index + 1))


print(max_price([1200, 85000, 45000, 2200]))
```

Output:

```text
85000
```

## 4. Reverse Product Name

### Problem

Reverse a product name recursively.

### Explanation

Put the first character after the reversed remaining string.

### Solution

```python
def reverse_text(text):
    if len(text) <= 1:
        return text

    return reverse_text(text[1:]) + text[0]


print(reverse_text("laptop"))
```

Output:

```text
potpal
```

## 5. Check Palindrome Product Code

### Problem

Check if a product code is a palindrome.

### Explanation

Compare first and last characters, then recurse on the middle.

### Solution

```python
def is_palindrome(code):
    if len(code) <= 1:
        return True

    if code[0] != code[-1]:
        return False

    return is_palindrome(code[1:-1])


print(is_palindrome("ABBA"))
print(is_palindrome("LAPTOP"))
```

Output:

```text
True
False
```

## 6. Calculate Recursive Discount

### Problem

Apply a fixed discount multiple times recursively.

### Explanation

Reduce the number of remaining discounts in every call.

### Solution

```python
def apply_discount(price, discount, times):
    if times == 0:
        return price

    return apply_discount(price - discount, discount, times - 1)


print(apply_discount(10000, 500, 3))
```

Output:

```text
8500
```

## 7. Factorial for Order Arrangement Count

### Problem

Find how many ways `n` ordered items can be arranged.

### Explanation

`n! = n * (n - 1)!`, and `0! = 1`.

### Solution

```python
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(4))
```

Output:

```text
24
```

## 8. Power Calculation for Quantity Bundles

### Problem

Calculate `base ** exponent` recursively.

### Explanation

Multiply one base at a time until exponent becomes zero.

### Solution

```python
def power(base, exponent):
    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)


print(power(2, 5))
```

Output:

```text
32
```

## 9. Binary Search Recursively

### Problem

Search for a product price in a sorted price list.

### Explanation

Compare with the middle value and search only one half.

### Solution

```python
def binary_search(values, target, left=0, right=None):
    if right is None:
        right = len(values) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if values[mid] == target:
        return mid
    if target < values[mid]:
        return binary_search(values, target, left, mid - 1)
    return binary_search(values, target, mid + 1, right)


print(binary_search([1000, 1500, 2500, 5000], 2500))
```

Output:

```text
2
```

## 10. Count Digits in Order ID

### Problem

Count digits in an order ID recursively.

### Explanation

Divide by 10 until only one digit remains.

### Solution

```python
def count_digits(number):
    number = abs(number)
    if number < 10:
        return 1

    return 1 + count_digits(number // 10)


print(count_digits(987654))
```

Output:

```text
6
```

## 11. Sum Digits in Invoice Number

### Problem

Find the sum of digits in an invoice number.

### Explanation

Add the last digit to the digit sum of the remaining number.

### Solution

```python
def sum_digits(number):
    number = abs(number)
    if number == 0:
        return 0

    return number % 10 + sum_digits(number // 10)


print(sum_digits(5729))
```

Output:

```text
23
```

## 12. Flatten Nested Category List

### Problem

Flatten nested product categories.

### Explanation

If an item is a list, recursively flatten it. Otherwise add it to the result.

### Solution

```python
def flatten_categories(categories):
    result = []

    for category in categories:
        if isinstance(category, list):
            result.extend(flatten_categories(category))
        else:
            result.append(category)

    return result


categories = ["Computers", ["Laptops", ["Gaming", "Business"]], "Accessories"]
print(flatten_categories(categories))
```

Output:

```text
['Computers', 'Laptops', 'Gaming', 'Business', 'Accessories']
```

## 13. Traverse Category Tree

### Problem

Print all product categories from a tree.

### Explanation

Visit the current category, then recursively visit child categories.

### Solution

```python
category_tree = {
    "Computers": {
        "Laptops": {},
        "Desktops": {},
    },
    "Accessories": {
        "Mouse": {},
    },
}


def print_categories(tree):
    for category, children in tree.items():
        print(category)
        print_categories(children)


print_categories(category_tree)
```

Output:

```text
Computers
Laptops
Desktops
Accessories
Mouse
```

## 14. Generate All Product Bundles

### Problem

Generate all subsets of products for bundle offers.

### Explanation

For each product, choose it or skip it.

### Solution

```python
def subsets(items, index=0, path=None, result=None):
    if path is None:
        path = []
    if result is None:
        result = []

    if index == len(items):
        result.append(path[:])
        return result

    path.append(items[index])
    subsets(items, index + 1, path, result)
    path.pop()

    subsets(items, index + 1, path, result)
    return result


print(subsets(["mouse", "bag"]))
```

Output:

```text
[['mouse', 'bag'], ['mouse'], ['bag'], []]
```

## 15. Generate Product Permutations

### Problem

Generate all arrangements of selected products.

### Explanation

Choose each unused product, recurse, then undo the choice.

### Solution

```python
def permutations(items, path=None, used=None, result=None):
    if path is None:
        path = []
    if used is None:
        used = [False] * len(items)
    if result is None:
        result = []

    if len(path) == len(items):
        result.append(path[:])
        return result

    for index, item in enumerate(items):
        if used[index]:
            continue
        used[index] = True
        path.append(item)
        permutations(items, path, used, result)
        path.pop()
        used[index] = False

    return result


print(permutations(["mouse", "bag"]))
```

Output:

```text
[['mouse', 'bag'], ['bag', 'mouse']]
```

## 16. Combination Sum for Exact Cart Total

### Problem

Find combinations of product prices that match a target total.

### Explanation

Try each price, keep the same index for reusable items, and backtrack.

### Solution

```python
def combination_sum(prices, target, start=0, path=None, result=None):
    if path is None:
        path = []
    if result is None:
        result = []

    if target == 0:
        result.append(path[:])
        return result
    if target < 0:
        return result

    for index in range(start, len(prices)):
        path.append(prices[index])
        combination_sum(prices, target - prices[index], index, path, result)
        path.pop()

    return result


print(combination_sum([500, 1000], 1500))
```

Output:

```text
[[500, 500, 500], [500, 1000]]
```

## 17. Backtrack Valid Coupon Code

### Problem

Generate all two-character coupon codes from given characters.

### Explanation

Build the code character by character and stop when length is two.

### Solution

```python
def coupon_codes(chars, length, path="", result=None):
    if result is None:
        result = []

    if len(path) == length:
        result.append(path)
        return result

    for char in chars:
        coupon_codes(chars, length, path + char, result)

    return result


print(coupon_codes(["A", "B"], 2))
```

Output:

```text
['AA', 'AB', 'BA', 'BB']
```

## 18. Find Path in Warehouse Grid

### Problem

Find one path from top-left to bottom-right in a grid.

### Explanation

Try moving right and down. If a path fails, undo the move.

### Solution

```python
def find_path(rows, cols, row=0, col=0, path=None):
    if path is None:
        path = []

    path.append((row, col))

    if row == rows - 1 and col == cols - 1:
        return path[:]

    if col + 1 < cols:
        right_path = find_path(rows, cols, row, col + 1, path)
        if right_path:
            return right_path

    if row + 1 < rows:
        down_path = find_path(rows, cols, row + 1, col, path)
        if down_path:
            return down_path

    path.pop()
    return []


print(find_path(2, 3))
```

Output:

```text
[(0, 0), (0, 1), (0, 2), (1, 2)]
```

## 19. Recursive DFS for Product Page Links

### Problem

Visit all linked product pages recursively.

### Explanation

DFS visits a page, marks it seen, then recursively visits unseen neighbors.

### Solution

```python
def dfs(graph, page, visited=None):
    if visited is None:
        visited = set()

    if page in visited:
        return []

    visited.add(page)
    order = [page]

    for neighbor in graph[page]:
        order.extend(dfs(graph, neighbor, visited))

    return order


graph = {
    "laptop": ["mouse", "bag"],
    "mouse": ["keyboard"],
    "bag": [],
    "keyboard": [],
}

print(dfs(graph, "laptop"))
```

Output:

```text
['laptop', 'mouse', 'keyboard', 'bag']
```

## 20. Solve Stock Allocation With Backtracking

### Problem

Check whether stock boxes can exactly fill an order quantity.

### Explanation

Try taking or skipping each box quantity.

### Solution

```python
def can_fill_order(boxes, target, index=0):
    if target == 0:
        return True
    if target < 0 or index == len(boxes):
        return False

    take = can_fill_order(boxes, target - boxes[index], index + 1)
    skip = can_fill_order(boxes, target, index + 1)

    return take or skip


print(can_fill_order([3, 5, 8], 11))
print(can_fill_order([3, 5, 8], 10))
```

Output:

```text
True
False
```

## Final Notes

- A recursive solution needs a clear base case.
- Recursive calls must move closer to the base case.
- Backtracking requires undoing choices after recursive exploration.
- Recursion is natural for trees, DFS, subsets, permutations, and constraint search.
