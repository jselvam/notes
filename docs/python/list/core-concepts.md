# Python Lists: Core Concepts & Shopping Examples

A Python **list** stores an ordered collection of items. Lists are useful when order matters, duplicates are allowed, and you need to access or update items by position.

In an online computer shopping management system, lists can represent:

- products shown on a catalog page
- items in a cart
- recent orders
- search results
- subscription features in display order
- product prices used for interview problems

## Overview

Lists are:

- **Ordered** — items keep their position.
- **Mutable** — items can be added, changed, and removed.
- **Indexable** — access items with `list[index]`.
- **Duplicate-friendly** — the same value can appear multiple times.

```python
cart_items = ["laptop", "mouse", "mouse", "office-suite"]

print(cart_items[0])  # laptop
print(cart_items[1])  # mouse
```

## Creating a List

Use square brackets:

```python
products = ["laptop", "mouse", "keyboard"]
prices = [999, 25, 75]
mixed = ["laptop", 999, True]
```

Use `list()` to convert another iterable:

```python
category_name = "mouse"
characters = list(category_name)

print(characters)
# ["m", "o", "u", "s", "e"]
```

## Empty List

Use `[]` for an empty list.

```python
cart = []

cart.append("laptop")
cart.append("mouse")

print(cart)
```

## Indexing

List indexes start at `0`.

```python
products = ["laptop", "mouse", "keyboard", "monitor"]

print(products[0])   # laptop
print(products[2])   # keyboard
print(products[-1])  # monitor
```

## Slicing

Slicing returns part of a list.

```python
products = ["laptop", "mouse", "keyboard", "monitor", "office-suite"]

print(products[1:4])
# ["mouse", "keyboard", "monitor"]

print(products[:2])
# ["laptop", "mouse"]

print(products[::2])
# ["laptop", "keyboard", "office-suite"]
```

## Updating Items

Lists are mutable, so you can replace values by index.

```python
cart = ["laptop", "mouse", "old-monitor"]

cart[2] = "new-monitor"

print(cart)
# ["laptop", "mouse", "new-monitor"]
```

## Adding Items

Use `append()` to add one item at the end.

```python
cart = ["laptop"]
cart.append("mouse")

print(cart)
```

Use `insert()` to add at a specific position.

```python
cart = ["laptop", "monitor"]
cart.insert(1, "keyboard")

print(cart)
# ["laptop", "keyboard", "monitor"]
```

Use `extend()` to add many items.

```python
cart = ["laptop"]
accessories = ["mouse", "keyboard"]

cart.extend(accessories)

print(cart)
# ["laptop", "mouse", "keyboard"]
```

## Removing Items

Use `remove()` to remove by value.

```python
cart = ["laptop", "mouse", "keyboard"]
cart.remove("mouse")

print(cart)
```

Use `pop()` to remove by index and return the removed item.

```python
cart = ["laptop", "mouse", "keyboard"]
removed_item = cart.pop(1)

print(removed_item)  # mouse
print(cart)          # ["laptop", "keyboard"]
```

Use `del` when you do not need the removed value.

```python
cart = ["laptop", "mouse", "keyboard"]
del cart[0]

print(cart)
```

## Looping Through a List

```python
cart = ["laptop", "mouse", "office-suite"]

for item in cart:
    print(item)
```

Use `enumerate()` when you need both index and value.

```python
cart = ["laptop", "mouse", "office-suite"]

for index, item in enumerate(cart):
    print(index, item)
```

## List Comprehension

List comprehensions create new lists from existing iterables.

```python
prices = [999, 25, 75, 199]
discounted_prices = [price * 0.9 for price in prices]

print(discounted_prices)
```

Filter with an `if` condition:

```python
prices = [999, 25, 75, 199]
expensive_prices = [price for price in prices if price >= 100]

print(expensive_prices)
# [999, 199]
```

## Nested Lists

A list can contain other lists.

```python
orders = [
    ["laptop", "mouse"],
    ["monitor", "keyboard"],
    ["office-suite", "pdf-editor"],
]

print(orders[0][1])  # mouse
```

## Common Interview Points

### Why use a list instead of a set?

Use a list when order matters, duplicates matter, or index-based access is needed.

```python
cart = ["mouse", "mouse", "keyboard"]
print(cart[0])  # mouse
```

### What is the time complexity of list indexing?

Indexing is **O(1)**.

```python
products = ["laptop", "mouse", "keyboard"]
print(products[1])
```

### What is the time complexity of searching in a list?

Searching with `in` is **O(n)** because Python may need to scan each item.

```python
products = ["laptop", "mouse", "keyboard"]
print("keyboard" in products)
```

### Why can appending be efficient?

`append()` is **O(1)** amortized because Python lists are dynamic arrays.

```python
cart = []
cart.append("laptop")
```

## Practice Problems

1. Find the maximum product price.
2. Find the second largest price.
3. Reverse a product list without using `reverse()`.
4. Remove duplicate product IDs but preserve order.
5. Move all out-of-stock items to the end.
6. Merge two sorted price lists.
7. Rotate a list of recently viewed products.
8. Find all products above a given price.

## See also

- [Python list methods](methods.md)
- [Python list interview problems](interview-problems.md)
- [Python list remove items](remove-list-items.md)
- [Python interview questions](../interview-questions.md)
