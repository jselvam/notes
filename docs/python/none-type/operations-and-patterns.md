# Python NoneType Operations & Patterns: Interview Notes

`None` does not have many operations. Interview questions usually focus on **checking for None**, **safe defaults**, **optional returns**, and **avoiding truthiness bugs**.

## Quick Table

| Pattern | Use | Interview example |
|---------|-----|-------------------|
| `is None` | Check missing value | Coupon not found |
| `is not None` | Check value exists | Discount configured |
| `return None` | Not found / no result | Search product |
| default `None` | Avoid mutable defaults | `cart=None` |
| `Optional` / `T | None` | Type hint missing value | `float | None` |
| sentinel object | Distinguish omitted from `None` | Advanced APIs |

## Checking Missing Value

```python
coupon = None

if coupon is None:
    print("Coupon not found")
```

## Checking Existing Value

```python
discount = 0

if discount is not None:
    print("Discount was provided")
```

### Interview Point

`0` is a real value. Do not accidentally treat it as missing.

## Optional Return Pattern

```python
def find_product(products, product_id):
    for product in products:
        if product["id"] == product_id:
            return product

    return None
```

Caller:

```python
product = find_product([{"id": 101, "name": "laptop"}], 999)

if product is None:
    print("Product not found")
```

## Safe Mutable Default Pattern

Bad:

```python
def add_item_bad(item, cart=[]):
    cart.append(item)
    return cart
```

Good:

```python
def add_item(item, cart=None):
    if cart is None:
        cart = []

    cart.append(item)
    return cart
```

## `dict.get()` and `None`

`.get()` returns `None` by default when key is missing.

```python
prices = {"laptop": 999}

print(prices.get("mouse"))  # None
```

Use a custom default when `None` is a valid value.

```python
missing = object()

value = prices.get("mouse", missing)

if value is missing:
    print("Price key missing")
```

## `None` vs Falsey Values

```python
values = [None, 0, False, "", [], {}]

for value in values:
    print(value, bool(value))
```

All are falsey, but they do not mean the same thing.

## Avoid `x or default` When Falsey Values Are Valid

```python
discount = 0
default_discount = 10

print(discount or default_discount)
# 10, but 0 may be valid
```

Correct:

```python
discount = 0
default_discount = 10

if discount is None:
    discount = default_discount

print(discount)
```

## Type Hints

```python
def find_discount(coupon: str) -> int | None:
    discounts = {"SAVE10": 10}
    return discounts.get(coupon)
```

Older style:

```python
from typing import Optional


def find_discount_old(coupon: str) -> Optional[int]:
    discounts = {"SAVE10": 10}
    return discounts.get(coupon)
```

## Sentinel Object Pattern

Use a custom sentinel when `None` itself is a valid argument.

```python
MISSING = object()


def update_discount(discount=MISSING):
    if discount is MISSING:
        return "discount not provided"
    if discount is None:
        return "remove discount"
    return f"set discount to {discount}"
```

### Interview Point

This is advanced, but useful for API design.

## Common Interview Questions

### Why use `is None`?

Because `None` is a singleton, and identity check is the intended pattern.

### Is `None` falsey?

Yes, but do not rely on truthiness when falsey values like `0` are valid.

### What does a missing `return` produce?

`None`.

### What is the safe default for list/dict parameters?

Use `None`, then create the list/dict inside the function.

## Practice Problems

1. Search a product and return `None` if missing.
2. Fix `discount or 10` when `0` is valid.
3. Fix a mutable default list bug.
4. Use `int | None` in a function return type.
5. Use a sentinel object to distinguish omitted value from `None`.
6. Show why `.get()` can be ambiguous when stored values may be `None`.

## See also

- [Python NoneType core concepts](core-concepts.md)
- [Python NoneType interview problems](interview-problems.md)
- [Python NoneType FAQ](frequently-asked-questions.md)
