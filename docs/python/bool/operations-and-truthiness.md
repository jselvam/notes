# Python Boolean Operations & Truthiness: Interview Notes

Boolean interview questions often test `and`, `or`, `not`, truthy/falsey values, comparison chaining, short-circuiting, and common pitfalls.

## Quick Table

| Topic | Meaning | Interview use case |
|-------|---------|--------------------|
| `and` | Both sides must be truthy | Checkout allowed |
| `or` | At least one side truthy | Coupon or member discount |
| `not` | Negates truthiness | Empty cart check |
| `bool()` | Converts to boolean | Input validation |
| Truthy | Treated as true | Non-empty cart |
| Falsey | Treated as false | Empty list, zero, `None` |
| Short-circuit | Stop once result known | Safe checks |
| Chained comparison | `a < b < c` | Price range |

## `and`

`and` returns the first falsey value, otherwise the last value.

```python
is_logged_in = True
cart_has_items = True

print(is_logged_in and cart_has_items)
# True
```

### Interview Point

`and` does not always return `True` or `False`; it returns one of the original values.

```python
print("laptop" and "mouse")  # mouse
print("" and "mouse")        # ""
```

## `or`

`or` returns the first truthy value, otherwise the last value.

```python
coupon = ""
default_coupon = "WELCOME10"

active_coupon = coupon or default_coupon

print(active_coupon)
# WELCOME10
```

### Interview Point

This is commonly used for defaults, but be careful when `0` is a valid value.

```python
discount = 0
default_discount = 10

print(discount or default_discount)
# 10, maybe wrong if 0 is valid
```

## `not`

`not` returns a real boolean.

```python
cart = []

if not cart:
    print("Cart is empty")
```

## Truthy Values

Most non-empty and non-zero values are truthy.

```python
print(bool("laptop"))  # True
print(bool([101]))     # True
print(bool({"id": 1})) # True
print(bool(25))        # True
```

## Falsey Values

```python
print(bool(False))  # False
print(bool(None))   # False
print(bool(0))      # False
print(bool(""))     # False
print(bool([]))     # False
print(bool({}))     # False
```

## Short-Circuit Evaluation

Python only evaluates what is needed.

```python
cart = []

if cart and cart[0] == "laptop":
    print("Laptop is first")
```

This avoids `IndexError` because `cart[0]` is skipped when `cart` is empty.

## Comparison Operators

Comparisons return booleans.

```python
price = 999

print(price > 100)
print(price == 999)
print(price != 25)
```

## Chained Comparisons

```python
price = 500

if 100 <= price <= 1000:
    print("Price is in range")
```

This is clearer than:

```python
if price >= 100 and price <= 1000:
    print("Price is in range")
```

## `is` vs `==`

`==` compares values. `is` compares identity.

```python
is_active = True

print(is_active == True)
print(is_active is True)
```

### Interview Point

Prefer direct boolean checks:

```python
if is_active:
    print("Active")
```

Use `is None` for `None` checks:

```python
discount = None

if discount is None:
    print("No discount configured")
```

## `any()`

Returns `True` if at least one item is truthy.

```python
stock_flags = [False, False, True]

print(any(stock_flags))
# True
```

Use case: at least one warehouse has stock.

## `all()`

Returns `True` if all items are truthy.

```python
checks = [True, True, False]

print(all(checks))
# False
```

Use case: all checkout validations pass.

## Common Interview Questions

### What does `and` return?

It returns the first falsey value, or the last value if all are truthy.

### What does `or` return?

It returns the first truthy value, or the last value if all are falsey.

### Why can `x or default` be risky?

It replaces valid falsey values like `0`, `""`, or `False`.

### What is the Pythonic way to check an empty list?

Use `if not items:`.

## Practice Problems

1. Check if checkout is allowed only when user is logged in and cart has items.
2. Use `any()` to check if any warehouse has stock.
3. Use `all()` to check if all validation rules pass.
4. Check if a price is between 100 and 1000 using chained comparison.
5. Show why `discount or 10` can be wrong when discount is `0`.
6. Use short-circuiting to avoid accessing an empty cart.

## See also

- [Python boolean core concepts](core-concepts.md)
- [Python boolean interview problems](interview-problems.md)
- [Python boolean FAQ](frequently-asked-questions.md)
