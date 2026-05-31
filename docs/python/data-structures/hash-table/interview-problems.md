# Hash Table: Interview Problems

This page contains **20 interview problems** for hash tables in Python.

These avoid duplicate classic problems already used elsewhere in the Python notes, such as Two Sum, anagram check, generic frequency count, remove duplicates, and duplicate detection.

## 1. Build SKU to Product Lookup

### Problem

Create a dictionary that maps SKU to product details.

### Solution

```python
products = [
    {"sku": "LAP-101", "name": "Laptop", "price": 999},
    {"sku": "MOU-201", "name": "Mouse", "price": 25},
]

lookup = {product["sku"]: product for product in products}

print(lookup["LAP-101"]["name"])
```

Output:

```text
Laptop
```

## 2. Find Missing Product Details

### Problem

Given requested SKUs, return SKUs not present in the catalog.

### Solution

```python
catalog = {"LAP-101": "Laptop", "MOU-201": "Mouse"}
requested = ["LAP-101", "KEY-301", "MOU-201", "MON-401"]

missing = [sku for sku in requested if sku not in catalog]

print(missing)
```

Output:

```text
['KEY-301', 'MON-401']
```

## 3. Map Customer to Latest Order

### Problem

Store only the latest order ID for each customer.

### Solution

```python
orders = [
    {"customer": "Anu", "order_id": 1001},
    {"customer": "Ravi", "order_id": 1002},
    {"customer": "Anu", "order_id": 1003},
]

latest = {}
for order in orders:
    latest[order["customer"]] = order["order_id"]

print(latest)
```

Output:

```text
{'Anu': 1003, 'Ravi': 1002}
```

## 4. Group Products by Category

### Problem

Group product names by their category.

### Solution

```python
products = [
    {"name": "Laptop", "category": "computer"},
    {"name": "Mouse", "category": "accessory"},
    {"name": "Keyboard", "category": "accessory"},
]

groups = {}
for product in products:
    groups.setdefault(product["category"], []).append(product["name"])

print(groups)
```

Output:

```text
{'computer': ['Laptop'], 'accessory': ['Mouse', 'Keyboard']}
```

## 5. Build Inventory by Warehouse

### Problem

Use a tuple key `(sku, warehouse)` to store stock.

### Solution

```python
stock_rows = [
    ("LAP-101", "WH-1", 5),
    ("LAP-101", "WH-2", 3),
    ("MOU-201", "WH-1", 20),
]

inventory = {}
for sku, warehouse, count in stock_rows:
    inventory[(sku, warehouse)] = count

print(inventory[("LAP-101", "WH-2")])
```

Output:

```text
3
```

## 6. Find Products Below Reorder Level

### Problem

Given stock and reorder limits, find products that need restocking.

### Solution

```python
stock = {"LAP-101": 3, "MOU-201": 20, "KEY-301": 2}
reorder_level = {"LAP-101": 5, "MOU-201": 10, "KEY-301": 5}

needs_restock = []
for sku, count in stock.items():
    if count < reorder_level.get(sku, 0):
        needs_restock.append(sku)

print(needs_restock)
```

Output:

```text
['LAP-101', 'KEY-301']
```

## 7. Validate Coupon Code

### Problem

Check whether a coupon exists and return its discount.

### Solution

```python
coupons = {
    "WELCOME10": 10,
    "FESTIVAL20": 20,
}

code = "FESTIVAL20"
discount = coupons.get(code, 0)

print(discount)
```

Output:

```text
20
```

## 8. Convert Product List to Price Map

### Problem

Convert a product list into a map of SKU to price.

### Solution

```python
products = [
    {"sku": "LAP-101", "price": 999},
    {"sku": "MOU-201", "price": 25},
]

prices = {product["sku"]: product["price"] for product in products}

print(prices)
```

Output:

```text
{'LAP-101': 999, 'MOU-201': 25}
```

## 9. Detect Price Changes Between Two Catalogs

### Problem

Compare old and new price maps and list changed SKUs.

### Solution

```python
old_prices = {"LAP-101": 999, "MOU-201": 25}
new_prices = {"LAP-101": 899, "MOU-201": 25, "KEY-301": 75}

changed = []
for sku, new_price in new_prices.items():
    if sku in old_prices and old_prices[sku] != new_price:
        changed.append(sku)

print(changed)
```

Output:

```text
['LAP-101']
```

## 10. Merge Stock From Multiple Warehouses

### Problem

Combine stock counts from different warehouses by SKU.

### Solution

```python
warehouse_a = {"LAP-101": 5, "MOU-201": 10}
warehouse_b = {"LAP-101": 3, "KEY-301": 7}

total_stock = {}
for stock_map in [warehouse_a, warehouse_b]:
    for sku, count in stock_map.items():
        total_stock[sku] = total_stock.get(sku, 0) + count

print(total_stock)
```

Output:

```text
{'LAP-101': 8, 'MOU-201': 10, 'KEY-301': 7}
```

## 11. Find First Repeated Order Status

### Problem

Return the first status that appears again in a status stream.

### Solution

```python
statuses = ["created", "paid", "packed", "paid", "shipped"]
seen = set()
first_repeated = None

for status in statuses:
    if status in seen:
        first_repeated = status
        break
    seen.add(status)

print(first_repeated)
```

Output:

```text
paid
```

## 12. Create Session Token Lookup

### Problem

Map session tokens to user IDs and validate a token.

### Solution

```python
sessions = {
    "tok_abc": 101,
    "tok_xyz": 102,
}

token = "tok_abc"
user_id = sessions.get(token)

print(user_id)
```

Output:

```text
101
```

## 13. Find Orders for a Customer

### Problem

Group order IDs by customer ID.

### Solution

```python
orders = [
    {"customer_id": 1, "order_id": 1001},
    {"customer_id": 2, "order_id": 1002},
    {"customer_id": 1, "order_id": 1003},
]

orders_by_customer = {}
for order in orders:
    orders_by_customer.setdefault(order["customer_id"], []).append(order["order_id"])

print(orders_by_customer[1])
```

Output:

```text
[1001, 1003]
```

## 14. Build Product Rank Map

### Problem

Map each product SKU to its rank in a sorted bestseller list.

### Solution

```python
bestsellers = ["LAP-101", "MOU-201", "KEY-301"]
rank = {sku: index + 1 for index, sku in enumerate(bestsellers)}

print(rank["MOU-201"])
```

Output:

```text
2
```

## 15. Find Common SKUs Across Two Warehouses

### Problem

Return SKUs available in both warehouses.

### Solution

```python
warehouse_a = {"LAP-101": 5, "MOU-201": 10}
warehouse_b = {"LAP-101": 3, "KEY-301": 7}

common = [sku for sku in warehouse_a if sku in warehouse_b]

print(common)
```

Output:

```text
['LAP-101']
```

## 16. Replace Product IDs With Names

### Problem

Given order product IDs, replace each ID with its product name.

### Solution

```python
product_names = {
    101: "Laptop",
    201: "Mouse",
    301: "Keyboard",
}

order_items = [101, 301, 201]
names = [product_names[item_id] for item_id in order_items]

print(names)
```

Output:

```text
['Laptop', 'Keyboard', 'Mouse']
```

## 17. Find Unmapped Product IDs

### Problem

Find product IDs in an order that are missing from the product map.

### Solution

```python
product_names = {
    101: "Laptop",
    201: "Mouse",
}

order_items = [101, 301, 201, 401]
missing = [item_id for item_id in order_items if item_id not in product_names]

print(missing)
```

Output:

```text
[301, 401]
```

## 18. Cache Shipping Rate by Pincode

### Problem

Avoid recalculating shipping rate for the same pincode.

### Solution

```python
cache = {}


def get_shipping_rate(pincode):
    if pincode not in cache:
        cache[pincode] = len(pincode) * 10
    return cache[pincode]


print(get_shipping_rate("600001"))
print(get_shipping_rate("600001"))
print(cache)
```

Output:

```text
60
60
{'600001': 60}
```

## 19. Find Highest Stock Product Per Category

### Problem

For each category, store the product with highest stock.

### Solution

```python
products = [
    {"name": "Laptop", "category": "computer", "stock": 5},
    {"name": "Monitor", "category": "computer", "stock": 9},
    {"name": "Mouse", "category": "accessory", "stock": 30},
]

best = {}
for product in products:
    category = product["category"]
    if category not in best or product["stock"] > best[category]["stock"]:
        best[category] = product

print({category: product["name"] for category, product in best.items()})
```

Output:

```text
{'computer': 'Monitor', 'accessory': 'Mouse'}
```

## 20. Implement a Simple Hash Table

### Problem

Implement a small hash table with separate chaining.

### Solution

```python
class SimpleHashTable:
    def __init__(self, size=5):
        self.buckets = [[] for _ in range(size)]

    def _index(self, key):
        return hash(key) % len(self.buckets)

    def set(self, key, value):
        bucket = self.buckets[self._index(key)]
        for index, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[index] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        bucket = self.buckets[self._index(key)]
        for existing_key, value in bucket:
            if existing_key == key:
                return value
        return None


table = SimpleHashTable()
table.set("LAP-101", "Laptop")
table.set("MOU-201", "Mouse")
print(table.get("LAP-101"))
print(table.get("KEY-301"))
```

Output:

```text
Laptop
None
```

## Final Notes

- Hash tables are best when lookup speed matters.
- Python `dict` and `set` are hash-table based.
- Use hashable keys.
- Use `.get()` for optional keys.
- Mention average `O(1)` lookup in interviews.
