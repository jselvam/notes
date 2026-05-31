# Python Dictionaries: Core Concepts & Shopping Examples

A Python **dictionary** (`dict`) stores data as **key-value pairs**. Dictionaries are one of the most important interview data structures because they provide fast lookup by key.

In an online computer shopping management system, dictionaries can represent:

- product details by product ID
- price lookup by SKU
- cart quantity by product name
- inventory count by warehouse/product key
- subscription feature flags
- frequency counts for product IDs or coupon codes

## Overview

Dictionaries are:

- **Key-value based** — each key maps to a value.
- **Mutable** — you can add, update, and delete entries.
- **Fast for lookup** — key lookup is average **O(1)**.
- **Insertion ordered** — modern Python keeps insertion order.
- **Unique by key** — duplicate keys overwrite older values.

```python
product_prices = {
    "laptop": 999,
    "mouse": 25,
    "keyboard": 75,
}

print(product_prices["laptop"])  # 999
```

## Creating a Dictionary

Use curly braces with `key: value` pairs.

```python
product = {
    "id": 101,
    "name": "laptop",
    "price": 999,
    "in_stock": True,
}
```

Use `dict()` when building from pairs.

```python
pairs = [("laptop", 999), ("mouse", 25)]
prices = dict(pairs)

print(prices)
```

## Empty Dictionary

Use `{}` or `dict()`.

```python
cart_quantities = {}
inventory = dict()
```

## Accessing Values

Use square brackets when the key must exist.

```python
prices = {"laptop": 999, "mouse": 25}

print(prices["mouse"])
```

Use `.get()` when the key may be missing.

```python
prices = {"laptop": 999}

print(prices.get("monitor"))       # None
print(prices.get("monitor", 0))    # 0
```

## Adding and Updating Values

```python
cart = {}

cart["laptop"] = 1
cart["mouse"] = 2
cart["mouse"] = 3

print(cart)
# {"laptop": 1, "mouse": 3}
```

Duplicate keys do not create two entries. The latest value replaces the old value.

## Deleting Values

Use `del` when the key must exist.

```python
cart = {"laptop": 1, "mouse": 2}
del cart["mouse"]

print(cart)
```

Use `.pop()` when you want the removed value.

```python
cart = {"laptop": 1, "mouse": 2}
removed_quantity = cart.pop("mouse")

print(removed_quantity)
print(cart)
```

## Iterating Through a Dictionary

Loop over keys by default.

```python
prices = {"laptop": 999, "mouse": 25}

for product_name in prices:
    print(product_name)
```

Use `.items()` for key and value.

```python
for product_name, price in prices.items():
    print(product_name, price)
```

## Dictionary Comprehension

```python
products = ["laptop", "mouse", "keyboard"]
default_stock = {product: 0 for product in products}

print(default_stock)
```

Filter while building:

```python
prices = {"laptop": 999, "mouse": 25, "monitor": 199}
expensive = {name: price for name, price in prices.items() if price >= 100}

print(expensive)
```

## Frequency Counting

Dictionaries are commonly used to count occurrences.

```python
cart_items = ["mouse", "laptop", "mouse", "keyboard"]
counts = {}

for item in cart_items:
    counts[item] = counts.get(item, 0) + 1

print(counts)
# {"mouse": 2, "laptop": 1, "keyboard": 1}
```

## Dictionary as a Lookup Table

```python
discounts = {
    "SAVE10": 10,
    "OFFICE20": 20,
}

coupon = "SAVE10"
discount = discounts.get(coupon, 0)

print(discount)
```

## Tuple Keys for Composite Lookup

Use tuple keys when one key is not enough.

```python
stock = {
    ("warehouse-a", 101): 25,
    ("warehouse-b", 101): 8,
}

print(stock[("warehouse-a", 101)])
```

## Common Interview Points

### Why use a dictionary instead of a list?

Use a dictionary when you need fast lookup by key.

```python
prices = {"laptop": 999}
print(prices["laptop"])  # O(1) average
```

### What happens with duplicate keys?

The latest value wins.

```python
prices = {"mouse": 25, "mouse": 20}
print(prices)  # {"mouse": 20}
```

### Can dictionary keys be lists?

No. Keys must be hashable.

```python
# invalid = {["laptop", "mouse"]: 1}  # TypeError
valid = {("laptop", "mouse"): 1}
```

## Practice Problems

1. Count product frequencies in a cart.
2. Find the first repeated product ID using a dictionary.
3. Store prices by product name.
4. Build inventory using `(warehouse_id, product_id)` keys.
5. Group products by category.
6. Find two prices that sum to a target and return indices.
7. Merge two product-price dictionaries.
8. Convert a list of product records into a dictionary keyed by ID.

## See also

- [Python dictionary methods](methods.md)
- [Python dictionary interview problems](interview-problems.md)
- [Python dictionary FAQ](frequently-asked-questions.md)
- [Python tuple core concepts](../tuple/core-concepts.md)
