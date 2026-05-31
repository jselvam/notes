# Python Sets: Core Concepts & Shopping Examples

A Python **set** stores **unique** values. Sets are useful when you need to remove duplicates, check membership quickly, compare groups, or find common / different items.

In an online computer shopping management system, sets can help with examples like:

- unique product categories: laptop, mouse, keyboard, monitor
- software and subscription tags: PDF editor, office suite, antivirus
- products available in one warehouse but not another
- items common between wishlist and cart
- duplicate product IDs from imports

## Overview

Sets are:

- **Unordered** — items do not keep insertion order for indexing.
- **Unique** — duplicate values are stored only once.
- **Mutable** — you can add or remove items.
- **Fast for membership checks** — `item in my_set` is usually very efficient.

```python
categories = {"laptop", "mouse", "keyboard", "monitor", "mouse"}

print(categories)
# Output order may vary, but "mouse" appears only once
```

## Creating a Set

Use curly braces for non-empty sets:

```python
product_types = {"hardware", "software", "subscription"}
print(product_types)
```

Use `set()` for an empty set. Do **not** use `{}` because that creates an empty dictionary.

```python
empty_cart_product_ids = set()
empty_dict = {}

print(type(empty_cart_product_ids))  # <class 'set'>
print(type(empty_dict))              # <class 'dict'>
```

## Removing Duplicate Products

If an imported product list contains repeated product IDs, convert it to a set.

```python
imported_product_ids = [101, 102, 103, 101, 104, 102]
unique_product_ids = set(imported_product_ids)

print(unique_product_ids)
# {101, 102, 103, 104}
```

This is useful when loading products from supplier feeds where the same laptop, mouse, or software license may appear more than once.

## Membership Check

Use `in` to check whether an item exists.

```python
available_categories = {"laptop", "mouse", "keyboard", "monitor", "pdf", "office-suite"}

if "laptop" in available_categories:
    print("Laptop category is available")

if "printer" not in available_categories:
    print("Printer category is not available")
```

## Adding and Removing Items

Use `.add()` to add one item.

```python
cart_items = {"laptop", "mouse"}

cart_items.add("keyboard")
print(cart_items)
```

Use `.remove()` when the item must exist. It raises `KeyError` if the item is missing.

```python
cart_items = {"laptop", "mouse", "keyboard"}

cart_items.remove("mouse")
print(cart_items)
```

Use `.discard()` when the item may or may not exist.

```python
cart_items = {"laptop", "keyboard"}

cart_items.discard("monitor")  # No error even though monitor is missing
print(cart_items)
```

## Set Operations

Set operations are the main reason sets are useful in real projects.

### Union: All Items

`|` or `.union()` combines both sets.

```python
hardware_products = {"laptop", "mouse", "keyboard", "monitor"}
software_products = {"pdf-editor", "office-suite", "antivirus"}

all_products = hardware_products | software_products
print(all_products)
```

Use case: show all available product groups in the shopping system.

### Intersection: Common Items

`&` or `.intersection()` returns items present in both sets.

```python
wishlist = {"laptop", "monitor", "office-suite"}
cart = {"laptop", "mouse", "office-suite"}

already_in_cart = wishlist & cart
print(already_in_cart)
# {"laptop", "office-suite"}
```

Use case: tell the user which wishlist items are already in the cart.

### Difference: Items Missing From Another Set

`-` or `.difference()` returns items present in the first set but not the second.

```python
required_bundle = {"laptop", "mouse", "keyboard", "office-suite"}
cart = {"laptop", "mouse"}

missing_items = required_bundle - cart
print(missing_items)
# {"keyboard", "office-suite"}
```

Use case: recommend missing accessories or software for a complete office setup.

### Symmetric Difference: Items That Are Different

`^` or `.symmetric_difference()` returns items that are in either set, but not both.

```python
warehouse_a = {"laptop", "mouse", "monitor"}
warehouse_b = {"laptop", "keyboard", "monitor", "pdf-editor"}

different_stock = warehouse_a ^ warehouse_b
print(different_stock)
# {"mouse", "keyboard", "pdf-editor"}
```

Use case: compare two warehouses and find stock differences.

## Subset and Superset

Use `.issubset()` to check whether all required items exist in another set.

```python
required_for_office = {"laptop", "office-suite"}
customer_cart = {"laptop", "mouse", "office-suite", "pdf-editor"}

print(required_for_office.issubset(customer_cart))  # True
```

Use `.issuperset()` to check whether a set contains all items from another set.

```python
print(customer_cart.issuperset(required_for_office))  # True
```

## Frozen Set

A `frozenset` is an immutable set. You cannot add or remove items after creating it.

```python
allowed_subscription_plans = frozenset({"monthly", "yearly", "enterprise"})

print("monthly" in allowed_subscription_plans)  # True
```

Use `frozenset` when a group of values should not change.

## Common Interview Questions

### Why use a set instead of a list?

Use a set when you need **unique values** and fast membership checks.

```python
blocked_product_ids = {1001, 1002, 1003}

if 1002 in blocked_product_ids:
    print("Do not show this product")
```

A list is better when order and duplicates matter.

### Can a set contain duplicate values?

No. Duplicates are automatically removed.

```python
items = {"mouse", "mouse", "keyboard"}
print(items)
# {"mouse", "keyboard"}
```

### Can we access a set item using index?

No. Sets are unordered and do not support indexing.

```python
items = {"laptop", "mouse"}

# items[0]  # TypeError
```

### Can a set contain a list?

No. Set elements must be hashable. Lists are mutable and not hashable.

```python
# invalid_set = {["laptop", "mouse"]}  # TypeError

valid_set = {("laptop", "mouse")}
print(valid_set)
```

## Practice Problems

1. Remove duplicate product IDs from a list.
2. Find common products between wishlist and cart.
3. Find products available in warehouse A but not warehouse B.
4. Check whether a customer cart contains all products from a required office setup bundle.
5. Compare two subscription feature sets and find features that differ.

## See also

- [Python strings: core concepts](../strings/core-concepts.md)
- [Python interview questions](../interview-questions.md)
