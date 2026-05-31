# Python Set Interview Problems

Sets are often used in interviews when the question needs **fast lookup**, **duplicate detection**, or **group comparison**.

In Python, `x in my_set` is usually **O(1)** average time, while `x in my_list` is **O(n)**. That is why many brute-force list problems become efficient when solved with a set.

## Interview Pattern: When to Think About Sets

Use a set when the problem says or implies:

- find duplicates
- remove duplicates
- check if something was seen before
- find common elements
- find missing values
- compare two groups
- detect cycles
- avoid repeated work
- check whether two values form a target

Typical shopping management examples:

- duplicate product IDs from supplier import
- cart items that already exist in wishlist
- unavailable products in a customer order
- products common between two warehouses
- subscription features missing from a plan
- repeated license keys or coupon codes

## 1. Remove Duplicate Product IDs

### Problem

Given a list of product IDs from an import file, return only unique IDs.

```python
product_ids = [101, 102, 101, 103, 102, 104]
```

### Approach

Convert the list to a set. Sets automatically keep only unique values.

### Solution

```python
def unique_product_ids(product_ids):
    return set(product_ids)


product_ids = [101, 102, 101, 103, 102, 104]
print(unique_product_ids(product_ids))
# {101, 102, 103, 104}
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

### Interview note

If the interviewer asks to preserve order, use a `seen` set and build a new list.

```python
def unique_product_ids_preserve_order(product_ids):
    seen = set()
    result = []

    for product_id in product_ids:
        if product_id not in seen:
            seen.add(product_id)
            result.append(product_id)

    return result
```

## 2. Check If Product IDs Have Duplicates

### Problem

Return `True` if any product ID appears more than once.

### Approach

Track IDs in a `seen` set. If an ID is already in `seen`, it is a duplicate.

### Solution

```python
def has_duplicate_product(product_ids):
    seen = set()

    for product_id in product_ids:
        if product_id in seen:
            return True
        seen.add(product_id)

    return False


print(has_duplicate_product([101, 102, 103]))       # False
print(has_duplicate_product([101, 102, 101, 103]))  # True
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

### Interview note

This is the same core idea as LeetCode **Contains Duplicate**.

## 3. Find the First Repeated Product ID

### Problem

Return the first product ID that repeats while scanning left to right.

```python
product_ids = [101, 102, 103, 102, 101]
# answer: 102
```

### Approach

Use a `seen` set. The first time we find an already-seen value, return it.

### Solution

```python
def first_repeated_product_id(product_ids):
    seen = set()

    for product_id in product_ids:
        if product_id in seen:
            return product_id
        seen.add(product_id)

    return None


print(first_repeated_product_id([101, 102, 103, 102, 101]))  # 102
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

### Interview note

Do not sort if the problem asks for the first repeated value by original order. Sorting changes the order.

## 4. Find Common Items Between Cart and Wishlist

### Problem

Find products that are present in both cart and wishlist.

### Approach

Use set intersection (`&`).

### Solution

```python
def common_cart_wishlist_items(cart, wishlist):
    return set(cart) & set(wishlist)


cart = ["laptop", "mouse", "office-suite"]
wishlist = ["monitor", "laptop", "office-suite", "pdf-editor"]

print(common_cart_wishlist_items(cart, wishlist))
# {"laptop", "office-suite"}
```

### Complexity

- Time: **O(n + m)**
- Space: **O(n + m)**

### Interview note

If duplicate counts matter, use `collections.Counter` instead of `set`.

## 5. Find Items Missing From an Order

### Problem

Given required items for an office setup and the customer cart, find missing items.

### Approach

Use set difference (`required - cart`).

### Solution

```python
def missing_bundle_items(required_items, cart_items):
    return set(required_items) - set(cart_items)


required_items = ["laptop", "mouse", "keyboard", "office-suite"]
cart_items = ["laptop", "mouse"]

print(missing_bundle_items(required_items, cart_items))
# {"keyboard", "office-suite"}
```

### Complexity

- Time: **O(n + m)**
- Space: **O(n + m)**

### Interview note

This pattern appears in inventory, permissions, feature flags, and validation problems.

## 6. Check If Cart Contains All Required Bundle Items

### Problem

Return `True` if the cart contains every item required for a bundle.

### Approach

Use `.issubset()`.

### Solution

```python
def has_complete_bundle(required_items, cart_items):
    return set(required_items).issubset(set(cart_items))


required = ["laptop", "office-suite"]
cart = ["laptop", "mouse", "office-suite", "pdf-editor"]

print(has_complete_bundle(required, cart))  # True
```

### Complexity

- Time: **O(n + m)**
- Space: **O(n + m)**

### Interview note

You can also write `set(required_items) <= set(cart_items)`, but `.issubset()` is clearer for beginners.

## 7. Two Sum Using a Set

### Problem

Given product prices and a target budget, check whether two prices add up to the target.

```python
prices = [499, 99, 129, 899]
target = 628
# 499 + 129 = 628
```

### Approach

For each price, calculate `target - price`. If the needed value is already in `seen`, we found a pair.

### Solution

```python
def has_two_prices_for_budget(prices, target):
    seen = set()

    for price in prices:
        needed = target - price

        if needed in seen:
            return True

        seen.add(price)

    return False


print(has_two_prices_for_budget([499, 99, 129, 899], 628))  # True
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

### Interview note

If the interviewer asks for indices, use a dictionary (`price -> index`) instead of only a set.

## 8. Find Two Prices That Match a Budget

### Problem

Return the actual pair of prices that add up to the target.

### Approach

Use a set for complements, but return the pair when found.

### Solution

```python
def find_two_prices_for_budget(prices, target):
    seen = set()

    for price in prices:
        needed = target - price

        if needed in seen:
            return needed, price

        seen.add(price)

    return None


print(find_two_prices_for_budget([499, 99, 129, 899], 628))
# (499, 129)
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

### Interview note

This is the common **complement lookup** pattern.

## 9. Longest Consecutive Product Number Sequence

### Problem

Given product numbers, find the length of the longest consecutive sequence.

```python
product_numbers = [1004, 1001, 1002, 2000, 1003]
# longest sequence: 1001, 1002, 1003, 1004 => length 4
```

### Approach

Put all numbers in a set. Start counting only from numbers that do not have a previous number (`num - 1`) in the set.

### Solution

```python
def longest_consecutive_product_sequence(product_numbers):
    numbers = set(product_numbers)
    longest = 0

    for num in numbers:
        if num - 1 not in numbers:
            current = num
            length = 1

            while current + 1 in numbers:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


print(longest_consecutive_product_sequence([1004, 1001, 1002, 2000, 1003]))
# 4
```

### Complexity

- Time: **O(n)** average
- Space: **O(n)**

### Interview note

This is a popular interview problem. The trick is to start only at sequence beginnings.

## 10. Find Missing Product Number From 1 to n

### Problem

Product numbers should contain every number from `1` to `n`, but one is missing.

```python
product_numbers = [1, 2, 4, 5]
# missing: 3
```

### Approach

Convert the list to a set and check each number from `1` to `n`.

### Solution

```python
def missing_product_number(product_numbers, n):
    numbers = set(product_numbers)

    for expected in range(1, n + 1):
        if expected not in numbers:
            return expected

    return None


print(missing_product_number([1, 2, 4, 5], 5))  # 3
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

### Interview note

There is also a math formula solution using `n * (n + 1) // 2`. The set solution is easier to explain and can be extended to multiple missing values.

## 11. Find Multiple Missing Product Numbers

### Problem

Find all missing product numbers from `1` to `n`.

### Approach

Use a set for existing values and scan the full expected range.

### Solution

```python
def missing_product_numbers(product_numbers, n):
    existing = set(product_numbers)
    missing = []

    for expected in range(1, n + 1):
        if expected not in existing:
            missing.append(expected)

    return missing


print(missing_product_numbers([1, 2, 4, 7], 7))
# [3, 5, 6]
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

### Interview note

This pattern is common in audit, reconciliation, and missing-record questions.

## 12. Check If Two Warehouses Have No Common Products

### Problem

Return `True` if two warehouses have completely different products.

### Approach

Use `.isdisjoint()`.

### Solution

```python
def have_no_common_products(warehouse_a, warehouse_b):
    return set(warehouse_a).isdisjoint(set(warehouse_b))


warehouse_a = ["laptop", "mouse"]
warehouse_b = ["monitor", "office-suite"]

print(have_no_common_products(warehouse_a, warehouse_b))  # True
```

### Complexity

- Time: **O(n + m)**
- Space: **O(n + m)**

### Interview note

`.isdisjoint()` is clearer than checking whether intersection length is zero.

## 13. Unique Characters in a Coupon Code

### Problem

Return `True` if every character in a coupon code is unique.

```python
"SAVE10"  # duplicate? no
"DISCOUNT"  # duplicate? yes, because "D" appears once but other examples may repeat
```

### Approach

Compare the length of the string with the length of `set(string)`.

### Solution

```python
def has_unique_characters(code):
    normalized = code.lower()
    return len(normalized) == len(set(normalized))


print(has_unique_characters("SAVE10"))   # True
print(has_unique_characters("OFFER50"))  # False, "f" appears twice
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

### Interview note

Clarify whether the check should be case-sensitive. `"A"` and `"a"` may be considered same or different depending on requirements.

## 14. Detect Cycle in Repeated Calculations

### Problem

Some problems require detecting whether a value repeats during a process. For example, repeatedly transform a license number until it reaches a target or loops forever.

This pattern is similar to LeetCode **Happy Number**.

### Approach

Store previously seen numbers in a set. If the same number appears again, there is a cycle.

### Solution

```python
def digit_square_sum(num):
    total = 0

    while num > 0:
        digit = num % 10
        total += digit * digit
        num //= 10

    return total


def reaches_one(num):
    seen = set()

    while num != 1:
        if num in seen:
            return False

        seen.add(num)
        num = digit_square_sum(num)

    return True


print(reaches_one(19))  # True
print(reaches_one(20))  # False
```

### Complexity

- Time: depends on how many unique states appear before repeat
- Space: **O(k)** where `k` is the number of seen states

### Interview note

Whenever a process may repeat states, a `seen` set is a simple cycle detector.

## 15. Validate No Duplicate Rows, Columns, or Boxes

### Problem

In grid-based validation problems, detect if a value was already used in a row, column, or group.

This pattern is similar to Sudoku validation.

### Approach

Store tuples in a set, such as:

- `("row", row_index, value)`
- `("col", col_index, value)`
- `("box", box_index, value)`

### Solution

```python
def is_valid_product_grid(grid):
    seen = set()

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            value = grid[row][col]

            if value == "":
                continue

            box = (row // 3, col // 3)
            checks = [
                ("row", row, value),
                ("col", col, value),
                ("box", box, value),
            ]

            for check in checks:
                if check in seen:
                    return False
                seen.add(check)

    return True
```

### Complexity

- Time: **O(rows * cols)**
- Space: **O(rows * cols)**

### Interview note

This is a powerful pattern: store a **meaningful tuple key** in a set to represent a rule that must stay unique.

## Summary: Set Patterns to Remember

| Pattern | Set idea | Example |
|---------|----------|---------|
| Duplicate detection | `if x in seen` | repeated product ID |
| Remove duplicates | `set(items)` | unique imported products |
| Common elements | `a & b` | cart and wishlist overlap |
| Missing elements | `required - existing` | missing bundle items |
| Pair sum | complement in `seen` | two prices match budget |
| Consecutive sequence | lookup neighbors | product number sequence |
| Cycle detection | repeated state in `seen` | happy number style problem |
| Rule validation | tuple keys in `seen` | grid / Sudoku-like validation |

## Quick Interview Tips

- Mention average **O(1)** lookup for sets.
- Explain why a list lookup would be slower for large inputs.
- Clarify whether duplicates, order, and counts matter.
- If counts matter, use `dict` or `collections.Counter`, not only `set`.
- If indices matter, use `dict` instead of only `set`.
- If order must be preserved, combine a list result with a `seen` set.

## See also

- [Python sets: core concepts](core-concepts.md)
- [Python interview questions](../interview-questions.md)
