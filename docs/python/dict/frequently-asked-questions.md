# Python Dictionaries: Frequently Asked Interview Questions

This page collects frequently asked Python `dict` interview questions from **basic** to **pro** level. Examples use online computer shopping system ideas like products, carts, prices, inventory, and subscriptions.

## Basic Level

### 1. What is a dictionary in Python?

A dictionary stores key-value pairs.

```python
product = {"id": 101, "name": "laptop"}
```

### 2. How do you create a dictionary?

Use `{key: value}` syntax.

```python
prices = {"laptop": 999, "mouse": 25}
```

### 3. How do you create an empty dictionary?

Use `{}` or `dict()`.

```python
cart = {}
prices = dict()
```

### 4. Are dictionary keys unique?

Yes. Duplicate keys overwrite old values.

```python
prices = {"mouse": 25, "mouse": 20}
print(prices)
```

### 5. Are dictionaries ordered?

Modern Python dictionaries preserve insertion order.

```python
product = {"id": 101, "name": "laptop", "price": 999}
print(list(product.keys()))
```

### 6. How do you access a value by key?

Use square brackets.

```python
prices = {"laptop": 999}
print(prices["laptop"])
```

### 7. What happens if a key is missing with square brackets?

Python raises `KeyError`.

```python
prices = {"laptop": 999}
# print(prices["mouse"])  # KeyError
```

### 8. How do you safely access a missing key?

Use `.get()`.

```python
prices = {"laptop": 999}
print(prices.get("mouse", 0))
```

### 9. How do you add a new key-value pair?

Assign to a new key.

```python
prices = {}
prices["laptop"] = 999
```

### 10. How do you update an existing value?

Assign a new value to the existing key.

```python
prices = {"laptop": 999}
prices["laptop"] = 899
```

### 11. How do you delete a key?

Use `del` or `pop()`.

```python
prices = {"laptop": 999, "mouse": 25}
del prices["mouse"]
```

### 12. How do you check if a key exists?

Use `in`.

```python
prices = {"laptop": 999}
print("laptop" in prices)
```

### 13. Does `in` check keys or values?

By default, `in` checks keys.

```python
prices = {"laptop": 999}
print("laptop" in prices)  # True
print(999 in prices)       # False
```

### 14. How do you get all keys?

Use `.keys()`.

```python
prices = {"laptop": 999}
print(prices.keys())
```

### 15. How do you get all values?

Use `.values()`.

```python
prices = {"laptop": 999}
print(prices.values())
```

## Intermediate Level

### 16. How do you get key-value pairs?

Use `.items()`.

```python
for product, price in {"laptop": 999}.items():
    print(product, price)
```

### 17. What is the difference between `dict[key]` and `get()`?

`dict[key]` raises `KeyError` if missing. `get()` returns `None` or a default.

### 18. What does `update()` do?

It adds or updates entries.

```python
prices = {"laptop": 999}
prices.update({"mouse": 25, "laptop": 899})
```

### 19. What does `pop()` do?

It removes a key and returns the value.

```python
cart = {"mouse": 2}
quantity = cart.pop("mouse")
```

### 20. What does `popitem()` do?

It removes and returns the latest inserted key-value pair.

```python
cart = {"laptop": 1, "mouse": 2}
print(cart.popitem())
```

### 21. What does `setdefault()` do?

It returns an existing value or inserts a default value.

```python
groups = {}
groups.setdefault("hardware", []).append("laptop")
```

### 22. What does `clear()` do?

It removes all entries.

```python
cache = {"x": 1}
cache.clear()
```

### 23. What does `copy()` do?

It creates a shallow copy.

```python
prices = {"laptop": 999}
backup = prices.copy()
```

### 24. What does `fromkeys()` do?

It creates a dictionary from keys with the same value.

```python
products = ["laptop", "mouse"]
stock = dict.fromkeys(products, 0)
```

### 25. What is a dictionary comprehension?

A compact way to create a dictionary.

```python
prices = {"laptop": 999, "mouse": 25}
expensive = {name: price for name, price in prices.items() if price > 100}
```

### 26. How do you count frequencies with a dictionary?

Use `get()` with default `0`.

```python
counts = {}
for item in ["mouse", "mouse", "laptop"]:
    counts[item] = counts.get(item, 0) + 1
```

### 27. When should you use `Counter` instead?

Use `Counter` when the main task is counting.

```python
from collections import Counter
print(Counter(["mouse", "mouse", "laptop"]))
```

### 28. How do you group values by key?

Use `setdefault()` or `defaultdict(list)`.

```python
groups = {}
groups.setdefault("hardware", []).append("mouse")
```

### 29. What is `defaultdict`?

A dictionary subclass that creates default values automatically.

```python
from collections import defaultdict

groups = defaultdict(list)
groups["hardware"].append("laptop")
```

### 30. Can dictionary values be any type?

Yes. Values can be lists, dictionaries, objects, or any Python value.

```python
product = {"tags": ["hardware", "sale"]}
```

## Advanced Level

### 31. What types can be dictionary keys?

Keys must be hashable, such as strings, numbers, and tuples of hashable values.

```python
stock = {("warehouse-a", 101): 25}
```

### 32. Can lists be dictionary keys?

No. Lists are mutable and unhashable.

```python
# invalid = {["laptop"]: 999}
```

### 33. Can tuples be dictionary keys?

Yes, if all tuple elements are hashable.

```python
inventory = {("warehouse-a", 101): 25}
```

### 34. What is the average time complexity of dictionary lookup?

Average **O(1)**.

```python
prices = {"laptop": 999}
print(prices["laptop"])
```

### 35. What is the worst-case time complexity of dictionary lookup?

Worst case can be **O(n)** because of hash collisions, but average is **O(1)**.

### 36. How does a dictionary help solve Two Sum?

Map number to index and check complements.

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
```

### 37. How do you find the first non-repeating value?

Count first, then scan original order.

```python
def first_unique(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    for item in items:
        if counts[item] == 1:
            return item
```

### 38. How do you invert a dictionary?

Swap keys and values, if values are unique and hashable.

```python
prices = {"laptop": 999, "mouse": 25}
inverted = {price: name for name, price in prices.items()}
```

### 39. What problem happens when inverting duplicate values?

Later keys overwrite earlier keys.

```python
data = {"a": 1, "b": 1}
print({v: k for k, v in data.items()})
```

### 40. How do you merge dictionaries in modern Python?

Use `|` or `update()`.

```python
old = {"laptop": 999}
new = {"mouse": 25}
merged = old | new
```

### 41. What is the difference between `|` and `update()`?

`|` returns a new dictionary. `update()` mutates the original.

### 42. How do you sort a dictionary by value?

Use `sorted()` on `.items()`.

```python
prices = {"laptop": 999, "mouse": 25}
print(sorted(prices.items(), key=lambda item: item[1]))
```

### 43. How do you filter a dictionary?

Use dictionary comprehension.

```python
expensive = {k: v for k, v in prices.items() if v >= 100}
```

### 44. What is a nested dictionary?

A dictionary whose values are dictionaries.

```python
products = {101: {"name": "laptop", "price": 999}}
```

### 45. How do you safely read nested dictionary values?

Chain `.get()` calls with defaults.

```python
products = {101: {"name": "laptop"}}
print(products.get(101, {}).get("price", 0))
```

## Pro Level

### 46. How are dictionaries implemented internally?

Python dictionaries are hash-table based.

### 47. What is hashability?

A hashable object has a stable hash and can be compared for equality.

```python
print(hash("laptop"))
```

### 48. Why must dictionary keys be hashable?

The dictionary uses a key's hash to find where values are stored.

### 49. What is a hash collision?

Two different keys can have the same hash bucket. Python resolves collisions internally.

### 50. How do equality and hashing interact in dictionary keys?

If two keys compare equal and have the same hash, they represent the same dictionary key.

```python
data = {1: "one", True: "true"}
print(data)
```

### 51. Why is `1` and `True` surprising as dictionary keys?

`1 == True` is `True`, so they collide as equivalent keys.

### 52. What is a dictionary view?

`.keys()`, `.values()`, and `.items()` return dynamic views, not fixed lists.

```python
prices = {"laptop": 999}
keys = prices.keys()
prices["mouse"] = 25
print(keys)
```

### 53. What is shallow copy behavior in dictionaries?

The outer dictionary is copied, but nested objects are shared.

```python
cart = {"items": ["laptop"]}
backup = cart.copy()
backup["items"].append("mouse")
print(cart)
```

### 54. How do you deep copy a dictionary?

Use `copy.deepcopy()`.

```python
import copy
backup = copy.deepcopy(cart)
```

### 55. Why should you avoid mutable defaults with `fromkeys()`?

All keys share the same mutable object.

```python
bad = dict.fromkeys(["a", "b"], [])
bad["a"].append(1)
print(bad)
```

### 56. How do dictionaries help with memoization?

Store input-to-output results.

```python
cache = {}
cache[101] = "calculated score"
```

### 57. How do dictionaries help with idempotency?

Track processed IDs and their results.

```python
processed = {}
processed["order-1"] = "processed"
```

### 58. When should you choose dict over set?

Choose dict when you need a value associated with each key.

### 59. When should you choose set over dict?

Choose set when you only need uniqueness or membership.

### 60. What should you say if asked “dictionary or list?”

Use a dictionary for key-based lookup and a list for ordered sequences or index-based algorithms.

## Final Interview Checklist

- Dictionaries store key-value pairs.
- Keys are unique and must be hashable.
- Lookup, insert, and delete are average **O(1)**.
- Use `get()` to avoid `KeyError`.
- Use dictionaries for frequency counting, grouping, lookup tables, caching, and Two Sum indices.
- Use tuple keys for composite lookup.
- Use `Counter` for counting-heavy problems.
- Understand shallow copy, dictionary views, and mutable `fromkeys()` pitfalls.

## See also

- [Python dictionaries: core concepts](core-concepts.md)
- [Python dictionary methods](methods.md)
- [Python dictionary interview problems](interview-problems.md)
- [Python tuple FAQ](../tuple/frequently-asked-questions.md)
