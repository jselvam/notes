# Python Sets: Frequently Asked Interview Questions

This page collects commonly asked Python `set` interview questions from **basic** to **pro** level. Most answers use examples from an online computer shopping system: product IDs, cart items, inventory, software licenses, and subscription features.

## Basic Level

### 1. What is a set in Python?

A `set` is an unordered collection of unique, hashable values.

```python
items = {"laptop", "mouse", "mouse"}
print(items)  # {"laptop", "mouse"}
```

### 2. Why are sets useful in interviews?

Sets are useful for duplicate removal, fast membership checks, common items, missing items, and seen-before tracking.

```python
seen_products = {101, 102}
print(101 in seen_products)  # True
```

### 3. How do you create a set?

Use `{}` with values or `set()` from an iterable.

```python
categories = {"laptop", "mouse", "keyboard"}
product_ids = set([101, 102, 101])
```

### 4. How do you create an empty set?

Use `set()`. `{}` creates an empty dictionary.

```python
empty_set = set()
empty_dict = {}

print(type(empty_set))   # <class 'set'>
print(type(empty_dict))  # <class 'dict'>
```

### 5. Can a set contain duplicate values?

No. Duplicates are automatically removed.

```python
ids = {101, 102, 101, 103}
print(ids)  # {101, 102, 103}
```

### 6. Are sets ordered?

No. A set does not support indexing or guaranteed insertion order.

```python
items = {"laptop", "mouse"}
# print(items[0])  # TypeError
```

### 7. Can you access set items by index?

No. Sets are unordered, so indexing is not supported.

```python
products = {"laptop", "mouse"}

for product in products:
    print(product)
```

### 8. How do you check if an item exists in a set?

Use the `in` operator.

```python
available = {"laptop", "monitor", "office-suite"}
print("laptop" in available)  # True
```

### 9. What is the average time complexity of membership check in a set?

Average case is **O(1)**.

```python
blocked_ids = {1001, 1002, 1003}
print(1002 in blocked_ids)  # O(1) average
```

### 10. How do you add one item to a set?

Use `add()`.

```python
cart = {"laptop"}
cart.add("mouse")
print(cart)
```

### 11. How do you add multiple items to a set?

Use `update()`.

```python
cart = {"laptop"}
cart.update(["mouse", "keyboard", "mouse"])
print(cart)
```

### 12. What is the difference between `add()` and `update()`?

`add()` adds one object. `update()` adds each item from an iterable.

```python
items = {"laptop"}
items.add("mouse")
items.update(["keyboard", "monitor"])
```

### 13. How do you remove an item from a set?

Use `remove()` or `discard()`.

```python
cart = {"laptop", "mouse"}
cart.remove("mouse")
```

### 14. What is the difference between `remove()` and `discard()`?

`remove()` raises `KeyError` if the item is missing. `discard()` does not.

```python
cart = {"laptop"}
cart.discard("mouse")  # no error
# cart.remove("mouse")  # KeyError
```

### 15. What does `pop()` do on a set?

`pop()` removes and returns an arbitrary item because sets are unordered.

```python
review_queue = {"laptop", "mouse", "monitor"}
item = review_queue.pop()
print(item)
```

## Intermediate Level

### 16. How do you remove duplicates from a list?

Convert the list to a set.

```python
product_ids = [101, 102, 101, 103]
unique_ids = set(product_ids)
print(unique_ids)
```

### 17. How do you remove duplicates but preserve order?

Use a `seen` set and build a result list.

```python
def unique_preserve_order(product_ids):
    seen = set()
    result = []

    for product_id in product_ids:
        if product_id not in seen:
            seen.add(product_id)
            result.append(product_id)

    return result
```

### 18. How do you find common elements between two lists?

Use set intersection.

```python
cart = ["laptop", "mouse", "office-suite"]
wishlist = ["monitor", "laptop", "office-suite"]

print(set(cart) & set(wishlist))
```

### 19. How do you find items in one list but not another?

Use set difference.

```python
required = {"laptop", "mouse", "keyboard"}
cart = {"laptop", "mouse"}

print(required - cart)  # {"keyboard"}
```

### 20. How do you find items that are different between two sets?

Use symmetric difference.

```python
warehouse_a = {"laptop", "mouse"}
warehouse_b = {"laptop", "monitor"}

print(warehouse_a ^ warehouse_b)  # {"mouse", "monitor"}
```

### 21. What is `union()`?

`union()` returns all unique items from both sets.

```python
hardware = {"laptop", "mouse"}
software = {"pdf-editor", "office-suite"}

print(hardware.union(software))
```

### 22. What is `intersection()`?

`intersection()` returns items common to both sets.

```python
cart = {"laptop", "mouse"}
discount_items = {"mouse", "keyboard"}

print(cart.intersection(discount_items))  # {"mouse"}
```

### 23. What is `difference()`?

`difference()` returns items from the first set that are not in the second.

```python
all_items = {"laptop", "mouse", "keyboard"}
out_of_stock = {"mouse"}

print(all_items.difference(out_of_stock))  # {"laptop", "keyboard"}
```

### 24. What is `symmetric_difference()`?

It returns items that are in either set, but not in both.

```python
a = {"laptop", "mouse"}
b = {"mouse", "monitor"}

print(a.symmetric_difference(b))  # {"laptop", "monitor"}
```

### 25. How do you check if one set is a subset of another?

Use `issubset()` or `<=`.

```python
required = {"laptop", "office-suite"}
cart = {"laptop", "mouse", "office-suite"}

print(required.issubset(cart))  # True
```

### 26. How do you check if one set is a superset of another?

Use `issuperset()` or `>=`.

```python
cart = {"laptop", "mouse", "office-suite"}
required = {"laptop", "office-suite"}

print(cart.issuperset(required))  # True
```

### 27. How do you check if two sets have no common elements?

Use `isdisjoint()`.

```python
hardware = {"laptop", "mouse"}
subscriptions = {"cloud-storage", "support-plan"}

print(hardware.isdisjoint(subscriptions))  # True
```

### 28. What is the difference between `union()` and `update()`?

`union()` returns a new set. `update()` modifies the original set.

```python
a = {"laptop"}
b = {"mouse"}

c = a.union(b)
print(a)  # {"laptop"}

a.update(b)
print(a)  # {"laptop", "mouse"}
```

### 29. What is the difference between `intersection()` and `intersection_update()`?

`intersection()` returns a new set. `intersection_update()` changes the original set.

```python
cart = {"laptop", "mouse", "monitor"}
wishlist = {"laptop", "monitor"}

cart.intersection_update(wishlist)
print(cart)  # {"laptop", "monitor"}
```

### 30. What is the difference between `difference()` and `difference_update()`?

`difference()` returns a new set. `difference_update()` modifies the original set.

```python
available = {"laptop", "mouse", "monitor"}
out_of_stock = {"mouse"}

available.difference_update(out_of_stock)
print(available)  # {"laptop", "monitor"}
```

## Advanced Level

### 31. How would you solve Contains Duplicate using a set?

Track seen values. If a value appears again, return `True`.

```python
def contains_duplicate(product_ids):
    seen = set()

    for product_id in product_ids:
        if product_id in seen:
            return True
        seen.add(product_id)

    return False
```

### 32. How would you solve Two Sum using a set?

Store previous values in a set and check whether the complement exists.

```python
def has_two_prices(prices, target):
    seen = set()

    for price in prices:
        needed = target - price
        if needed in seen:
            return True
        seen.add(price)

    return False
```

### 33. When is a dictionary better than a set for Two Sum?

Use a dictionary when the problem asks for indices.

```python
def two_sum_indices(prices, target):
    seen = {}

    for index, price in enumerate(prices):
        needed = target - price
        if needed in seen:
            return [seen[needed], index]
        seen[price] = index
```

### 34. How do you find the first repeated value?

Scan left to right and use a `seen` set.

```python
def first_repeated(product_ids):
    seen = set()

    for product_id in product_ids:
        if product_id in seen:
            return product_id
        seen.add(product_id)

    return None
```

### 35. How do you find all duplicate values?

Use one set for seen values and another set for duplicates.

```python
def all_duplicates(product_ids):
    seen = set()
    duplicates = set()

    for product_id in product_ids:
        if product_id in seen:
            duplicates.add(product_id)
        else:
            seen.add(product_id)

    return duplicates
```

### 36. How do you find missing numbers from `1` to `n`?

Put existing numbers in a set and scan the expected range.

```python
def missing_numbers(values, n):
    existing = set(values)
    return [num for num in range(1, n + 1) if num not in existing]
```

### 37. How do you find the longest consecutive sequence?

Use a set and start counting only when `num - 1` is not present.

```python
def longest_consecutive(nums):
    values = set(nums)
    longest = 0

    for num in values:
        if num - 1 not in values:
            current = num
            length = 1

            while current + 1 in values:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest
```

### 38. Why is the longest consecutive sequence set solution O(n) average?

Each number is visited as a possible start once, and sequence expansion happens across values without repeatedly starting from the middle.

```python
# Start only at 1001, not at 1002, 1003, 1004
product_numbers = {1001, 1002, 1003, 1004}
```

### 39. How can a set help detect cycles?

Store visited states. If a state repeats, there is a cycle.

```python
def has_cycle_states(states):
    seen = set()

    for state in states:
        if state in seen:
            return True
        seen.add(state)

    return False
```

### 40. How do you validate uniqueness rules with tuple keys?

Store a tuple representing each uniqueness rule.

```python
seen = set()
entry = ("warehouse", "A", 101)

if entry in seen:
    print("Duplicate product in warehouse")
else:
    seen.add(entry)
```

### 41. Why can tuples be stored in sets but lists cannot?

Set elements must be hashable. A tuple is hashable if its contents are hashable. A list is mutable and unhashable.

```python
valid = {("laptop", 101)}
# invalid = {["laptop", 101]}  # TypeError
```

### 42. Can a set contain a dictionary?

No. Dictionaries are mutable and unhashable.

```python
# invalid = {{"id": 101}}  # TypeError
valid = {("id", 101)}
```

### 43. Can a set contain another set?

No, because normal sets are mutable and unhashable. Use `frozenset`.

```python
bundle = frozenset({"laptop", "mouse"})
bundles = {bundle}
print(bundles)
```

### 44. What is a `frozenset`?

A `frozenset` is an immutable set.

```python
allowed_plans = frozenset({"monthly", "yearly"})
print("monthly" in allowed_plans)
```

### 45. When would you use `frozenset`?

Use it when you need an immutable group of unique values, especially as a dictionary key or set element.

```python
bundle_prices = {
    frozenset({"laptop", "mouse"}): 999
}
```

## Pro Level

### 46. How are sets implemented internally in Python?

Python sets are hash-table based. This is why membership checks are average **O(1)**.

```python
ids = {101, 102, 103}
print(102 in ids)
```

### 47. What does hashable mean?

An object is hashable if it has a stable hash value during its lifetime and can be compared for equality.

```python
print(hash("laptop"))
print(hash((101, "laptop")))
```

### 48. Why are mutable objects not allowed inside sets?

If an object changes after insertion, its hash position could become invalid. That would break fast lookup.

```python
product = ["laptop", 101]
# products = {product}  # TypeError
```

### 49. What happens when two objects have the same hash?

That is a hash collision. Python resolves collisions internally, but too many collisions can reduce performance.

```python
# Normal interview answer: set lookup is O(1) average, not guaranteed O(1) worst case.
```

### 50. What is the worst-case time complexity of set lookup?

Worst case can be **O(n)** if many values collide, but average case is **O(1)**.

```python
blocked_ids = {101, 102, 103}
print(101 in blocked_ids)
```

### 51. How do equality and hashing affect sets?

If two objects are equal and have the same hash, a set stores only one logical value.

```python
values = {1, True}
print(values)  # {1}
```

`1 == True` is `True`, and their hashes are equal.

### 52. Why can set iteration order look stable but should not be relied on?

Set order is an implementation detail affected by hashing and runtime behavior. Do not write logic that depends on it.

```python
items = {"laptop", "mouse", "keyboard"}
for item in items:
    print(item)
```

### 53. How do you choose between `set`, `list`, `dict`, and `Counter`?

Use `set` for uniqueness and membership, `list` for order, `dict` for key-value mapping, and `Counter` for counts.

```python
from collections import Counter

items = ["mouse", "mouse", "laptop"]
print(Counter(items))  # counts duplicates
```

### 54. Why is a set not enough when duplicate counts matter?

A set only stores whether a value exists, not how many times it appears.

```python
items = ["mouse", "mouse", "laptop"]
print(set(items))  # {"mouse", "laptop"}
```

Use `Counter` when counts matter.

### 55. Why is a set not enough when indices matter?

A set does not store positions. Use a dictionary when you need value-to-index lookup.

```python
price_to_index = {499: 0, 129: 1}
print(price_to_index[129])
```

### 56. How do you safely use custom objects in a set?

Define consistent `__eq__` and `__hash__`, and avoid mutating fields used for hashing.

```python
class Product:
    def __init__(self, product_id):
        self.product_id = product_id

    def __eq__(self, other):
        return isinstance(other, Product) and self.product_id == other.product_id

    def __hash__(self):
        return hash(self.product_id)
```

### 57. What is a dangerous mistake with custom objects in sets?

Mutating a field used by `__hash__` after insertion can make the object hard to find.

```python
# Avoid changing product_id after adding Product(product_id) to a set.
```

### 58. How do you compare required permissions with user permissions?

Use subset logic.

```python
required = {"view-products", "place-order"}
user_permissions = {"view-products", "place-order", "refund"}

print(required <= user_permissions)  # True
```

### 59. How do sets help with idempotency?

Track processed IDs so repeated events are ignored.

```python
processed_order_ids = set()

def process_order(order_id):
    if order_id in processed_order_ids:
        return "already processed"

    processed_order_ids.add(order_id)
    return "processed"
```

### 60. How do sets help avoid repeated work in graph or search problems?

Use a `visited` set so the same node is not processed multiple times.

```python
def visit_category(category, graph, visited):
    if category in visited:
        return

    visited.add(category)

    for child in graph.get(category, []):
        visit_category(child, graph, visited)
```

## Final Interview Checklist

- Say sets store **unique hashable values**.
- Mention average **O(1)** lookup, insert, and delete.
- Use `seen` for duplicate detection and cycle detection.
- Use set algebra for group problems: union, intersection, difference, symmetric difference.
- Use subset / superset for validation problems.
- Use `Counter` instead of `set` when counts matter.
- Use `dict` instead of `set` when indices or mapped values matter.
- Do not rely on set order.

## See also

- [Python sets: core concepts](core-concepts.md)
- [Python set methods](methods.md)
- [Python set interview problems](interview-problems.md)
