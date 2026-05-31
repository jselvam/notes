# Python Classes and Objects Reference

## Quick Table

| Term | Meaning | Example |
|------|---------|---------|
| Class | blueprint for objects | `class Product:` |
| Object | instance of a class | `Product("Laptop")` |
| Attribute | data on an object or class | `product.price` |
| Method | function inside class | `product.label()` |
| `__init__` | initializes object state | `def __init__(self, name):` |
| `self` | current object | `self.name = name` |
| Instance attribute | belongs to one object | `self.price` |
| Class attribute | shared by all objects | `store_name = "Shop"` |

## Class Syntax

```python
class Product:
    pass
```

## Object Creation

```python
product = Product()
```

## Constructor Pattern

```python
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
```

## Instance Method Pattern

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def label(self):
        return f"{self.name}: ${self.price:.2f}"
```

## Class Attribute Pattern

```python
class Product:
    currency = "USD"

    def __init__(self, name, price):
        self.name = name
        self.price = price
```

## Access Attributes

```python
product = Product("Monitor", 199.99)

print(product.name)
print(product.price)
```

## Update Attributes

```python
product.price = 179.99
print(product.price)
```

## Add Attributes Dynamically

Python allows adding attributes after object creation.

```python
product.discount = 10
print(product.discount)
```

This is flexible, but in real projects it can make objects harder to understand.

## `__str__`

`__str__()` controls the user-friendly string representation.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


print(Product("Laptop", 999.99))
```

## `__repr__`

`__repr__()` gives a developer-friendly representation.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price!r})"
```

## Common Comparisons

| Pair | Difference |
|------|------------|
| Class vs object | blueprint vs instance |
| Attribute vs method | data vs behavior |
| Instance attribute vs class attribute | per-object vs shared |
| `__str__` vs `__repr__` | user-friendly vs developer-friendly |
| `self` vs class name | current object vs blueprint |

## See also

- [Python classes and objects: core concepts](core-concepts.md)
- [Python classes and objects interview problems](interview-problems.md)
- [Python classes and objects FAQ](frequently-asked-questions.md)
