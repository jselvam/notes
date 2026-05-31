# Python Advanced OOP Concepts: Core Concepts

Advanced OOP concepts help you understand how Python resolves methods, combines behaviors, inspects objects, and creates flexible class designs.

This page covers:

- Method Resolution Order (MRO)
- Diamond Problem
- Mixins
- Nested Classes
- Dynamic attributes
- Object introspection with `type()`, `isinstance()`, and `issubclass()`

Examples use an online computer shopping system.

## Method Resolution Order (MRO)

MRO is the order Python follows when looking for a method in an inheritance hierarchy.

```python
class Product:
    def label(self):
        return "Product"


class DigitalProduct(Product):
    pass


print(DigitalProduct.mro())
```

Python looks in `DigitalProduct`, then `Product`, then `object`.

## Diamond Problem

The diamond problem happens when a class inherits from two classes that share the same parent.

```python
class Product:
    def info(self):
        return "Product"


class Downloadable(Product):
    def info(self):
        return "Downloadable product"


class Licensed(Product):
    def info(self):
        return "Licensed product"


class SoftwareProduct(Downloadable, Licensed):
    pass


software = SoftwareProduct()
print(software.info())
print(SoftwareProduct.mro())
```

Python uses MRO to decide which `info()` method runs.

## Mixins

A mixin is a small class that adds reusable behavior. Mixins are not usually meant to be used alone.

```python
class DiscountMixin:
    def apply_discount(self, price, percent):
        return price - (price * percent / 100)


class Product(DiscountMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price


product = Product("Laptop", 1000)
print(product.apply_discount(product.price, 10))
```

Use mixins for small reusable capabilities like logging, discount calculation, serialization, or validation.

## Nested Classes

A nested class is a class defined inside another class.

```python
class Order:
    class Status:
        CREATED = "created"
        PAID = "paid"
        SHIPPED = "shipped"

    def __init__(self, order_id):
        self.order_id = order_id
        self.status = self.Status.CREATED


order = Order("ORD-501")
print(order.status)
```

Nested classes can group closely related concepts, but overusing them can make code harder to read.

## Dynamic Attributes

Python objects can often get attributes at runtime.

```python
class Product:
    pass


product = Product()
product.name = "Mouse"
product.price = 25

print(product.name)
```

Dynamic attributes are flexible, but they can make code harder to reason about in large projects.

## Object Introspection

Introspection means examining objects at runtime.

```python
class Product:
    pass


product = Product()

print(type(product))
print(isinstance(product, Product))
print(issubclass(Product, object))
```

## `type()`

`type()` returns the exact type of an object.

```python
print(type("Laptop"))
print(type(999))
```

## `isinstance()`

`isinstance()` checks whether an object is an instance of a class or subclass.

```python
class Product:
    pass


class DigitalProduct(Product):
    pass


software = DigitalProduct()
print(isinstance(software, Product))
```

## `issubclass()`

`issubclass()` checks whether one class is a subclass of another.

```python
print(issubclass(DigitalProduct, Product))
```

## Common Gotchas

### Prefer `isinstance()` over exact `type()` checks

`isinstance()` respects inheritance.

### Use mixins carefully

Too many mixins can make method lookup hard to follow.

### Avoid unnecessary nested classes

Use nested classes only when the inner class is strongly tied to the outer class.

## Practice Problems

1. Print the MRO of a multiple-inheritance class.
2. Create a diamond inheritance example.
3. Add a `DiscountMixin` to `Product`.
4. Create an `Order.Status` nested class.
5. Compare `type()`, `isinstance()`, and `issubclass()`.

## See also

- [Python advanced OOP reference](advanced-oop-reference.md)
- [Python advanced OOP interview problems](interview-problems.md)
- [Python advanced OOP FAQ](frequently-asked-questions.md)
- [Python inheritance](../inheritance/core-concepts.md)
