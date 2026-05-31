# Python Error Types Interview Problems

## 1. Fix `TypeError` in Cart Total

### Problem

Price is stored as a string and tax is an integer.

```python
def calculate_total(price, tax):
    return int(price) + tax


print(calculate_total("999", 50))
```

**Error avoided:** `TypeError`  
**Complexity:** `O(1)` time and space.

## 2. Handle `ValueError` for Quantity Input

```python
def parse_quantity(value):
    try:
        return int(value)
    except ValueError:
        return 1


print(parse_quantity("two"))
```

## 3. Avoid `KeyError` for Missing Price

```python
def get_price(product):
    return product.get("price", 0)


print(get_price({"name": "Mouse"}))
```

## 4. Avoid `IndexError` in Cart Lookup

```python
def get_cart_item(cart, index):
    if 0 <= index < len(cart):
        return cart[index]
    return None


print(get_cart_item(["laptop"], 3))
```

## 5. Fix `AttributeError`

```python
def add_product(products, product):
    products.append(product)
    return products


print(add_product(["laptop"], "mouse"))
```

If `products` were a dictionary, `append()` would raise `AttributeError`.

## 6. Fix `NameError`

```python
def cart_total(items):
    total = sum(items)
    return total


print(cart_total([999, 25]))
```

Always define variables before use.

## 7. Handle `FileNotFoundError`

```python
def read_inventory(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return ""


print(read_inventory("inventory.csv"))
```

## 8. Handle `ModuleNotFoundError`

```python
def load_payment_sdk():
    try:
        import fake_payment_sdk
    except ModuleNotFoundError:
        return None
    return fake_payment_sdk
```

In real projects, fix the dependency installation or module name.

## 9. Avoid `ZeroDivisionError`

```python
def average_order_value(revenue, order_count):
    if order_count == 0:
        return 0
    return revenue / order_count


print(average_order_value(1000, 0))
```

## 10. Fix `RecursionError`

```python
def count_items(items, index=0):
    if index == len(items):
        return 0
    return 1 + count_items(items, index + 1)


print(count_items(["laptop", "mouse"]))
```

The base case prevents infinite recursion.

## 11. Handle `JSONDecodeError`

```python
import json


def parse_product_json(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


print(parse_product_json('{"name": "Laptop",}'))
```

## 12. Raise `ValueError` for Business Rule

```python
def validate_discount(percent):
    if percent < 0 or percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    return percent


print(validate_discount(10))
```

## Summary

| Scenario | Likely error |
|----------|--------------|
| wrong operation on type | `TypeError` |
| bad conversion value | `ValueError` |
| missing dict key | `KeyError` |
| invalid list index | `IndexError` |
| missing object method | `AttributeError` |
| missing file | `FileNotFoundError` |
| missing module | `ModuleNotFoundError` |
| divide by zero | `ZeroDivisionError` |

## See also

- [Python error types: core concepts](core-concepts.md)
- [Python error types reference](error-types-reference.md)
- [Python error types FAQ](frequently-asked-questions.md)
