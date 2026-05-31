# Python Generators, Decorators, and Context Managers: Core Concepts

Generators, decorators, and context managers are advanced Python features that help write memory-efficient, reusable, and reliable code.

This page covers:

- generators with `yield`
- generator expressions
- function decorators
- class decorators
- decorator chaining
- context managers
- `with`, `__enter__()`, and `__exit__()`

Examples use an online computer shopping system.

## Generators

A generator produces values one at a time instead of building the full result in memory.

```python
def product_ids():
    yield 101
    yield 102
    yield 103


for product_id in product_ids():
    print(product_id)
```

When Python sees `yield`, the function becomes a generator function.

## Why Use Generators?

Use generators when data can be processed lazily:

- reading large product exports
- streaming order IDs
- processing logs line by line
- generating report rows

```python
def available_products(products):
    for product in products:
        if product["stock"] > 0:
            yield product
```

## `yield` vs `return`

| Keyword | Meaning |
|---------|---------|
| `return` | exits the function and gives one final value |
| `yield` | pauses the function and gives the next value |

```python
def discounts():
    yield "WELCOME10"
    yield "FESTIVAL20"
```

The generator remembers where it paused.

## Generator Expressions

A generator expression is like a list comprehension, but lazy.

```python
prices = [999.99, 25.5, 75.0]
discounted_prices = (price * 0.9 for price in prices)

for price in discounted_prices:
    print(price)
```

Use generator expressions when you do not need the whole list at once.

## Decorators

A decorator wraps a function or class to add behavior.

```python
def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@log_action
def place_order(order_id):
    return f"Order {order_id} placed"
```

The `@log_action` syntax is shorthand for:

```python
place_order = log_action(place_order)
```

## Function Decorators

Function decorators commonly add:

- logging
- authorization
- validation
- caching
- timing

```python
def require_admin(func):
    def wrapper(user, *args, **kwargs):
        if user["role"] != "admin":
            raise PermissionError("Admin required")
        return func(user, *args, **kwargs)
    return wrapper
```

## Class Decorators

A class decorator receives a class and returns the same class or a modified class.

```python
def add_category(cls):
    cls.category = "computer"
    return cls


@add_category
class Product:
    pass


print(Product.category)
```

## Decorator Chaining

Multiple decorators can be stacked.

```python
@log_action
@require_admin
def cancel_order(user, order_id):
    return f"Cancelled order {order_id}"
```

Decorators apply from bottom to top:

```python
cancel_order = log_action(require_admin(cancel_order))
```

## Context Managers

A context manager manages setup and cleanup around a block of code.

The common example is file handling:

```python
with open("orders.txt", "w", encoding="utf-8") as file:
    file.write("Order 1001")
```

The file is closed automatically after the block.

## `__enter__()` and `__exit__()`

Custom context managers use `__enter__()` and `__exit__()`.

```python
class OrderLock:
    def __enter__(self):
        print("Lock acquired")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Lock released")


with OrderLock():
    print("Updating order")
```

`__enter__()` runs before the block. `__exit__()` runs after the block, even if an exception occurs.

## Common Interview Summary

- Generators are lazy iterators.
- `yield` pauses and resumes a function.
- Generator expressions save memory compared with list comprehensions.
- Decorators add behavior without changing the original function body.
- Decorators can wrap functions or classes.
- Chained decorators apply from bottom to top.
- Context managers guarantee setup and cleanup.
- `with` calls `__enter__()` and `__exit__()`.

## See also

- [Advanced functions reference](advanced-functions-reference.md)
- [Advanced functions interview problems](interview-problems.md)
- [Advanced functions FAQ](frequently-asked-questions.md)
- [Python functions](../functions/core-concepts.md)
- [Dunder methods](../dunder-methods/core-concepts.md)
- [File handling](../file-handling/core-concepts.md)
