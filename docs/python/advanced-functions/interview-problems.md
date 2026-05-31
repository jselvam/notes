# Python Generators, Decorators, and Context Managers Interview Problems

## 1. Generate Product IDs Lazily

### Problem

Create a generator that yields product IDs one by one.

```python
def product_ids(products):
    for product in products:
        yield product["id"]


products = [{"id": 101}, {"id": 102}, {"id": 103}]

for product_id in product_ids(products):
    print(product_id)
```

### Interview Point

Generators avoid building a full list in memory.

## 2. Filter Available Products With `yield`

```python
def available_products(products):
    for product in products:
        if product["stock"] > 0:
            yield product


products = [
    {"name": "Laptop", "stock": 3},
    {"name": "Mouse", "stock": 0},
]

print(list(available_products(products)))
```

## 3. Use a Generator Expression

```python
prices = [999.99, 25.5, 75.0]
discounted = (price * 0.9 for price in prices)

print(next(discounted))
```

Generator expressions are lazy and usually consumed once.

## 4. Write a Logging Decorator

```python
from functools import wraps


def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@log_action
def place_order(order_id):
    return f"Order {order_id} placed"
```

## 5. Write an Authorization Decorator

```python
from functools import wraps


def require_admin(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user["role"] != "admin":
            raise PermissionError("Admin required")
        return func(user, *args, **kwargs)
    return wrapper
```

## 6. Write a Decorator With Arguments

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

## 7. Chain Decorators

```python
@log_action
@require_role("admin")
def cancel_order(user, order_id):
    return f"Cancelled order {order_id}"
```

The lower decorator runs closer to the original function.

## 8. Write a Class Decorator

```python
def add_model_name(cls):
    cls.model_name = cls.__name__.lower()
    return cls


@add_model_name
class Product:
    pass


print(Product.model_name)
```

## 9. Create a Context Manager

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

## 10. Handle Exceptions in `__exit__()`

```python
class InventoryTransaction:
    def __enter__(self):
        print("Start transaction")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print("Rollback")
        else:
            print("Commit")
```

Returning `True` from `__exit__()` suppresses the exception. Usually avoid that unless required.

## 11. Use Context Manager Instead of `try/finally`

```python
with open("orders.txt", "w", encoding="utf-8") as file:
    file.write("Order 1001")
```

The file closes automatically even if an exception occurs.

## 12. Choose the Right Feature

| Scenario | Feature |
|----------|---------|
| stream product rows | generator |
| lazy price calculation | generator expression |
| add logging/security | decorator |
| add metadata to a class | class decorator |
| manage file or lock cleanup | context manager |

## See also

- [Advanced functions: core concepts](core-concepts.md)
- [Advanced functions reference](advanced-functions-reference.md)
- [Advanced functions FAQ](frequently-asked-questions.md)
