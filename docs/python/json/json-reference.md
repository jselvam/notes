# Python JSON Reference

## Quick Table

| Function | Use case | Input | Output |
|----------|----------|-------|--------|
| `json.dumps()` | Python object to JSON string | `dict`, `list` | `str` |
| `json.loads()` | JSON string to Python object | `str` | `dict`, `list`, etc. |
| `json.dump()` | Python object to JSON file | object + file | writes file |
| `json.load()` | JSON file to Python object | file | Python object |

## `json.dumps()`

```python
import json

product = {"name": "Laptop", "price": 999.99}
json_text = json.dumps(product)

print(json_text)
```

## Pretty JSON With `indent`

```python
import json

product = {"name": "Laptop", "price": 999.99, "tags": ["hardware", "computer"]}

print(json.dumps(product, indent=2))
```

## Preserve Non-ASCII Text

```python
import json

product = {"name": "Café Keyboard"}

print(json.dumps(product, ensure_ascii=False))
```

## Sort Keys

```python
import json

product = {"price": 999.99, "name": "Laptop"}

print(json.dumps(product, sort_keys=True))
```

## `json.loads()`

```python
import json

response = '{"order_id": 501, "paid": true}'
order = json.loads(response)

print(order["paid"])
```

## `json.dump()`

```python
import json

order = {"order_id": 501, "items": ["laptop", "mouse"]}

with open("order.json", "w", encoding="utf-8") as file:
    json.dump(order, file, indent=2)
```

## `json.load()`

```python
import json

with open("order.json", "r", encoding="utf-8") as file:
    order = json.load(file)

print(order["order_id"])
```

## Handle Invalid JSON

```python
import json

bad_json = '{"name": "Laptop",}'

try:
    json.loads(bad_json)
except json.JSONDecodeError as error:
    print(error)
```

## Common Comparisons

| Pair | Difference |
|------|------------|
| `dump()` vs `dumps()` | `dump()` writes to file; `dumps()` returns string |
| `load()` vs `loads()` | `load()` reads from file; `loads()` reads from string |
| JSON object vs Python dict | JSON is text; dict is an in-memory Python object |
| `null` vs `None` | JSON uses `null`; Python uses `None` |

## See also

- [Python JSON: core concepts](core-concepts.md)
- [Python JSON interview problems](interview-problems.md)
- [Python JSON FAQ](frequently-asked-questions.md)
