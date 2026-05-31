# Python-Specific OOP Features Interview Problems

## 1. Create Product Dataclass

### Problem

Create a lightweight product data object.

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

**Complexity:** `O(1)` time and space per object.

## 2. Avoid Mutable Default in Dataclass

```python
from dataclasses import dataclass, field


@dataclass
class Cart:
    items: list[str] = field(default_factory=list)


cart = Cart()
cart.items.append("Mouse")
print(cart.items)
```

Use `default_factory` for lists and dictionaries.

## 3. Create Immutable Product ID

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class ProductId:
    value: int


product_id = ProductId(101)
print(product_id)
```

## 4. Use Slots for CartItem

```python
class CartItem:
    __slots__ = ("product_name", "quantity")

    def __init__(self, product_name, quantity):
        self.product_name = product_name
        self.quantity = quantity


item = CartItem("Keyboard", 2)
print(item.product_name)
```

## 5. Use Dataclass With Slots

```python
from dataclasses import dataclass


@dataclass(slots=True)
class InventoryItem:
    sku: str
    stock: int
```

This combines dataclass convenience with slot memory benefits.

## 6. Validate Price With Property

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

## 7. Create Reusable Descriptor

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


class Product:
    price = PositiveNumber()
    stock = PositiveNumber()

    def __init__(self, price, stock):
        self.price = price
        self.stock = stock


product = Product(999.99, 5)
print(product.price)
```

## 8. Add Metadata With Metaclass

```python
class ModelMeta(type):
    def __new__(cls, name, bases, namespace):
        namespace["model_name"] = name.lower()
        return super().__new__(cls, name, bases, namespace)


class Product(metaclass=ModelMeta):
    pass


print(Product.model_name)
```

## 9. Compare Normal Class and Dataclass

```python
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
```

Dataclasses reduce boilerplate when classes mostly store data.

## 10. Explain When Not to Use Metaclasses

Use normal classes, decorators, or class methods unless you truly need to control class creation. Metaclasses are usually for frameworks and advanced libraries.

## Summary

| Problem pattern | Feature |
|-----------------|---------|
| data-only object | `@dataclass` |
| mutable default list | `field(default_factory=list)` |
| immutable ID | `@dataclass(frozen=True)` |
| memory-efficient objects | `__slots__` |
| validated value | property setter |
| reusable validation | descriptor |
| class creation hook | metaclass |

## See also

- [Python-specific OOP: core concepts](core-concepts.md)
- [Python-specific OOP reference](python-specific-oop-reference.md)
- [Python-specific OOP FAQ](frequently-asked-questions.md)
