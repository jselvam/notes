# Python Classes and Objects: Core Concepts

Classes and objects are the foundation of Object-Oriented Programming in Python.

A **class** is a blueprint. An **object** is a real instance created from that blueprint.

In an online computer shopping system, classes can model:

- `Product`
- `Customer`
- `Cart`
- `Order`
- `Payment`
- `InventoryItem`

## Create a Class

Use the `class` keyword.

```python
class Product:
    pass
```

`pass` means the class body is intentionally empty.

## Create an Object

Call the class like a function.

```python
class Product:
    pass


laptop = Product()
print(laptop)
```

`laptop` is an object of the `Product` class.

## Add Attributes With `__init__`

`__init__()` initializes object data.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


laptop = Product("Laptop", 999.99)
print(laptop.name)
print(laptop.price)
```

## What Is `self`?

`self` refers to the current object.

```python
class Customer:
    def __init__(self, name):
        self.name = name
```

Each `Customer` object has its own `name`.

## Instance Attributes

Instance attributes belong to one object.

```python
laptop = Product("Laptop", 999.99)
mouse = Product("Mouse", 25.00)

print(laptop.name)
print(mouse.name)
```

## Instance Methods

Methods are functions inside a class. Instance methods receive `self`.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def label(self):
        return f"{self.name}: ${self.price:.2f}"


product = Product("Keyboard", 75)
print(product.label())
```

## Class Attributes

Class attributes are shared by all objects.

```python
class Product:
    store_name = "Computer Shop"

    def __init__(self, name):
        self.name = name


laptop = Product("Laptop")
mouse = Product("Mouse")

print(laptop.store_name)
print(mouse.store_name)
```

## Update Object State

Methods can change object attributes.

```python
class InventoryItem:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def sell(self, quantity):
        self.stock -= quantity


item = InventoryItem("Mouse", 10)
item.sell(2)
print(item.stock)
```

## Common Gotchas

### Forgetting `self`

```python
class Product:
    def label():
        return "Product"
```

Instance methods need `self` as the first parameter.

### Class attributes can be shared unexpectedly

Avoid mutable class attributes for per-object data.

```python
class Cart:
    items = []
```

Use instance attributes instead.

```python
class Cart:
    def __init__(self):
        self.items = []
```

## Practice Problems

1. Create a `Product` class with `name`, `price`, and `stock`.
2. Create two product objects.
3. Add a `label()` method.
4. Create a `Cart` class with an instance-level `items` list.
5. Explain class attribute vs instance attribute.

## See also

- [Python classes and objects reference](classes-and-objects-reference.md)
- [Python classes and objects interview problems](interview-problems.md)
- [Python classes and objects FAQ](frequently-asked-questions.md)
- [Python OOP core concepts](../oop/core-concepts.md)
