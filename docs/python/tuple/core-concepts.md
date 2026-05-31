# Python Tuples: Core Concepts & Shopping Examples

A Python **tuple** stores an ordered collection of values that should not be changed after creation. Tuples are commonly used for fixed records, multiple return values, coordinates, keys, and safe grouping.

In an online computer shopping management system, tuples can represent:

- fixed product identity: `(product_id, sku)`
- warehouse location: `("warehouse-a", "rack-3")`
- price range: `(min_price, max_price)`
- order status transition: `("paid", "shipped")`
- dictionary keys for combined lookup: `(warehouse_id, product_id)`

## Overview

Tuples are:

- **Ordered** — items have positions.
- **Immutable** — you cannot add, remove, or change items after creation.
- **Indexable** — access values with `tuple[index]`.
- **Duplicate-friendly** — duplicate values are allowed.
- **Hashable when contents are hashable** — useful as dictionary keys or set items.

```python
product = (101, "laptop", 999)

print(product[0])  # 101
print(product[1])  # laptop
```

## Creating a Tuple

Use parentheses:

```python
product = (101, "laptop", 999)
location = ("warehouse-a", "rack-3")
```

Parentheses are often optional, but they improve readability.

```python
product_id, name, price = 101, "laptop", 999
```

## Single-Item Tuple

A one-item tuple needs a trailing comma.

```python
not_tuple = ("laptop")
single_item_tuple = ("laptop",)

print(type(not_tuple))          # <class 'str'>
print(type(single_item_tuple))  # <class 'tuple'>
```

## Empty Tuple

```python
empty = ()
also_empty = tuple()
```

## Indexing

```python
product = (101, "laptop", 999)

print(product[0])   # 101
print(product[-1])  # 999
```

## Slicing

```python
product = (101, "laptop", "hardware", 999, "in-stock")

print(product[1:4])
# ("laptop", "hardware", 999)
```

## Tuple Packing

Packing means putting multiple values into one tuple.

```python
product = 101, "laptop", 999

print(product)
# (101, "laptop", 999)
```

## Tuple Unpacking

Unpacking means assigning tuple values to variables.

```python
product = (101, "laptop", 999)
product_id, name, price = product

print(product_id)
print(name)
print(price)
```

Use `_` for values you do not need.

```python
product = (101, "laptop", 999)
product_id, _, price = product
```

## Extended Unpacking

Use `*` to collect remaining values.

```python
order = ("ORD-1", "laptop", "mouse", "keyboard")

order_id, *items = order

print(order_id)  # ORD-1
print(items)     # ["laptop", "mouse", "keyboard"]
```

## Immutability

You cannot change tuple items directly.

```python
product = (101, "laptop", 999)

# product[2] = 899  # TypeError
```

To "change" a tuple, create a new tuple.

```python
product = (101, "laptop", 999)
updated_product = (product[0], product[1], 899)

print(updated_product)
```

## Tuple as Dictionary Key

Tuples are useful for composite keys.

```python
stock = {
    ("warehouse-a", 101): 25,
    ("warehouse-b", 101): 8,
}

print(stock[("warehouse-a", 101)])
# 25
```

This is useful when one field is not enough for lookup.

## Tuple in a Set

Tuples can be stored in sets if all values inside are hashable.

```python
unique_locations = {
    ("warehouse-a", "rack-1"),
    ("warehouse-a", "rack-1"),
    ("warehouse-b", "rack-2"),
}

print(unique_locations)
```

## Tuple vs List

| Feature | Tuple | List |
|---------|-------|------|
| Syntax | `(1, 2)` | `[1, 2]` |
| Mutable | No | Yes |
| Use case | Fixed data | Changing data |
| Can be dict key | Yes, if hashable | No |
| Methods | Few | Many |

## Common Interview Points

### Why use a tuple instead of a list?

Use a tuple when the values should stay fixed, such as product identity or warehouse-location keys.

```python
product_key = (101, "SKU-LAPTOP-13")
```

### Are tuples always hashable?

No. A tuple is hashable only if all its elements are hashable.

```python
valid = (101, "laptop")
# invalid = (101, ["laptop", "mouse"])  # unhashable because list is inside
```

### Can a tuple contain a list?

Yes, but then the tuple is not hashable.

```python
order = ("ORD-1", ["laptop", "mouse"])
order[1].append("keyboard")

print(order)
```

The tuple itself is immutable, but the list inside can still change.

## Practice Problems

1. Unpack `(product_id, name, price)` into variables.
2. Swap two prices using tuple unpacking.
3. Use `(warehouse_id, product_id)` as a stock dictionary key.
4. Count duplicate warehouse-location tuples.
5. Return multiple values from a function using a tuple.
6. Convert a list of product records into tuples.
7. Explain why `(101, ["mouse"])` cannot be a set item.

## See also

- [Python tuple methods](methods.md)
- [Python tuple interview problems](interview-problems.md)
- [Python tuple FAQ](frequently-asked-questions.md)
- [Python lists: core concepts](../list/core-concepts.md)
