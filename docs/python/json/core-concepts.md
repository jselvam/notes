# Python JSON: Core Concepts

JSON stands for **JavaScript Object Notation**. It is a text format used to exchange structured data between systems.

In an online computer shopping system, JSON is commonly used for:

- API request and response bodies
- product catalog data
- cart payloads
- order events
- payment gateway responses
- configuration files

## JSON and Python Types

JSON data maps naturally to Python dictionaries, lists, strings, numbers, booleans, and `None`.

```python
product = {
    "id": 101,
    "name": "Laptop",
    "price": 999.99,
    "in_stock": True,
    "tags": ["hardware", "computer"],
    "warranty": None,
}
```

## Importing the JSON Module

Python provides JSON support through the built-in `json` module.

```python
import json
```

## Convert Python to JSON String

Use `json.dumps()`.

```python
import json

product = {"name": "Laptop", "price": 999.99, "in_stock": True}
json_text = json.dumps(product)

print(json_text)
```

## Convert JSON String to Python

Use `json.loads()`.

```python
import json

json_text = '{"name": "Mouse", "price": 25.5, "in_stock": true}'
product = json.loads(json_text)

print(product["name"])
```

## Read JSON From a File

Use `json.load()`.

```python
import json

with open("products.json", "r", encoding="utf-8") as file:
    products = json.load(file)

print(products)
```

## Write JSON to a File

Use `json.dump()`.

```python
import json

cart = {"items": ["laptop", "mouse"], "total": 1024.99}

with open("cart.json", "w", encoding="utf-8") as file:
    json.dump(cart, file, indent=2)
```

## JSON Type Mapping

| JSON | Python |
|------|--------|
| object | `dict` |
| array | `list` |
| string | `str` |
| number | `int` or `float` |
| true | `True` |
| false | `False` |
| null | `None` |

## Common Gotchas

### JSON uses lowercase booleans

JSON uses `true`, `false`, and `null`. Python uses `True`, `False`, and `None`.

### JSON keys must be strings

JSON object keys are strings. Python dictionaries can use other hashable keys, but JSON cannot.

### `loads()` vs `load()`

Use `loads()` for a JSON string and `load()` for a file object.

## Practice Problems

1. Convert a product dictionary into a JSON string.
2. Parse a cart JSON response and print the total.
3. Read products from `products.json`.
4. Write an order summary to `order.json`.
5. Explain the difference between `json.dumps()` and `json.dump()`.

## See also

- [Python JSON reference](json-reference.md)
- [Python JSON interview problems](interview-problems.md)
- [Python JSON FAQ](frequently-asked-questions.md)
- [Python dictionaries: core concepts](../dict/core-concepts.md)
