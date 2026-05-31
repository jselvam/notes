# Python Exception Handling: Core Concepts

Exception handling lets Python programs respond to runtime errors without crashing immediately. The main keywords are `try`, `except`, `else`, and `finally`.

In an online computer shopping system, exception handling is useful for:

- invalid product IDs
- missing cart fields
- failed payment API calls
- invalid JSON input
- missing files
- database or network failures

## Basic Syntax

```python
try:
    risky_code()
except SomeError:
    handle_error()
else:
    run_if_no_error()
finally:
    always_run_cleanup()
```

## `try`

Put code that may fail inside `try`.

```python
try:
    price = float("999.99")
except ValueError:
    price = 0.0

print(price)
```

## `except`

`except` handles a specific exception.

```python
cart = {"quantity": "two"}

try:
    quantity = int(cart["quantity"])
except ValueError:
    quantity = 1

print(quantity)
```

## Multiple `except` Blocks

Handle different errors differently.

```python
cart = {"price": "999"}

try:
    total = int(cart["price"]) * int(cart["quantity"])
except KeyError as error:
    print(f"Missing field: {error}")
except ValueError:
    print("Quantity or price is not a valid number")
```

## `else`

The `else` block runs only when no exception happens in `try`.

```python
try:
    quantity = int("3")
except ValueError:
    print("Invalid quantity")
else:
    print(f"Quantity accepted: {quantity}")
```

Use `else` for success-path code that should not be inside the `try` block.

## `finally`

The `finally` block runs whether an exception happens or not.

```python
try:
    print("Open inventory file")
    quantity = int("5")
except ValueError:
    print("Invalid quantity")
finally:
    print("Close inventory file")
```

Use `finally` for cleanup, such as closing files, releasing locks, or ending sessions.

## Catch Specific Exceptions

Prefer specific exceptions.

```python
try:
    discount = int("SAVE10")
except ValueError:
    discount = 0
```

Avoid broad `except:` unless you have a strong reason.

## Raise Exceptions

Use `raise` when a function receives invalid data.

```python
def apply_discount(price, percent):
    if percent < 0:
        raise ValueError("Discount percent cannot be negative")
    return price - (price * percent / 100)
```

## Common Interview Points

### When does `else` run?

`else` runs only if the `try` block completes without an exception.

### When does `finally` run?

`finally` runs whether an exception happens or not.

### Why catch specific exceptions?

Specific exceptions avoid hiding bugs.

## Practice Problems

1. Handle invalid product quantity input.
2. Handle missing product price from a dictionary.
3. Use `else` after successful JSON parsing.
4. Use `finally` to close a file.
5. Raise `ValueError` for negative cart quantity.

## See also

- [Python exception handling reference](exception-handling-reference.md)
- [Python exception handling interview problems](interview-problems.md)
- [Python exception handling FAQ](frequently-asked-questions.md)
- [Python control flow: core concepts](../control-flow/core-concepts.md)
