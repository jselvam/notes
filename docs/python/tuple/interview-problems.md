# Python Tuple Interview Problems

Tuples appear in interviews when problems involve **fixed records**, **multiple return values**, **composite keys**, **safe grouping**, and **unpacking**.

## Interview Pattern: When to Think About Tuples

Use a tuple when the problem needs:

- fixed-size records
- immutable grouped values
- return multiple values
- dictionary keys made from multiple fields
- set items made from multiple fields
- easy swapping or unpacking

## 1. Unpack Product Record

### Problem

Given a product tuple, unpack it into variables.

```python
product = (101, "laptop", 999)
```

### Python Solution

```python
def unpack_product(product):
    product_id, name, price = product
    return product_id, name, price


print(unpack_product((101, "laptop", 999)))
```

### Complexity

- Time: **O(1)**
- Space: **O(1)**

### Interview Follow-up

If tuple size may vary, use extended unpacking.

```python
product_id, name, *extra = (101, "laptop", 999, "in-stock")
```

## 2. Swap Two Product Prices

### Problem

Swap two values without using a temporary variable.

### Python Solution

```python
def swap_prices(old_price, new_price):
    old_price, new_price = new_price, old_price
    return old_price, new_price


print(swap_prices(999, 899))
```

### Complexity

- Time: **O(1)**
- Space: **O(1)**

## 3. Return Min and Max Price

### Problem

Return both the minimum and maximum prices from a list.

### Python Solution

```python
def min_max_price(prices):
    if not prices:
        return None

    minimum = prices[0]
    maximum = prices[0]

    for price in prices[1:]:
        if price < minimum:
            minimum = price
        if price > maximum:
            maximum = price

    return minimum, maximum


lowest, highest = min_max_price([999, 25, 75, 199])
print(lowest, highest)
```

### Complexity

- Time: **O(n)**
- Space: **O(1)**

## 4. Use Tuple as Composite Dictionary Key

### Problem

Store inventory by both warehouse ID and product ID.

### Python Solution

```python
def get_stock(stock, warehouse_id, product_id):
    key = (warehouse_id, product_id)
    return stock.get(key, 0)


stock = {
    ("warehouse-a", 101): 25,
    ("warehouse-b", 101): 8,
}

print(get_stock(stock, "warehouse-a", 101))
```

### Complexity

- Time: **O(1)** average dictionary lookup
- Space: **O(1)** extra

### Interview Follow-up

Use tuple keys when multiple fields together identify a value.

## 5. Find Duplicate Product Records

### Problem

Given product records as tuples, find duplicate records.

### Optimized Approach

Use a set because tuples are hashable when their contents are hashable.

### Python Solution

```python
def duplicate_records(records):
    seen = set()
    duplicates = set()

    for record in records:
        if record in seen:
            duplicates.add(record)
        else:
            seen.add(record)

    return duplicates


records = [
    (101, "laptop"),
    (102, "mouse"),
    (101, "laptop"),
]

print(duplicate_records(records))
```

### Complexity

- Time: **O(n)** average
- Space: **O(n)**

## 6. Convert Product Lists to Tuples

### Problem

Convert mutable product rows into immutable records.

### Python Solution

```python
def freeze_records(rows):
    return [tuple(row) for row in rows]


rows = [[101, "laptop"], [102, "mouse"]]
print(freeze_records(rows))
```

### Complexity

- Time: **O(n * m)** for `n` rows of size `m`
- Space: **O(n * m)**

## 7. Sort Tuple Records by Price

### Problem

Sort product records where each record is `(product_id, name, price)`.

### Python Solution

```python
def sort_products_by_price(products):
    return sorted(products, key=lambda product: product[2])


products = [
    (101, "laptop", 999),
    (102, "mouse", 25),
    (103, "monitor", 199),
]

print(sort_products_by_price(products))
```

### Complexity

- Time: **O(n log n)**
- Space: **O(n)**

## 8. Group Unique Warehouse Locations

### Problem

Return unique `(warehouse, rack)` locations.

### Python Solution

```python
def unique_locations(locations):
    return set(locations)


locations = [
    ("warehouse-a", "rack-1"),
    ("warehouse-a", "rack-1"),
    ("warehouse-b", "rack-2"),
]

print(unique_locations(locations))
```

### Complexity

- Time: **O(n)** average
- Space: **O(n)**

## 9. Validate Tuple Size

### Problem

Check whether every product record has exactly three fields.

### Python Solution

```python
def all_records_valid(records):
    for record in records:
        if len(record) != 3:
            return False
    return True


print(all_records_valid([(101, "laptop", 999), (102, "mouse", 25)]))
```

### Complexity

- Time: **O(n)**
- Space: **O(1)**

## 10. Count Repeated Category Pairs

### Problem

Count repeated `(main_category, sub_category)` pairs.

### Python Solution

```python
from collections import Counter


def count_category_pairs(pairs):
    return Counter(pairs)


pairs = [
    ("hardware", "laptop"),
    ("hardware", "mouse"),
    ("hardware", "laptop"),
]

print(count_category_pairs(pairs))
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

## Summary: Tuple Patterns to Remember

| Pattern | Tuple idea | Example |
|---------|------------|---------|
| Fixed record | ordered immutable fields | `(id, name, price)` |
| Multiple return | return grouped values | `(min_price, max_price)` |
| Composite key | hashable tuple key | `(warehouse_id, product_id)` |
| Unique pair | tuple inside set | unique locations |
| Unpacking | assign fields clearly | `id, name, price = product` |
| Sorting records | key by tuple position | `product[2]` |

## See also

- [Python tuples: core concepts](core-concepts.md)
- [Python tuple methods](methods.md)
- [Python tuple FAQ](frequently-asked-questions.md)
- [Python list interview problems](../list/interview-problems.md)
