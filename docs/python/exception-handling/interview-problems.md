# Python Exception Handling Interview Problems

## 1. Convert Quantity Safely

### Problem

Convert user input to quantity. If invalid, use `1`.

```python
def parse_quantity(value):
    try:
        return int(value)
    except ValueError:
        return 1


print(parse_quantity("3"))
print(parse_quantity("three"))
```

**Complexity:** `O(1)` time and space.

## 2. Handle Missing Product Price

```python
def get_product_price(product):
    try:
        return product["price"]
    except KeyError:
        return 0


print(get_product_price({"name": "Mouse"}))
```

## 3. Use `else` for Success Path

```python
def parse_discount(value):
    try:
        discount = int(value)
    except ValueError:
        return "Invalid discount"
    else:
        return f"Discount accepted: {discount}%"


print(parse_discount("10"))
```

## 4. Use `finally` for Cleanup

```python
def process_order(order_id):
    try:
        print(f"Processing order {order_id}")
        return "success"
    except RuntimeError:
        return "failed"
    finally:
        print("Cleanup order resources")


print(process_order("ORD-501"))
```

## 5. Catch Multiple Exception Types

```python
def calculate_total(cart):
    try:
        return float(cart["price"]) * int(cart["quantity"])
    except KeyError as error:
        return f"Missing field: {error}"
    except (TypeError, ValueError):
        return "Invalid price or quantity"


print(calculate_total({"price": "999", "quantity": "2"}))
```

## 6. Raise Error for Invalid Quantity

```python
def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    return quantity


print(validate_quantity(2))
```

## 7. Custom Out-of-Stock Exception

```python
class OutOfStockError(Exception):
    pass


def reserve_stock(product, quantity):
    if product["stock"] < quantity:
        raise OutOfStockError("Not enough stock available")
    product["stock"] -= quantity
    return product


product = {"name": "Laptop", "stock": 1}

try:
    reserve_stock(product, 2)
except OutOfStockError as error:
    print(error)
```

## 8. Parse JSON Safely

```python
import json


def parse_order(json_text):
    try:
        order = json.loads(json_text)
    except json.JSONDecodeError:
        return None
    else:
        return order


print(parse_order('{"order_id": 501}'))
```

## 9. File Read With Exception Handling

```python
def read_products(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return ""


print(read_products("products.txt"))
```

## 10. Re-Raise After Logging

```python
def parse_price(value):
    try:
        return float(value)
    except ValueError:
        print(f"Invalid price received: {value}")
        raise
```

Use re-raise when the current function should log context but still let the caller handle the failure.

## Summary

| Problem pattern | Exception tool |
|-----------------|----------------|
| invalid input conversion | `ValueError` |
| missing dictionary field | `KeyError` |
| success-only logic | `else` |
| cleanup | `finally` |
| invalid business rule | `raise` |
| domain-specific failure | custom exception |

## See also

- [Python exception handling: core concepts](core-concepts.md)
- [Python exception handling reference](exception-handling-reference.md)
- [Python exception handling FAQ](frequently-asked-questions.md)
