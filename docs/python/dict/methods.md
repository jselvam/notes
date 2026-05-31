# Python Dictionary Methods: Interview Notes

Dictionary methods are frequently used in interviews for lookup tables, frequency counting, grouping, caching, and index mapping.

## Quick Method Table

| Method | What it does | Interview use case |
|--------|--------------|--------------------|
| `get()` | Safe key lookup | Avoid `KeyError` |
| `keys()` | View of keys | Iterate product IDs |
| `values()` | View of values | Iterate prices |
| `items()` | View of key-value pairs | Loop key and value |
| `update()` | Merge/update entries | Merge price maps |
| `pop()` | Remove key and return value | Delete cart item |
| `popitem()` | Remove latest key-value pair | Stack-like dict removal |
| `setdefault()` | Get or initialize key | Grouping values |
| `clear()` | Remove all entries | Reset state |
| `copy()` | Shallow copy | Preserve original dict |
| `fromkeys()` | Create dict from keys | Default values |

## `get()`

Returns the value for a key, or a default if missing.

```python
prices = {"laptop": 999, "mouse": 25}

print(prices.get("monitor"))      # None
print(prices.get("monitor", 0))   # 0
```

### Interview point

Use `get()` for frequency counting.

```python
cart = ["mouse", "laptop", "mouse"]
counts = {}

for item in cart:
    counts[item] = counts.get(item, 0) + 1

print(counts)
```

## `keys()`

Returns a dynamic view of keys.

```python
prices = {"laptop": 999, "mouse": 25}

print(prices.keys())
```

### Interview point

Keys are unique and support fast membership checks.

```python
if "laptop" in prices:
    print("Laptop has a price")
```

## `values()`

Returns a view of values.

```python
prices = {"laptop": 999, "mouse": 25}

print(prices.values())
```

### Interview point

Membership in values is **O(n)** because values are not hash-indexed.

## `items()`

Returns key-value pairs.

```python
prices = {"laptop": 999, "mouse": 25}

for product, price in prices.items():
    print(product, price)
```

### Interview point

Use `.items()` when filtering or transforming dictionaries.

```python
expensive = {name: price for name, price in prices.items() if price >= 100}
```

## `update()`

Adds or updates entries from another dictionary or iterable of pairs.

```python
prices = {"laptop": 999}
new_prices = {"mouse": 25, "laptop": 899}

prices.update(new_prices)

print(prices)
# {"laptop": 899, "mouse": 25}
```

### Interview point

Existing keys are overwritten.

## `pop()`

Removes a key and returns its value.

```python
cart = {"laptop": 1, "mouse": 2}

quantity = cart.pop("mouse")

print(quantity)
print(cart)
```

Use a default to avoid `KeyError`.

```python
quantity = cart.pop("monitor", 0)
```

## `popitem()`

Removes and returns the latest inserted key-value pair.

```python
cart = {"laptop": 1, "mouse": 2}

print(cart.popitem())
```

### Interview point

Modern Python dictionaries preserve insertion order, so `popitem()` removes the last inserted pair.

## `setdefault()`

Returns a value if the key exists; otherwise inserts the key with a default value.

```python
products_by_category = {}

products_by_category.setdefault("hardware", []).append("laptop")
products_by_category.setdefault("hardware", []).append("mouse")

print(products_by_category)
```

### Interview point

Useful for grouping, but `defaultdict(list)` is often cleaner.

## `clear()`

Removes all entries.

```python
cache = {"product-101": "laptop"}
cache.clear()

print(cache)
# {}
```

## `copy()`

Returns a shallow copy.

```python
prices = {"laptop": 999, "mouse": 25}
backup = prices.copy()

backup["laptop"] = 899

print(prices)
print(backup)
```

### Interview point

Nested values are still shared in a shallow copy.

```python
cart = {"items": ["laptop"]}
backup = cart.copy()

backup["items"].append("mouse")
print(cart)
```

## `fromkeys()`

Creates a dictionary from keys with the same default value.

```python
products = ["laptop", "mouse", "keyboard"]
stock = dict.fromkeys(products, 0)

print(stock)
```

### Interview point

Be careful with mutable default values.

```python
bad = dict.fromkeys(["cart-a", "cart-b"], [])
bad["cart-a"].append("laptop")
print(bad)
```

Both keys share the same list.

## Common Interview Questions

### What is the difference between `dict[key]` and `get()`?

`dict[key]` raises `KeyError` if missing. `get()` returns `None` or a default.

### What is the difference between `update()` and assignment?

Assignment updates one key. `update()` can update many keys.

### What is the difference between `pop()` and `del`?

`pop()` returns the removed value. `del` does not.

### What is the difference between `setdefault()` and `defaultdict`?

`setdefault()` is a dict method. `defaultdict` defines default behavior when the dictionary is created.

```python
from collections import defaultdict

groups = defaultdict(list)
groups["hardware"].append("laptop")
```

## Practice Problems

1. Count product names in a cart using `get()`.
2. Group products by category using `setdefault()`.
3. Merge two price dictionaries using `update()`.
4. Safely remove a product using `pop()`.
5. Create default stock values using `fromkeys()`.
6. Filter products above a price using `.items()`.
7. Explain shallow copy behavior with nested lists.
8. Compare `dict[key]`, `get()`, and `setdefault()`.

## See also

- [Python dictionaries: core concepts](core-concepts.md)
- [Python dictionary interview problems](interview-problems.md)
- [Python dictionary FAQ](frequently-asked-questions.md)
