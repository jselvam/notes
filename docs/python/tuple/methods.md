# Python Tuple Methods: Interview Notes

Tuples are immutable, so they have only a few methods. In interviews, tuple questions are usually about **immutability**, **unpacking**, **hashability**, and the two tuple methods: `count()` and `index()`.

## Quick Method Table

| Method | What it does | Interview use case |
|--------|--------------|--------------------|
| `count()` | Counts occurrences of a value | Duplicate values in fixed records |
| `index()` | Returns first index of a value | Locate value inside fixed tuple |

Tuples also support built-in operations like `len()`, `in`, slicing, iteration, `min()`, `max()`, and `sum()` for numeric tuples.

## `count()`

`count(value)` returns how many times a value appears in the tuple.

```python
cart_categories = ("hardware", "software", "hardware", "subscription")

print(cart_categories.count("hardware"))
# 2
```

### Interview point

Use `count()` for quick checks, but avoid repeatedly calling it in loops for large inputs because each call scans the tuple.

```python
product_ids = (101, 102, 101, 103)

if product_ids.count(101) > 1:
    print("Duplicate product ID found")
```

## `index()`

`index(value)` returns the first index where the value appears.

```python
product = (101, "laptop", "hardware", 999)

print(product.index("hardware"))
# 2
```

### Interview point

`index()` raises `ValueError` if the value is missing.

```python
product = (101, "laptop", 999)

if "laptop" in product:
    print(product.index("laptop"))
```

## `len()`

`len()` returns the number of items.

```python
product = (101, "laptop", 999)

print(len(product))
# 3
```

## Membership Check with `in`

```python
product = (101, "laptop", "hardware", 999)

print("laptop" in product)
# True
```

### Interview point

Membership check in a tuple is **O(n)** because Python may scan each item.

## Iteration

```python
product = (101, "laptop", 999)

for value in product:
    print(value)
```

Use `enumerate()` when you need index and value.

```python
for index, value in enumerate(product):
    print(index, value)
```

## Slicing

```python
product = (101, "laptop", "hardware", 999, "in-stock")

print(product[1:4])
# ("laptop", "hardware", 999)
```

Slicing returns a new tuple.

## Concatenation

Use `+` to create a new tuple.

```python
base_product = (101, "laptop")
price_info = (999, "in-stock")

full_product = base_product + price_info

print(full_product)
```

## Repetition

Use `*` to repeat tuple values.

```python
divider = ("-",) * 3

print(divider)
# ("-", "-", "-")
```

## Tuple Unpacking

```python
product = (101, "laptop", 999)

product_id, name, price = product

print(product_id, name, price)
```

## Swapping Values

Tuple unpacking makes swaps concise.

```python
old_price = 999
new_price = 899

old_price, new_price = new_price, old_price

print(old_price, new_price)
```

## Returning Multiple Values

Python functions often return multiple values as a tuple.

```python
def min_max_price(prices):
    return min(prices), max(prices)


lowest, highest = min_max_price([25, 75, 999])

print(lowest, highest)
```

## Common Interview Questions

### Why do tuples have fewer methods than lists?

Tuples are immutable. Methods that mutate data, like `append()`, `remove()`, and `sort()`, do not exist for tuples.

### What is the difference between `tuple.index()` and list indexing?

`tuple.index(value)` searches by value and is **O(n)**. `tuple[index]` accesses by position and is **O(1)**.

### Can `count()` detect duplicates?

Yes for one value, but for many values use a dictionary or `collections.Counter`.

```python
from collections import Counter

product_ids = (101, 102, 101, 103)
print(Counter(product_ids))
```

### Does tuple concatenation modify the original tuple?

No. It creates a new tuple.

```python
a = ("laptop",)
b = a + ("mouse",)

print(a)  # ("laptop",)
print(b)  # ("laptop", "mouse")
```

## Practice Problems

1. Count how many times `"hardware"` appears in a tuple.
2. Find the index of `"office-suite"` in a product tuple.
3. Unpack `(product_id, name, price)` into variables.
4. Return `(min_price, max_price)` from a price list.
5. Use tuple concatenation to create a new product record.
6. Explain why tuples do not have `append()`.

## See also

- [Python tuples: core concepts](core-concepts.md)
- [Python tuple interview problems](interview-problems.md)
- [Python tuple FAQ](frequently-asked-questions.md)
