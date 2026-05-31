# Python NoneType: Core Concepts

`None` represents **no value**, **missing value**, or **not available yet** in Python. Its type is `NoneType`.

In an online computer shopping management system, `None` can represent:

- product has no discount
- coupon lookup did not find a coupon
- payment method is not selected yet
- optional delivery date is not available
- function did not find a product
- API field is missing or unknown

## What Is `None`?

`None` is a singleton object in Python.

```python
discount = None

print(discount)
print(type(discount))
# <class 'NoneType'>
```

There is only one `None` object.

## `None` Means Missing, Not Zero

`None`, `0`, `False`, and `""` are different values.

```python
discount = None
quantity = 0
is_active = False
coupon = ""

print(discount is None)  # True
print(quantity == 0)     # True
```

### Interview Point

Do not treat `None` and `0` as the same thing. A discount of `0` can be valid.

## Checking for `None`

Use `is None` and `is not None`.

```python
discount = None

if discount is None:
    print("No discount configured")
```

```python
discount = 0

if discount is not None:
    print("Discount value exists")
```

## Why `is None` Instead of `== None`?

`None` is a singleton, so identity check is the Pythonic and safe pattern.

```python
value = None

print(value is None)
```

## Function Without Return

A function returns `None` by default when there is no `return`.

```python
def log_order(order_id):
    print(f"Order: {order_id}")


result = log_order("ORD-1001")
print(result)  # None
```

## Function Returning `None` for Not Found

```python
def find_product(products, target):
    for product in products:
        if product == target:
            return product
    return None


result = find_product(["mouse", "keyboard"], "laptop")

if result is None:
    print("Product not found")
```

## `None` as Default Parameter

Use `None` as a safe default when the real default should be a new list, dict, or set.

```python
def add_to_cart(item, cart=None):
    if cart is None:
        cart = []

    cart.append(item)
    return cart
```

This avoids the mutable default argument bug.

## `None` and Truthiness

`None` is falsey.

```python
print(bool(None))  # False
```

But do not use truthiness when `0`, `False`, or `""` are valid values.

```python
discount = 0

if discount is None:
    print("Use default discount")
else:
    print(f"Use configured discount: {discount}")
```

## `Optional` Type Hint

Use `Optional[T]` or `T | None` when a value can be `None`.

```python
def find_price(product_id: int) -> float | None:
    prices = {101: 999.99}
    return prices.get(product_id)
```

## Common Interview Points

### What is the type of `None`?

The type of `None` is `NoneType`.

```python
print(type(None))
```

### Is `None` the same as `False`?

No. `None` is falsey, but it is not equal to `False`.

```python
print(None == False)  # False
```

### Is `None` the same as `0`?

No.

```python
print(None == 0)  # False
```

## Practice Problems

1. Write a function that returns a product or `None` if not found.
2. Check whether a coupon is missing using `is None`.
3. Fix a mutable default argument using `None`.
4. Explain why `discount or 10` is wrong when discount can be `0`.
5. Add a type hint for a function that may return `None`.
6. Show that a function without `return` returns `None`.

## See also

- [Python NoneType operations](operations-and-patterns.md)
- [Python NoneType interview problems](interview-problems.md)
- [Python NoneType FAQ](frequently-asked-questions.md)
- [Python function parameters](../functions/parameters-and-arguments.md)
