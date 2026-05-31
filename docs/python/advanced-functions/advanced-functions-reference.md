# Python Advanced Functions Reference

## Quick Reference

| Feature | Syntax | Purpose |
|---------|--------|---------|
| generator function | `yield value` | produce values lazily |
| generator expression | `(x for x in items)` | lazy comprehension |
| function decorator | `@decorator` | wrap function behavior |
| class decorator | `@decorator` on class | modify or register class |
| chained decorators | multiple `@decorator` lines | apply multiple wrappers |
| context manager | `with manager:` | setup and cleanup |
| context protocol | `__enter__`, `__exit__` | implement custom `with` support |

## Generator Function

```python
def order_ids(orders):
    for order in orders:
        yield order["id"]
```

Use with:

```python
orders = [{"id": 1001}, {"id": 1002}]

for order_id in order_ids(orders):
    print(order_id)
```

## Generator Expression

```python
products = [
    {"name": "Laptop", "stock": 3},
    {"name": "Mouse", "stock": 0},
]

available_names = (
    product["name"]
    for product in products
    if product["stock"] > 0
)
```

## `next()`

```python
def coupons():
    yield "WELCOME10"
    yield "FESTIVAL20"


coupon_generator = coupons()
print(next(coupon_generator))
print(next(coupon_generator))
```

When no values remain, Python raises `StopIteration`.

## List Comprehension vs Generator Expression

| Feature | List comprehension | Generator expression |
|---------|--------------------|----------------------|
| Syntax | `[x for x in items]` | `(x for x in items)` |
| Evaluation | immediate | lazy |
| Memory | stores all values | stores one value at a time |
| Reusable | yes | no, usually consumed once |

## Function Decorator

```python
from functools import wraps


def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

Use `functools.wraps` to preserve function metadata such as `__name__`.

## Decorator With Arguments

```python
from functools import wraps


def require_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if user["role"] != role:
                raise PermissionError(f"{role} required")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator
```

Usage:

```python
@require_role("admin")
def update_price(user, product_id, price):
    return f"Updated {product_id} to {price}"
```

## Class Decorator

```python
def register_model(cls):
    cls.registered = True
    return cls


@register_model
class Product:
    pass
```

## Decorator Chaining

```python
@log_action
@require_role("admin")
def delete_product(user, product_id):
    return f"Deleted product {product_id}"
```

Execution wrapping:

```python
delete_product = log_action(require_role("admin")(delete_product))
```

## Context Manager Class

```python
class InventoryTransaction:
    def __enter__(self):
        print("Start transaction")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print("Rollback transaction")
        else:
            print("Commit transaction")
```

Usage:

```python
with InventoryTransaction():
    print("Update stock")
```

## `__exit__()` Arguments

| Argument | Meaning |
|----------|---------|
| `exc_type` | exception class, or `None` |
| `exc_value` | exception object, or `None` |
| `traceback` | traceback object, or `None` |

If `__exit__()` returns `True`, it suppresses the exception. Usually, return `False` or nothing.

## Common Comparisons

| Comparison | Difference |
|------------|------------|
| iterator vs generator | generator is an easy way to create an iterator |
| `yield` vs `return` | `yield` pauses; `return` exits |
| list comprehension vs generator expression | eager list vs lazy generator |
| decorator vs normal wrapper | decorator is wrapper syntax |
| function decorator vs class decorator | wraps function vs modifies class |
| context manager vs `try/finally` | reusable cleanup abstraction |

## Best Practices

- Use generators for large or streamed data.
- Do not reuse a generator after it is consumed.
- Use `functools.wraps` in decorators.
- Keep decorators small and predictable.
- Be careful with decorator order.
- Use context managers for resources that require cleanup.
- Avoid suppressing exceptions in `__exit__()` unless intentional.

## See also

- [Advanced functions: core concepts](core-concepts.md)
- [Advanced functions interview problems](interview-problems.md)
- [Advanced functions FAQ](frequently-asked-questions.md)
