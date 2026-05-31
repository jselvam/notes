# Python Set Methods: Interview Notes

Python `set` methods are useful when interview problems involve **unique values**, **fast lookup**, **duplicates**, **common elements**, or **missing elements**.

Use a set when you want average **O(1)** membership checks:

```python
blocked_product_ids = {101, 205, 309}

print(205 in blocked_product_ids)  # True
```

## Quick Method Table

| Method | What it does | Interview use case |
|--------|--------------|--------------------|
| `add()` | Adds one item | Add one product/category |
| `update()` | Adds many items | Merge imported IDs |
| `remove()` | Removes item, errors if missing | Strict delete |
| `discard()` | Removes item, no error if missing | Safe delete |
| `pop()` | Removes random item | Usually avoid in interview logic |
| `clear()` | Removes all items | Reset state |
| `copy()` | Shallow copy | Preserve original set |
| `union()` / `|` | All unique items | Combine catalogs |
| `intersection()` / `&` | Common items | Cart and wishlist overlap |
| `difference()` / `-` | Items in first, not second | Missing items |
| `symmetric_difference()` / `^` | Items not common | Compare two warehouses |
| `issubset()` | All items exist in another set | Bundle validation |
| `issuperset()` | Contains all items from another set | Cart contains required items |
| `isdisjoint()` | No common items | No category overlap |

## `add()`

Adds a single item to the set.

```python
categories = {"laptop", "mouse"}

categories.add("keyboard")
categories.add("mouse")  # duplicate, no effect

print(categories)
```

### Interview point

Use `add()` with a `seen` set when scanning input.

```python
def has_duplicate_product_id(product_ids):
    seen = set()

    for product_id in product_ids:
        if product_id in seen:
            return True
        seen.add(product_id)

    return False
```

## `update()`

Adds multiple items from another iterable.

```python
hardware = {"laptop", "mouse"}
new_arrivals = ["keyboard", "monitor", "mouse"]

hardware.update(new_arrivals)

print(hardware)
# {"laptop", "mouse", "keyboard", "monitor"}
```

### Interview point

Use `update()` when merging many values into the same set. It modifies the original set.

```python
warehouse_product_ids = {101, 102}
imported_product_ids = [103, 104, 101]

warehouse_product_ids.update(imported_product_ids)

print(warehouse_product_ids)
# {101, 102, 103, 104}
```

## `remove()`

Removes an item. Raises `KeyError` if the item does not exist.

```python
cart_items = {"laptop", "mouse", "keyboard"}

cart_items.remove("mouse")

print(cart_items)
```

### Interview point

Use `remove()` when missing data should be treated as a bug.

```python
active_coupon_codes = {"SAVE10", "OFFICE20"}

active_coupon_codes.remove("SAVE10")
# active_coupon_codes.remove("UNKNOWN")  # KeyError
```

## `discard()`

Removes an item if it exists. Does **not** raise an error if the item is missing.

```python
cart_items = {"laptop", "keyboard"}

cart_items.discard("mouse")

print(cart_items)
# {"laptop", "keyboard"}
```

### Interview point

Use `discard()` when deleting should be safe even if the item is absent.

```python
def remove_item_from_cart(cart_items, item):
    cart_items.discard(item)
    return cart_items
```

## `pop()`

Removes and returns an arbitrary item.

```python
items_to_review = {"laptop", "mouse", "monitor"}

item = items_to_review.pop()
print(item)
print(items_to_review)
```

### Interview point

Sets are unordered, so do not use `pop()` when you need the first, last, smallest, or largest item.

## `clear()`

Removes all items.

```python
temporary_import_ids = {101, 102, 103}

temporary_import_ids.clear()

print(temporary_import_ids)
# set()
```

### Interview point

Useful for resetting state between test cases.

## `copy()`

Creates a shallow copy.

```python
original_categories = {"laptop", "mouse", "keyboard"}
backup_categories = original_categories.copy()

backup_categories.add("monitor")

print(original_categories)
print(backup_categories)
```

### Interview point

Use `copy()` when you want to try changes without modifying the original set.

## `union()` or `|`

Returns all unique items from both sets.

```python
hardware = {"laptop", "mouse", "keyboard"}
software = {"pdf-editor", "office-suite", "antivirus"}

all_products = hardware.union(software)

print(all_products)
```

Prefer writing the normal form:

```python
all_products = hardware.union(software)
# or
all_products = hardware | software
```

### Interview point

Use union when the question asks for “all unique values from two groups”.

```python
def all_unique_products(catalog_a, catalog_b):
    return set(catalog_a) | set(catalog_b)
```

## `intersection()` or `&`

Returns common items.

```python
cart = {"laptop", "mouse", "office-suite"}
wishlist = {"monitor", "laptop", "office-suite"}

common_items = cart.intersection(wishlist)

print(common_items)
# {"laptop", "office-suite"}
```

### Interview point

Use intersection for overlap problems.

```python
def has_any_common_item(group_a, group_b):
    return len(set(group_a) & set(group_b)) > 0
```

## `intersection_update()`

Keeps only common items and modifies the original set.

```python
cart = {"laptop", "mouse", "office-suite"}
wishlist = {"laptop", "monitor", "office-suite"}

cart.intersection_update(wishlist)

print(cart)
# {"laptop", "office-suite"}
```

### Interview point

Use update-style methods only when mutation is acceptable. Otherwise use `intersection()`.

## `difference()` or `-`

Returns items in the first set that are not in the second.

```python
required_bundle = {"laptop", "mouse", "keyboard", "office-suite"}
cart = {"laptop", "mouse"}

missing_items = required_bundle.difference(cart)

print(missing_items)
# {"keyboard", "office-suite"}
```

### Interview point

Use difference for missing-item and validation problems.

```python
def missing_required_items(required_items, existing_items):
    return set(required_items) - set(existing_items)
```

## `difference_update()`

Removes items from the original set that are present in another set.

```python
available_products = {"laptop", "mouse", "keyboard", "monitor"}
out_of_stock = {"mouse", "monitor"}

available_products.difference_update(out_of_stock)

print(available_products)
# {"laptop", "keyboard"}
```

### Interview point

Use when the original set should be changed in place.

## `symmetric_difference()` or `^`

Returns items that are in either set, but not in both.

```python
warehouse_a = {"laptop", "mouse", "monitor"}
warehouse_b = {"laptop", "keyboard", "monitor", "pdf-editor"}

different_items = warehouse_a.symmetric_difference(warehouse_b)

print(different_items)
# {"mouse", "keyboard", "pdf-editor"}
```

### Interview point

Use symmetric difference when comparing two groups and asking “what is different between them?”

## `symmetric_difference_update()`

Updates the original set with items that are not common.

```python
warehouse_a = {"laptop", "mouse", "monitor"}
warehouse_b = {"laptop", "keyboard", "monitor", "pdf-editor"}

warehouse_a.symmetric_difference_update(warehouse_b)

print(warehouse_a)
# {"mouse", "keyboard", "pdf-editor"}
```

### Interview point

This mutates the first set. In interviews, mention mutation clearly.

## `issubset()`

Returns `True` if every item in one set exists in another set.

```python
required = {"laptop", "office-suite"}
cart = {"laptop", "mouse", "office-suite", "pdf-editor"}

print(required.issubset(cart))
# True
```

### Interview point

Use this for “does this group contain all required items?” problems.

```python
def can_place_order(required_items, cart_items):
    return set(required_items).issubset(set(cart_items))
```

## `issuperset()`

Returns `True` if a set contains all items from another set.

```python
cart = {"laptop", "mouse", "office-suite", "pdf-editor"}
required = {"laptop", "office-suite"}

print(cart.issuperset(required))
# True
```

### Interview point

`a.issuperset(b)` means `a` has everything from `b`.

## `isdisjoint()`

Returns `True` if two sets have no common items.

```python
subscription_features = {"cloud-storage", "priority-support"}
hardware_items = {"laptop", "mouse", "keyboard"}

print(subscription_features.isdisjoint(hardware_items))
# True
```

### Interview point

Use `isdisjoint()` when you only need to know whether overlap exists.

```python
def has_no_blocked_products(cart_product_ids, blocked_product_ids):
    return set(cart_product_ids).isdisjoint(set(blocked_product_ids))
```

## Common Interview Questions

### What is the time complexity of checking if an item exists in a set?

Average case is **O(1)**.

```python
product_ids = {101, 102, 103}
print(102 in product_ids)  # O(1) average
```

Worst case can degrade because of hash collisions, but interview answers usually mention average **O(1)**.

### What is the difference between `remove()` and `discard()`?

`remove()` raises `KeyError` if the item is missing. `discard()` does not.

```python
items = {"laptop"}

items.discard("mouse")  # no error
# items.remove("mouse")  # KeyError
```

### What is the difference between `update()` and `union()`?

`update()` modifies the original set. `union()` returns a new set.

```python
a = {"laptop"}
b = {"mouse"}

c = a.union(b)
print(a)  # {"laptop"}
print(c)  # {"laptop", "mouse"}

a.update(b)
print(a)  # {"laptop", "mouse"}
```

### What is the difference between `difference()` and `symmetric_difference()`?

`difference()` returns values from the first set that are not in the second.

`symmetric_difference()` returns values that are different across both sets.

```python
a = {"laptop", "mouse"}
b = {"mouse", "keyboard"}

print(a.difference(b))             # {"laptop"}
print(a.symmetric_difference(b))   # {"laptop", "keyboard"}
```

### Why can a tuple be in a set but a list cannot?

Set elements must be **hashable**. Tuples are hashable if their contents are hashable. Lists are mutable and not hashable.

```python
valid = {("laptop", 101)}
print(valid)

# invalid = {["laptop", 101]}  # TypeError
```

### When should you not use a set?

Do not use a set when:

- order matters
- duplicate counts matter
- you need indexing
- you need to map keys to values

Use a `list` for order, `collections.Counter` for counts, and `dict` for key-value lookup.

## Practice Problems

1. Given imported product IDs, remove duplicates but preserve original order.
2. Given cart and wishlist, find common products.
3. Given required bundle items and cart items, find missing items.
4. Given two warehouses, find products that differ between them.
5. Given cart product IDs and blocked product IDs, check whether the cart is valid.
6. Given product numbers, find the longest consecutive product number sequence.
7. Given coupon codes, detect the first repeated code.
8. Given subscription features, check whether a plan includes all required features.

## See also

- [Python sets: core concepts](core-concepts.md)
- [Python set interview problems](interview-problems.md)
- [Python interview questions](../interview-questions.md)
