# Python Exception Handling Reference

## Quick Table

| Keyword | Purpose | When it runs |
|---------|---------|--------------|
| `try` | Wrap risky code | first |
| `except` | Handle an error | when matching exception occurs |
| `else` | Run success code | only when `try` has no exception |
| `finally` | Cleanup | always after `try`/`except`/`else` |
| `raise` | Trigger an exception | when code decides input/state is invalid |

## Basic Pattern

```python
try:
    quantity = int("3")
except ValueError:
    print("Invalid quantity")
else:
    print("Quantity is valid")
finally:
    print("Validation finished")
```

## Catch One Exception

```python
try:
    price = float("999.99")
except ValueError:
    price = 0.0
```

## Catch Multiple Exceptions

```python
cart = {"price": "999"}

try:
    total = float(cart["price"]) * int(cart["quantity"])
except KeyError as error:
    print(f"Missing key: {error}")
except ValueError:
    print("Invalid number")
```

## Catch Multiple Exceptions in One Block

```python
try:
    value = int(None)
except (TypeError, ValueError):
    value = 0
```

## Access Exception Object

```python
try:
    int("SAVE10")
except ValueError as error:
    print(error)
```

## Raise an Exception

```python
def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    return quantity
```

## Re-Raise an Exception

```python
try:
    int("bad")
except ValueError:
    print("Logging invalid quantity")
    raise
```

## Custom Exception

```python
class OutOfStockError(Exception):
    pass


def reserve_stock(product, quantity):
    if product["stock"] < quantity:
        raise OutOfStockError("Not enough stock")
    product["stock"] -= quantity
```

## File Handling With `finally`

```python
file = None

try:
    file = open("products.txt", "r", encoding="utf-8")
    content = file.read()
except FileNotFoundError:
    content = ""
finally:
    if file is not None:
        file.close()
```

Prefer `with` for files when possible.

```python
try:
    with open("products.txt", "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    content = ""
```

## Common Exception Types

| Exception | Common cause |
|-----------|--------------|
| `ValueError` | valid type, invalid value |
| `TypeError` | wrong data type |
| `KeyError` | missing dictionary key |
| `IndexError` | invalid list index |
| `FileNotFoundError` | missing file |
| `ZeroDivisionError` | division by zero |
| `ImportError` | import problem |
| `JSONDecodeError` | invalid JSON |

## See also

- [Python exception handling: core concepts](core-concepts.md)
- [Python exception handling interview problems](interview-problems.md)
- [Python exception handling FAQ](frequently-asked-questions.md)
