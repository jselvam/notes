# Python OOP Reference

## Quick Table

| Term | Meaning | Example |
|------|---------|---------|
| Class | blueprint | `class Product:` |
| Object | instance of a class | `Product("Laptop", 999)` |
| Attribute | data stored on object | `product.price` |
| Method | function inside class | `product.label()` |
| Constructor | initialization method | `__init__()` |
| `self` | current object | `self.name = name` |
| Encapsulation | data + behavior together | `Cart.add_item()` |
| Inheritance | reuse parent behavior | `DigitalProduct(Product)` |
| Polymorphism | same interface, different behavior | `payment.pay()` |
| Abstraction | hide internal detail | service method/API |

## Basic Class

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
```

## Create Object

```python
laptop = Product("Laptop", 999.99)
print(laptop.name)
```

## Instance Method

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def label(self):
        return f"{self.name}: ${self.price:.2f}"
```

## Class Attribute

```python
class Product:
    store_name = "Computer Shop"

    def __init__(self, name):
        self.name = name
```

`store_name` is shared by all instances.

## Instance Attribute

```python
product = Product("Mouse")
print(product.name)
```

`name` belongs to a specific object.

## Inheritance

```python
class Product:
    def __init__(self, name):
        self.name = name


class SubscriptionProduct(Product):
    def renew(self):
        return f"Renewing {self.name}"
```

## Method Overriding

```python
class Product:
    def delivery_type(self):
        return "standard delivery"


class DigitalProduct(Product):
    def delivery_type(self):
        return "download link"
```

## Polymorphism

```python
def print_delivery(product):
    print(product.delivery_type())
```

Any object with `delivery_type()` can be passed.

## `@property`

```python
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def formatted_price(self):
        return f"${self.price:.2f}"
```

Use `@property` when computed data should feel like an attribute.

## Common Comparisons

| Pair | Difference |
|------|------------|
| Class vs object | blueprint vs instance |
| Attribute vs method | data vs behavior |
| Instance attribute vs class attribute | per-object vs shared |
| Inheritance vs composition | is-a relationship vs has-a relationship |
| Overloading vs overriding | same name variations vs child replacing parent behavior |

## See also

- [Python OOP: core concepts](core-concepts.md)
- [Python OOP interview problems](interview-problems.md)
- [Python OOP FAQ](frequently-asked-questions.md)
