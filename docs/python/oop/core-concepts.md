# Python OOP: Core Concepts

OOP stands for **Object-Oriented Programming**. It is a programming style that organizes code around **objects** that combine data and behavior.

In an online computer shopping system, OOP can model real-world entities such as:

- `Product`
- `Cart`
- `Order`
- `Customer`
- `Payment`
- `Subscription`
- `Inventory`

## What Is a Class?

A **class** is a blueprint for creating objects.

```python
class Product:
    pass
```

## What Is an Object?

An **object** is an instance of a class.

```python
class Product:
    pass


laptop = Product()
print(type(laptop))
```

## Attributes

Attributes store object data.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


laptop = Product("Laptop", 999.99)
print(laptop.name)
print(laptop.price)
```

## Methods

Methods are functions that belong to a class.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_label(self):
        return f"{self.name}: ${self.price:.2f}"


laptop = Product("Laptop", 999.99)
print(laptop.display_label())
```

## `self`

`self` refers to the current object.

```python
class CartItem:
    def __init__(self, product_name, quantity):
        self.product_name = product_name
        self.quantity = quantity
```

Each object has its own values for `product_name` and `quantity`.

## The Four Main OOP Concepts

| Concept | Meaning |
|---------|---------|
| Encapsulation | Keep data and related behavior together |
| Inheritance | Reuse behavior from a parent class |
| Polymorphism | Different classes can share the same method name |
| Abstraction | Hide details and expose only important behavior |

## Encapsulation

Encapsulation groups data and methods in one class.

```python
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def item_count(self):
        return len(self.items)
```

The cart manages its own items instead of exposing every step to outside code.

## Inheritance

Inheritance lets a child class reuse behavior from a parent class.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class DigitalProduct(Product):
    def download_link(self):
        return f"/downloads/{self.name.lower()}"
```

## Polymorphism

Polymorphism means different objects can respond to the same method name.

```python
class CardPayment:
    def pay(self, amount):
        return f"Paid ${amount:.2f} by card"


class UPIPayment:
    def pay(self, amount):
        return f"Paid ${amount:.2f} by UPI"


def checkout(payment_method, amount):
    return payment_method.pay(amount)
```

## Abstraction

Abstraction hides internal details and exposes a simple interface.

```python
class InventoryService:
    def is_available(self, product_id, quantity):
        # Caller does not need to know where inventory data comes from.
        return quantity <= 10
```

## Common Interview Points

### Why use OOP?

OOP helps organize related data and behavior, reduce duplication, and model real-world business concepts.

### Is Python fully object-oriented?

Python supports OOP strongly, but it also supports procedural and functional programming styles.

### What is the difference between class and object?

A class is a blueprint. An object is a real instance created from that blueprint.

## Practice Problems

1. Create a `Product` class with `name` and `price`.
2. Add a method to format the product label.
3. Create a `Cart` class with `add_item()` and `total_items()`.
4. Create `DigitalProduct` from `Product`.
5. Create two payment classes with the same `pay()` method.

## See also

- [Python OOP reference](oop-reference.md)
- [Python OOP interview problems](interview-problems.md)
- [Python OOP FAQ](frequently-asked-questions.md)
- [Python functions](../functions/core-concepts.md)
