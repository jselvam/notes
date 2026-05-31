# Python Dictionary Interview Problems

Dictionaries are the main Python tool for **fast key lookup**, **frequency counting**, **index mapping**, **grouping**, and **caching**.

## Interview Pattern: When to Think About Dictionaries

Use a dictionary when the problem needs:

- lookup by key
- counts or frequencies
- mapping values to indices
- grouping values
- caching repeated work
- composite keys
- storing relationships

## 1. Count Products in Cart

### Problem

Count how many times each product appears in a cart.

```python
cart = ["mouse", "laptop", "mouse", "keyboard"]
```

### Optimized Approach

Use a dictionary where key is product name and value is count.

### Python Solution

```python
def count_products(cart):
    counts = {}

    for product in cart:
        counts[product] = counts.get(product, 0) + 1

    return counts


print(count_products(["mouse", "laptop", "mouse", "keyboard"]))
```

### Complexity

- Time: **O(n)**
- Space: **O(k)** where `k` is number of unique products

## 2. Two Sum Return Indices

### Problem

Given prices and a target, return indices of two prices that add up to the target.

### Optimized Approach

Use a dictionary mapping price to index.

### Python Solution

```python
def two_sum_indices(prices, target):
    seen = {}

    for index, price in enumerate(prices):
        needed = target - price

        if needed in seen:
            return [seen[needed], index]

        seen[price] = index

    return []


print(two_sum_indices([499, 129, 99], 628))
# [0, 1]
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

### Interview Follow-up

Use a set if only existence is needed. Use a dictionary when indices are needed.

## 3. First Non-Repeating Product Code

### Problem

Find the first product code that appears only once.

### Python Solution

```python
def first_non_repeating_code(codes):
    counts = {}

    for code in codes:
        counts[code] = counts.get(code, 0) + 1

    for code in codes:
        if counts[code] == 1:
            return code

    return None


print(first_non_repeating_code(["A", "B", "A", "C", "B"]))
# C
```

### Complexity

- Time: **O(n)**
- Space: **O(k)**

## 4. Group Products by Category

### Problem

Group product names by category.

### Python Solution

```python
def group_by_category(products):
    groups = {}

    for name, category in products:
        groups.setdefault(category, []).append(name)

    return groups


products = [
    ("laptop", "hardware"),
    ("mouse", "hardware"),
    ("office-suite", "software"),
]

print(group_by_category(products))
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

## 5. Build Product Lookup by ID

### Problem

Convert a list of product dictionaries into a lookup by product ID.

### Python Solution

```python
def build_product_lookup(products):
    lookup = {}

    for product in products:
        lookup[product["id"]] = product

    return lookup


products = [
    {"id": 101, "name": "laptop"},
    {"id": 102, "name": "mouse"},
]

print(build_product_lookup(products)[101])
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

## 6. Find Duplicate Product IDs

### Problem

Find product IDs that appear more than once.

### Python Solution

```python
def duplicate_product_ids(product_ids):
    counts = {}
    duplicates = []

    for product_id in product_ids:
        counts[product_id] = counts.get(product_id, 0) + 1

    for product_id, count in counts.items():
        if count > 1:
            duplicates.append(product_id)

    return duplicates


print(duplicate_product_ids([101, 102, 101, 103, 102]))
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

## 7. Merge Product Price Maps

### Problem

Merge old and new price maps. New prices should override old prices.

### Python Solution

```python
def merge_prices(old_prices, new_prices):
    merged = old_prices.copy()
    merged.update(new_prices)
    return merged


old_prices = {"laptop": 999, "mouse": 25}
new_prices = {"laptop": 899, "keyboard": 75}

print(merge_prices(old_prices, new_prices))
```

### Complexity

- Time: **O(n + m)**
- Space: **O(n + m)**

## 8. Inventory Lookup With Composite Key

### Problem

Find stock using both warehouse ID and product ID.

### Python Solution

```python
def get_stock(stock, warehouse_id, product_id):
    return stock.get((warehouse_id, product_id), 0)


stock = {
    ("warehouse-a", 101): 25,
    ("warehouse-b", 101): 8,
}

print(get_stock(stock, "warehouse-b", 101))
```

### Complexity

- Time: **O(1)** average
- Space: **O(1)** extra

## 9. Cache Expensive Product Calculation

### Problem

Avoid repeated expensive calculation for the same product ID.

### Python Solution

```python
def calculate_score(product_id):
    return product_id * 10


def get_score(product_id, cache):
    if product_id not in cache:
        cache[product_id] = calculate_score(product_id)
    return cache[product_id]


cache = {}
print(get_score(101, cache))
print(get_score(101, cache))
```

### Complexity

- First lookup: depends on calculation
- Repeated lookup: **O(1)** average

## 10. Compare Two Product Dictionaries

### Problem

Find changed prices between two dictionaries.

### Python Solution

```python
def changed_prices(old_prices, new_prices):
    changes = {}

    for product, new_price in new_prices.items():
        old_price = old_prices.get(product)
        if old_price is not None and old_price != new_price:
            changes[product] = (old_price, new_price)

    return changes


old_prices = {"laptop": 999, "mouse": 25}
new_prices = {"laptop": 899, "mouse": 25}

print(changed_prices(old_prices, new_prices))
```

### Complexity

- Time: **O(n)**
- Space: **O(k)** for changed items

## Summary: Dictionary Patterns to Remember

| Pattern | Dictionary idea | Example |
|---------|-----------------|---------|
| Frequency count | value -> count | cart product counts |
| Index map | value -> index | Two Sum indices |
| Grouping | category -> list | products by category |
| Lookup table | id -> record | product lookup |
| Cache | input -> output | expensive calculation |
| Composite key | tuple -> value | warehouse stock |
| Diff map | key -> change | changed prices |

## See also

- [Python dictionaries: core concepts](core-concepts.md)
- [Python dictionary methods](methods.md)
- [Python dictionary FAQ](frequently-asked-questions.md)
- [Python tuple interview problems](../tuple/interview-problems.md)
