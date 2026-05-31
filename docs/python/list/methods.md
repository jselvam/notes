# Python List Methods: Interview Notes

Python list methods are commonly asked because lists are used in many interview problems: arrays, two pointers, sliding window, sorting, stacks, and queues.

## Quick Method Table

| Method | What it does | Interview use case |
|--------|--------------|--------------------|
| `append()` | Adds one item at the end | Stack push, build result |
| `extend()` | Adds many items | Merge items into same list |
| `insert()` | Adds item at index | Insert priority product |
| `remove()` | Removes first matching value | Delete by value |
| `pop()` | Removes and returns item by index | Stack pop, queue-like removal |
| `clear()` | Removes all items | Reset state |
| `index()` | Finds first index of value | Locate product |
| `count()` | Counts occurrences | Count duplicates |
| `sort()` | Sorts list in place | Sort prices/products |
| `reverse()` | Reverses list in place | Reverse display order |
| `copy()` | Shallow copy | Preserve original list |

## `append()`

Adds one item to the end of the list.

```python
cart = ["laptop"]
cart.append("mouse")

print(cart)
# ["laptop", "mouse"]
```

### Interview point

Use `append()` to build a result list.

```python
def products_above_price(products, prices, minimum):
    result = []

    for index, price in enumerate(prices):
        if price >= minimum:
            result.append(products[index])

    return result
```

## `extend()`

Adds all items from an iterable.

```python
cart = ["laptop"]
accessories = ["mouse", "keyboard"]

cart.extend(accessories)

print(cart)
# ["laptop", "mouse", "keyboard"]
```

### Interview point

`extend()` adds each element. `append()` adds the object as one item.

```python
items = ["laptop"]
items.append(["mouse", "keyboard"])
print(items)
# ["laptop", ["mouse", "keyboard"]]
```

## `insert()`

Inserts an item at a specific index.

```python
products = ["laptop", "monitor"]
products.insert(1, "keyboard")

print(products)
# ["laptop", "keyboard", "monitor"]
```

### Interview point

Insertion in the middle is **O(n)** because elements may need to shift.

## `remove()`

Removes the first matching value.

```python
cart = ["laptop", "mouse", "mouse", "keyboard"]
cart.remove("mouse")

print(cart)
# ["laptop", "mouse", "keyboard"]
```

### Interview point

`remove()` raises `ValueError` if the value does not exist.

```python
if "mouse" in cart:
    cart.remove("mouse")
```

## `pop()`

Removes and returns an item by index. Without an index, it removes the last item.

```python
cart = ["laptop", "mouse", "keyboard"]

last_item = cart.pop()
first_item = cart.pop(0)

print(last_item)   # keyboard
print(first_item)  # laptop
print(cart)        # ["mouse"]
```

### Interview point

`pop()` from the end is **O(1)**. `pop(0)` is **O(n)** because remaining items shift.

## `clear()`

Removes all items.

```python
temporary_cart = ["laptop", "mouse"]
temporary_cart.clear()

print(temporary_cart)
# []
```

## `index()`

Returns the first index of a value.

```python
products = ["laptop", "mouse", "keyboard"]

print(products.index("mouse"))
# 1
```

### Interview point

`index()` raises `ValueError` if the value is missing and takes **O(n)** time.

## `count()`

Counts how many times a value appears.

```python
cart = ["mouse", "laptop", "mouse", "keyboard"]

print(cart.count("mouse"))
# 2
```

### Interview point

For counting many values, use `collections.Counter` instead of repeated `count()`.

```python
from collections import Counter

cart = ["mouse", "laptop", "mouse"]
print(Counter(cart))
```

## `sort()`

Sorts the list in place.

```python
prices = [999, 25, 75, 199]
prices.sort()

print(prices)
# [25, 75, 199, 999]
```

Sort descending:

```python
prices.sort(reverse=True)
print(prices)
```

Sort with a key:

```python
products = [
    {"name": "laptop", "price": 999},
    {"name": "mouse", "price": 25},
]

products.sort(key=lambda product: product["price"])
```

### Interview point

`sort()` mutates the original list. Use `sorted()` when you need a new list.

## `reverse()`

Reverses the list in place.

```python
recently_viewed = ["laptop", "mouse", "monitor"]
recently_viewed.reverse()

print(recently_viewed)
# ["monitor", "mouse", "laptop"]
```

### Interview point

Use slicing `[::-1]` when you want a reversed copy.

```python
items = ["laptop", "mouse", "monitor"]
reversed_items = items[::-1]
```

## `copy()`

Returns a shallow copy.

```python
cart = ["laptop", "mouse"]
backup_cart = cart.copy()

backup_cart.append("keyboard")

print(cart)        # ["laptop", "mouse"]
print(backup_cart) # ["laptop", "mouse", "keyboard"]
```

### Interview point

`copy()` is shallow. Nested objects are still shared.

```python
orders = [["laptop"], ["mouse"]]
backup = orders.copy()

backup[0].append("keyboard")
print(orders)
# [["laptop", "keyboard"], ["mouse"]]
```

## Common Interview Questions

### What is the difference between `append()` and `extend()`?

`append()` adds one object. `extend()` iterates and adds each element.

### What is the difference between `sort()` and `sorted()`?

`sort()` modifies the original list and returns `None`. `sorted()` returns a new sorted list.

### What is the difference between `remove()`, `pop()`, and `del`?

`remove()` deletes by value. `pop()` deletes by index and returns the value. `del` deletes by index or slice and returns nothing.

### Why is `pop(0)` slower than `pop()`?

`pop(0)` shifts all remaining items left, so it is **O(n)**. `pop()` from the end is **O(1)**.

## Practice Problems

1. Build a cart list using `append()`.
2. Merge cart and recommended accessories using `extend()`.
3. Remove the first unavailable product using `remove()`.
4. Use `pop()` to simulate stack behavior.
5. Sort product prices ascending and descending.
6. Count duplicate products in a cart.
7. Reverse recently viewed products.
8. Copy a list and explain shallow copy behavior.

## See also

- [Python lists: core concepts](core-concepts.md)
- [Python list interview problems](interview-problems.md)
- [Python list FAQ](frequently-asked-questions.md)
