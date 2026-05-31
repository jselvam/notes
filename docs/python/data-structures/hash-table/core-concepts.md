# Hash Table in Python: Core Concepts

A hash table stores key-value pairs and gives fast average lookup, insert, and delete operations.

In Python, the main hash-table based data structures are:

- `dict`
- `set`

Examples use an online computer shopping system.

## Why Hash Tables Matter

Hash tables are used when you need fast lookup by a key.

Shopping examples:

- find product by SKU
- check whether a coupon code exists
- map order ID to order details
- track user sessions by token
- store inventory count by warehouse

## Key-Value Mapping

```python
products = {
    "LAP-101": "Laptop",
    "MOU-201": "Mouse",
    "KEY-301": "Keyboard",
}

print(products["LAP-101"])
```

Output:

```text
Laptop
```

## Hash Function Idea

A hash function converts a key into a number. That number helps decide where the value should be stored internally.

Simple mental model:

```text
"LAP-101" -> hash value -> bucket index -> product details
```

Python handles the real hashing internally.

## Average Complexity

| Operation | Average complexity |
|-----------|--------------------|
| insert key | `O(1)` |
| lookup key | `O(1)` |
| delete key | `O(1)` |
| scan all items | `O(n)` |

Worst-case lookup can degrade if many keys collide, but Python dictionaries are highly optimized.

## Hashable Keys

Dictionary keys must be hashable.

Common hashable keys:

- `str`
- `int`
- `float`
- `bool`
- `tuple` containing only hashable values

Unhashable keys:

- `list`
- `dict`
- `set`

```python
product_locations = {
    ("LAP-101", "WH-1"): 10,
    ("LAP-101", "WH-2"): 4,
}

print(product_locations[("LAP-101", "WH-1")])
```

Output:

```text
10
```

## Collision

A collision happens when two different keys map to the same internal bucket.

Python handles collisions internally. In interviews, you should know the concept but you usually do not implement collision handling unless asked.

## Dictionary vs Set

| Structure | Stores | Example use |
|-----------|--------|-------------|
| `dict` | key-value pairs | SKU to product details |
| `set` | unique keys only | valid coupon codes |

```python
valid_coupons = {"WELCOME10", "FESTIVAL20"}

print("WELCOME10" in valid_coupons)
```

Output:

```text
True
```

## Common Hash Table Patterns

### Lookup Table

```python
products_by_sku = {
    "LAP-101": {"name": "Laptop", "price": 999},
    "MOU-201": {"name": "Mouse", "price": 25},
}

print(products_by_sku.get("MOU-201"))
```

### Index Map

```python
product_positions = {
    "LAP-101": 0,
    "MOU-201": 1,
}
```

### Grouping Map

```python
products_by_category = {}

for product in ["laptop", "mouse", "monitor"]:
    first_letter = product[0]
    products_by_category.setdefault(first_letter, []).append(product)
```

### Counting Map

```python
cart_count = {}

for sku in ["LAP-101", "MOU-201", "LAP-101"]:
    cart_count[sku] = cart_count.get(sku, 0) + 1

print(cart_count)
```

Output:

```text
{'LAP-101': 2, 'MOU-201': 1}
```

## Common Mistakes

### Using list lookup when key lookup is needed

Searching a list is `O(n)`. Dictionary lookup is average `O(1)`.

### Using mutable keys

Lists and dictionaries cannot be dictionary keys.

### Assuming dictionaries are sorted by value

Python dictionaries preserve insertion order, not sorted order.

### Forgetting `.get()`

Use `.get()` when a key may be missing.

```python
stock = {"LAP-101": 5}
print(stock.get("MOU-201", 0))
```

Output:

```text
0
```

## See also

- [Interview problems](interview-problems.md)
- [Interview questions](interview-questions.md)
- [Python dictionaries](../../dict/core-concepts.md)
- [Python sets](../../set/core-concepts.md)
