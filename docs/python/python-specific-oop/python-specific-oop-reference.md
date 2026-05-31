# Python-Specific OOP Features Reference

## Quick Table

| Feature | Purpose | Example |
|---------|---------|---------|
| `@dataclass` | auto-generate boilerplate methods | `@dataclass class Product` |
| `field()` | configure dataclass fields | `field(default_factory=list)` |
| `frozen=True` | immutable dataclass | `@dataclass(frozen=True)` |
| `__slots__` | restrict attributes and save memory | `__slots__ = ("name",)` |
| `@property` | attribute-style method | `product.total` |
| setter | validate assignment | `@price.setter` |
| descriptor | reusable attribute access control | `__get__`, `__set__` |
| metaclass | customize class creation | `metaclass=ModelMeta` |

## Dataclass

```python
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
```

## Dataclass With Default Factory

Use `default_factory` for mutable defaults.

```python
from dataclasses import dataclass, field


@dataclass
class Cart:
    items: list[str] = field(default_factory=list)
```

## Frozen Dataclass

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class ProductId:
    value: int
```

## Slots

```python
class CartItem:
    __slots__ = ("product_name", "quantity")

    def __init__(self, product_name, quantity):
        self.product_name = product_name
        self.quantity = quantity
```

## Dataclass With Slots

```python
from dataclasses import dataclass


@dataclass(slots=True)
class Product:
    name: str
    price: float
```

## Property

```python
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def formatted_price(self):
        return f"${self.price:.2f}"
```

## Property Setter

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

## Descriptor

```python
class PositiveNumber:
    def __set_name__(self, owner, name):
        self.storage_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value cannot be negative")
        setattr(instance, self.storage_name, value)
```

## Metaclass

```python
class ModelMeta(type):
    def __new__(cls, name, bases, namespace):
        namespace["table_name"] = name.lower()
        return super().__new__(cls, name, bases, namespace)
```

## Common Comparisons

| Pair | Difference |
|------|------------|
| dataclass vs normal class | less boilerplate vs full manual control |
| dataclass vs namedtuple | mutable by default vs tuple-like immutable record |
| `__slots__` vs `__dict__` | fixed attributes vs dynamic attributes |
| property vs descriptor | per-class controlled access vs reusable attribute protocol |
| descriptor vs decorator | attribute behavior protocol vs function/class wrapper |
| class vs metaclass | object blueprint vs class blueprint |

## See also

- [Python-specific OOP: core concepts](core-concepts.md)
- [Python-specific OOP interview problems](interview-problems.md)
- [Python-specific OOP FAQ](frequently-asked-questions.md)
