# Python File Handling: Core Concepts

File handling means reading data from files and writing data back to files. Python commonly works with text files, CSV files, JSON files, and binary files such as Pickle files.

This page covers:

- reading and writing files
- file modes
- CSV files
- JSON files
- Pickle files

Examples use an online computer shopping system.

## Why File Handling Matters

Applications often store and exchange data using files:

- product catalogs
- inventory exports
- order reports
- customer support logs
- JSON API payloads
- cached Python objects

## Opening Files

Use `open()` to work with files.

```python
file = open("products.txt", "r", encoding="utf-8")
content = file.read()
file.close()
```

The safer pattern is `with`, because it closes the file automatically.

```python
with open("products.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

## Common File Modes

| Mode | Meaning |
|------|---------|
| `r` | read existing file |
| `w` | write new content, overwrite existing file |
| `a` | append to end of file |
| `x` | create new file, fail if it exists |
| `b` | binary mode |
| `t` | text mode, default |
| `+` | read and write |

## Reading Text Files

```python
with open("products.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

Use this for simple logs, notes, and line-based reports.

## Writing Text Files

```python
products = ["Laptop", "Mouse", "Keyboard"]

with open("products.txt", "w", encoding="utf-8") as file:
    for product in products:
        file.write(product + "\n")
```

`w` overwrites the file. Use `a` to append.

## CSV Files

CSV is useful for tabular data such as inventory or product exports.

```python
import csv

products = [
    {"sku": "LAP-101", "name": "Laptop", "price": 999.99},
    {"sku": "MOU-201", "name": "Mouse", "price": 25.50},
]

with open("products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["sku", "name", "price"])
    writer.writeheader()
    writer.writerows(products)
```

Use `newline=""` with CSV files to avoid extra blank lines on some platforms.

## Reading CSV Files

```python
import csv

with open("products.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["sku"], row["name"], row["price"])
```

CSV values are read as strings by default.

## JSON Files

JSON is useful for structured data such as API payloads, configuration, and nested order data.

```python
import json

order = {
    "order_id": 1001,
    "customer": "Anu",
    "items": ["Laptop", "Mouse"],
}

with open("order.json", "w", encoding="utf-8") as file:
    json.dump(order, file, indent=2)
```

## Reading JSON Files

```python
import json

with open("order.json", "r", encoding="utf-8") as file:
    order = json.load(file)

print(order["order_id"])
```

Use `json.load()` for files and `json.loads()` for strings.

## Pickle Files

Pickle stores Python objects in binary format.

```python
import pickle

cart = {"items": ["Laptop", "Mouse"], "total": 1025.49}

with open("cart.pkl", "wb") as file:
    pickle.dump(cart, file)
```

Read it back with `pickle.load()`.

```python
import pickle

with open("cart.pkl", "rb") as file:
    cart = pickle.load(file)
```

## Pickle Security Warning

Never unpickle data from an untrusted source. Pickle can execute code during loading.

Use JSON for safe data exchange. Use Pickle only for trusted Python-only data.

## Common Gotchas

### Forgetting to close files

Use `with open(...)` to close files automatically.

### Confusing `json.load()` and `json.loads()`

`load()` reads from a file object. `loads()` reads from a string.

### Reading CSV numbers as strings

Convert values manually:

```python
price = float(row["price"])
```

### Using Pickle for public APIs

Pickle is Python-specific and unsafe for untrusted input.

## See also

- [File handling reference](file-handling-reference.md)
- [File handling interview problems](interview-problems.md)
- [File handling FAQ](frequently-asked-questions.md)
- [Python JSON](../json/core-concepts.md)
- [Exception handling](../exception-handling/core-concepts.md)
