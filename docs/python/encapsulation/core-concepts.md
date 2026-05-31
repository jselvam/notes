# Python Encapsulation: Core Concepts

Encapsulation is an OOP concept that keeps data and the methods that work on that data together. It also controls how object data is accessed or modified.

In an online computer shopping system, encapsulation helps protect:

- product price from becoming negative
- inventory stock from invalid updates
- cart items from accidental external changes
- payment status from unauthorized changes
- customer account data from direct mutation

## Why Encapsulation Matters

Without encapsulation, outside code can change object data freely.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


product = Product("Laptop", 999.99)
product.price = -100
```

A negative price is invalid, but direct access allowed it.

## Encapsulate With Methods

Use methods to control updates.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self._price = price

    def get_price(self):
        return self._price
```

## Python Access Conventions

Python uses naming conventions instead of strict access modifiers.

| Style | Meaning |
|-------|---------|
| `name` | public |
| `_name` | protected/internal by convention |
| `__name` | name-mangled private-style attribute |

## Public Attributes

Public attributes are intended for normal external access.

```python
class Product:
    def __init__(self, name):
        self.name = name
```

## Protected/Internal Attributes

A single underscore means "internal use".

```python
class Product:
    def __init__(self, price):
        self._price = price
```

This is a convention. Python does not fully block access.

## Private-Style Attributes

Double underscore triggers name mangling.

```python
class Product:
    def __init__(self, price):
        self.__price = price
```

Python internally changes `__price` to reduce accidental access from outside or subclasses.

## Encapsulation With `@property`

`@property` gives attribute-style access while keeping validation logic.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value


product = Product("Mouse", 25)
product.price = 30
print(product.price)
```

## Encapsulate Business Rules

```python
class InventoryItem:
    def __init__(self, product_name, stock):
        self.product_name = product_name
        self._stock = stock

    def reserve(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if quantity > self._stock:
            return False
        self._stock -= quantity
        return True

    @property
    def stock(self):
        return self._stock
```

Outside code can read `stock`, but stock changes must go through `reserve()`.

## Common Interview Points

### Is encapsulation strict in Python?

No. Python relies mostly on conventions and properties instead of strict private access.

### Why use `_name`?

It signals that the attribute is internal and should not be used directly from outside the class.

### Why use `@property`?

It keeps the external API clean while allowing validation or computed values internally.

## Practice Problems

1. Protect product price from negative values.
2. Make inventory stock read-only from outside.
3. Add a method to reserve stock safely.
4. Use `_balance` or `_stock` as an internal attribute.
5. Explain public vs protected vs private-style naming.

## See also

- [Python encapsulation reference](encapsulation-reference.md)
- [Python encapsulation interview problems](interview-problems.md)
- [Python encapsulation FAQ](frequently-asked-questions.md)
- [Python class properties and self](../class-properties-self/core-concepts.md)
