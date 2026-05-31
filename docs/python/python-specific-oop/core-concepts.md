# Python-Specific OOP Features: Core Concepts

Python has several OOP features that make classes more concise, memory-efficient, flexible, or powerful.

This page covers:

- `@dataclass`
- `__slots__`
- properties
- descriptors
- metaclasses

Examples use an online computer shopping system.

## Dataclasses

`@dataclass` automatically generates common methods such as `__init__()`, `__repr__()`, and comparison helpers.

```python
from dataclasses import dataclass


@dataclass
class Product:
    product_id: int
    name: str
    price: float


product = Product(101, "Laptop", 999.99)
print(product)
```

Use dataclasses for classes that mostly store data.

## Dataclass Defaults

```python
from dataclasses import dataclass


@dataclass
class CartItem:
    product_name: str
    quantity: int = 1


item = CartItem("Mouse")
print(item)
```

## Slots

`__slots__` restricts which attributes objects can have and can reduce memory usage.

```python
class Product:
    __slots__ = ("name", "price")

    def __init__(self, name, price):
        self.name = name
        self.price = price


product = Product("Keyboard", 75)
print(product.name)
```

With `__slots__`, adding an undeclared attribute raises `AttributeError`.

## Properties

Properties let methods behave like attributes.

```python
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def formatted_price(self):
        return f"${self.price:.2f}"


product = Product(999.9)
print(product.formatted_price)
```

## Property Setters

Setters validate assignment.

```python
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
```

## Descriptors

A descriptor is an object that controls attribute access using methods such as `__get__()`, `__set__()`, or `__delete__()`.

```python
class PositiveNumber:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value cannot be negative")
        setattr(instance, self.name, value)


class Product:
    price = PositiveNumber()

    def __init__(self, price):
        self.price = price
```

Descriptors are advanced. Properties are often enough for everyday validation.

## Metaclasses

A metaclass controls how classes are created. Most Python code does not need custom metaclasses.

```python
class ModelMeta(type):
    def __new__(cls, name, bases, namespace):
        namespace["model_name"] = name.lower()
        return super().__new__(cls, name, bases, namespace)


class Product(metaclass=ModelMeta):
    pass


print(Product.model_name)
```

Metaclasses are useful in frameworks, ORMs, validation libraries, and advanced APIs.

## When to Use Each Feature

| Feature | Best use |
|---------|----------|
| `@dataclass` | simple data objects |
| `__slots__` | many objects, fixed attributes, memory saving |
| `@property` | computed values or validation |
| descriptor | reusable attribute behavior across classes |
| metaclass | customize class creation itself |

## Common Gotchas

### Do not overuse metaclasses

Metaclasses are powerful but can make code harder to understand.

### `__slots__` removes normal dynamic attributes

This is useful for memory and correctness, but less flexible.

### Dataclasses are not always immutable

Use `@dataclass(frozen=True)` if you need immutable objects.

## Practice Problems

1. Create a `Product` dataclass.
2. Create an immutable `ProductId` dataclass.
3. Use `__slots__` for a lightweight `CartItem`.
4. Add a `price` property with validation.
5. Create a reusable positive-number descriptor.

## See also

- [Python-specific OOP reference](python-specific-oop-reference.md)
- [Python-specific OOP interview problems](interview-problems.md)
- [Python-specific OOP FAQ](frequently-asked-questions.md)
- [Python advanced OOP](../advanced-oop/core-concepts.md)
