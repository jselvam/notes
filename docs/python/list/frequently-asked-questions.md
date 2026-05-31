# Python Lists: Frequently Asked Interview Questions

This page collects frequently asked Python `list` interview questions from **basic** to **pro** level. Examples use online computer shopping system ideas: carts, products, prices, inventory, and subscriptions.

## Basic Level

### 1. What is a list in Python?

A list is an ordered, mutable collection of items.

```python
cart = ["laptop", "mouse", "keyboard"]
```

### 2. Can a list contain duplicate values?

Yes. Lists allow duplicates.

```python
cart = ["mouse", "mouse", "keyboard"]
```

### 3. Can a list contain mixed data types?

Yes, but in real projects it is cleaner to keep one kind of data per list.

```python
product = ["laptop", 999, True]
```

### 4. How do you create an empty list?

Use `[]` or `list()`.

```python
cart = []
orders = list()
```

### 5. How do you access the first item?

Use index `0`.

```python
products = ["laptop", "mouse"]
print(products[0])
```

### 6. How do you access the last item?

Use index `-1`.

```python
products = ["laptop", "mouse"]
print(products[-1])
```

### 7. What happens if you access an invalid index?

Python raises `IndexError`.

```python
products = ["laptop"]
# print(products[5])  # IndexError
```

### 8. How do you find the length of a list?

Use `len()`.

```python
cart = ["laptop", "mouse"]
print(len(cart))
```

### 9. How do you check if an item exists in a list?

Use `in`. This is **O(n)** for lists.

```python
cart = ["laptop", "mouse"]
print("mouse" in cart)
```

### 10. How do you loop through a list?

Use a `for` loop.

```python
for item in ["laptop", "mouse"]:
    print(item)
```

### 11. How do you get both index and value?

Use `enumerate()`.

```python
products = ["laptop", "mouse"]

for index, product in enumerate(products):
    print(index, product)
```

### 12. How do you slice a list?

Use `start:stop:step`.

```python
products = ["laptop", "mouse", "keyboard", "monitor"]
print(products[1:3])
```

### 13. How do you reverse a list using slicing?

Use `[::-1]`.

```python
products = ["laptop", "mouse", "keyboard"]
print(products[::-1])
```

### 14. Are lists mutable?

Yes. You can update items by index.

```python
products = ["old-monitor"]
products[0] = "new-monitor"
```

### 15. What is the difference between list and tuple?

A list is mutable. A tuple is immutable.

```python
cart = ["laptop"]
fixed_location = ("warehouse-a", "rack-1")
```

## Intermediate Level

### 16. What is `append()`?

`append()` adds one item to the end.

```python
cart = ["laptop"]
cart.append("mouse")
```

### 17. What is `extend()`?

`extend()` adds each item from an iterable.

```python
cart = ["laptop"]
cart.extend(["mouse", "keyboard"])
```

### 18. What is the difference between `append()` and `extend()`?

`append()` adds the object as one item. `extend()` adds each element.

```python
items = ["laptop"]
items.append(["mouse", "keyboard"])
print(items)
```

### 19. What is `insert()`?

`insert(index, value)` adds a value at a specific index.

```python
products = ["laptop", "monitor"]
products.insert(1, "mouse")
```

### 20. What is `remove()`?

`remove(value)` deletes the first matching value.

```python
cart = ["mouse", "laptop", "mouse"]
cart.remove("mouse")
```

### 21. What is `pop()`?

`pop()` removes and returns an item. Without an index, it removes the last item.

```python
cart = ["laptop", "mouse"]
removed = cart.pop()
```

### 22. What is the difference between `remove()` and `pop()`?

`remove()` deletes by value and returns nothing. `pop()` deletes by index and returns the removed item.

### 23. What is the difference between `del` and `pop()`?

`del` removes by index or slice and returns nothing. `pop()` returns the removed value.

```python
cart = ["laptop", "mouse"]
del cart[0]
```

### 24. What does `clear()` do?

It removes all items.

```python
cart = ["laptop", "mouse"]
cart.clear()
```

### 25. What does `index()` do?

It returns the first index of a value.

```python
products = ["laptop", "mouse"]
print(products.index("mouse"))
```

### 26. What does `count()` do?

It counts occurrences.

```python
cart = ["mouse", "mouse", "laptop"]
print(cart.count("mouse"))
```

### 27. What does `sort()` do?

It sorts the list in place.

```python
prices = [999, 25, 75]
prices.sort()
```

### 28. What is the difference between `sort()` and `sorted()`?

`sort()` mutates the original list. `sorted()` returns a new list.

```python
prices = [999, 25, 75]
new_prices = sorted(prices)
```

### 29. What does `reverse()` do?

It reverses the list in place.

```python
items = ["laptop", "mouse"]
items.reverse()
```

### 30. What is a list comprehension?

A compact way to build a new list.

```python
prices = [999, 25, 75]
expensive = [price for price in prices if price > 100]
```

## Advanced Level

### 31. What is the time complexity of list indexing?

Indexing is **O(1)**.

```python
products = ["laptop", "mouse"]
print(products[1])
```

### 32. What is the time complexity of list search?

Search with `in` is **O(n)**.

```python
print("mouse" in ["laptop", "mouse"])
```

### 33. What is the time complexity of `append()`?

`append()` is **O(1)** amortized.

```python
cart = []
cart.append("laptop")
```

### 34. Why is `insert(0, value)` expensive?

All existing items may need to shift right, so it is **O(n)**.

### 35. Why is `pop(0)` expensive?

All remaining items shift left, so it is **O(n)**.

### 36. How do you use a list as a stack?

Use `append()` for push and `pop()` for pop.

```python
stack = []
stack.append("add-laptop")
stack.pop()
```

### 37. Should you use a list as a queue?

Avoid `pop(0)` for large queues. Use `collections.deque`.

```python
from collections import deque

queue = deque(["order-1", "order-2"])
queue.popleft()
```

### 38. How do you remove duplicates but preserve order?

Use a set for seen values and a list for result.

```python
def unique_ordered(items):
    seen = set()
    result = []

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result
```

### 39. How do you find the second largest number in a list?

Track largest and second largest in one pass.

```python
def second_largest(values):
    first = second = None

    for value in values:
        if value == first:
            continue
        if first is None or value > first:
            second = first
            first = value
        elif second is None or value > second:
            second = value

    return second
```

### 40. How do you reverse a list in place manually?

Use two pointers.

```python
def reverse_in_place(items):
    left, right = 0, len(items) - 1

    while left < right:
        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1

    return items
```

### 41. How do you merge two sorted lists?

Use two pointers and append the smaller current item.

```python
def merge_sorted(a, b):
    i = j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    return result + a[i:] + b[j:]
```

### 42. How do you rotate a list?

Use slicing.

```python
def rotate_right(items, k):
    if not items:
        return items
    k %= len(items)
    return items[-k:] + items[:-k]
```

### 43. What is a shallow copy?

A shallow copy copies the outer list, but nested objects are shared.

```python
orders = [["laptop"], ["mouse"]]
copy_orders = orders.copy()
copy_orders[0].append("keyboard")
print(orders)
```

### 44. How do you make a deep copy?

Use `copy.deepcopy()`.

```python
import copy

orders = [["laptop"], ["mouse"]]
safe_copy = copy.deepcopy(orders)
```

### 45. What is list unpacking?

Assign list values to variables.

```python
product, price = ["laptop", 999]
```

## Pro Level

### 46. How are Python lists implemented internally?

Python lists are dynamic arrays. They store references to objects and support fast indexing.

### 47. Why is `append()` amortized O(1)?

Python over-allocates list capacity, so most appends do not require resizing.

### 48. Why can list resizing be expensive sometimes?

When capacity is full, Python may allocate a larger array and copy references.

### 49. Why is membership check slower in list than set?

A list scans values one by one (**O(n)**). A set uses hashing (**O(1)** average).

### 50. When should you choose a list over a set?

Choose a list when order, duplicates, or index access matter.

### 51. When should you choose a set over a list?

Choose a set for uniqueness and fast membership checks.

### 52. When should you choose `deque` over a list?

Choose `deque` for efficient appends and pops from both ends.

### 53. What is aliasing in lists?

Two variables can point to the same list.

```python
cart = ["laptop"]
backup = cart
backup.append("mouse")
print(cart)
```

### 54. How do you avoid accidental aliasing?

Use `copy()`, slicing, or `list()`.

```python
backup = cart.copy()
```

### 55. What is wrong with `[[]] * 3`?

It creates three references to the same inner list.

```python
rows = [[]] * 3
rows[0].append("laptop")
print(rows)
```

### 56. What is the correct way to create independent nested lists?

Use a comprehension.

```python
rows = [[] for _ in range(3)]
```

### 57. Why should you avoid modifying a list while iterating?

It can skip items or behave unexpectedly.

```python
items = ["mouse", "mouse", "laptop"]
# Build a new list instead of removing while looping.
```

### 58. How do you safely filter a list?

Create a new list.

```python
items = ["mouse", "laptop", "mouse"]
filtered = [item for item in items if item != "mouse"]
```

### 59. Can list elements be unhashable?

Yes. Lists can contain anything, including dictionaries and other lists.

```python
products = [{"id": 101}, {"id": 102}]
```

### 60. Can a list be used as a dictionary key or set item?

No. Lists are mutable and unhashable.

```python
# invalid = {["laptop", "mouse"]}
valid = {("laptop", "mouse")}
```

## Final Interview Checklist

- Lists are ordered, mutable, and allow duplicates.
- Indexing is **O(1)**.
- Search is **O(n)**.
- `append()` is **O(1)** amortized.
- Insert/delete near the front is **O(n)**.
- Use list + set to remove duplicates while preserving order.
- Use `deque` for queue behavior.
- Understand shallow copy vs deep copy.
- Avoid modifying a list while iterating.

## See also

- [Python lists: core concepts](core-concepts.md)
- [Python list methods](methods.md)
- [Python list interview problems](interview-problems.md)
- [Python set FAQ](../set/frequently-asked-questions.md)
