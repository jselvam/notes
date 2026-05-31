# Python File Handling Reference

## Quick Reference

| Task | Tool |
|------|------|
| read full text file | `file.read()` |
| read one line | `file.readline()` |
| read all lines | `file.readlines()` |
| iterate lines | `for line in file` |
| write text | `file.write()` |
| write many lines | `file.writelines()` |
| read CSV rows | `csv.reader`, `csv.DictReader` |
| write CSV rows | `csv.writer`, `csv.DictWriter` |
| read JSON file | `json.load()` |
| write JSON file | `json.dump()` |
| save Python object | `pickle.dump()` |
| load Python object | `pickle.load()` |

## File Modes

| Mode | Description |
|------|-------------|
| `r` | read only |
| `w` | write and overwrite |
| `a` | append |
| `x` | exclusive create |
| `rb` | read binary |
| `wb` | write binary |
| `r+` | read and write |

## Text File Read Patterns

```python
with open("inventory.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

```python
with open("inventory.txt", "r", encoding="utf-8") as file:
    for line in file:
        sku = line.strip()
        print(sku)
```

## Text File Write Patterns

```python
with open("inventory.txt", "w", encoding="utf-8") as file:
    file.write("LAP-101\n")
    file.write("MOU-201\n")
```

Append without deleting existing content:

```python
with open("inventory.txt", "a", encoding="utf-8") as file:
    file.write("KEY-301\n")
```

## CSV Reader

```python
import csv

with open("products.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

## CSV DictReader

```python
import csv

with open("products.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["sku"], row["name"])
```

## CSV DictWriter

```python
import csv

rows = [
    {"sku": "LAP-101", "name": "Laptop", "stock": 5},
    {"sku": "MOU-201", "name": "Mouse", "stock": 20},
]

with open("inventory.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["sku", "name", "stock"])
    writer.writeheader()
    writer.writerows(rows)
```

## JSON Dump and Load

```python
import json

data = {"sku": "LAP-101", "price": 999.99}

with open("product.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2)

with open("product.json", "r", encoding="utf-8") as file:
    product = json.load(file)
```

## JSON String vs JSON File

| Function | Input |
|----------|-------|
| `json.loads()` | JSON string |
| `json.load()` | file object |
| `json.dumps()` | Python object to JSON string |
| `json.dump()` | Python object to JSON file |

## Pickle Dump and Load

```python
import pickle

cart = {"items": ["Laptop"], "total": 999.99}

with open("cart.pkl", "wb") as file:
    pickle.dump(cart, file)

with open("cart.pkl", "rb") as file:
    loaded_cart = pickle.load(file)
```

## Common Exceptions

| Exception | Common cause |
|-----------|--------------|
| `FileNotFoundError` | reading missing file |
| `PermissionError` | no permission to read/write |
| `IsADirectoryError` | path points to directory |
| `UnicodeDecodeError` | wrong text encoding |
| `json.JSONDecodeError` | invalid JSON |
| `csv.Error` | malformed CSV usage |
| `pickle.UnpicklingError` | invalid pickle data |

## Best Practices

- Use `with open(...)` for automatic closing.
- Specify `encoding="utf-8"` for text files.
- Use `newline=""` for CSV files.
- Use JSON for portable data.
- Use Pickle only for trusted Python-only data.
- Handle expected file exceptions.
- Do not hardcode sensitive file paths.

## See also

- [File handling: core concepts](core-concepts.md)
- [File handling interview problems](interview-problems.md)
- [File handling FAQ](frequently-asked-questions.md)
- [Python JSON](../json/core-concepts.md)
