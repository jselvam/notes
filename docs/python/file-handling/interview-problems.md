# Python File Handling Interview Problems

## 1. Read a Product Text File

### Problem

Read product names from a text file and print them without extra spaces.

```python
with open("products.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

### Complexity

`O(n)` time where `n` is the file size.

## 2. Write Product Names to a File

```python
products = ["Laptop", "Mouse", "Keyboard"]

with open("products.txt", "w", encoding="utf-8") as file:
    for product in products:
        file.write(product + "\n")
```

Use `w` when you want to replace the file content.

## 3. Append an Order Log

```python
order_id = 1001

with open("orders.log", "a", encoding="utf-8") as file:
    file.write(f"Order {order_id} placed\n")
```

Use `a` for logs because old entries should remain.

## 4. Count Lines in a File

```python
count = 0

with open("orders.log", "r", encoding="utf-8") as file:
    for _ in file:
        count += 1

print(count)
```

This reads line by line and avoids loading the entire file into memory.

## 5. Read Product CSV With `DictReader`

```python
import csv

with open("products.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["sku"], row["name"], float(row["price"]))
```

CSV values are strings, so convert numbers when needed.

## 6. Write Inventory CSV

```python
import csv

inventory = [
    {"sku": "LAP-101", "stock": 5},
    {"sku": "MOU-201", "stock": 20},
]

with open("inventory.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["sku", "stock"])
    writer.writeheader()
    writer.writerows(inventory)
```

## 7. Read JSON Order File

```python
import json

with open("order.json", "r", encoding="utf-8") as file:
    order = json.load(file)

print(order["order_id"])
```

Use `json.load()` for file objects.

## 8. Write JSON Order File

```python
import json

order = {"order_id": 1001, "items": ["Laptop", "Mouse"]}

with open("order.json", "w", encoding="utf-8") as file:
    json.dump(order, file, indent=2)
```

## 9. Save and Load Cart With Pickle

```python
import pickle

cart = {"items": ["Laptop"], "total": 999.99}

with open("cart.pkl", "wb") as file:
    pickle.dump(cart, file)

with open("cart.pkl", "rb") as file:
    loaded_cart = pickle.load(file)
```

Only unpickle trusted files.

## 10. Handle Missing File

```python
try:
    with open("missing-products.txt", "r", encoding="utf-8") as file:
        data = file.read()
except FileNotFoundError:
    data = ""

print(data)
```

## 11. Convert CSV Rows to Dictionaries

```python
import csv

products = {}

with open("products.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        products[row["sku"]] = {
            "name": row["name"],
            "price": float(row["price"]),
        }
```

## 12. Choose CSV, JSON, or Pickle

| Need | Format |
|------|--------|
| spreadsheet-style product export | CSV |
| nested API-style order data | JSON |
| trusted Python object cache | Pickle |

## Summary

Use text files for simple lines, CSV for tables, JSON for portable structured data, and Pickle for trusted Python-specific object storage.

## See also

- [File handling: core concepts](core-concepts.md)
- [File handling reference](file-handling-reference.md)
- [File handling FAQ](frequently-asked-questions.md)
- [Exception handling](../exception-handling/core-concepts.md)
