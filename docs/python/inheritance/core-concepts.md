# Python Inheritance: Core Concepts

Inheritance lets one class reuse or extend another class. The existing class is called the **parent class**, **base class**, or **superclass**. The new class is called the **child class**, **derived class**, or **subclass**.

In an online computer shopping system, inheritance can model relationships such as:

- `DigitalProduct` is a `Product`
- `PhysicalProduct` is a `Product`
- `CardPayment` is a `PaymentMethod`
- `PremiumCustomer` is a `Customer`

## Basic Inheritance

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def label(self):
        return f"{self.name}: ${self.price:.2f}"


class DigitalProduct(Product):
    pass


pdf_editor = DigitalProduct("PDF Editor", 49.99)
print(pdf_editor.label())
```

`DigitalProduct` inherits `__init__()` and `label()` from `Product`.

## Add Child-Specific Behavior

```python
class DigitalProduct(Product):
    def download_message(self):
        return f"{self.name} is available as a download"


software = DigitalProduct("Office Suite", 99.99)
print(software.download_message())
```

## Method Overriding

A child class can replace a parent method.

```python
class Product:
    def delivery_type(self):
        return "standard delivery"


class DigitalProduct(Product):
    def delivery_type(self):
        return "download link"


print(DigitalProduct().delivery_type())
```

## `super()`

`super()` calls behavior from the parent class.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class PhysicalProduct(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight


monitor = PhysicalProduct("Monitor", 199.99, 2.5)
print(monitor.name)
print(monitor.weight)
```

## `isinstance()` and `issubclass()`

```python
print(isinstance(monitor, PhysicalProduct))
print(isinstance(monitor, Product))
print(issubclass(PhysicalProduct, Product))
```

## Single Inheritance

Single inheritance means a class inherits from one parent.

```python
class SubscriptionProduct(Product):
    pass
```

## Multiple Inheritance

Multiple inheritance means a class inherits from more than one parent.

```python
class Downloadable:
    def download(self):
        return "download started"


class Licensed:
    def license_key(self):
        return "license key generated"


class SoftwareProduct(Downloadable, Licensed):
    pass
```

Use multiple inheritance carefully because it can make method lookup harder to understand.

## Method Resolution Order

MRO means **Method Resolution Order**. It is the order Python follows when looking for a method.

```python
print(SoftwareProduct.mro())
```

## Inheritance vs Composition

Inheritance means **is-a**.

Composition means **has-a**.

```python
class Cart:
    def __init__(self, items):
        self.items = items


class Order:
    def __init__(self, cart):
        self.cart = cart
```

`Order` has a `Cart`, so composition is clearer than inheritance.

## Common Gotchas

### Do not overuse inheritance

Use inheritance only when the child is truly a specialized version of the parent.

### Remember to call `super().__init__()`

If the parent initializes important attributes, the child should usually call it.

### Multiple inheritance can be confusing

Check `ClassName.mro()` when method lookup is unclear.

## Practice Problems

1. Create `Product` and `DigitalProduct`.
2. Override `delivery_type()` for digital products.
3. Use `super()` to initialize a child class.
4. Use `isinstance()` and `issubclass()`.
5. Explain inheritance vs composition using `Order` and `Cart`.

## See also

- [Python inheritance reference](inheritance-reference.md)
- [Python inheritance interview problems](interview-problems.md)
- [Python inheritance FAQ](frequently-asked-questions.md)
- [Python OOP core concepts](../oop/core-concepts.md)
