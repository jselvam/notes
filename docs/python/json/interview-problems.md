# Python JSON Interview Problems

## 1. Parse Product JSON

### Problem

Parse product JSON and return the product name.

```python
import json


def get_product_name(json_text):
    product = json.loads(json_text)
    return product["name"]


print(get_product_name('{"name": "Laptop", "price": 999.99}'))
```

**Complexity:** `O(n)` time and space, where `n` is JSON size.

## 2. Convert Cart Dictionary to JSON

```python
import json


def cart_to_json(cart):
    return json.dumps(cart, indent=2)


cart = {"items": ["laptop", "mouse"], "total": 1024.99}
print(cart_to_json(cart))
```

## 3. Validate Required Product Fields

```python
import json


def has_required_fields(json_text):
    product = json.loads(json_text)
    required = {"id", "name", "price"}
    return required.issubset(product)


print(has_required_fields('{"id": 1, "name": "Mouse", "price": 25}'))
```

## 4. Handle Invalid JSON Safely

```python
import json


def parse_json_safe(json_text):
    try:
        return json.loads(json_text)
    except json.JSONDecodeError:
        return None


print(parse_json_safe('{"name": "Laptop",}'))
```

## 5. Extract Product IDs From JSON Array

```python
import json


def product_ids(json_text):
    products = json.loads(json_text)
    return [product["id"] for product in products]


data = '[{"id": 101, "name": "Laptop"}, {"id": 102, "name": "Mouse"}]'
print(product_ids(data))
```

## 6. Convert JSON `null` to Python `None`

```python
import json

data = '{"coupon": null}'
cart = json.loads(data)

print(cart["coupon"] is None)
```

## 7. Pretty Print API Response

```python
import json


def pretty_response(json_text):
    data = json.loads(json_text)
    return json.dumps(data, indent=2, sort_keys=True)


print(pretty_response('{"total":1024.99,"items":["laptop","mouse"]}'))
```

## 8. Merge JSON Product Updates

```python
import json


def merge_product_update(product_json, update_json):
    product = json.loads(product_json)
    update = json.loads(update_json)
    product.update(update)
    return json.dumps(product, indent=2)


print(merge_product_update('{"name": "Laptop", "stock": 5}', '{"stock": 3}'))
```

## 9. Count Products by Category From JSON

```python
import json
from collections import Counter


def count_categories(json_text):
    products = json.loads(json_text)
    return Counter(product["category"] for product in products)


data = '[{"category":"hardware"},{"category":"hardware"},{"category":"software"}]'
print(count_categories(data))
```

## 10. Reject Non-Serializable Data

```python
import json


def can_convert_to_json(value):
    try:
        json.dumps(value)
        return True
    except TypeError:
        return False


print(can_convert_to_json({"ids": {101, 102}}))
```

## Summary

| Problem pattern | JSON idea |
|-----------------|-----------|
| API response parsing | `json.loads()` |
| API request body | `json.dumps()` |
| File read | `json.load()` |
| File write | `json.dump()` |
| Invalid JSON | `JSONDecodeError` |
| Missing fields | dictionary and set checks |

## See also

- [Python JSON: core concepts](core-concepts.md)
- [Python JSON reference](json-reference.md)
- [Python JSON FAQ](frequently-asked-questions.md)
